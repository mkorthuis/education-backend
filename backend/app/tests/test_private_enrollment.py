"""
Tests for the private schools' enrollment load (NHED's "NonPublic School Enrollments by Grade"), run
against the local database after `alembic upgrade head`:

    docker exec -w /app education-backend-backend-1 python -m unittest app.tests.test_private_enrollment -v
"""
import unittest

import pandas as pd
from sqlalchemy import text

from app.core.db import engine
from app.etl import private_enrollment
from app.etl.core import load_config

CONFIG = load_config(private_enrollment.CONFIG)
HEADER = ["School #", "School Name", "Town", "PS", "KG", *[str(n) for n in range(1, 13)], "PG", "UGEL", "UGSE", "Total"]


def export(*schools, state=None, kind="Final", title="2024 - 2025"):
    """An export as the report gives it: its notes, title, header, State Total row and schools"""
    rows = [[f"Type of Data: {kind}"], [f"{title} Nonpublic School Enrollments in New Hampshire by Grade by Town"], HEADER]
    counts = [list(school[3:]) for school in schools]
    totals = state or [sum(column) for column in zip(*counts)]
    rows.append(["", "", "State Total", *map(str, totals)])
    rows += [[*map(str, school)] for school in schools]
    width = len(HEADER)
    return pd.DataFrame([row + [""] * (width - len(row)) for row in rows])


# A school with 2 in preschool, 3 in kindergarten, 1 in grade 12, 1 ungraded secondary: 7 in all
SCHOOL = (20290, "Concord Christian Academy", "Concord", 2, 3, *[0] * 11, 1, 0, 0, 1, 7)


class PrivateEnrollmentReadTests(unittest.TestCase):
    def read(self, df):
        return private_enrollment.read_export(df, 2025, CONFIG, "test.xlsx")

    def test_a_schools_counts_by_column(self):
        school = self.read(export(SCHOOL))[0]
        self.assertEqual((school["school_id"], school["PS"], school["KG"], school["12"], school["UGSE"], school["Total"]),
                         (20290, 2, 3, 1, 1, 7))

    def test_counts_that_dont_add_up_stop_the_load(self):
        with self.assertRaises(ValueError):                       # the school's grades and its total
            self.read(export((*SCHOOL[:-1], 8)))
        with self.assertRaises(ValueError):                       # the schools and the State Total
            self.read(export(SCHOOL, state=[2, 3, *[0] * 11, 1, 0, 0, 1, 9]))

    def test_only_a_years_final_report(self):
        with self.assertRaises(ValueError):
            self.read(export(SCHOOL, kind="Preliminary"))
        with self.assertRaises(ValueError):
            self.read(export(SCHOOL, title="2023 - 2024"))


class PrivateEnrollmentDatabaseTests(unittest.TestCase):
    """Against the loaded database"""

    def query(self, sql, **params):
        with engine.connect() as conn:
            return conn.execute(text(sql), params).fetchall()

    def test_fifteen_years_as_the_state_totals_them(self):
        totals = dict(self.query("SELECT year, sum(total) FROM school_private_enrollment_total GROUP BY year"))
        self.assertEqual((min(totals), max(totals), len(totals)), (2012, 2026, 15))
        self.assertEqual((totals[2012], totals[2025], totals[2026]), (14622, 16716, 16794))

    def test_a_schools_grades_add_up_to_its_total(self):
        rows = self.query("""
            SELECT t.year, t.total, t.ungraded_elementary + t.ungraded_secondary + coalesce(sum(e.enrollment), 0)
            FROM school_private_enrollment_total t
            LEFT JOIN school_private_enrollment e ON e.school_id_fk = t.school_id_fk AND e.year = t.year
            WHERE t.school_id_fk = 20290 GROUP BY t.year, t.total, t.ungraded_elementary, t.ungraded_secondary ORDER BY t.year
        """)
        self.assertTrue(all(total == added for _, total, added in rows))
        self.assertEqual({year: total for year, total, _ in rows if year >= 2023}, {2023: 346, 2024: 336, 2025: 340, 2026: 309})

    def test_none_of_it_is_in_the_public_schools_enrollment(self):
        rows = self.query("""
            SELECT count(*) FROM school_enrollment e JOIN school_private_enrollment_total t ON t.school_id_fk = e.school_id_fk
        """)
        self.assertEqual(rows[0][0], 0)


if __name__ == "__main__":
    unittest.main()
