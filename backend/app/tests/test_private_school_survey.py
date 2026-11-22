"""
Tests for the NCES Private School Survey load, run against the local database after `alembic upgrade head`:

    docker exec -w /app education-backend-backend-1 python -m unittest app.tests.test_private_school_survey -v
"""
import csv
import os
import tempfile
import unittest
from decimal import Decimal

from sqlalchemy import text

from app.core.db import engine
from app.etl import private_school_survey
from app.etl.core import config_path, load_config

CONFIG = load_config(private_school_survey.CONFIG)
DIRECTORY = config_path(CONFIG["directory"])
GRADE_IDS = {"Preschool": 1, "Kindergarten": 2, **{f"Grade {n}": n + 2 for n in range(1, 13)}}


class PrivateSurveyReadTests(unittest.TestCase):
    columns = ["PPIN", "TYPOLOGY", "RELIG", "ORIENT", "LEVEL", "UCOMMTYP", "NUMSTUDS", "P305", "MALES", "P350", "P360",
               "NUMTEACH", "STTCH_RT", "TOTHRS", "P_INDIAN", "P_ASIAN", "P_PACIFIC", "P_HISP", "P_WHITE", "P_BLACK", "P_TR",
               "P150", "P160", "P170", "P180", "P190", "P300"]

    def read(self, *records, matches=None, year=2024):
        with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.columns)
            writer.writeheader()
            writer.writerows(records)
        try:
            return private_school_survey.survey_rows(f.name, year, matches or {"00000001": (1, None)}, CONFIG, GRADE_IDS)
        finally:
            os.unlink(f.name)

    def record(self, **values):
        base = dict(PPIN="00000001", TYPOLOGY="4", RELIG="2", ORIENT="8", LEVEL="3", UCOMMTYP="3", NUMSTUDS="30", P305="35",
                    MALES="14", P350="5", P360="0", NUMTEACH="3.333", STTCH_RT="9.004", TOTHRS="7", P_INDIAN="0", P_ASIAN="0",
                    P_PACIFIC="0", P_HISP="3.3333", P_WHITE="96.6667", P_BLACK="0", P_TR="0",
                    P150="5", P160="4", P170="1", P180="2", P190="8", P300="15")
        base.update(values)
        return base

    def test_a_school_year_with_labels_rounded_measures_and_grades(self):
        rows, grades, unmatched = self.read(self.record(), self.record(PPIN="99999999"))
        row = dict(zip(private_school_survey.COLUMNS, rows[0]))
        self.assertEqual((row["typology"], row["affiliation"], row["religious_orientation"], row["level"], row["community_type"]),
                         ("Other religious, conservative Christian", "Other religious", "Christian (no specific denomination)",
                          "Combined elementary and secondary", "Town"))
        self.assertEqual((row["students"], row["students_with_preschool"], row["teachers_fte"], row["students_per_teacher"]),
                         (30, 35, Decimal("3.33"), Decimal("9.00")))
        # 0% to college is an answer, kept
        self.assertEqual((row["seniors_prior_year"], row["to_four_year_college_pct"]), (5, 0))
        # Transitional kindergarten with kindergarten, transitional first grade with grade 1
        self.assertEqual(grades, [(1, 2024, 1, 5), (1, 2024, 2, 5), (1, 2024, 3, 10), (1, 2024, 14, 15)])
        self.assertEqual(unmatched, ["99999999"])

    def test_skipped_answers_are_empty(self):
        rows, _, _ = self.read(self.record(P350="-1", P360="-1", UCOMMTYP=" "))
        row = dict(zip(private_school_survey.COLUMNS, rows[0]))
        self.assertEqual((row["seniors_prior_year"], row["to_four_year_college_pct"], row["community_type"]), (None, None, None))

    def test_an_earlier_ppin_counts_only_in_its_years(self):
        matches = {"00000001": (1, None), "00000002": (1, {2022})}
        rows, _, unmatched = self.read(self.record(), self.record(PPIN="00000002"), matches=matches)
        self.assertEqual((len(rows), unmatched), (1, ["00000002"]))
        with self.assertRaises(ValueError):
            self.read(self.record(), self.record(PPIN="00000002"), matches={"00000001": (1, None), "00000002": (1, None)})

    def test_a_code_without_a_label_stops_the_load(self):
        with self.assertRaises(ValueError):
            self.read(self.record(TYPOLOGY="12"))


class PrivateSurveyDatabaseTests(unittest.TestCase):
    """Against the loaded database"""

    def query(self, sql, **params):
        with engine.connect() as conn:
            return conn.execute(text(sql), params).fetchall()

    def test_four_surveys_of_the_schools_on_the_states_list(self):
        self.assertEqual(dict(self.query("SELECT year, count(*) FROM school_private_survey GROUP BY year")),
                         {2018: 85, 2020: 85, 2022: 87, 2024: 95})

    def test_a_schools_answers_as_its_page_gives_them(self):
        row = self.query("""
            SELECT teachers_fte, students_per_teacher, seniors_prior_year, to_four_year_college_pct, students, students_with_preschool
            FROM school_private_survey WHERE school_id_fk = 20290 AND year = 2024
        """)[0]
        self.assertEqual(tuple(row), (Decimal("27.80"), Decimal("11.65"), 30, 73, 324, 336))
        grades = self.query("SELECT grade_id_fk, students FROM school_private_survey_grade WHERE school_id_fk = 20290 AND year = 2024 ORDER BY 1")
        self.assertEqual(dict(grades), {1: 12, 2: 22, 3: 20, 4: 21, 5: 16, 6: 24, 7: 20, 8: 25, 9: 37, 10: 26, 11: 27, 12: 34, 13: 31, 14: 21})

    def test_a_renumbered_school_keeps_its_earlier_years(self):
        rows = self.query("SELECT year, ppin FROM school_private_survey WHERE school_id_fk = 28520 ORDER BY year")
        self.assertEqual([tuple(row) for row in rows], [(2018, "A0507889"), (2020, "A0507889"), (2022, "A0507889"), (2024, "A2301518")])


if __name__ == "__main__":
    unittest.main()
