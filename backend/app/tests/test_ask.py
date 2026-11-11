"""
Tests for Ask NH Education Facts, run against the local database with a fake Claude client:

    docker exec -w /app education-backend-backend-1 python -m unittest app.tests.test_ask -v
"""
import io
import json
from datetime import timedelta
import time
import unittest
from types import SimpleNamespace
from unittest import mock

from fastapi.testclient import TestClient
from sqlalchemy import delete, func, inspect
from sqlmodel import Session, select

from app.api.v1.routes import ask as ask_route
from app.core.config import settings
from app.core.db import engine
from app.main import app
from app.model.ask import AskQuestion
from app.service.internal.ask import ask_service, question_log
from app.service.internal.ask.ask_service import AskFailed, AskLimitReached, AskUnavailable, DatasetRegistry, build_answer
from app.service.internal.ask.data_tools import DataToolError, get_data


def tool_use(block_id, name, tool_input):
    return SimpleNamespace(type="tool_use", id=block_id, name=name, input=tool_input)


def reply(stop_reason, *content):
    return SimpleNamespace(stop_reason=stop_reason, content=list(content), usage={})


def final(payload):
    return reply("end_turn", SimpleNamespace(type="text", text=json.dumps(payload)))


def plain(text):
    return final({"status": "answered", "answer": [text], "charts": [], "tables": [], "references": [], "follow_ups": []})


class FakeStream:
    """A streamed response: its text a few characters at a time, `pause` seconds apart, then the whole message."""

    def __init__(self, response, pause=0):
        self.response = response
        self.pause = pause

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def __iter__(self):
        for block in self.response.content:
            if block.type != "text":
                continue
            for start in range(0, len(block.text), 7):
                time.sleep(self.pause)
                yield SimpleNamespace(type="text", text=block.text[start:start + 7])

    def get_final_message(self):
        return self.response


class FakeClient:
    """Plays back Claude's responses in order, each after `delay` seconds (its text `pause` seconds a
    piece), and records each request."""

    def __init__(self, responses, delay=0, pause=0):
        self.responses = list(responses)
        self.delay = delay
        self.pause = pause
        self.requests = []
        self.messages = SimpleNamespace(stream=self._stream)

    def _stream(self, **kwargs):
        self.requests.append(kwargs)
        time.sleep(self.delay)
        return FakeStream(self.responses.pop(0), self.pause)


