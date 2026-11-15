"""
Tests for the NAEP state standard load (NCES's state mapping study) and API, run against the local database after
`alembic upgrade head`:

    docker exec -w /app education-backend-backend-1 python -m unittest app.tests.test_naep_state_standard -v
"""
import copy
import unittest

from sqlalchemy import text

from app.core.db import engine
from app.etl import naep_state_standard
from app.etl.core import load_config

CONFIG = load_config(naep_state_standard.CONFIG)
TABLES = [f"{year}{letter}" for year in CONFIG["years"] for letter in "ab"] + [f"{n}{letter}" for n in (1, 2, 3) for letter in "ab"]


class NaepStateStandardParseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = naep_state_standard.read(CONFIG)
        naep_state_standard.check(cls.rows)

    def find(self, table, place, subject, grade):
        [row] = [r for r in self.rows if (r["nces_table"], r["place"], r["subject"], r["grade"]) == (table, place, subject, grade)]
        return row

    def test_every_table_has_each_state_and_dc_in_both_subjects_and_grades(self):
        for table in TABLES:
            rows = [r for r in self.rows if r["nces_table"] == table]
            self.assertEqual(len({r["place"] for r in rows}), 51, table)
            self.assertEqual(len(rows), 102, table)
        self.assertEqual(len(self.rows), 2040)

    def test_new_hampshires_per_year_scores_are_unrounded(self):
        nh = self.find("2022a", "New Hampshire", "mat", 4)
        self.assertAlmostEqual(nh["naep_equivalent"], 242.911045, places=5)
        self.assertAlmostEqual(nh["standard_error"], 0.790978, places=5)
        self.assertEqual((nh["testing_program"], nh["caution"]), (None, False))
        self.assertAlmostEqual(self.find("2013b", "New Hampshire", "rea", 8)["naep_equivalent"], 245.021578, places=5)

    def test_2009_has_the_per_year_and_the_2005_2009_studys_estimates(self):
        self.assertAlmostEqual(self.find("2009a", "New Hampshire", "rea", 4)["naep_equivalent"], 210.102436, places=5)
        study = self.find("1a", "New Hampshire", "rea", 4)
        self.assertEqual((study["year"], study["naep_equivalent"], study["standard_error"], study["relative_error"]),
                         (2009, 211.0, 1.1, None))
        self.assertEqual(study["note"], "States that test in the fall.")
        self.assertEqual(self.find("2b", "New Hampshire", "mat", 4)["naep_equivalent"], 239.0)

    def test_a_state_left_out_keeps_ncess_reason(self):
        for table, grade in (("2017a", 4), ("2019b", 8)):
            nh = self.find(table, "New Hampshire", "mat", grade)
            self.assertIsNone(nh["naep_equivalent"])
            self.assertEqual(nh["note"], "New Hampshire was not included in the study because the state did not use the same "
                                         f"assessment for all students in grade {grade} for reading and mathematics.")
        self.assertEqual(self.find("3a", "New Hampshire", "rea", 4)["note"], "State assessment data not available.")

    def test_a_note_about_one_subject_goes_on_that_subjects_rows_and_names_the_right_state(self):
        # "West Virginia was not included in grade 4 reading": not on its math row, and not on Virginia's
        self.assertIn("reading data were not available", self.find("2019a", "West Virginia", "rea", 4)["note"])
        self.assertIsNone(self.find("2019a", "West Virginia", "mat", 4)["note"])
        self.assertIsNone(self.find("2019a", "Virginia", "rea", 4)["note"])
        # Footnote 1 marks Connecticut's name
        self.assertIn("Connecticut, Montana, and Oregon were not included in estimating the SBAC reading standard",
                      self.find("2022a", "Connecticut", "rea", 4)["note"])

    def test_a_state_row_repeating_its_consortiums_estimate_says_so(self):
        # In 2015 grade 8, NCES's table gives every SBAC state's row the SBAC-wide estimate (Wisconsin's reading aside)
        nh = self.find("2015b", "New Hampshire", "rea", 8)
        self.assertEqual((nh["testing_program"], nh["note"]), ("SBAC", "NCES's table gives the SBAC estimate for this state."))
        self.assertEqual(self.find("2015b", "California", "rea", 8)["naep_equivalent"], nh["naep_equivalent"])
        self.assertNotIn("SBAC estimate", self.find("2015b", "Wisconsin", "rea", 8)["note"] or "")
        self.assertIsNone(self.find("2015a", "New Hampshire", "rea", 4)["note"])

    def test_the_caution_mark_follows_the_relative_error(self):
        marked = [r for r in self.rows if r["caution"] and r["relative_error"] is not None]
        self.assertTrue(marked and all(r["relative_error"] > 0.5 for r in marked))
        self.assertTrue(self.find("1a", "Georgia", "rea", 4)["caution"])  # "!" on the 2005–2009 study's page

    def test_rows_that_dont_hold_together_stop_the_load(self):
        for change in ({"caution": True}, {"standard_error": None}, {"naep_equivalent": 520.0}):
            rows = copy.deepcopy(self.rows)
            rows[0].update(change)
            with self.assertRaises(ValueError):
                naep_state_standard.check(rows)
        with self.assertRaisesRegex(ValueError, "twice"):
            naep_state_standard.check(self.rows + self.rows[:1])

    def test_an_unknown_place_stops_the_load(self):
        config = copy.deepcopy(CONFIG)
        config["not_loaded"] = []
        with self.assertRaisesRegex(ValueError, "Puerto Rico"):
            naep_state_standard.read(config)


