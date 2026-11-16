"""
Tests for the reference library: parsing the Markdown, the load, the Ask's look_up_reference tool,
the outside sources an answer may link to, and the API. Run against the local database after
`alembic upgrade head`:

    docker exec -w /app education-backend-backend-1 python -m unittest app.tests.test_reference -v
"""
import os
import tempfile
import unittest
from datetime import date, timedelta

from fastapi.testclient import TestClient
from sqlalchemy import text
from sqlmodel import Session, select

from app.core.config import settings
from app.core.db import engine
from app.etl import reference
from app.etl.core import load_config
from app.main import app
from app.model.location import District
from app.model.reference import ReferenceFact, ReferenceTopic
from app.service.internal.ask.ask_service import DatasetRegistry, build_answer
from app.service.internal.ask.data_tools import DataToolError
from app.service.internal.ask.national_tools import NAEP_SOURCE, naep_results
from app.service.internal.ask import reference_tools
from app.service.internal.ask.reference_tools import look_up_reference, site, tool_definition
from app.service.public.reference_service import FACTS_PER_PAGE, MAX_FACTS_PER_PAGE

CONFIG = load_config(reference.CONFIG)

SHARED = """## district-transportation: {title}

- kind: local
- question_type: {question_type}
- description: Bus service.

1. {town}'s buses are run by a contractor. See table {town_lower}_ride_minutes.
   - source: https://example.org/{town_lower}
   - as_of: 2026-11-13
   - review_by: 2027-11-13
   - place: district {town}

## {town_lower}_ride_minutes: Ride Times

- unit: minutes
- period: 2026-27

| Place | Minutes |
|---|---|
| {town} | 35 |
"""

SAMPLE = """# A file

## Summary

1. Not a fact: a summary list.

## bullying-duties: What Schools Must Do About Bullying

- kind: rule
- question_type: rules
- description: What NH law requires after a bullying report.

1. Parents must be told within 48 hours of the report.
   - citation: RSA 193-F:4, II(i)
   - source: https://gc.nh.gov/rsa/html/XV/193-F/193-F-4.htm
   - as_of: 2026-11-08
   - review_by: 2027-08-15
2. A program's page, with no citation.
   - source: https://picnh.org/about-us/
   - as_of: Wayback snapshot 2026-10-30
   - review_by: 2027-11-08
   - place: district Rochester

## naep_g4_math_score: A Number Table

- unit: score

| Place | Value |
|---|---|

## Not retrieved

1. Something that couldn't be found.
"""


