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
        self.assertEqual(rows[0], {"district": "Fall Mountain Regional", "yes": 3160, "no": 2092, "percent": 60.2, "note": None,
                                   "passed": True, "towns": "Acworth; Alstead"})
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

    def test_a_town_has_no_result_of_its_own(self):
        towns = pd.DataFrame([{"town": "Acworth", "yes_votes": 275, "no_votes": 184, "yes_percent": 59.9}])
        self.assertEqual(question_two.parse_file(towns, 60, "towns.csv", "town", decides=False),
                         [{"town": "Acworth", "yes": 275, "no": 184, "percent": 59.9, "note": None}])

    def test_the_2026_files_check_out(self):
        config = question_two.load_config(question_two.CONFIG)
        election = config["elections"][2026]
        found = {}
        for level, (_, key, _, decides) in question_two.LEVELS.items():
            df = pd.read_csv(question_two.config_path(f"{config['directory']}/{election[level]}"), dtype={key: str})
            found[level] = question_two.parse_file(df, config["threshold_percent"], election[level], key, decides)
        self.assertEqual((len(found["districts"]), sum(r["passed"] for r in found["districts"])), (179, 93))
        self.assertEqual((len(found["saus"]), sum(r["passed"] for r in found["saus"])), (107, 60))
        self.assertEqual(len(found["towns"]), 236)
        # Every total is its towns' own votes added up, as the source counts them. Concord votes in two
        # parts, each the rest of its total; wherever a part appears it's the same, and the two make the city's
        votes = {r["town"]: (r["yes"], r["no"]) for r in found["towns"]}
        parts = {}
        for r in [*found["districts"], *found["saus"]]:
            whole = [votes[t] for t in r["towns"].split("; ") if t in votes]
            remainder = (r["yes"] - sum(v[0] for v in whole), r["no"] - sum(v[1] for v in whole))
            missing = [t for t in r["towns"].split("; ") if t not in votes]
            if missing:
                self.assertEqual(len(missing), 1, r)
                parts.setdefault(missing[0], set()).add(remainder)
            else:
                self.assertEqual(remainder, (0, 0), r)
        self.assertEqual(sorted(parts), ["Concord (the part in Merrimack Valley)", "Concord (the part in the Concord School District)"])
        self.assertTrue(all(len(found) == 1 for found in parts.values()))
        self.assertEqual(tuple(map(sum, zip(*(next(iter(found)) for found in parts.values())))), votes["Concord"])


class QuestionTwoApiTests(unittest.TestCase):
    """Against the loaded database"""

    @classmethod
    def setUpClass(cls):
        cls.api = TestClient(app)

    def get(self, **params):
        return self.get_from("district", **params)

    def get_from(self, level, **params):
        response = self.api.get(f"{settings.API_V1_STR}/question-two/{level}", params=params)
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

    def test_saus_give_the_spending_cap_vote_with_their_districts_and_notes(self):
        saus = self.get_from("sau", year=2026)
        self.assertEqual((len(saus), sum(r["passed"] for r in saus)), (107, 60))
        self.assertEqual([r["sau_id"] for r in saus], sorted(r["sau_id"] for r in saus))
        concord = self.get_from("sau", sau_id=8)[0]
        self.assertEqual((concord["districts"], concord["towns"], concord["yes_votes"], concord["passed"]),
                         (["Concord"], ["Concord (the part in the Concord School District)"], 8289, False))
        # Where WMUR's listing puts a town in the wrong SAU, the note says so
        self.assertIn("Allenstown", self.get_from("sau", sau_id=4)[0]["note"])
        self.assertIn("Allenstown", self.get_from("sau", sau_id=53)[0]["note"])
        self.assertEqual(self.get_from("sau", sau_id=90), [])

    def test_towns_give_their_own_vote(self):
        towns = self.get_from("town", year=2026)
        self.assertEqual(len(towns), 236)
        concord = next(r for r in towns if r["town_name"] == "Concord")
        self.assertEqual((concord["yes_votes"], concord["no_votes"]), (8289 + 1130, 7497 + 1013))  # its two parts
        self.assertIn("two parts", concord["note"])
        fall_mountain = next(r for r in self.get(year=2026) if r["district_name"] == "Fall Mountain Regional")
        self.assertEqual(fall_mountain["towns"], ["Acworth", "Alstead", "Charlestown", "Langdon", "Walpole"])
        by_district = self.get_from("town", district_id=fall_mountain["district_id"])
        self.assertEqual([r["town_name"] for r in by_district], fall_mountain["towns"])
        self.assertEqual(sum(r["yes_votes"] for r in by_district), fall_mountain["yes_votes"])

    def test_filters(self):
        coos = next(r for r in self.get(year=2026) if r["district_name"] == "Coos County School District")
        self.assertEqual(self.get(district_id=coos["district_id"]), [coos])
        self.assertEqual((coos["yes_votes"], coos["no_votes"], coos["passed"]), (4, 14, False))
        self.assertEqual(len(self.get(year=2026, passed=True)), 93)
        self.assertEqual(self.get(year=2028), [])
