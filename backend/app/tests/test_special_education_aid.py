"""
Tests for the special education aid load and API, run against the local database after `alembic upgrade head`:

    docker exec -w /app education-backend-backend-1 python -m unittest app.tests.test_special_education_aid -v
"""
import copy
import unittest

from sqlalchemy import text

from app.core.db import engine
from app.etl import special_education_aid
from app.etl.core import load_config

CONFIG = load_config(special_education_aid.CONFIG)
CONWAY, ALLENSTOWN, EXETER = 113, 9, 173
DISTRICTS = {2021: 116, 2022: 117, 2023: 116, 2024: 119, 2025: 119, 2026: 125}


class SpecialEducationAidParseTests(unittest.TestCase):
    def test_every_years_file_reads_and_checks_out(self):
        for year in CONFIG["years"]:
            parsed = special_education_aid.read_year(CONFIG, year)
            self.assertEqual(len(parsed["districts"]), DISTRICTS[year], f"FY{year}")
            special_education_aid.check_year(CONFIG, year, parsed, special_education_aid.bands_for(CONFIG, year))

    def test_allenstowns_fy2026_row_and_its_arithmetic(self):
        parsed = special_education_aid.read_year(CONFIG, 2026)
        allenstown = next(d for d in parsed["districts"] if d["name"] == "Allenstown")
        self.assertEqual(allenstown["bands"], {1: 150639.37, 2: 108332.13, 3: 0.0})
        self.assertEqual((allenstown["total_cost"], allenstown["entitlement"], allenstown["aid_paid"]), (258971.50, 86665.70, 78988.66))
        self.assertEqual(round(0.8 * allenstown["bands"][2], 2), allenstown["entitlement"])
        rate = special_education_aid.check_year(CONFIG, 2026, parsed, special_education_aid.bands_for(CONFIG, 2026))
        self.assertAlmostEqual(rate, 49917000 / 54768513.81)
        # The state row has the counts; no district does
        self.assertEqual((parsed["state"]["students"], parsed["state"]["band_students"][3]), (885, 96))
        self.assertTrue(all(d["students"] is None for d in parsed["districts"]))

    def test_a_year_paid_in_full_gets_its_entitlement_as_aid(self):
        parsed = special_education_aid.read_year(CONFIG, 2021)
        self.assertIsNone(parsed["state"]["aid_paid"])
        self.assertEqual(special_education_aid.check_year(CONFIG, 2021, parsed, special_education_aid.bands_for(CONFIG, 2021)), 1.0)
        self.assertTrue(all(d["aid_paid"] == d["entitlement"] for d in parsed["districts"]))
        self.assertEqual(parsed["districts"][0]["district_id"], ALLENSTOWN)  # FY2021's IDs have no heading

    def test_a_figure_that_doesnt_check_stops_the_load(self):
        parsed = special_education_aid.read_year(CONFIG, 2025)
        parsed["districts"][0]["entitlement"] += 1
        with self.assertRaisesRegex(ValueError, "entitlement"):
            special_education_aid.check_year(CONFIG, 2025, parsed, special_education_aid.bands_for(CONFIG, 2025))
        config = copy.deepcopy(CONFIG)
        config["years"][2022]["total_cost_differs"] = []
        with self.assertRaisesRegex(ValueError, "add up to"):
            special_education_aid.check_year(config, 2022, special_education_aid.read_year(config, 2022),
                                             special_education_aid.bands_for(config, 2022))
        config["years"][2026]["threshold_cost"] = 75000
        with self.assertRaisesRegex(ValueError, "threshold_cost"):
            special_education_aid.check_year(config, 2026, special_education_aid.read_year(config, 2026),
                                             special_education_aid.bands_for(config, 2026))

    def test_the_formula_changes_in_fy2029(self):
        self.assertEqual([(b["from"], b["state_share"]) for b in special_education_aid.bands_for(CONFIG, 2028)],
                         [(0, 0), (3.5, 0.8), (10, 1.0)])
        self.assertEqual([(b["from"], b["state_share"]) for b in special_education_aid.bands_for(CONFIG, 2029)],
                         [(0, 0), (2.5, 0.15), (3.5, 0.8), (10, 0.9)])

    def test_districts_match_by_id_or_by_name(self):
        with engine.connect() as conn:
            fy2025 = special_education_aid.read_year(CONFIG, 2025)
            ids = special_education_aid.district_ids(conn, CONFIG, 2025, fy2025["districts"])
            self.assertEqual(ids[[d["name"] for d in fy2025["districts"]].index("Exeter School District")], EXETER)
            wrong = [{**fy2025["districts"][0], "district_id": CONWAY}]
            with self.assertRaisesRegex(ValueError, "isn't the district of that name"):
                special_education_aid.district_ids(conn, CONFIG, 2025, wrong)


