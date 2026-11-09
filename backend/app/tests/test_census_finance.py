"""
Tests for the Census school finance data load and API, run against the local database after
`alembic upgrade head`:

    docker exec -w /app education-backend-backend-1 python -m unittest app.tests.test_census_finance -v
"""
import unittest

import pandas as pd
from fastapi.testclient import TestClient

from app.core.config import settings
from app.etl import census_finance
from app.etl.core import load_config
from app.main import app
from app.service.inflation import in_dollars_of

CONFIG = load_config(census_finance.CONFIG)
COLUMNS = ["STATE", "NAME", "NCESID", "V33", "TOTALREV", "TFEDREV", "C14", "TSTREV", "C01", "TLOCREV", "T06", "D11", "TOTALEXP"]


def systems(*rows):
    return pd.DataFrame([dict(zip(COLUMNS, row)) for row in rows], columns=COLUMNS, dtype=str)


class CensusFinanceParseTests(unittest.TestCase):
    def test_school_systems_add_up_by_state_without_revenue_from_other_systems(self):
        revenue = census_finance.state_revenue(systems(
            ("30", "CONCORD", "3302460", "4000", "0", "10", "6", "20", "20", "35", "30", "5", "0"),
            ("30", "BEDFORD", "3300750", "4000", "0", "4", "4", "8", "8", "12", "12", "0", "0"),
            ("22", "BOSTON", "2502790", "45000", "0", "100", "60", "200", "200", "300", "300", "0", "0"),
        ), CONFIG)
        self.assertEqual(revenue["NH"], {"C14": 10, "C01": 28, "T06": 42})
        self.assertEqual(revenue["US"], {"C14": 70, "C01": 228, "T06": 342})
        self.assertNotIn("D11", revenue["NH"])

    def test_unknown_items_and_mismatched_state_codes_stop_the_fetch(self):
        unknown = systems(("30", "CONCORD", "3302460", "1", "0", "1", "1", "1", "1", "1", "1", "0", "0")).rename(columns={"C14": "C99"})
        with self.assertRaises(ValueError):
            census_finance.state_revenue(unknown, CONFIG)
        # Census's state code 30 is New Hampshire, whose NCES ids start with its FIPS code, 33
        with self.assertRaises(ValueError):
            census_finance.state_revenue(systems(("30", "X", "2502790", "1", "0", "1", "1", "1", "1", "1", "1", "0", "0")), CONFIG)

    def test_totals_must_match_table_1_except_known_errors(self):
        revenue = {"NE": {"C14": 5, "C01": 10, "T06": 3415577}}
        census_finance.check(revenue, {"NE": {"federal": 5, "state": 10, "local": 3415577}}, 2023, CONFIG)
        with self.assertRaises(ValueError):
            census_finance.check(revenue, {"NE": {"federal": 5, "state": 11, "local": 3415577}}, 2023, CONFIG)
        # Table 1's 2024 Nebraska local revenue is a known error, skipped only while it shows that figure
        census_finance.check(revenue, {"NE": {"federal": 5, "state": 10, "local": 1164342}}, 2024, CONFIG)
        with self.assertRaises(ValueError):
            census_finance.check(revenue, {"NE": {"federal": 5, "state": 10, "local": 1164343}}, 2024, CONFIG)

    def test_table_labels_and_not_applicable_cells(self):
        self.assertEqual(census_finance._label("New Hampshire......................"), "New Hampshire")
        self.assertEqual(census_finance._label("District of Columbia 1"), "District of Columbia")
        self.assertEqual(census_finance._amount("(X)"), 0)
        self.assertEqual(census_finance._amount(1144508), 1144508)