class ReferenceParseTests(unittest.TestCase):
    def test_fact_topics_are_read_and_other_sections_skipped(self):
        [topic] = reference.parse_file(SAMPLE, "sample.md", CONFIG)
        self.assertEqual((topic["slug"], topic["kind"], len(topic["facts"])), ("bullying-duties", "rule", 2))
        first, second = topic["facts"]
        self.assertEqual(first["citation"], "RSA 193-F:4, II(i)")
        self.assertNotIn("citation", second)
        self.assertEqual(second["place"], "district Rochester")
        self.assertEqual(reference._date(second["as_of"]), date(2026, 10, 30))

    def test_incomplete_facts_and_topics_stop_the_load(self):
        broken = [
            SAMPLE.replace("   - source: https://gc.nh.gov/rsa/html/XV/193-F/193-F-4.htm\n", ""),
            SAMPLE.replace("- kind: rule", "- kind: opinion"),
            SAMPLE.replace("   - review_by: 2027-08-15", "   - review_by: next year"),
            SAMPLE.replace("place: district Rochester", "place: county Strafford"),
            SAMPLE.replace("   - as_of: 2026-11-08", "   - as_of: 2026-11-08\n   - author: someone"),
            SAMPLE.replace("https://picnh.org/about-us/", "https://picnh.org/about-us/ (and its contact page)"),
        ]
        for text_ in broken:
            with self.assertRaises(ValueError):
                reference.parse_file(text_, "sample.md", CONFIG)

    def test_places_include_saus_and_schools_outside_the_state(self):
        for place in ("sau 9", "maine Fryeburg Academy", "town Jackson"):
            [topic] = reference.parse_file(SAMPLE.replace("district Rochester", place), "sample.md", CONFIG)
            self.assertEqual(topic["facts"][1]["place"], place)

    def test_a_statement_that_runs_onto_a_list_stops_the_load(self):
        with self.assertRaises(ValueError):
            reference.parse_file(SAMPLE.replace("   - citation: RSA 193-F:4, II(i)", "   - the reporting staff member\n   - citation: RSA 193-F:4, II(i)"),
                                 "sample.md", CONFIG)

    def test_a_fact_number_used_twice_stops_the_load(self):
        with self.assertRaises(ValueError):
            reference.parse_file(SAMPLE.replace("2. A program's page", "1. A program's page"), "sample.md", CONFIG)

    def test_number_tables_are_read_with_their_fields(self):
        [table] = reference.parse_tables(SHARED.format(title="Buses", question_type="local_practice", town="Albany", town_lower="albany"), "a.md")
        self.assertEqual((table["slug"], table["fields"]["unit"], table["columns"], table["rows"]),
                         ("albany_ride_minutes", "minutes", ["Place", "Minutes"], [["Albany", "35"]]))
        # A topic's own section isn't a table
        self.assertEqual([tb["slug"] for tb in reference.parse_tables(SAMPLE, "sample.md")], ["naep_g4_math_score"])

    def test_shared_topics_merge_across_files_and_tables_follow_their_facts(self):
        with tempfile.TemporaryDirectory() as directory:
            for town, question_type in (("Albany", "local_practice"), ("Madison", "local_practice")):
                with open(os.path.join(directory, f"{town.lower()}.md"), "w") as f:
                    f.write(SHARED.format(title=f"{town}'s Buses", question_type=question_type, town=town, town_lower=town.lower()))
            config = {**CONFIG, "directory": directory, "files": ["*.md"], "shared_topics": None}
            [topic] = reference.read_library(config)
            self.assertEqual((topic["slug"], topic["title"], topic["files"]), ("district-transportation", "Albany's Buses", ["albany.md", "madison.md"]))
            self.assertEqual([(f["file"], f["section_title"]) for f in topic["facts"]],
                             [("albany.md", "Albany's Buses"), ("madison.md", "Madison's Buses")])
            tables = reference.read_tables(config)
            reference.link_tables([topic], tables)
            self.assertEqual([(tb["fields"]["topic"], tb["fields"]["place"]) for tb in tables],
                             [("district-transportation", "district Albany"), ("district-transportation", "district Madison")])
            # The same topic can't be a different kind in another file
            with open(os.path.join(directory, "madison.md"), "w") as f:
                f.write(SHARED.format(title="Madison's Buses", question_type="rules", town="Madison", town_lower="madison"))
            with self.assertRaises(ValueError):
                reference.read_library(config)

    def test_facts_numbered_ten_and_up_keep_their_fields(self):
        facts = "".join(f"{n}. Fact {n}.\n{' ' * len(f'{n}. ')}- source: https://example.org/{n}\n{' ' * len(f'{n}. ')}- as_of: 2026-11-08\n"
                        f"{' ' * len(f'{n}. ')}- review_by: 2027-11-08\n" for n in range(1, 12))
        [topic] = reference.parse_file(f"## many: Many Facts\n\n- kind: term\n- question_type: terms\n- description: d\n\n{facts}", "sample.md", CONFIG)
        self.assertEqual(topic["facts"][10]["source"], "https://example.org/11")

    def test_the_library_files_parse_with_unique_topics(self):
        topics = reference.read_library(CONFIG)
        self.assertGreater(len(topics), 150)
        self.assertGreater(sum(len(t["facts"]) for t in topics), 1500)
        # Every file in the library contributes facts, and each topic appears once
        self.assertEqual({f["file"] for t in topics for f in t["facts"]}, set(reference.library_files(CONFIG)))
        self.assertEqual(len({t["slug"] for t in topics}), len(topics))

    def test_sourced_facts_outside_a_topic_stop_the_load(self):
        for heading in ("## How the Taxes and Aid Work", "## bullying-duties: What Schools Must Do About Bullying\n\n- question_type: rules"):
            text_ = SAMPLE.replace("## bullying-duties: What Schools Must Do About Bullying\n\n- kind: rule\n- question_type: rules", heading)
            with self.assertRaises(ValueError):
                reference.parse_file(text_, "sample.md", CONFIG)