class SpecialEducationAidLoadTests(unittest.TestCase):
    def query(self, sql, **params):
        with engine.connect() as conn:
            return conn.execute(text(sql), params).all()

    def test_every_year_and_district_is_loaded_and_adds_up(self):
        self.assertEqual(dict(self.query("SELECT fiscal_year, count(*) FROM district_special_education_aid GROUP BY 1")), DISTRICTS)
        self.assertEqual(self.query("""
            SELECT count(*) FROM special_education_aid_year y JOIN (
                SELECT fiscal_year, sum(total_cost) c, sum(entitlement) e, sum(aid_paid) p FROM district_special_education_aid GROUP BY 1
            ) d ON d.fiscal_year = y.fiscal_year
            WHERE abs(d.c - y.state_total_cost) > 1 OR abs(d.e - y.state_entitlement) > 1 OR abs(d.p - y.state_aid_paid) > 1
        """)[0][0], 0)
        self.assertEqual(self.query("SELECT count(*) FROM district_special_education_aid_band")[0][0], 3 * sum(DISTRICTS.values()))

    def test_fy2026s_threshold_proration_and_bands(self):
        [(average, threshold, rate, minimum)] = self.query(
            "SELECT state_average_cost, threshold_cost, proration_rate, minimum_share FROM special_education_aid_year WHERE fiscal_year = 2026")
        self.assertEqual((float(average), float(threshold), float(minimum)), (21519.91, 75319.68, 0.8))
        self.assertAlmostEqual(float(rate), 0.9114178)
        self.assertEqual([(float(f), float(s)) for f, s in self.query(
            "SELECT from_multiple, state_share FROM special_education_aid_band WHERE fiscal_year = 2026 ORDER BY band")],
            [(0, 0), (3.5, 0.8), (10, 1.0)])

    def test_the_summary_matches_what_conway_reported(self):
        rows = {year: tuple(float(v) for v in values) for year, *values in self.query("""
            SELECT fiscal_year, total_cost, cost_below_threshold, cost_above_threshold, entitlement, aid_paid, reported_difference
            FROM district_special_education_aid_summary WHERE district_id_fk = :d AND fiscal_year <= 2025 ORDER BY 1
        """, d=CONWAY)}
        self.assertEqual(rows[2025], (84630.17, 69697.81, 14932.36, 11945.89, 8217.89, 0))
        self.assertTrue(all(r[-1] == 0 for r in rows.values()))


class SpecialEducationAidApiTests(unittest.TestCase):
    """Against the loaded database (the app needs the backend's image: python -m unittest in Docker)"""

    @classmethod
    def setUpClass(cls):
        from fastapi.testclient import TestClient
        from app.core.config import settings
        from app.main import app
        cls.api, cls.prefix = TestClient(app), f"{settings.API_V1_STR}/finance/special-education-aid"

    def get(self, path, status=200, **params):
        response = self.api.get(f"{self.prefix}/{path}", params=params)
        self.assertEqual(response.status_code, status, response.text)
        return response.json()

    def test_years_with_their_bands_and_totals(self):
        years = self.get("years")
        self.assertEqual([y["fiscal_year"] for y in years], list(range(2021, 2027)))
        [fy2026] = self.get("years", year=2026)
        self.assertEqual((fy2026["cost_school_year"], fy2026["threshold_cost"], fy2026["aid_paid"], fy2026["districts"]),
                         ("2024-25", 75319.68, 49917000.0, 125))
        self.assertEqual([b["label"] for b in fy2026["bands"]][1], "3.5 to 10 times the state average: 80% state aid")
        self.assertEqual(self.get("years", year=2019), [])

    def test_a_districts_aid_by_year_with_its_bands(self):
        conway = self.get("district", district_id=CONWAY)
        self.assertEqual([d["fiscal_year"] for d in conway], [2021, 2022, 2025, 2026])  # none in FY2023-FY2024
        fy2026 = conway[-1]
        self.assertEqual((fy2026["total_cost"], fy2026["entitlement"], fy2026["aid_paid"], fy2026["reported_aid"]),
                         (406452.33, 144394.62, 131603.83, None))
        self.assertEqual([b["cost"] for b in fy2026["bands"]], [225959.06, 180493.27, 0.0])
        self.assertAlmostEqual(sum(b["cost"] for b in fy2026["bands"]), fy2026["total_cost"], places=2)
        self.assertEqual(len(self.get("district", year=2025)), 119)
