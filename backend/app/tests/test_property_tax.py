"""
Tests for the property tax load and API, run against the local database after `alembic upgrade head`:

    docker exec -w /app education-backend-backend-1 python -m unittest app.tests.test_property_tax -v
"""
import copy
import unittest

from sqlalchemy import text

from app.core.db import engine
from app.etl import property_tax
from app.etl.core import load_config

CONFIG = load_config(property_tax.CONFIG)
YEARS = range(2011, 2026)
HAMPTON, AMHERST, CONCORD, PENACOOK, LOUDON = 225, 17, 111, 429, 321
SOUHEGAN, WINNACUNNET = 493, 581
DRA_TOWNS = {2014: 236, **{year: 237 for year in range(2015, 2026)}}


class PropertyTaxParseTests(unittest.TestCase):
    def setUp(self):
        self.dra, self.doe = property_tax.read(CONFIG, YEARS)

    def test_both_files_read_and_check_out(self):
        self.assertEqual((len(self.dra), len(self.doe)), (2843, 3555))
        self.assertEqual(sum(len(r["coop_shares"]) for r in self.doe), 420)
        notes = property_tax.check(CONFIG, self.dra, self.doe)
        self.assertIn("0.00", notes[(LOUDON, 2020)])

    def test_only_the_configured_years_are_read(self):
        # The CSV's 2026 rows are the towns set by October 30, 2026; they wait for DRA's final file
        dra, doe = property_tax.read(CONFIG, [2026])
        self.assertEqual((dra, doe), ([], []))
        self.assertEqual({r["tax_year"] for r in self.dra}, set(range(2014, 2026)))
        with engine.connect() as conn, self.assertRaisesRegex(ValueError, "aren't in"):
            property_tax.load(conn, [2026])

    def test_hamptons_cooperative_share(self):
        hampton = next(r for r in self.doe if r["town_id"] == HAMPTON and r["tax_year"] == 2025)
        self.assertEqual(hampton["coop_shares"], [{"name": "WINNACUNNET COOP", "footnote": "C", "amount": 12796162.270408}])
        self.assertEqual(hampton["local_educ_tax"], 37350019)

    def test_a_difference_the_config_doesnt_list_stops_the_load(self):
        dra = copy.deepcopy(self.dra)
        next(r for r in dra if r["town_id"] == HAMPTON and r["tax_year"] == 2025)["local_education_rate"] += 0.02
        with self.assertRaisesRegex(ValueError, "rates don't add up|differs from DRA's"):
            property_tax.check(CONFIG, dra, self.doe)
        config = copy.deepcopy(CONFIG)
        config["dra_total_differs"] = []
        with self.assertRaisesRegex(ValueError, f"DRA town {PENACOOK} 2014: its rates don't add up"):
            property_tax.check(config, self.dra, self.doe)
        # A listed difference that isn't one is stale
        config = copy.deepcopy(CONFIG)
        config["rate_differences"].append({"town_id": HAMPTON, "tax_year": 2025, "rates": ["local"]})
        with self.assertRaisesRegex(ValueError, "rate_differences lists it"):
            property_tax.check(config, self.dra, self.doe)

    def test_dras_concord_is_the_does_concord_and_penacook(self):
        config = copy.deepcopy(CONFIG)
        config["combined_towns"] = {}
        with self.assertRaisesRegex(ValueError, f"town {CONCORD} 2018: the DOE's local_educ_tax"):
            property_tax.check(config, self.dra, self.doe)

    def test_every_file_a_row_cites_is_in_the_repo(self):
        property_tax.check_files(CONFIG, self.dra, self.doe)
        # The 2015 rates: DRA's PDF, with three rows fixed from its 2015 workbook
        self.assertEqual({r["rate_source_file"] for r in self.dra if r["tax_year"] == 2015},
                         {"dra/15-final-tax-rates.pdf", "dra/15-final-tax-rates.pdf; dra/15-tax-rate-information.xlsx"})
        dra = copy.deepcopy(self.dra)
        dra[0]["rate_source_file"] = "dra/not-saved.xlsx"
        with self.assertRaisesRegex(ValueError, "not-saved.xlsx"):
            property_tax.check_files(CONFIG, dra, self.doe)

    def test_the_state_education_tax_is_the_next_years_swept(self):
        hampton = next(r for r in self.doe if r["town_id"] == HAMPTON and r["tax_year"] == 2025)
        property_tax.check(CONFIG, self.dra, self.doe, {(HAMPTON, 2026): hampton["state_educ_tax"]})
        with self.assertRaisesRegex(ValueError, "FY2026 SWEPT"):
            property_tax.check(CONFIG, self.dra, self.doe, {(HAMPTON, 2026): hampton["state_educ_tax"] + 5})