class NaepStateStandardLoadTests(unittest.TestCase):
    def query(self, sql, **params):
        with engine.connect() as conn:
            return conn.execute(text(sql), params).all()

    def test_every_table_is_loaded(self):
        self.assertEqual(sorted(t for (t,) in self.query("SELECT DISTINCT nces_table FROM naep_state_standard")), sorted(TABLES))
        self.assertEqual(self.query("SELECT count(*), count(naep_equivalent) FROM naep_state_standard")[0], (2040, 1860))

    def test_reloading_changes_nothing(self):
        with engine.connect() as conn:
            counts = naep_state_standard.load(conn)
            conn.rollback()
        self.assertEqual(counts["naep_state_standard"]["unchanged"], 2040)
        with engine.connect() as conn, self.assertRaisesRegex(ValueError, "2021"):
            naep_state_standard.load(conn, [2021])


class NaepStateStandardApiTests(unittest.TestCase):
    """Against the loaded database (the app needs the backend's image: python -m unittest in Docker)"""

    @classmethod
    def setUpClass(cls):
        from fastapi.testclient import TestClient
        from app.core.config import settings
        from app.main import app
        cls.api, cls.prefix = TestClient(app), f"{settings.API_V1_STR}/naep/state-standard"

    def get(self, **params):
        response = self.api.get(self.prefix, params=params)
        self.assertEqual(response.status_code, 200, response.text)
        return response.json()

    def test_new_hampshire_by_year(self):
        rows = self.get(jurisdiction="nh")
        self.assertEqual(sorted({r["year"] for r in rows}), [2005, 2007, 2009, 2011, 2013, 2015, 2017, 2019, 2022])
        self.assertEqual(len(rows), 40)
        g4_math = [(r["year"], r["nces_table"], r["naep_equivalent"] and round(r["naep_equivalent"]))
                   for r in rows if r["subject"]["name"] == "mat" and r["grade"]["name"] == "Grade 4"]
        self.assertEqual(g4_math, [(2005, "3b", None), (2007, "2b", 239), (2009, "2009a", 234), (2009, "1b", 237),
                                   (2011, "2011a", 237), (2013, "2013a", 235), (2015, "2015a", 250), (2017, "2017a", None),
                                   (2019, "2019a", None), (2022, "2022a", 243)])

    def test_filters(self):
        rows = self.get(year=2022, grade_id=10, assessment_subject_id=2)
        self.assertEqual(len(rows), 51)
        ma = next(r for r in rows if r["jurisdiction"]["code"] == "MA")
        self.assertEqual((ma["nces_table"], ma["grade"]["name"], ma["subject"]["name"]), ("2022b", "Grade 8", "rea"))
        self.assertEqual(self.get(year=2021), [])