class ReferenceDatabaseTests(unittest.TestCase):
    def setUp(self):
        self.session = Session(engine)

    def tearDown(self):
        self.session.rollback()
        self.session.close()

    def district(self, name):
        return self.session.exec(select(District).where(District.name == name)).first()

    def test_the_load_matches_the_files(self):
        topics = reference.read_library(CONFIG)
        self.assertEqual(len(self.session.exec(select(ReferenceTopic)).all()), len(topics))
        self.assertEqual(len(self.session.exec(select(ReferenceFact)).all()), sum(len(t["facts"]) for t in topics))
        # District practices are tied to their district
        rochester = self.district("Rochester")
        self.assertTrue(self.session.exec(select(ReferenceFact).where(ReferenceFact.district_id_fk == rochester.id)).first())
        # Every fact keeps its key, file and heading
        keys = self.session.execute(text("SELECT count(*), count(DISTINCT fact_key), count(section_title) FROM reference_fact")).one()
        self.assertEqual(len(set(keys)), 1)
        # Where each district's students go
        services = self.session.execute(text("SELECT count(*) FROM district_service")).scalar()
        self.assertEqual(services, len(reference.read_places(CONFIG)["district_service"]))

    def test_the_ask_tool_gives_facts_with_ids_and_keeps_links_aside(self):
        result = look_up_reference(self.session, ["bullying-school-duties"])
        [topic] = result["topics"]
        self.assertTrue(topic["facts"])
        fact = topic["facts"][0]
        self.assertTrue(fact["id"].startswith("r"))
        self.assertNotIn("url", fact)
        self.assertEqual(result["_sources"][fact["id"]]["site"], "gc.nh.gov")
        with self.assertRaises(DataToolError):
            look_up_reference(self.session, ["no-such-topic"])

    def test_district_practices_need_a_district(self):
        slug = self.session.exec(select(ReferenceTopic.slug).where(ReferenceTopic.kind == "local")).first()
        [without] = look_up_reference(self.session, [slug])["topics"]
        self.assertIn("note", without)
        merrimack = self.district("Merrimack")
        [with_district] = look_up_reference(self.session, [slug], merrimack.id)["topics"]
        ids = [int(f["id"][1:]) for f in with_district["facts"]]
        places = {self.session.get(ReferenceFact, i).district_id_fk for i in ids}
        self.assertTrue(places <= {merrimack.id, None})

    def test_a_district_gets_the_facts_of_the_schools_its_students_attend(self):
        jackson, merrimack = self.district("Jackson"), self.district("Merrimack")
        [entry] = look_up_reference(self.session, ["budget-form-and-vote-dates"], jackson.id)["topics"]
        places = [f.get("place") for f in entry["facts"]]
        # Jackson's own fact first, then Conway's (Kennett High), each named
        self.assertIn("Conway", places)
        self.assertLess(places.index("Jackson"), places.index("Conway"))
        [other] = look_up_reference(self.session, ["budget-form-and-vote-dates"], merrimack.id)["topics"]
        self.assertNotIn("Conway", [f.get("place") for f in other["facts"]])

    def test_a_district_gets_the_facts_of_the_districts_that_send_it_students(self):
        conway, jackson = self.district("Conway"), self.district("Jackson")
        souhegan, amherst = self.district("Souhegan Cooperative"), self.district("Amherst")
        # Conway's own fact first, then Jackson's, which tuitions its high school students to Kennett
        [entry] = look_up_reference(self.session, ["budget-form-and-vote-dates"], conway.id)["topics"]
        places = [f.get("place") for f in entry["facts"]]
        self.assertLess(places.index("Conway"), places.index("Jackson"))
        self.assertEqual(reference_tools.related_places(self.session, conway)[("district", jackson.id)], reference_tools.SENDS)
        # A cooperative gets its member districts' facts, and each member the cooperative's
        [coop] = look_up_reference(self.session, ["budget-form-and-vote-dates"], souhegan.id)["topics"]
        places = [f.get("place") for f in coop["facts"]]
        self.assertLess(places.index("Souhegan Cooperative"), places.index("Amherst"))
        self.assertIn("Mont Vernon", places)
        # Amherst sends its high school students to Souhegan and takes Mont Vernon's grades 7-8
        places = reference_tools.related_places(self.session, amherst)
        self.assertEqual((places[("district", souhegan.id)], places[("district", self.district("Mont Vernon").id)]),
                         (reference_tools.SERVES, reference_tools.SENDS))
        # Two districts don't share each other's facts just because they send students to the same place
        self.assertNotIn(("district", jackson.id), reference_tools.related_places(self.session, self.district("Albany")))

    def test_districts_that_share_a_town_say_how_their_students_go(self):
        # The state's district/town list links a cooperative or interstate district to its member towns; a
        # district_service row (places.yaml) must link it to each member district, which a change in next
        # year's list would break. Districts that run no grades, such as In-State Facility, don't count.
        missing = self.session.execute(text("""
            SELECT DISTINCT a.name || ' / ' || b.name
            FROM town_district_xref x JOIN town_district_xref y ON y.town_id_fk = x.town_id_fk AND y.district_id_fk > x.district_id_fk
            JOIN district a ON a.id = x.district_id_fk JOIN district b ON b.id = y.district_id_fk
            WHERE a.is_current AND b.is_current
              AND EXISTS (SELECT 1 FROM district_grade_xref g WHERE g.district_id_fk = a.id)
              AND EXISTS (SELECT 1 FROM district_grade_xref g WHERE g.district_id_fk = b.id)
              AND NOT EXISTS (SELECT 1 FROM district_service s WHERE (s.district_id_fk = a.id AND s.receiving_district_id_fk = b.id)
                                                                 OR (s.district_id_fk = b.id AND s.receiving_district_id_fk = a.id))
            ORDER BY 1""")).scalars().all()
        self.assertEqual(missing, [])

    def test_statewide_topics_keep_their_facts_about_places(self):
        [entry] = look_up_reference(self.session, ["cte-centers-overview"])["topics"]
        self.assertIn("Town of Berlin", [f.get("place") for f in entry["facts"]])

    def test_long_topics_are_capped_and_a_query_ranks_them(self):
        limit = reference_tools.MAX_FACTS
        reference_tools.MAX_FACTS = 3
        try:
            [entry] = look_up_reference(self.session, ["bullying-school-duties"])["topics"]
            self.assertEqual(len(entry["facts"]), 3)
            self.assertIn("more_facts", entry)
            [ranked] = look_up_reference(self.session, ["bullying-school-duties"], None, "48 hours parents notified")["topics"]
            self.assertIn("48 hours", ranked["facts"][0]["statement"])
        finally:
            reference_tools.MAX_FACTS = limit
        with self.assertRaises(DataToolError):
            look_up_reference(self.session, ["bullying-school-duties"], None, ["a list"])

    def test_tables_come_with_their_topic_and_can_be_cited(self):
        slug = self.session.execute(text(
            "SELECT t.slug FROM reference_table tb JOIN reference_topic t ON t.id = tb.reference_topic_id_fk "
            "WHERE tb.source_url IS NOT NULL AND t.kind <> 'local' LIMIT 1")).scalar()
        result = look_up_reference(self.session, [slug])
        [table, *_] = result["topics"][0]["tables"]
        self.assertTrue(table["id"].startswith("rt") and table["columns"])
        self.assertIn(table["id"], result["_sources"])

    def test_facts_past_their_review_date_are_withheld(self):
        topic = self.session.exec(select(ReferenceTopic).where(ReferenceTopic.slug == "bullying-school-duties")).one()
        fact = self.session.exec(select(ReferenceFact).where(ReferenceFact.reference_topic_id_fk == topic.id)).first()
        self.session.execute(text("UPDATE reference_fact SET review_by = :past WHERE id = :id"),
                             {"past": date.today() - timedelta(days=1), "id": fact.id})
        self.session.expire_all()
        [entry] = look_up_reference(self.session, ["bullying-school-duties"])["topics"]
        self.assertNotIn(f"r{fact.id}", [f["id"] for f in entry["facts"]])
        self.assertIn("facts_withheld", entry)

    def test_answers_link_only_to_sources_the_tools_returned(self):
        registry = DatasetRegistry()
        result = registry.add_reference(look_up_reference(self.session, ["bullying-school-duties"]))
        self.assertNotIn("_sources", result)
        fact_id = result["topics"][0]["facts"][0]["id"]
        cited = [{"id": fact_id, "reason": "  The 48-hour deadline\nto tell both families "}, {"id": "r999999", "reason": "Made up"},
                 {"id": "https://example.com", "reason": "A link Claude wrote"}]
        answer = build_answer({"status": "answered", "answer": ["..."], "sources": cited}, registry)
        self.assertEqual(len(answer["sources"]), 1)
        self.assertEqual(answer["sources"][0]["site"], "gc.nh.gov")
        self.assertEqual(answer["sources"][0]["reasons"], ["The 48-hour deadline to tell both families"])
        # A declined answer links nowhere
        self.assertEqual(build_answer({"status": "declined", "answer": ["..."], "sources": cited}, registry)["sources"], [])
        # Facts from the same page share one link, with each fact's reason
        by_url = {}
        for ident, source in registry.sources.items():
            by_url.setdefault(source["url"], []).append(ident)
        first, second = next(ids for ids in by_url.values() if len(ids) > 1)[:2]
        answer = build_answer({"status": "answered", "answer": ["..."],
                               "sources": [{"id": first, "reason": "One thing"}, {"id": second, "reason": "Another"}, {"id": second, "reason": "Another"}]}, registry)
        self.assertEqual([s["reasons"] for s in answer["sources"]], [["One thing", "Another"]])
        # Reasons are one short line of plain text, without links
        for reason, shown in (("See https://example.com", []), ("x" * 300, ["x" * 159 + "…"]), ("", [])):
            answer = build_answer({"status": "answered", "answer": ["..."], "sources": [{"id": fact_id, "reason": reason}]}, registry)
            self.assertEqual(answer["sources"][0]["reasons"], shown)
        # A chart from national data brings its source, even uncited
        registry.add(naep_results(self.session, "math", 8, "average_score", ["NH", "MA"], "All students"))
        answer = build_answer({"status": "answered", "answer": ["..."], "sources": [],
                               "charts": [{"dataset": "d1", "kind": "line", "title": "NAEP", "series": ["New Hampshire"]}]}, registry)
        self.assertEqual([s["site"] for s in answer["sources"]], ["nationsreportcard.gov"])
        self.assertEqual(answer["sources"][0]["reasons"], [])
        # Cited with a reason, the shared NAEP source is copied, not changed
        answer = build_answer({"status": "answered", "answer": ["..."], "sources": [{"id": "d1", "reason": "Scores by state"}]}, registry)
        self.assertEqual(answer["sources"][0]["reasons"], ["Scores by state"])
        self.assertNotIn("reasons", NAEP_SOURCE)

    def test_facts_about_this_site_are_used_but_not_linked(self):
        fact = self.session.exec(select(ReferenceFact).where(ReferenceFact.source_url == "https://nhfacts.com")).first()
        slug = self.session.get(ReferenceTopic, fact.reference_topic_id_fk).slug
        result = look_up_reference(self.session, [slug])
        self.assertIn(f"r{fact.id}", [f["id"] for f in result["topics"][0]["facts"]])
        self.assertNotIn(f"r{fact.id}", result["_sources"])

    def test_the_tool_checks_its_own_input(self):
        # Not strict, so the topic list doesn't count toward the API's grammar limit
        self.assertNotIn("strict", tool_definition())
        self.assertIn("bullying-school-duties", tool_definition()["input_schema"]["properties"]["topics"]["items"]["enum"])
        self.assertIn("query", tool_definition()["input_schema"]["properties"])
        for topics, district_id in (("bullying-school-duties", None), ([1], None), (["bullying-school-duties"], "335")):
            with self.assertRaises(DataToolError):
                look_up_reference(self.session, topics, district_id)

    def test_sites_drop_www(self):
        self.assertEqual(site("https://www.ecfr.gov/current/title-34"), "ecfr.gov")


class ReferenceApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api = TestClient(app)
        cls.url = f"{settings.API_V1_STR}/reference"

    def test_topics_facts_and_the_review_report(self):
        topics = self.api.get(f"{self.url}/topic", params={"kind": "rule"}).json()
        self.assertTrue(topics and all(t["kind"] == "rule" for t in topics))
        topic = self.api.get(f"{self.url}/topic/bullying-school-duties").json()
        self.assertEqual(topic["slug"], "bullying-school-duties")
        self.assertTrue(all(f["source_url"].startswith("http") for f in topic["facts"]))
        self.assertTrue(all(f["section_title"] and f["source_file"] for f in topic["facts"]))
        self.assertEqual(self.api.get(f"{self.url}/topic/no-such-topic").status_code, 404)
        review = self.api.get(f"{self.url}/review", params={"within_days": 730}).json()
        self.assertTrue(review)
        self.assertEqual([r["review_by"] for r in review], sorted(r["review_by"] for r in review))

    def test_a_topics_facts_come_a_page_at_a_time(self):
        biggest = max(self.api.get(f"{self.url}/topic").json(), key=lambda t: t["current_facts"])
        total = biggest["current_facts"]
        self.assertGreater(total, FACTS_PER_PAGE)
        url = f"{self.url}/topic/{biggest['slug']}"
        first = self.api.get(url).json()
        self.assertEqual((first["current_facts"], first["offset"], first["limit"], len(first["facts"])), (total, 0, FACTS_PER_PAGE, FACTS_PER_PAGE))
        # The pages follow on, in load order, without repeating a fact
        second = self.api.get(url, params={"offset": FACTS_PER_PAGE, "limit": 10}).json()
        ids = [f["id"] for f in first["facts"] + second["facts"]]
        self.assertEqual(ids, sorted(set(ids)))
        self.assertEqual(len(second["facts"]), 10)
        self.assertEqual(self.api.get(url, params={"offset": total}).json()["facts"], [])
        for params in ({"limit": 0}, {"limit": MAX_FACTS_PER_PAGE + 1}, {"offset": -1}):
            self.assertEqual(self.api.get(url, params=params).status_code, 422)


if __name__ == "__main__":
    unittest.main()
