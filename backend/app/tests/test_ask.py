"""
Tests for Ask NH Education Facts, run against the local database with a fake Claude client:

    docker exec -w /app education-backend-backend-1 python -m unittest app.tests.test_ask -v
"""
import json
import time
import unittest
from types import SimpleNamespace
from unittest import mock

from fastapi.testclient import TestClient
from sqlmodel import Session

from app.api.v1.routes import ask as ask_route
from app.core.config import settings
from app.core.db import engine
from app.main import app
from app.service.internal.ask import ask_service
from app.service.internal.ask.ask_service import AskFailed, AskLimitReached, DatasetRegistry, build_answer
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

    def tearDown(self):
        for patch in self.patches:
            patch.stop()
        self.session.close()

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

    def test_data_tools_check_places(self):
        with self.assertRaises(DataToolError):
            get_data(self.session, "staff", "school", 27010)
        with self.assertRaises(DataToolError):
            get_data(self.session, "graduation", "district", None)


if __name__ == "__main__":
    unittest.main()