class PropertyTaxLoadTests(unittest.TestCase):
    def query(self, sql, **params):
        with engine.connect() as conn:
            return conn.execute(text(sql), params).all()

    def test_every_year_and_town_is_loaded(self):
        self.assertEqual([y for (y,) in self.query("SELECT DISTINCT tax_year FROM town_school_tax ORDER BY 1")], list(YEARS))
        self.assertEqual(dict(self.query("SELECT tax_year, count(*) FROM town_property_tax GROUP BY 1")), DRA_TOWNS)
        self.assertEqual(dict(self.query("SELECT tax_year, count(*) FROM town_school_tax GROUP BY 1")), {y: 237 for y in YEARS})
        self.assertEqual(self.query("SELECT count(*) FROM town_school_tax_coop_share")[0][0], 420)
        self.assertEqual(self.query("SELECT count(*) FROM town_property_tax_summary")[0][0], 237 * len(YEARS))

    def test_each_row_has_its_district_and_cooperative(self):
        # A member town's cooperative, from the report's name; a single-town district's row has none
        self.assertEqual(self.query("""
            SELECT count(*) FILTER (WHERE cooperative_district_id_fk IS NOT NULL), count(*) FROM town_school_tax
        """)[0], (1390, 3555))
        # The report's district numbers, as site ids: none on a few towns' rows (Randolph and Shelburne's every year)
        self.assertEqual(dict(self.query(
            "SELECT tax_year, count(*) FROM town_school_tax WHERE district_id_fk IS NULL GROUP BY 1 HAVING count(*) > 2 ORDER BY 1")), {
            2011: 5, 2012: 5, 2013: 6, 2014: 6, 2015: 7, 2016: 7, 2017: 4})
        # Gorham Randolph Shelburne's older number (201) is the site's 203; Wilton's 2011-2016 rows carry its own district
        self.assertEqual(self.query(
            "SELECT DISTINCT district_id_fk, cooperative_district_id_fk FROM town_school_tax WHERE town_id_fk = 201 AND tax_year >= 2011"), [(203, 203)])
        self.assertEqual(self.query("""
            SELECT tax_year, district_id_fk, cooperative_district_id_fk FROM town_school_tax WHERE town_id_fk = 571 AND tax_year IN (2016, 2017) ORDER BY 1
        """), [(2016, 571, 572), (2017, 572, 572)])

    def test_the_state_education_tax_is_the_next_years_swept(self):
        compared, differ = self.query("""
            SELECT count(*), count(*) FILTER (WHERE abs(s.state_education_tax - a.value) > 1)
            FROM town_school_tax s
            JOIN town_adequacy_aid a ON a.town_id_fk = s.town_id_fk AND a.fiscal_year = s.tax_year + 1
            JOIN adequacy_aid_component c ON c.id = a.component_id_fk AND c.code = 'swept'
        """)[0]
        self.assertGreater(compared, 1600)
        self.assertEqual(differ, 0)

    def test_hamptons_rates_and_school_taxes(self):
        [row] = self.query("""
            SELECT municipal_rate, county_rate, local_education_rate, state_education_rate, total_rate, equalization_ratio,
                   full_value_tax_rate, school_share_of_total_rate, local_education_tax, state_education_tax
            FROM town_property_tax_summary WHERE town_id_fk = :t AND tax_year = 2025
        """, t=HAMPTON)
        self.assertEqual(tuple(float(v) for v in row), (4.71, 0.61, 6.13, 1.16, 12.61, 89.68, 11.20, 57.8, 37350019, 6813213))
        # Before DRA's figures, the DOE's rates give the school share
        [(dra_rate, share)] = self.query(
            "SELECT total_rate, school_share_of_total_rate FROM town_property_tax_summary WHERE town_id_fk = :t AND tax_year = 2011", t=HAMPTON)
        self.assertIsNone(dra_rate)
        self.assertIsNotNone(share)


