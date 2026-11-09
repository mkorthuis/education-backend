"""
Tests for the NAEP data load and API, run against the local database after `alembic upgrade head`:

    docker exec -w /app education-backend-backend-1 python -m unittest app.tests.test_naep -v
"""
import unittest

from fastapi.testclient import TestClient

from app.core.config import settings
from app.etl import naep
from app.etl.core import load_config
from app.main import app

CONFIG = load_config(naep.CONFIG)


def result(**fields):
    return {"year": 2024, "sample": "R3", "stattype": "MN:MN", "subject": "MAT", "grade": 4, "jurisdiction": "NH",
            "variable": "TOTAL", "varValue": "1", "value": 242.3, "isStatDisplayable": 1, "errorFlag": 0, **fields}


def place_test(**fields):
    return {"year": 2024, "sample": "R3", "statType": "MN:MN", "subject": "MAT", "grade": 8, "focalJurisdiction": "NH",
            "targetJurisdiction": "MA", "variable": "TOTAL", "valValue": "1", "gap": -3.72, "sig": "EQUAL",
            "isSigDisplayable": 1, "focalErrorFlag": 0, "targetErrorFlag": 0, **fields}


class NaepParseTests(unittest.TestCase):
    def test_results_keep_unrounded_values_and_mark_figures_naep_doesnt_report(self):
        rows = naep.parse_results([result(), result(jurisdiction="MA", value=99.0, isStatDisplayable=0, errorFlag=257)], CONFIG)
        self.assertEqual(rows[(2024, "NH", "mat", "Grade 4", "MN:MN", ("TOTAL", "1"))], (242.3, True))
        self.assertEqual(rows[(2024, "MA", "mat", "Grade 4", "MN:MN", ("TOTAL", "1"))], (None, False))

    def test_unexpected_samples_places_measures_and_groups_stop_the_load(self):
        for bad in (result(sample="R2"), result(jurisdiction="XX"), result(stattype="SD:SD"),
                    result(variable="ECONDIS", varValue="3"), result(variable="PARED", varValue="1")):
            with self.assertRaises(ValueError):
                naep.parse_results([bad], CONFIG)

    def test_reporting_follows_naeps_displayable_marker_not_its_footnote_flags(self):
        # A small share at Advanced that NAEP reports, though its footnote flags include bit 256
        reported = naep.parse_results([result(variable="IEP2009", varValue="1", stattype="ALC:AD", value=0.88,
                                              errorFlag=33554690)], CONFIG)
        self.assertEqual(list(reported.values()), [(0.88, True)])
        withheld = naep.parse_results([result(variable="SRACE10", varValue="2", isStatDisplayable=0, errorFlag=4194561)], CONFIG)
        self.assertEqual(list(withheld.values()), [(None, False)])

    def test_student_groups_keep_their_variable_and_category(self):
        rows = naep.parse_results([result(variable="GENDER", varValue="2", value=239.6)], CONFIG)
        self.assertEqual(rows, {(2024, "NH", "mat", "Grade 4", "MN:MN", ("GENDER", "2")): (239.6, True)})
        # The fetch keeps only the configured categories, so "Information not available" isn't saved
        kept = naep.keep("group-results", [result(variable="ECONDIS", varValue="1"), result(variable="ECONDIS", varValue="3")], CONFIG)
        self.assertEqual([r["varValue"] for r in kept], ["1"])

    def test_comparisons_keep_the_basis_and_naeps_verdict(self):
        tests = naep.parse_comparisons("states", [place_test(), place_test(statType="ALC:AP", sig="LOWER", gap=-5.2),
                                                  place_test(targetJurisdiction="TX", isSigDisplayable=0)], CONFIG)
        group = ("TOTAL", "1")
        self.assertEqual(tests[(2024, "NH", 2024, "MA", "mat", "Grade 8", "MN:MN", group, "all_jurisdictions")], ("not_significant", -3.72))
        self.assertEqual(tests[(2024, "NH", 2024, "MA", "mat", "Grade 8", "ALC:AP", group, "all_jurisdictions")], ("lower", -5.2))
        # A test NAEP couldn't report is left out
        self.assertEqual(len(tests), 2)
        years = naep.parse_comparisons("years", [{
            "focalYear": 2024, "targetYear": 2019, "focalSample": "R3", "targetSample": "R3", "statType": "MN:MN",
            "subject": "RED", "grade": 8, "jurisdiction": "NH", "variable": "TOTAL", "valValue": "1", "gap": -4.1,
            "sig": "LOWER", "isSigDisplayable": 1, "focalErrorFlag": 0, "targetErrorFlag": 0,
        }], CONFIG)
        self.assertEqual(years, {(2024, "NH", 2019, "NH", "rea", "Grade 8", "MN:MN", group, "pair"): ("lower", -4.1)})

    def test_the_fetch_keeps_new_hampshires_comparisons_and_the_latest_year(self):
        kept = naep.keep("states", [place_test(), place_test(focalJurisdiction="MA", targetJurisdiction="NH")], CONFIG)
        self.assertEqual([r["focalJurisdiction"] for r in kept], ["NH"])
        self.assertEqual(set(kept[0]), set(naep.FIELDS["states"]))
        plan = naep.requests_for(CONFIG)
        # One request per pair of years, the latest against each earlier year
        self.assertEqual(len(plan[("years", "reading", 8)]), len(CONFIG["years"]) - 1)
        self.assertIn("Year=2003,2024", plan[("years", "reading", 8)][0])


