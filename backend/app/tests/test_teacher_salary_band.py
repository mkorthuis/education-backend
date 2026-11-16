"""
Tests for the teacher salary band load: NH DOE's impossible values are skipped and logged, and a
district's published schedule corrects them. Run against the local database after `alembic upgrade head`:

    docker exec -w /app education-backend-backend-1 python -m unittest app.tests.test_teacher_salary_band -v
"""
import copy
import unittest
from collections import Counter

import pandas as pd
from sqlalchemy import text
from sqlmodel import Session

from app.core.db import engine
from app.etl import teacher_salary_band
from app.etl.core import load_config

CONFIG = load_config(teacher_salary_band.CONFIG)
DISTRICTS = {113, 271, 399}


def sheet(*rows):
    """A sheet in NH DOE's layout: SAU, SAU name, district, district name, band, minimum, maximum, steps."""
    return pd.DataFrame([[9, "SAU", district, "District", band, low, high, steps] for district, band, low, high, steps in rows])


class SalaryBandParseTests(unittest.TestCase):
    def test_impossible_salaries_are_skipped_and_long_step_counts_dropped(self):
        skips = Counter()
        rows = teacher_salary_band.parse_year(sheet(
            (399, "BA15", 45167, 73112, 15),
            (399, "BA", 440367, 71330, 15),    # a minimum above the maximum
            (399, "MA15", 14, 68802, 14),      # a minimum of $14
            (399, "MA", 47453, 76812, 1300),   # 1,300 steps
        ), 2024, CONFIG, DISTRICTS, skips)
        self.assertEqual(rows, [(399, 2, 2024, 45167.0, 73112.0, 15), (399, 4, 2024, 47453.0, 76812.0, None)])
        self.assertEqual(skips["rows with an impossible salary"], 2)

    def test_a_districts_schedule_corrects_nh_does_values(self):
        rows = teacher_salary_band.parse_year(sheet(
            (271, "BA", 4600, 59500, 10),
            (113, "BA", 40442, 83192, 46),
            (113, "MA", 45636, 93875, 464),
        ), 2026, CONFIG, DISTRICTS, Counter())
        self.assertEqual(rows, [(271, 1, 2026, 46000, 59500.0, 10), (113, 1, 2026, 42571, 87571, 46),
                                (113, 4, 2026, 45636.0, 93875.0, 46)])

    def test_a_correction_that_matches_no_row_stops_the_load(self):
        config = copy.deepcopy(CONFIG)
        config["corrections"].append({"district_id": 399, "year": 2026, "band": "BA", "min_salary": 44037, "source": "x"})
        with self.assertRaises(ValueError):
            teacher_salary_band.parse_year(sheet((271, "BA", 4600, 59500, 10)), 2026, config, DISTRICTS, Counter())


class SalaryBandDatabaseTests(unittest.TestCase):
    def test_the_loaded_bands_are_within_the_limits_and_corrected(self):
        limits = CONFIG["limits"]
        with Session(engine) as session:
            bad = session.execute(text(
                "SELECT count(*) FROM district_teacher_salary_band WHERE min_salary < :low OR max_salary < min_salary OR steps > :steps"),
                {"low": limits["min_salary"], "steps": limits["max_steps"]}).scalar()
            self.assertEqual(bad, 0)
            jackson = session.execute(text(
                "SELECT min_salary FROM district_teacher_salary_band WHERE district_id_fk = 271 AND year = 2026 AND teacher_salary_band_type_id_fk = 1")).scalar()
            self.assertEqual(jackson, 46000)
            conway = session.execute(text(
                "SELECT min_salary, max_salary, steps FROM district_teacher_salary_band "
                "WHERE district_id_fk = 113 AND year = 2026 AND teacher_salary_band_type_id_fk = 1")).one()
            self.assertEqual(tuple(conway), (42571, 87571, 46))