class PropertyTaxApiTests(unittest.TestCase):
    """Against the loaded database (the app needs the backend's image: python -m unittest in Docker)"""

    @classmethod
    def setUpClass(cls):
        from fastapi.testclient import TestClient
        from app.core.config import settings
        from app.main import app
        cls.api, cls.prefix = TestClient(app), f"{settings.API_V1_STR}/finance/property-tax"

    def get(self, path, status=200, **params):
        response = self.api.get(f"{self.prefix}/{path}", params=params)
        self.assertEqual(response.status_code, status, response.text)
        return response.json()

    def test_years_with_their_towns(self):
        years = self.get("years")
        self.assertEqual([y["tax_year"] for y in years], list(YEARS))
        self.assertEqual((years[0]["school_year"], years[0]["dra_towns"], years[0]["doe_towns"]), ("2011-12", 0, 237))
        self.assertEqual(self.get("years", year=2025), [{"tax_year": 2025, "school_year": "2025-26", "dra_towns": 237, "doe_towns": 237}])
        self.assertEqual(self.get("years", year=2014)[0]["dra_towns"], 236)

    def test_a_towns_rates_school_taxes_and_cooperative_share(self):
        [hampton] = self.get("town", town_id=HAMPTON, year=2025)
        self.assertEqual((hampton["school_year"], hampton["district_name"], hampton["school_share_of_total_rate"]),
                         ("2025-26", "Hampton", 57.8))
        self.assertEqual((hampton["dra"]["total_rate"], hampton["dra"]["full_value_tax_rate"], hampton["doe"]["local_education_tax"]),
                         (12.61, 11.2, 37350019.0))
        self.assertEqual([(s["district_id"], s["local_education_tax"]) for s in hampton["doe"]["cooperative_shares"]],
                         [(WINNACUNNET, 12796162.270408)])
        years = self.get("town", town_id=HAMPTON)
        self.assertEqual([y["tax_year"] for y in years], list(YEARS))
        self.assertIsNone(years[0]["dra"])  # DRA's figures begin in 2014
        self.assertEqual(self.get("town", town_id=HAMPTON, year=2026), [])

    def test_a_member_towns_cooperative(self):
        [acworth] = self.get("town", town_id=3, year=2025)
        self.assertEqual((acworth["district_name"], acworth["doe"]["cooperative_district_name"]), ("Fall Mountain Regional", "Fall Mountain Regional"))
        [hampton] = self.get("town", town_id=HAMPTON, year=2025)
        self.assertIsNone(hampton["doe"]["cooperative_district_id"])

    def test_a_districts_towns(self):
        souhegan = self.get("district", district_id=SOUHEGAN, year=2025)
        self.assertEqual([t["town_name"] for t in souhegan], ["Amherst", "Mont Vernon"])
        amherst = souhegan[0]
        self.assertEqual([(s["district_id"], s["local_education_tax"]) for s in amherst["doe"]["cooperative_shares"]],
                         [(SOUHEGAN, 13720641.0)])
        self.get("district", status=422)