class CensusFinanceApiTests(unittest.TestCase):
    """Against the loaded database"""

    @classmethod
    def setUpClass(cls):
        cls.api = TestClient(app)
        cls.url = f"{settings.API_V1_STR}/census-finance"

    def get(self, path, **params):
        response = self.api.get(f"{self.url}/{path}", params=params)
        self.assertEqual(response.status_code, 200, response.text)
        return response.json()

    def test_every_year_and_place_has_enrollment(self):
        rows = self.get("enrollment", jurisdiction="NH")
        self.assertEqual([r["year"] for r in rows], list(range(2010, 2025)))
        # Census's published enrollment, not a sum of school systems
        self.assertEqual({r["year"]: r["enrollment"] for r in rows}[2024], 156325)
        self.assertEqual({r["year"]: r["enrollment"] for r in rows}[2010], 197131)
        self.assertEqual(len(self.get("enrollment", year=2024)), 52)

    def test_the_summary_gives_shares_and_per_pupil_amounts(self):
        [nh] = self.get("revenue/summary", year=2024, jurisdiction="nh")
        self.assertEqual(nh["total"]["amount"], 4_037_660_000)
        self.assertEqual({s: nh[s]["amount"] for s in ("federal", "state", "local")},
                         {"federal": 333_679_000, "state": 1_144_508_000, "local": 2_559_473_000})
        # Census's Table 5 gives 8.3%, 28.3% and 63.4%
        self.assertEqual([nh[s]["share_of_total"] for s in ("federal", "state", "local")], [8.26, 28.35, 63.39])
        self.assertAlmostEqual(nh["total"]["per_pupil"], 4_037_660_000 / 156_325, places=2)

    def test_categories_match_censuss_summary_tables(self):
        rows = self.get("revenue", year=2024, jurisdiction="NH", level="category")
        thousands = {(r["source"], r["category"]): r["amount"] // 1000 for r in rows}
        # Census's 2024 tables 2, 3 and 4, New Hampshire
        expected = {
            ("federal", "Title I"): 44950, ("federal", "Special education"): 50840, ("federal", "School meals"): 33261,
            ("federal", "Career and technical education"): 4586, ("federal", "Other federal through the state"): 194808,
            ("federal", "Impact Aid"): 0, ("state", "General formula assistance"): 1058939,
            ("state", "Career and technical education"): 8953, ("state", "Other state aid"): 76616,
            ("local", "Property taxes"): 2061653, ("local", "Parent government contributions"): 385122,
            ("local", "Cities and counties"): 93, ("local", "School meal charges"): 40717,
            ("local", "Tuition and transportation charges"): 7963, ("local", "Other charges"): 6903,
            ("local", "Other local revenue"): 57022,
        }
        for key, amount in expected.items():
            self.assertEqual(thousands[key], amount, key)
        # Each source's categories add up to the whole source
        federal = [r for r in rows if r["source"] == "federal"]
        self.assertAlmostEqual(sum(r["share_of_source"] for r in federal), 100, delta=0.05)

    def test_filters_keep_shares_of_the_full_totals(self):
        [title_i] = self.get("revenue", year=2024, jurisdiction="NH", source="federal", category="Title I")
        self.assertEqual((title_i["item"]["code"], title_i["amount"]), ("C14", 44_950_000))
        self.assertEqual(title_i["share_of_source"], round(100 * 44_950 / 333_679, 2))
        self.assertEqual(title_i["share_of_total"], round(100 * 44_950 / 4_037_660, 2))
        sources = self.get("revenue", year=2024, jurisdiction="NH", level="source")
        self.assertEqual([r["source"] for r in sources], ["federal", "state", "local"])
        self.assertTrue(all(r["category"] is None and r["item"] is None and r["share_of_source"] is None for r in sources))

    def test_amounts_can_be_given_in_another_years_dollars(self):
        [nh] = self.get("revenue/summary", year=2010, jurisdiction="NH", in_dollars_of=2024)
        self.assertEqual(nh["in_dollars_of"], 2024)
        self.assertEqual(nh["total"]["amount_adjusted"], in_dollars_of(nh["total"]["amount"], 2010, 2024))
        self.assertGreater(nh["total"]["per_pupil_adjusted"], nh["total"]["per_pupil"])

    def test_the_nation_is_every_state_and_dc(self):
        rows = self.get("revenue/summary", year=2024)
        states = [r for r in rows if r["jurisdiction"]["code"] != "US"]
        [nation] = [r for r in rows if r["jurisdiction"]["code"] == "US"]
        self.assertEqual(len(states), 51)
        self.assertEqual(sum(r["total"]["amount"] for r in states), nation["total"]["amount"])
        self.assertEqual(nation["enrollment"], 46_370_928)

    def test_bad_levels_and_sources_are_refused(self):
        self.assertEqual(self.api.get(f"{self.url}/revenue", params={"level": "program"}).status_code, 422)
        self.assertEqual(self.api.get(f"{self.url}/revenue", params={"source": "county"}).status_code, 422)


if __name__ == "__main__":
    unittest.main()
