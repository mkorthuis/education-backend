"""
Tests for the private schools' restraint and seclusion load, run against the local database after
`alembic upgrade head`:

    docker exec -w /app education-backend-backend-1 python -m unittest app.tests.test_private_safety -v
"""
import unittest

import pandas as pd
from fastapi.testclient import TestClient
from sqlalchemy import text

from app.core.config import settings
from app.core.db import engine
from app.etl import private_safety
from app.etl.core import load_config, year_file
from app.main import app

COLUMNS = ["year", "school_id", "school_name", *private_safety.VALUES]


def report(*rows):
    return pd.DataFrame([dict(zip(COLUMNS, row)) for row in rows], columns=COLUMNS)


class PrivateSafetyParseTests(unittest.TestCase):
    known = {20290: 20290, 26705: 26705, 11111: 22222}

    def parse(self, *rows):
        return private_safety.parse_year(report(*rows), 2024, self.known, "test.csv")

    def test_a_school_row_keeps_its_enrollment_and_every_count(self):
        rows, unknown, not_reported = self.parse((2024, 26705, "Wediko School", 88, 40, 1, 0, 0, 40, 12, 0, 12))
        self.assertEqual(rows, [(26705, 2024, 88, 40, 1, 0, 0, 40, 12, 0, 12)])
        self.assertEqual((unknown, not_reported), (set(), set()))

    def test_a_renumbered_school_loads_under_its_current_id(self):
        rows, _, _ = self.parse((2024, 11111, "Renamed School", 50, 0, 0, 0, 0, 0, 0, 0, 0))
        self.assertEqual(rows[0][0], 22222)

    def test_schools_missing_from_the_school_list_and_rows_without_counts_are_left_out(self):
        rows, unknown, not_reported = self.parse(
            (2024, 99999, "Closed School", 20, 0, 0, 0, 0, 0, 0, 0, 0),
            # Enrollment alone, every count blank: not reported, not zero
            (2024, 20290, "Concord Christian Academy", 336, None, None, None, None, None, None, None, None),
        )
        self.assertEqual((rows, unknown, not_reported), ([], {(2024, 99999)}, {(2024, 20290)}))

    def test_a_school_listed_twice_or_a_row_from_another_year_stops_the_load(self):
        row = (2024, 20290, "Concord Christian Academy", 336, 0, 0, 0, 0, 0, 0, 0, 0)
        with self.assertRaises(ValueError):
            self.parse(row, row)
        with self.assertRaises(ValueError):
            self.parse((2023, *row[1:]))

    def test_rows_that_dont_add_up_to_the_reports_totals_stop_the_load(self):
        df = report((2024, 26705, "Wediko School", 88, 40, 1, 0, 0, 40, 12, 0, 12))
        private_safety.check_totals(df, {"restraint_reports": 40, "seclusion_reports": 12}, "test.csv")
        with self.assertRaises(ValueError):
            private_safety.check_totals(df, {"restraint_reports": 41}, "test.csv")


class PrivateSafetyFileTests(unittest.TestCase):
    def test_every_years_file_adds_up_to_its_report(self):
        config = load_config(private_safety.CONFIG)
        schools = {}
        for year in range(2019, 2027):
            df = pd.read_csv(year_file(config["file_settings"], year))
            private_safety.check_totals(df, config["expected_totals"][year], str(year))
            self.assertEqual(df["school_id"].is_unique, True, year)
            schools[year] = len(df)
        self.assertEqual(schools, {2019: 151, 2020: 135, 2021: 134, 2022: 129, 2023: 136, 2024: 134, 2025: 134, 2026: 132})


class PrivateSafetyDatabaseTests(unittest.TestCase):
    """Against the loaded database"""

    @classmethod
    def setUpClass(cls):
        with engine.connect() as conn:
            cls.by_year = {row[0]: row[1:] for row in conn.execute(text("""
                SELECT year, count(*), sum(restraint_reports), sum(seclusion_reports)
                FROM private_school_restraint_seclusion GROUP BY year
            """))}
            cls.rows = {(row[0], row[1]): row[2:] for row in conn.execute(text("""
                SELECT school_id_fk, year, enrollment, restraint_reports, seclusion_reports
                FROM private_school_restraint_seclusion WHERE school_id_fk IN (20290, 26885)
            """))}
            cls.private_in_public_tables = conn.execute(text("""
                SELECT count(*) FROM (SELECT school_id_fk FROM school_restraint UNION ALL SELECT school_id_fk FROM school_seclusion) r
                JOIN school s ON s.id = r.school_id_fk JOIN school_type t ON t.id = s.school_type_id_fk
                WHERE t.code IN ('OT', 'IO', 'CH', 'PA', 'PR', 'IN')
            """)).scalar()

    def test_eight_years_of_the_schools_on_the_states_list(self):
        self.assertEqual({year: counts[0] for year, counts in self.by_year.items()},
                         {2019: 107, 2020: 120, 2021: 122, 2022: 123, 2023: 130, 2024: 129, 2025: 134, 2026: 132})
        # Each report's restraints and seclusions, every one at a school on the list: 2023-24's 1,380 and
        # 357, 2024-25's 1,310 and 638, 2025-26's 737 and 471
        self.assertEqual(self.by_year[2024][1:], (1380, 357))
        self.assertEqual(self.by_year[2025][1:], (1310, 638))
        self.assertEqual(self.by_year[2026][1:], (737, 471))

    def test_each_school_as_its_report_gives_it(self):
        # Concord Christian Academy: none in any year, its enrollment from 221 to 340 and back to 309
        self.assertEqual(self.rows[(20290, 2019)], (221, 0, 0))
        self.assertEqual(self.rows[(20290, 2025)], (340, 0, 0))
        self.assertEqual(self.rows[(20290, 2026)], (309, 0, 0))
        self.assertEqual(self.rows[(26885, 2023)], (124, 0, 0))

    def test_none_of_it_is_in_the_public_schools_tables(self):
        self.assertEqual(self.private_in_public_tables, 0)


class PrivateSafetyApiTests(unittest.TestCase):
    """Against the loaded database"""

    @classmethod
    def setUpClass(cls):
        cls.api = TestClient(app)

    def get(self, **params):
        response = self.api.get(f"{settings.API_V1_STR}/safety/private-school/restraint-seclusion", params=params)
        self.assertEqual(response.status_code, 200, response.text)
        return response.json()

    def test_a_schools_years_oldest_first_with_its_enrollment(self):
        rows = self.get(school_id=20290)
        self.assertEqual([row["year"] for row in rows], list(range(2019, 2027)))
        self.assertEqual([row["enrollment"] for row in rows], [221, 263, 272, 318, 346, 336, 340, 309])
        self.assertEqual(rows[-1], {"school_id": 20290, "year": 2026, "enrollment": 309, "restraint_reports": 0,
                                    "restraints_bodily_harm": 0, "restraints_serious_injury_or_death": 0,
                                    "restraint_investigations_active": 0, "restraint_investigations_closed": 0,
                                    "seclusion_reports": 0, "seclusion_investigations_active": 0,
                                    "seclusion_investigations_closed": 0})

    def test_one_year_for_every_school(self):
        rows = self.get(year=2024)
        self.assertEqual(len(rows), 129)
        self.assertEqual(sum(row["restraint_reports"] for row in rows), 1380)
        self.assertEqual(self.get(school_id=20285), [])  # Concord High: a public school


if __name__ == "__main__":
    unittest.main()
