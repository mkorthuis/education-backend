"""
Tests for the reference library: parsing the Markdown, the load, the Ask's look_up_reference tool,
the outside sources an answer may link to, and the API. Run against the local database after
`alembic upgrade head`:

    docker exec -w /app education-backend-backend-1 python -m unittest app.tests.test_reference -v
"""
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
from app.service.internal.ask.national_tools import naep_results
from app.service.internal.ask.reference_tools import look_up_reference, site

CONFIG = load_config(reference.CONFIG)

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

    def test_facts_numbered_ten_and_up_keep_their_fields(self):
        facts = "".join(f"{n}. Fact {n}.\n{' ' * len(f'{n}. ')}- source: https://example.org/{n}\n{' ' * len(f'{n}. ')}- as_of: 2026-11-08\n"
                        f"{' ' * len(f'{n}. ')}- review_by: 2027-11-08\n" for n in range(1, 12))
        [topic] = reference.parse_file(f"## many: Many Facts\n\n- kind: term\n- question_type: terms\n- description: d\n\n{facts}", "sample.md", CONFIG)
        self.assertEqual(topic["facts"][10]["source"], "https://example.org/11")

    def test_the_library_files_parse_with_unique_topics(self):
        topics = reference.read_library(CONFIG)
        self.assertGreater(len(topics), 150)
        self.assertGreater(sum(len(t["facts"]) for t in topics), 1500)
        self.assertEqual(len({t["slug"] for t in topics}), len(topics))


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
        answer = build_answer({"status": "answered", "answer": ["..."], "sources": [fact_id, "r999999", "https://example.com"]}, registry)
        self.assertEqual(len(answer["sources"]), 1)
        self.assertEqual(answer["sources"][0]["site"], "gc.nh.gov")
        # A declined answer links nowhere
        self.assertEqual(build_answer({"status": "declined", "answer": ["..."], "sources": [fact_id]}, registry)["sources"], [])
        # A chart from national data brings its source, even uncited
        registry.add(naep_results(self.session, "math", 8, "average_score", ["NH", "MA"], "All students"))
        answer = build_answer({"status": "answered", "answer": ["..."], "sources": [],
                               "charts": [{"dataset": "d1", "kind": "line", "title": "NAEP", "series": ["New Hampshire"]}]}, registry)
        self.assertEqual([s["site"] for s in answer["sources"]], ["nationsreportcard.gov"])

    def test_facts_about_this_site_are_used_but_not_linked(self):
        fact = self.session.exec(select(ReferenceFact).where(ReferenceFact.source_url == "https://nhfacts.com")).first()
        slug = self.session.get(ReferenceTopic, fact.reference_topic_id_fk).slug
        result = look_up_reference(self.session, [slug])
        self.assertIn(f"r{fact.id}", [f["id"] for f in result["topics"][0]["facts"]])
        self.assertNotIn(f"r{fact.id}", result["_sources"])

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
        self.assertEqual(self.api.get(f"{self.url}/topic/no-such-topic").status_code, 404)
        review = self.api.get(f"{self.url}/review", params={"within_days": 730}).json()
        self.assertTrue(review)
        self.assertEqual([r["review_by"] for r in review], sorted(r["review_by"] for r in review))


if __name__ == "__main__":
    unittest.main()