class AskTests(unittest.TestCase):
    def setUp(self):
        self.session = Session(engine)
        # No Redis: the daily count and answer cache stay in memory for the test
        self.patches = [
            mock.patch.object(ask_service, "_redis", return_value=None),
            mock.patch.object(ask_service.settings, "ANTHROPIC_API_KEY", "test-key"),
            mock.patch.object(ask_service.settings, "ASK_DAILY_LIMIT", 2),
        ]
        for patch in self.patches:
            patch.start()
        ask_service._memory_counts.clear()
        ask_service._memory_answers.clear()
        # Questions the tests log are removed afterwards
        self.last_logged = self.session.exec(select(func.max(AskQuestion.id))).one() or 0

    def tearDown(self):
        for patch in self.patches:
            patch.stop()
        self.session.exec(delete(AskQuestion).where(AskQuestion.id > self.last_logged))
        self.session.commit()
        self.session.close()

    def logged(self):
        """The questions logged during the test, oldest first"""
        with Session(engine) as session:
            return session.exec(select(AskQuestion).where(AskQuestion.id > self.last_logged).order_by(AskQuestion.id)).all()

    def answer(self, question, history=None):
        """As the route answers: a saved answer, or a new one within the daily limit."""
        earlier, saved = ask_service.prepare_question(question, history)
        return saved or ask_service.answer_afresh(self.session, question, earlier)

    def run_with(self, responses, question="How many students graduate in New Hampshire?"):
        client = FakeClient(responses)
        with mock.patch.object(ask_service, "_client", client):
            return self.answer(question), client

    def test_deep_think_uses_high_effort_a_longer_limit_and_its_own_saved_answers(self):
        payload = {"status": "answered", "answer": ["87.5% graduated."]}
        question = "How many students graduate in New Hampshire?"
        # Medium by default
        _, client = self.run_with([final(payload)], question)
        self.assertEqual(client.requests[0]["output_config"]["effort"], "medium")
        # Take More Time: high effort, more time, and not the usual answer from the cache
        deep_client = FakeClient([final(payload)])
        with mock.patch.object(ask_service, "_client", deep_client):
            earlier, saved = ask_service.prepare_question(question, None, deep=True)
            self.assertIsNone(saved)
            answer = ask_service.answer_afresh(self.session, question, earlier, deep=True)
        self.assertEqual(deep_client.requests[0]["output_config"]["effort"], "high")
        self.assertGreater(deep_client.requests[0]["timeout"], ask_service.TIME_LIMIT)
        self.assertFalse(answer["cached"])
        # Each kind is saved for its own next asker
        self.assertTrue(ask_service.prepare_question(question, None, deep=True)[1]["cached"])
        self.assertTrue(ask_service.prepare_question(question, None)[1]["cached"])

    def test_only_the_main_tools_are_strict(self):
        # The API compiles strict tools into one grammar and refuses it past a size limit, which no test
        # here can reach: a new strict tool needs a real question asked first
        strict = {tool["name"] for tool in ask_service.all_tools() if tool.get("strict")}
        self.assertEqual(strict, {"find_places", "get_data", "list_schools", "compare_places"})

    def test_charts_are_asked_for_whenever_an_answer_gives_figures(self):
        self.assertIn("show them in at least one chart or table", ask_service.SYSTEM_PROMPT)

    def test_charts_use_the_database_and_links_must_be_real_pages(self):
        graduation = get_data(self.session, "graduation", "state")["datasets"][0]
        answer, client = self.run_with([
            reply("tool_use", tool_use("t1", "get_data", {"topic": "graduation", "level": "state", "id": None})),
            final({
                "status": "answered",
                "answer": ["87.5% of the class of 2025 graduated in four years."],
                "charts": [{"dataset": "d1", "kind": "line", "title": "Graduation rate", "series": ["Graduated", "Not a column"]}],
                "tables": [{"dataset": "d1", "title": "By class", "columns": ["Graduated"]}],
                "references": [
                    {"label": "Graduation", "path": "https://www.nhfacts.com/state/outcomes"},
                    {"label": "Made up", "path": "/district/999999/outcomes"},
                ],
                "follow_ups": ["How does Concord compare?"],
            }),
        ])
        # The tool result went back to Claude as one message, with dataset ids
        tool_results = client.requests[1]["messages"][-1]["content"]
        self.assertEqual(json.loads(tool_results[0]["content"])["datasets"][0]["id"], "d1")
        chart = answer["charts"][0]
        self.assertEqual(chart["series"], ["Graduated"])
        self.assertEqual([p["label"] for p in chart["points"]], [row[0] for row in graduation["rows"]])
        self.assertEqual([p["values"][0] for p in chart["points"]], [row[1] for row in graduation["rows"]])
        # The table always keeps its label column
        self.assertEqual(answer["tables"][0]["columns"], ["Class", "Graduated"])
        self.assertEqual(answer["references"], [{"label": "Graduation", "path": "/state/outcomes"}])
        self.assertFalse(answer["cached"])

    def test_tool_errors_go_back_to_claude(self):
        answer, client = self.run_with([
            reply("tool_use", tool_use("t1", "get_data", {"topic": "spending", "level": "district", "id": 999999})),
            final({"status": "no_data", "answer": ["The site has no data for that district."], "charts": [], "tables": [], "references": [], "follow_ups": []}),
        ])
        result = client.requests[1]["messages"][-1]["content"][0]
        self.assertTrue(result["is_error"])
        self.assertIn("No public school district has id 999999", result["content"])
        self.assertEqual(answer["status"], "no_data")

    def test_repeat_questions_come_from_the_cache_and_the_daily_limit_holds(self):
        response = lambda: final({"status": "answered", "answer": ["Yes."], "charts": [], "tables": [], "references": [], "follow_ups": []})
        first, _ = self.run_with([response()], "Question one?")
        again, client = self.run_with([], "question ONE")
        self.assertTrue(again["cached"])
        self.assertEqual(client.requests, [])
        self.run_with([response()], "Question two?")
        with self.assertRaises(AskLimitReached):
            self.run_with([response()], "Question three?")

    def test_without_a_daily_limit_questions_are_counted_but_never_refused(self):
        response = lambda: final({"status": "answered", "answer": ["Yes."], "charts": [], "tables": [], "references": [], "follow_ups": []})
        with mock.patch.object(ask_service.settings, "ASK_DAILY_LIMIT", None):
            for n in range(3):
                self.run_with([response()], f"Question {n}?")
            self.assertEqual(list(ask_service._memory_counts.values()), [3])
        with mock.patch.object(ask_service.settings, "ASK_DAILY_LIMIT", 0):
            with self.assertRaises(AskUnavailable):
                self.run_with([response()], "Question four?")

    def test_follow_ups_bring_the_last_ten_earlier_questions_and_are_cached_with_them(self):
        response = lambda: final({"status": "answered", "answer": ["Science was 38%."], "charts": [], "tables": [], "references": [], "follow_ups": []})
        history = [{"question": f"Old question {n}?", "answer": ["An answer."]} for n in range(12)]
        history.append({"question": "How did Concord do in math?", "answer": ["Concord was 40% in math.", "x" * 5000]})
        client = FakeClient([response()])
        with mock.patch.object(ask_service, "_client", client):
            self.answer("What about science?", history)
        message = client.requests[0]["messages"][0]["content"]
        # The last ten, oldest first, each answer trimmed, then the new question
        self.assertNotIn("Old question 2?", message)
        self.assertLess(message.index("Old question 3?"), message.index("How did Concord do in math?"))
        self.assertIn("<answer_start>Concord was 40% in math.", message)
        self.assertLess(len(message), 4000)
        self.assertTrue(message.endswith("<new_question>What about science?</new_question>"))
        # Saved with its context: the same words after another question are asked afresh
        self.assertTrue(self.answer("what about science", history)["cached"])
        other = [{"question": "How did Bedford do in math?", "answer": ["Bedford was 75%."]}]
        client = FakeClient([response()])
        with mock.patch.object(ask_service, "_client", client):
            self.assertFalse(self.answer("What about science?", other)["cached"])
        self.assertIn("Bedford", client.requests[0]["messages"][0]["content"])

    def test_a_question_stops_at_the_time_limit(self):
        slow_lookup = reply("tool_use", tool_use("t1", "get_data", {"topic": "graduation", "level": "state", "id": None}))
        client = FakeClient([slow_lookup, plain("Too late.")], delay=0.06)
        with mock.patch.object(ask_service, "_client", client), mock.patch.object(ask_service, "TIME_LIMIT", 0.05):
            with self.assertRaises(AskFailed):
                self.answer("How many students graduate?")
        # Each request may take only what's left of the limit, and none starts after it
        self.assertEqual(len(client.requests), 1)
        self.assertLessEqual(client.requests[0]["timeout"], 0.05)

    def test_new_answers_stream_while_they_are_written(self):
        api = TestClient(app)
        url = f"{settings.API_V1_STR}/ask"
        with mock.patch.object(ask_route, "KEEP_ALIVE_SECONDS", 0.01), mock.patch.object(ask_route, "TEXT_SECONDS", 0.01):
            client = FakeClient([plain("Yes.")], delay=0.1)
            with mock.patch.object(ask_service, "_client", client):
                response = api.post(url, json={"question": "Is this streamed?"})
            # Spaces while Claude works, then the answer, which still reads as JSON
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.text.startswith("  "))
            self.assertEqual(response.json()["answer"], ["Yes."])
            self.assertFalse(response.json()["cached"])
            # Asked again: the saved answer, at once
            self.assertTrue(api.post(url, json={"question": "is this streamed"}).json()["cached"])
            # A failure once streaming has started is a message with no answer
            client = FakeClient([reply("max_tokens")], delay=0.05)
            with mock.patch.object(ask_service, "_client", client):
                response = api.post(url, json={"question": "Will this fail?"})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(set(response.json()), {"detail"})

    def test_every_question_is_logged_with_its_outcome_and_never_who_asked(self):
        api = TestClient(app)
        url = f"{settings.API_V1_STR}/ask"
        history = [{"question": "How did Concord do in math?", "answer": ["Concord was 40% in math."]}]
        response = lambda: final({"status": "answered", "answer": ["Science was 38%."], "charts": [], "tables": [], "references": [], "follow_ups": []})
        with mock.patch.object(ask_service, "_client", FakeClient([response()])):
            api.post(url, json={"question": "What about science?", "history": history, "deep": True})
        api.post(url, json={"question": "what about SCIENCE", "history": history, "deep": True})
        with mock.patch.object(ask_service, "_client", FakeClient([reply("max_tokens")])):
            api.post(url, json={"question": "Will this fail?"})
        # The limit is two new answers a day here
        api.post(url, json={"question": "Is the limit reached?"})
        with mock.patch.object(ask_service.settings, "ASK_DAILY_LIMIT", 0):
            api.post(url, json={"question": "Is asking off?"})
        rows = self.logged()
        self.assertEqual([(row.question, row.earlier_questions, row.deep, row.status, row.cached) for row in rows], [
            ("What about science?", ["How did Concord do in math?"], True, "answered", False),
            ("what about SCIENCE", ["How did Concord do in math?"], True, "answered", True),
            ("Will this fail?", [], False, "failed", False),
            ("Is the limit reached?", [], False, "limit", False),
            ("Is asking off?", [], False, "unavailable", False),
        ])
        self.assertIsNotNone(rows[0].seconds)
        self.assertIsNone(rows[1].seconds)
        # Nothing about who asked
        columns = {column["name"] for column in inspect(engine).get_columns("ask_question")}
        self.assertEqual(columns, {"id", "question", "earlier_questions", "deep", "cached", "status", "seconds", "date_created", "date_updated"})
        # Exported newest first
        out = io.StringIO()
        self.assertGreaterEqual(question_log.export_csv(1, out), 5)
        lines = out.getvalue().splitlines()
        self.assertEqual(lines[0], "asked_at_utc,question,earlier_questions,status,cached,more_time,seconds")
        self.assertIn(",Is asking off?,,unavailable,False,False,", lines[1])

    def test_questions_are_kept_for_a_year(self):
        old = AskQuestion(question="Asked over a year ago?", deep=False, date_created=question_log._utc_now() - timedelta(days=366))
        recent = AskQuestion(question="Asked this year?", deep=False, date_created=question_log._utc_now() - timedelta(days=364))
        self.session.add_all([old, recent])
        self.session.commit()
        question_log.record_question("Asked today?", [], False)
        self.assertEqual([row.question for row in self.logged()], ["Asked this year?", "Asked today?"])

    def test_a_question_is_answered_when_it_cant_be_logged(self):
        with mock.patch.object(question_log, "Session", side_effect=RuntimeError("database down")):
            self.assertIsNone(question_log.record_question("Is the log down?", [], False))
            question_log.record_outcome(5, "answered")
            with mock.patch.object(ask_service, "_client", FakeClient([plain("Yes.")])):
                response = TestClient(app).post(f"{settings.API_V1_STR}/ask", json={"question": "Is the log down?"})
        self.assertEqual(response.json()["answer"], ["Yes."])
        self.assertEqual(self.logged(), [])

    def test_answers_can_be_shown_as_they_re_written(self):
        api = TestClient(app)
        url = f"{settings.API_V1_STR}/ask"
        paragraphs = ["Concord spent $24,351 per student in 2024, more than the state's $21,000.", "That's up 4% from 2023."]
        with mock.patch.object(ask_route, "TEXT_SECONDS", 0.01):
            client = FakeClient([final({"status": "answered", "answer": paragraphs})], pause=0.02)
            with mock.patch.object(ask_service, "_client", client):
                response = api.post(url, json={"question": "How much does Concord spend?", "stream": True})
        lines = [json.loads(line) for line in response.text.splitlines() if line.strip()]
        partials = [line["partial"] for line in lines[:-1]]
        # The paragraphs grow, each update starting where the one before left off, then the answer
        self.assertGreater(len(partials), 3)
        for before, after in zip(partials, partials[1:]):
            self.assertTrue(len(after) >= len(before) and after[len(before) - 1].startswith(before[-1]))
        for partial in partials:
            self.assertTrue(all(paragraph in paragraphs or any(full.startswith(paragraph) for full in paragraphs) for paragraph in partial))
        self.assertEqual(lines[-1]["answer"], paragraphs)

    def test_the_answer_written_so_far_reads_from_unfinished_json(self):
        partial = ask_service.partial_answer
        self.assertEqual(partial('{"status": "answered", "ans'), [])
        self.assertEqual(partial('{"status": "answered", "answer": ['), [])
        self.assertEqual(partial('{"status": "answered", "answer": ["Concord sp'), ["Concord sp"])
        self.assertEqual(partial('{"status": "answered", "answer": ["One.", "Two'), ["One.", "Two"])
        self.assertEqual(partial('{"status": "answered", "answer": ["One.", "Two."], "charts": [{"title": "x'), ["One.", "Two."])
        # An escape cut off partway waits for the rest of it
        self.assertEqual(partial('{"answer": ["The \\"best'), ['The "best'])
        self.assertEqual(partial('{"answer": ["The \\'), ["The "])
        self.assertEqual(partial('{"answer": ["Caf\\u00'), ["Caf"])
        self.assertEqual(partial('{"answer": ["Caf\\u00e9'), ["Café"])
        self.assertEqual(partial('{"answer": ["C:\\\\'), ["C:\\"])
        self.assertEqual(partial('{"answer": ["Hi \\ud83d'), ["Hi "])
        # A declined question shows nothing until its message
        self.assertEqual(partial('{"status": "declined", "answer": ["This site can'), [])

    def test_the_route_refuses_questions_it_cant_take(self):
        api = TestClient(app)
        url = f"{settings.API_V1_STR}/ask"
        self.assertEqual(api.post(url, json={"question": "x" * 501}).status_code, 400)
        self.assertEqual(api.post(url, json={"question": "Hi?", "history": [{"question": "Q?", "answer": ["A."]}] * 21}).status_code, 422)
        with mock.patch.object(ask_service.settings, "ANTHROPIC_API_KEY", ""):
            self.assertEqual(api.post(url, json={"question": "Any key?"}).status_code, 503)
        with mock.patch.object(ask_service, "_client", FakeClient([plain("One."), plain("Two.")])):
            api.post(url, json={"question": "First?"})
            api.post(url, json={"question": "Second?"})
            self.assertEqual(api.post(url, json={"question": "Third?"}).status_code, 429)

    def test_declined_answers_have_no_fallback_links_and_aren_t_cached(self):
        answer, _ = self.run_with([reply("refusal")], "Tell me about my neighbor's kid")
        self.assertEqual(answer["status"], "declined")
        self.assertEqual(answer["references"], [])
        self.assertIsNone(ask_service.cached_answer("Tell me about my neighbor's kid"))

    def test_answers_without_links_point_to_the_data_used(self):
        registry = DatasetRegistry()
        registry.add(get_data(self.session, "spending", "district", 111))
        answer = build_answer({"status": "answered", "answer": ["Concord spent $24,351 per student."], "references": []}, registry)
        self.assertEqual(answer["references"][0]["path"], "/district/111/financials")

    def test_a_chart_keeps_one_unit_and_tables_give_each_column_s(self):
        registry = DatasetRegistry()
        registry.add(get_data(self.session, "graduation", "state"))
        answer = build_answer({
            "status": "answered", "answer": ["..."],
            "charts": [{"dataset": "d1", "kind": "line", "title": "Classes", "series": ["Graduated", "Students in class"]}],
            "tables": [{"dataset": "d1", "title": "Classes", "columns": ["Graduated", "Students in class"]}],
        }, registry)
        self.assertEqual(answer["charts"][0]["series"], ["Graduated"])
        self.assertEqual(answer["charts"][0]["unit"], "percent")
        self.assertEqual(answer["tables"][0]["units"], [None, "percent", "count"])

    def test_rankings_sort_every_district_and_charts_can_show_the_top(self):
        answer, client = self.run_with([
            reply("tool_use", tool_use("t1", "rank_districts", {"measure": "cost_per_student", "order": "highest"})),
            final({
                "status": "answered", "answer": ["..."],
                "charts": [{"dataset": "d1", "kind": "bar", "title": "Top 5", "series": ["Cost per student"], "first_rows": 5}],
                "tables": [], "follow_ups": [],
                "references": [],
            }),
        ], "Which districts spend the most per student?")
        sent = json.loads(client.requests[1]["messages"][-1]["content"][0]["content"])
        ranking = sent["datasets"][0]
        values = [row[1] for row in ranking["rows"]]
        self.assertEqual(values, sorted(values, reverse=True))
        self.assertGreater(len(values), 100)
        points = answer["charts"][0]["points"]
        self.assertEqual([p["values"][0] for p in points], values[:5])
        # Every district in the ranking can be linked to
        registry = DatasetRegistry()
        registry.add_ranking({"datasets": [], "districts": [{"name": "Concord", "page": "/district/111/financials"}]})
        self.assertIn("/district/111/financials", registry.pages)

    def test_general_answers_keep_only_the_links_claude_chose(self):
        registry = DatasetRegistry()
        registry.add(get_data(self.session, "efa", "state"))
        answer = build_answer({"status": "general", "answer": ["An IEP is a written plan for a student with a disability."], "references": []}, registry)
        self.assertEqual(answer["status"], "general")
        self.assertEqual(answer["references"], [])
        answer = build_answer({"status": "general", "answer": ["..."], "references": [{"label": "EFAs", "path": "/state/efa"}]}, registry)
        self.assertEqual(answer["references"], [{"label": "EFAs", "path": "/state/efa"}])

    def test_compare_places_lines_places_up_by_year(self):
        from app.service.internal.ask.data_tools import compare_places
        result = compare_places(self.session, "spending", [{"level": "district", "id": 111}, {"level": "state", "id": None}])
        trend = result["datasets"][0]
        self.assertEqual(trend["columns"], ["School year", "Concord", "New Hampshire"])
        concord = {row[0]: row[1] for row in get_data(self.session, "spending", "district", 111)["datasets"][0]["rows"]}
        self.assertEqual({row[0]: row[1] for row in trend["rows"] if row[1] is not None}, {k: v for k, v in concord.items() if v is not None})
        latest = result["datasets"][-1]
        self.assertEqual([row[0] for row in latest["rows"]], ["Concord", "New Hampshire"])
        with self.assertRaises(DataToolError):
            compare_places(self.session, "spending", [{"level": "district", "id": 111}])

    def test_schools_are_found_by_town_and_listed_by_district(self):
        from app.service.internal.ask.data_tools import find_places, list_schools
        found = [place["name"] for place in find_places(self.session, "Hampton") if place["kind"] == "school"]
        self.assertTrue(any("Marston" in name for name in found), found)
        schools = list_schools(self.session, 111)
        self.assertTrue(any(school["name"] == "Concord High School" for school in schools))
        self.assertTrue(all(school["page"].startswith("/school/") for school in schools))

    def test_money_figures_add_up_and_inflation_matches_the_site(self):
        from app.service.internal.ask.data_tools import in_dollars_of
        datasets = {d["key"] or d["title"]: d for d in get_data(self.session, "spending", "district", 111)["datasets"]}
        lines = datasets["Spending by line, Concord"]
        categories = {row[0]: row for row in datasets["categories"]["rows"]}
        for row in lines["rows"]:
            # The lines add up to the category total (to rounding)
            self.assertAlmostEqual(sum(row[1:]), categories[row[0]][5], delta=len(row))
        for row in datasets["revenue"]["rows"]:
            self.assertAlmostEqual(sum(row[1:5]), row[5], delta=4)
        # The site's CPI: 2022-23 to 2025-26 is 304.7 to 333.5
        self.assertEqual(in_dollars_of(100000, 2023, 2026), round(100000 * 333.5 / 304.7))
        self.assertEqual(in_dollars_of(100000, 2026, 2026), 100000)

    def test_efa_counts_districts_and_estimates_cost_from_the_aid_table(self):
        for level, place_id in (("state", None), ("district", 575)):
            students, aid = get_data(self.session, "efa", level, place_id)["datasets"][:2]
            latest = students["rows"][-1]
            self.assertEqual(latest[1], aid["rows"][0][1])  # the base amount's students are the EFA students
            self.assertEqual(latest[4], sum(row[3] for row in aid["rows"]))
        with self.assertRaises(DataToolError):
            get_data(self.session, "efa", "school", 22510)

    def test_naep_follows_naeps_own_tests_and_keeps_groups_to_new_hampshire_and_the_nation(self):
        from app.service.internal.ask.national_tools import naep_results
        trend, against_places, against_years = naep_results(self.session, "math", 8, "average_score", ["NH", "MA", "US"], "All students")["datasets"]
        self.assertEqual(trend["columns"], ["Year", "New Hampshire", "Massachusetts", "United States"])
        self.assertEqual(trend["rows"][-1], ["2024", 280, 283, 272])
        # Against every state at once, Massachusetts isn't significantly higher in 2024; the nation is tested on its own
        self.assertEqual(against_places["rows"][-1], ["2024", "not significantly different", "higher"])
        self.assertEqual(len(against_places["rows"]), len(trend["rows"]))
        # Every place's latest year is tested against its earlier years
        self.assertEqual(against_years["columns"][1:], ["New Hampshire in 2024 is", "Massachusetts in 2024 is", "United States in 2024 is"])
        self.assertTrue(all(row[0] < "2024" for row in against_years["rows"]))
        self.assertIsNone(trend["page"])
        ranking = naep_results(self.session, "reading", 4, "at_or_above_proficient", [], "All students")["datasets"][0]
        self.assertEqual(len(ranking["rows"]), 52)  # the states, DC and the nation
        with self.assertRaises(DataToolError):
            naep_results(self.session, "math", 4, "average_score", ["MA"], "Female")

    def test_school_revenue_by_state_is_per_pupil_with_shares_by_source(self):
        from app.service.internal.ask.national_tools import state_school_revenue
        trend, by_source, categories = state_school_revenue(self.session, ["NH", "US"], "per_pupil", "total")["datasets"]
        self.assertEqual(trend["rows"][-1][:2], ["2023-24", 25828.63])
        self.assertEqual(by_source["rows"][0][5:8], [8.26, 28.35, 63.39])  # federal, state and local shares
        self.assertIn("Federal: Title I", [row[0] for row in categories["rows"]])
        with self.assertRaises(DataToolError):
            state_school_revenue(self.session, ["NH"], "share_of_total", "total")

    def test_answers_from_national_data_link_no_site_page(self):
        from app.service.internal.ask.national_tools import state_school_revenue
        registry = DatasetRegistry()
        registry.add(state_school_revenue(self.session, ["NH"], "per_pupil", "local"))
        answer = build_answer({"status": "answered", "answer": ["New Hampshire's local revenue per pupil..."], "references": []}, registry)
        self.assertEqual(answer["references"], [])
        self.assertNotIn(None, registry.pages)

    def test_question_two_gives_each_district_s_vote_and_names_its_source(self):
        from app.service.internal.ask.data_tools import compare_places, find_places, rank_districts
        fall_mountain = next(place["id"] for place in find_places(self.session, "Fall Mountain") if place["kind"] == "district")
        district = get_data(self.session, "question_two", "district", fall_mountain)["datasets"][0]
        self.assertEqual(district["rows"], [["2026", 3160, 2092, 60.2, "Yes", "No"]])
        self.assertIsNone(district["page"])
        self.assertEqual(district["source"]["site"], "wmur.com")
        summary, by_district, by_sau = get_data(self.session, "question_two", "state")["datasets"]
        self.assertEqual(summary["rows"], [["School tax cap (school districts)", 179, 93, 86, "No"], ["SAU spending cap (SAUs)", 107, 60, 47, "No"]])
        self.assertEqual(len(by_sau["rows"]), 107)
        self.assertIn("no total for SAU 90", by_sau["note"])
        # A district's SAU and towns: Fall Mountain is SAU 60 on its own
        sau, towns = get_data(self.session, "question_two", "district", fall_mountain)["datasets"][1:]
        self.assertEqual(sau["rows"], [["2026", 3160, 2092, 60.2, "Yes", "No"]])
        self.assertEqual(sum(row[1] for row in towns["rows"]), 3160)
        # The part of Concord in Merrimack Valley is the district's total less its other towns
        merrimack_valley = next(place["id"] for place in find_places(self.session, "Merrimack Valley") if place["kind"] == "district")
        towns = get_data(self.session, "question_two", "district", merrimack_valley)["datasets"][-1]
        self.assertIn(["Concord (the part in Merrimack Valley)", 1130, 1013, 52.7], towns["rows"])
        shares = [row[3] for row in by_district["rows"]]
        self.assertEqual(len(shares), 179)
        self.assertEqual(shares, sorted(shares, reverse=True))
        self.assertTrue(all((row[3] >= 60) == (row[4] == "Yes") for row in by_district["rows"]))
        for level, place_id in (("school", 22510), ("district", 999)):  # a school, and an academy, which didn't vote
            with self.assertRaises(DataToolError):
                get_data(self.session, "question_two", level, place_id)
        ranking = rank_districts(self.session, "question_two_yes_share", "highest")
        self.assertEqual([row[1] for row in ranking["datasets"][0]["rows"]], shares)
        self.assertEqual(ranking["districts"], [])  # no site page to link
        compared = compare_places(self.session, "question_two", [{"level": "district", "id": 111}, {"level": "district", "id": fall_mountain}])
        self.assertEqual(compared["datasets"][0]["columns"], ["Election", "Concord", "Fall Mountain Regional"])
        self.assertTrue(all(item["source"]["site"] == "wmur.com" for item in compared["datasets"]))
        # An answer showing the results links WMUR's page as its source, and no site page
        registry = DatasetRegistry()
        registry.add({"datasets": [district]})
        answer = build_answer({"status": "answered", "answer": ["..."], "references": [],
                               "tables": [{"dataset": "d1", "title": "Question 2", "columns": ["Yes share"]}]}, registry)
        self.assertEqual(answer["references"], [])
        self.assertEqual([source["site"] for source in answer["sources"]], ["wmur.com"])

    def test_safety_has_serious_incidents_restraints_and_bullying_by_kind(self):
        datasets = {d["key"] or d["title"].split(",")[0]: d for d in get_data(self.session, "safety", "state")["datasets"]}
        self.assertIn(["2021-22", 1416], [row[:2] for row in datasets["restraint"]["rows"]])
        incidents, kinds = datasets["incidents"], datasets["Serious safety incidents by kind"]
        self.assertTrue(all(row[1] + row[2] == row[3] for row in incidents["rows"]))
        # The kinds add up to each year's total
        totals = {row[0]: row[3] for row in incidents["rows"]}
        for index, year in enumerate(kinds["columns"][1:], start=1):
            self.assertEqual(sum(row[index] for row in kinds["rows"]), totals[year])
        for title in ("Confirmed bullying incidents by what they were based on", "Confirmed bullying incidents by what they involved",
                      "Incidents that led to a suspension"):
            self.assertIn(title, datasets)
        school = [d["title"] for d in get_data(self.session, "safety", "school", 22510)["datasets"]]
        self.assertIn("Restraints and seclusions, Portsmouth Middle School", school)

    def test_students_by_grade_add_up_and_include_students_with_disabilities(self):
        for level, place_id in (("state", None), ("district", 111), ("school", 22510)):
            datasets = {d["key"] or d["title"]: d for d in get_data(self.session, "enrollment", level, place_id)["datasets"]}
            students = {row[0]: row[1] for row in datasets["students"]["rows"]}
            for row in datasets["grades"]["rows"]:
                self.assertEqual(sum(value or 0 for value in row[1:]), students[row[0]], (level, row[0]))
            latest = next(d for d in datasets.values() if d["title"].startswith("Students by grade, "))
            self.assertEqual(latest["rows"][-1][:2], ["All grades", students[latest["title"].split(", ")[1]]])
            self.assertTrue(datasets["disabilities"]["rows"])
        concord = {d["key"]: d for d in get_data(self.session, "enrollment", "district", 111)["datasets"] if d["key"]}
        self.assertIn(["2022-23", 19.8], concord["disabilities"]["rows"])

    def test_teacher_degrees_leave_out_years_that_count_too_many_teachers(self):
        degrees = next(d for d in get_data(self.session, "staff", "district", 111)["datasets"] if d["key"] == "degrees")
        # Concord's degree counts for 2014-15 to 2020-21 add up to far more teachers than it had
        self.assertEqual([row[0] for row in degrees["rows"]], ["2022-23", "2023-24", "2024-25", "2025-26"])
        for row in degrees["rows"]:
            self.assertAlmostEqual(row[-1], 100 * (row[2] + row[3]) / sum(row[1:5]), delta=0.1)

    def test_balance_sheets_add_up_and_are_for_districts_only(self):
        trend, lines = get_data(self.session, "balance_sheet", "district", 111)["datasets"]
        for row in trend["rows"]:
            self.assertAlmostEqual(row[4] - row[5], row[3], delta=2)  # assets less liabilities is the fund balance
        self.assertEqual(trend["rows"][-1][:2], ["2024-25", 2800000])
        self.assertIn(["Unassigned Fund Balance", "Fund balance: Unassigned", 2800000, 3379942], lines["rows"])
        self.assertEqual(lines["page"], "/district/111/financials/balance-sheet")
        for level, place_id in (("state", None), ("school", 22510)):
            with self.assertRaises(DataToolError):
                get_data(self.session, "balance_sheet", level, place_id)

    def test_schools_rank_by_level_or_district_and_can_be_linked(self):
        from app.service.internal.ask.data_tools import rank_schools
        ranking = rank_schools(self.session, "math_proficiency", "highest", "elementary")["datasets"][0]
        # The state's ">90%" ranks above every percentage it reports
        order = [{">90%": 90.5, "<10%": 9.5}.get(row[3], row[3]) for row in ranking["rows"]]
        self.assertEqual(order, sorted(order, reverse=True))
        self.assertFalse(any(row[2].endswith(("Grade 9", "Grade 10", "Grade 11", "Grade 12")) for row in ranking["rows"]))
        high = rank_schools(self.session, "graduation_rate", "lowest", "high")["datasets"][0]
        self.assertTrue(all(row[2].endswith("Grade 12") for row in high["rows"]))
        with self.assertRaises(DataToolError):
            rank_schools(self.session, "cost_per_student", "highest", "all")
        # Not a strict tool, so it checks the order itself rather than sorting the wrong way
        with self.assertRaises(DataToolError):
            rank_schools(self.session, "students", "descending", "all")
        # Ranked through the Ask: every school ranked can be linked to
        from app.service.internal.ask.data_tools import list_schools
        concord_high = next(school["page"] for school in list_schools(self.session, 111) if school["name"] == "Concord High School") + "/enrollment"
        answer, client = self.run_with([
            reply("tool_use", tool_use("t1", "rank_schools", {"measure": "students", "order": "highest", "level": "all", "district_id": 111})),
            final({
                "status": "answered", "answer": ["Concord High School is the largest."], "charts": [], "tables": [], "follow_ups": [],
                "references": [{"label": "Concord High School: Enrollment", "path": concord_high}],
            }),
        ], "Which Concord school has the most students?")
        rows = json.loads(client.requests[1]["messages"][-1]["content"][0]["content"])["datasets"][0]["rows"]
        self.assertEqual(rows[0][:2], ["Concord High School", "Concord"])
        self.assertTrue(all(row[1] == "Concord" for row in rows))
        self.assertEqual(answer["references"][0]["path"], concord_high)

    def test_data_tools_check_places(self):
        with self.assertRaises(DataToolError):
            get_data(self.session, "staff", "school", 27010)
        with self.assertRaises(DataToolError):
            get_data(self.session, "graduation", "district", None)


if __name__ == "__main__":
    unittest.main()
