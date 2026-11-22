"""
Tests for the private schools' tuition load, run against the local database after `alembic upgrade head`:

    docker exec -w /app education-backend-backend-1 python -m unittest app.tests.test_private_tuition -v
"""
import csv
import os
import tempfile
import unittest
from decimal import Decimal

from sqlalchemy import text

from app.core.db import engine
from app.etl import private_tuition

GRADE_IDS = {"Preschool": 1, "Kindergarten": 2, **{f"Grade {n}": n + 2 for n in range(1, 13)}, "Post Graduate": 15}
SOURCE = ["school_id", "year", "status", "source_url", "retrieved_on", "with_aid", "note"]
RATE = ["school_id", "year", "rate_no", "band", "lowest_grade", "highest_grade", "rate_type", "rate_label",
        "tuition", "required_fee", "fee_note", "rate_note"]


def written(header, rows):
    f = tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, newline="")
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)
    f.close()
    return f.name


class PrivateTuitionReadTests(unittest.TestCase):
    def read(self, sources, rates):
        sources_path, rates_path = written(SOURCE, sources), written(RATE, rates)
        try:
            read = private_tuition.read_sources(sources_path)
            return read, private_tuition.read_rates(rates_path, read, GRADE_IDS)
        finally:
            os.unlink(sources_path)
            os.unlink(rates_path)

    published = [1, 2027, "published", "https://example.org/tuition", "2026-11-21", "37% of students", ""]
    rate = [1, 2027, 1, "Grades 9-12", "Grade 9", "Grade 12", "boarding", "", "75400", "1480", "", ""]

    def test_a_school_years_source_and_rates(self):
        sources, rates = self.read([self.published, [2, 2027, "not_published", "", "2026-11-21", "", "Pages checked: ..."]], [self.rate])
        self.assertEqual([row["status"] for row in sources], ["published", "not_published"])
        self.assertEqual((rates[0]["lowest_grade_id_fk"], rates[0]["highest_grade_id_fk"], rates[0]["tuition"], rates[0]["required_fee"]),
                         (11, 14, Decimal("75400"), Decimal("1480")))

    def test_rates_must_belong_to_a_published_year_with_known_grades_and_types(self):
        for bad in ([1, 2026, *self.rate[2:]],                                  # no source for that year
                    [*self.rate[:4], "Grade 13", *self.rate[5:]],               # not a grade
                    [*self.rate[:4], "Grade 12", "Grade 9", *self.rate[6:]],    # backwards
                    [*self.rate[:6], "sibling", *self.rate[7:]]):               # not a rate type
            with self.assertRaises(ValueError, msg=bad):
                self.read([self.published], [bad])

    def test_a_fee_named_without_an_amount_is_unknown_not_zero(self):
        _, rates = self.read([self.published], [[*self.rate[:9], "", *self.rate[10:]]])
        self.assertIsNone(rates[0]["required_fee"])

    def test_a_published_school_needs_a_page_and_rates(self):
        with self.assertRaises(ValueError):
            self.read([[1, 2027, "published", "", "2026-11-21", "", ""]], [])
        with self.assertRaises(ValueError):
            self.read([self.published], [])


class PrivateTuitionDatabaseTests(unittest.TestCase):
    """Against the loaded database"""

    def query(self, sql, **params):
        with engine.connect() as conn:
            return conn.execute(text(sql), params).fetchall()

    def test_every_school_researched_has_a_source_row(self):
        self.assertEqual(self.query("SELECT count(DISTINCT school_id_fk) FROM school_tuition_source")[0][0], 103)
        statuses = dict(self.query("SELECT status, count(*) FROM school_tuition_source WHERE year = 2027 GROUP BY status"))
        self.assertGreater(statuses["published"], 60)
        self.assertEqual(self.query("""
            SELECT count(*) FROM school_tuition_source s
            WHERE s.status = 'published' AND NOT EXISTS (SELECT 1 FROM school_tuition t WHERE t.school_id_fk = s.school_id_fk AND t.year = s.year)
        """)[0][0], 0)

    def test_a_schools_rates_as_it_publishes_them(self):
        rates = self.query("""
            SELECT band, tuition + required_fee FROM school_tuition WHERE school_id_fk = 20290 AND year = 2027 ORDER BY rate_no
        """)
        self.assertEqual([tuple(row) for row in rates][:2], [("Kindergarten Readiness", Decimal("10500.00")), ("Kindergarten", Decimal("13000.00"))])
        self.assertEqual(self.query("SELECT with_aid FROM school_tuition_source WHERE school_id_fk = 20290")[0][0], "85% of students")


if __name__ == "__main__":
    unittest.main()
