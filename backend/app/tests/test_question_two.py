"""
Tests for the Question 2 results load and API, run against the local database after
`alembic upgrade head`:

    docker exec -w /app education-backend-backend-1 python -m unittest app.tests.test_question_two -v
"""
import unittest

import pandas as pd
from fastapi.testclient import TestClient

from app.core.config import settings
from app.etl import question_two
from app.main import app

COLUMNS = ["district", "wmur_name", "yes_votes", "no_votes", "yes_percent", "result", "towns"]


def results(*rows):
    return pd.DataFrame([dict(zip(COLUMNS, row)) for row in rows], columns=COLUMNS)


class QuestionTwoParseTests(unittest.TestCase):
    def test_a_district_passes_with_sixty_percent_yes(self):
        rows = question_two.parse_file(results(
            ("Fall Mountain Regional", "Fall Mountain Regional School District", 3160, 2092, 60.2, "PASS", "Acworth; Alstead"),
            ("Andover", "Andover School District", 604, 549, 52.4, "FAIL", "Andover"),
        ), 60, "test.csv")
        self.assertEqual(rows[0], {"district": "Fall Mountain Regional", "yes": 3160, "no": 2092, "percent": 60.2, "passed": True})
        self.assertFalse(rows[1]["passed"])

    def test_a_result_that_disagrees_with_the_votes_stops_the_load(self):
        # 59.9% yes marked PASS
        with self.assertRaises(ValueError):
            question_two.parse_file(results(("Acworth", "", 275, 184, 59.9, "PASS", "")), 60, "test.csv")
        # A share that doesn't match the votes
        with self.assertRaises(ValueError):
            question_two.parse_file(results(("Andover", "", 604, 549, 62.4, "PASS", "")), 60, "test.csv")
        # A district listed twice
        with self.assertRaises(ValueError):
            question_two.parse_file(results(("Andover", "", 604, 549, 52.4, "FAIL", ""), ("Andover", "", 604, 549, 52.4, "FAIL", "")), 60, "test.csv")

    def test_the_2026_file_checks_out(self):
        config = question_two.load_config(question_two.CONFIG)
        election = config["elections"][2026]
        df = pd.read_csv(question_two.config_path(f"{config['directory']}/{election['file']}"), dtype={"district": str})
        rows = question_two.parse_file(df, config["threshold_percent"], election["file"])
        self.assertEqual(len(rows), 179)
        self.assertEqual(sum(r["passed"] for r in rows), 93)


class QuestionTwoApiTests(unittest.TestCase):
    """Against the loaded database"""

    @classmethod
    def setUpClass(cls):
        cls.api = TestClient(app)
        cls.url = f"{settings.API_V1_STR}/question-two/district"

    def get(self, **params):
        response = self.api.get(self.url, params=params)
        self.assertEqual(response.status_code, 200, response.text)
        return response.json()

    def test_every_district_that_voted_in_2026(self):
        rows = self.get(year=2026)
        self.assertEqual(len(rows), 179)
        self.assertEqual(sum(r["passed"] for r in rows), 93)
        self.assertFalse(any(r["is_official"] for r in rows))
        self.assertEqual([r["district_name"] for r in rows], sorted(r["district_name"] for r in rows))

    def test_a_multi_town_district_adds_up_its_towns(self):
        fall_mountain = next(r for r in self.get(year=2026) if r["district_name"] == "Fall Mountain Regional")
        self.assertEqual((fall_mountain["yes_votes"], fall_mountain["no_votes"], fall_mountain["yes_percentage"], fall_mountain["passed"]),
                         (3160, 2092, 60.2, True))

    def test_filters(self):
        coos = next(r for r in self.get(year=2026) if r["district_name"] == "Coos County School District")
        self.assertEqual(self.get(district_id=coos["district_id"]), [coos])
        self.assertEqual((coos["yes_votes"], coos["no_votes"], coos["passed"]), (4, 14, False))
        self.assertEqual(len(self.get(year=2026, passed=True)), 93)
        self.assertEqual(self.get(year=2028), [])