class NaepApiTests(unittest.TestCase):
    """Against the loaded database"""

    @classmethod
    def setUpClass(cls):
        cls.api = TestClient(app)
        cls.url = f"{settings.API_V1_STR}/naep"
        cls.measures = {m["code"]: m["id"] for m in cls.api.get(f"{cls.url}/measure").json()}
        cls.groups = {(g["variable"], g["value"]): g["id"] for g in cls.api.get(f"{cls.url}/student-group").json()}
        cls.everyone = cls.groups[("TOTAL", "1")]

    def get(self, path, **params):
        response = self.api.get(f"{self.url}/{path}", params=params)
        self.assertEqual(response.status_code, 200, response.text)
        return response.json()

    def test_places_are_the_nation_the_states_dc_and_dodea(self):
        places = self.get("jurisdiction")
        # NAEP's nation (national public) and the Census's (the United States) share the table
        self.assertEqual(len(places), 54)
        self.assertEqual(places[0]["code"], "NP")
        self.assertIn("US", [p["code"] for p in places])
        self.assertEqual({p["kind"] for p in places}, {"nation", "state", "other"})

    def test_results_cover_every_place_and_year(self):
        rows = self.get("result", jurisdiction="nh", assessment_subject_id=1, grade_id=6, naep_measure_id=self.measures["MN:MN"],
                        naep_student_group_id=self.everyone)
        self.assertEqual([r["year"] for r in rows], CONFIG["years"])
        latest = rows[-1]
        self.assertEqual((latest["jurisdiction"]["code"], latest["grade"]["name"], latest["measure"]["unit"]), ("NH", "Grade 4", "score"))
        # NAEP publishes 242 for New Hampshire's 2024 grade 4 math average
        self.assertEqual(round(latest["value"]), 242)
        one_year = self.get("result", year=2024, assessment_subject_id=2, grade_id=10, naep_measure_id=self.measures["ALC:AP"],
                            naep_student_group_id=self.everyone)
        self.assertEqual(len(one_year), 53)

    def test_comparisons_follow_naeps_all_state_tests(self):
        # Against every state at once, Massachusetts's 2024 grade 8 math average isn't significantly different
        # from New Hampshire's, though the share at Proficient is
        tests = self.get("comparison", year=2024, assessment_subject_id=1, grade_id=10, jurisdiction="NH",
                         other_jurisdiction="MA", basis="all_jurisdictions")
        verdicts = {t["measure"]["code"]: t["result"] for t in tests}
        self.assertEqual(verdicts, {"MN:MN": "not_significant", "ALC:AP": "lower"})
        # Every other state, DC and DoDEA, for each compared measure
        all_states = self.get("comparison", year=2024, assessment_subject_id=1, grade_id=6, jurisdiction="NH",
                              basis="all_jurisdictions")
        self.assertEqual(len(all_states), 51 * len(CONFIG["compared_measures"]))
        nation = self.get("comparison", year=2024, assessment_subject_id=1, grade_id=6, jurisdiction="NH",
                          other_jurisdiction="NP", naep_measure_id=self.measures["MN:MN"], naep_student_group_id=self.everyone)
        self.assertEqual([(t["basis"], t["result"]) for t in nation], [("pair", "higher")])

    def test_year_comparisons_set_the_latest_year_against_each_earlier_one(self):
        tests = self.get("comparison", year=2024, jurisdiction="NH", other_jurisdiction="NH", assessment_subject_id=2,
                         grade_id=10, naep_measure_id=self.measures["MN:MN"], naep_student_group_id=self.everyone)
        self.assertEqual([t["other_year"] for t in tests], CONFIG["years"][:-1])
        self.assertTrue(all(t["basis"] == "pair" for t in tests))

    def test_student_groups_are_loaded_for_new_hampshire_and_the_nation(self):
        groups = self.get("student-group")
        self.assertEqual(len(groups), sum(len(g["values"]) for g in CONFIG["student_groups"].values()))
        self.assertEqual(groups[0]["name"], "All students")
        low_income = self.get("result", year=2024, assessment_subject_id=1, grade_id=6, naep_measure_id=self.measures["MN:MN"],
                              naep_student_group_id=self.groups[("ECONDIS", "1")])
        self.assertEqual(sorted(r["jurisdiction"]["code"] for r in low_income), ["NH", "NP"])
        self.assertTrue(all(r["is_displayable"] and r["value"] for r in low_income))
        # Too few Black eighth graders in New Hampshire for NAEP to report their reading results
        black = self.get("result", year=2024, assessment_subject_id=2, grade_id=10, jurisdiction="NH",
                         naep_measure_id=self.measures["MN:MN"], naep_student_group_id=self.groups[("SRACE10", "2")])
        self.assertEqual([(r["is_displayable"], r["value"]) for r in black], [(False, None)])
        # New Hampshire's groups are tested against the nation's and against their own earlier years
        for other in ("NP", "NH"):
            tests = self.get("comparison", year=2024, jurisdiction="NH", other_jurisdiction=other, assessment_subject_id=1,
                             grade_id=6, naep_measure_id=self.measures["MN:MN"], naep_student_group_id=self.groups[("ECONDIS", "1")])
            self.assertTrue(tests and all(t["basis"] == "pair" for t in tests))

    def test_a_bad_basis_is_refused(self):
        self.assertEqual(self.api.get(f"{self.url}/comparison", params={"basis": "any"}).status_code, 422)


if __name__ == "__main__":
    unittest.main()
