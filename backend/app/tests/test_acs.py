"""
Tests for the American Community Survey load, run against the local database after `alembic upgrade head`:

    docker exec -w /app education-backend-backend-1 python -m unittest app.tests.test_acs -v
"""
import unittest

from sqlalchemy import text

from app.core.db import engine
from app.etl import acs
from app.etl.core import load_config

CONFIG = load_config(acs.CONFIG)
CONWAY = "0600000US3300314660"


class AcsParseTests(unittest.TestCase):
    def test_both_table_list_formats_give_labels_and_indents(self):
        pipe = ["Table ID|Line|Indent|Unique ID|Label|Title|Universe|Type\n",
                "B25004|1.0|0|B25004_001|Total:|Vacancy Status|Vacant housing units|int\n",
                "B25004|6.0|1|B25004_006|For seasonal, recreational, or occasional use|Vacancy Status|Vacant housing units|int\n",
                "B01001|1.0|0|B01001_001|Total:|Sex by Age|Total population|int\n"]
        shells = acs.parse_shells(pipe, ["B25004"], pipe=True)
        self.assertEqual(shells["B25004"]["lines"][1], ["B25004_006", 1, "For seasonal, recreational, or occasional use"])
        self.assertEqual((shells["B25004"]["universe"], shells["B25004"]["five_year"]), ("Vacant housing units", True))
        old = ["Table ID,Line,UniqueID,Stub,Data Release\n",
               'B16002, ,,DETAILED HOUSEHOLD LANGUAGE BY HOUSEHOLD LIMITED ENGLISH SPEAKING STATUS,1\n',
               "B16002, ,,Universe:  Households,\n", "B16002,1,B16002_001,Total:,\n",
               'B25004, ,,VACANCY STATUS,"1,5"\n', "B25004,1,B25004_001,Total:,\n"]
        shells = acs.parse_shells(old, ["B16002", "B25004"], pipe=False)
        self.assertEqual((shells["B16002"]["five_year"], shells["B16002"]["universe"]), (False, "Households"))
        self.assertTrue(shells["B25004"]["five_year"])

    def test_a_summary_file_keeps_new_hampshires_rows(self):
        lines = ["GEO_ID|B19013_E001|B19013_M001\n", "0100000US|80000|100\n", f"{CONWAY}|64385|7855\n",
                 "0600000US2500100000|1|1\n", "9700000US3302490|64385|7855\n", "0700000US330031466014580|5|5\n",
                 "0400000US33|99031|-555555555\n"]
        columns, rows = acs._state_rows(lines, "33")
        self.assertEqual(columns, ["B19013_E001", "B19013_M001"])
        self.assertEqual(rows, {CONWAY: [64385, 7855], "9700000US3302490": [64385, 7855], "0400000US33": [99031, -555555555]})
        with self.assertRaises(ValueError):
            acs._state_rows(["<!DOCTYPE html>\n"], "33")

    def test_codes_become_annotations(self):
        ids = {a["code"]: i for i, a in CONFIG["annotations"].items()}
        self.assertEqual(acs.value_pair(64385, 7855, ids), (64385, 7855, None, None))
        # Controlled: no sampling error
        self.assertEqual(acs.value_pair(1394868, -555555555, ids), (1394868, 0, None, ids[-555555555]))
        self.assertEqual(acs.value_pair(-666666666, -222222222, ids), (None, None, ids[-666666666], ids[-222222222]))

    def test_places_match_by_name_alias_and_skip(self):
        config = {"town_aliases": {"Hale's location": "Hale's Location"}, "skip_towns": ["Beans purchase"],
                  "district_aliases": {"Oyster River Cooperative School District": "Oyster River Coop"}}
        towns = {"conway": 1, "hale's location": 2, "hart's location": 3}
        districts = {"conway": 10, "oyster river coop": 11, "coos county school district": 12}
        geographies = {
            "0400000US33": "New Hampshire",
            CONWAY: "Conway town, Carroll County, New Hampshire",
            "0600000US3300332500": "Hale's location, Carroll County, New Hampshire",
            "0600000US3300334500": "Hart's Location town, Carroll County, New Hampshire",
            "0600000US3300703700": "Beans purchase, Coos County, New Hampshire",
            "9700000US3302490": "Conway School District, New Hampshire",
            "9700000US3304590": "Oyster River Cooperative School District, New Hampshire",
            "9700000US3301230": "Coos County School District, New Hampshire",
            "9600000US3399999": "Remainder of New Hampshire, New Hampshire",
        }
        areas = acs.match_geographies(geographies, towns, districts, config)
        self.assertEqual(areas[CONWAY], ("town", 1, None))
        self.assertEqual({areas[g][1] for g in areas if areas[g][0] == "town"}, {1, 2, 3})
        self.assertEqual(areas["9700000US3304590"], ("district", 11, "unified"))
        self.assertEqual(areas["9700000US3301230"][1], 12)
        self.assertNotIn("9600000US3399999", areas)
        with self.assertRaises(ValueError):
            acs.match_geographies({**geographies, "0600000US3300799999": "Somewhere town, Coos County, New Hampshire"},
                                  towns, districts, config)
        with self.assertRaises(ValueError):  # two Census districts for one of ours
            acs.match_geographies({**geographies, "9500000US3302491": "Conway School District, New Hampshire"},
                                  towns, districts, config)

    def test_an_earlier_release_has_a_value_when_it_means_the_same(self):
        latest = {"tables": {"B25034": {"lines": [["B25034_002", 1, "Built 2020 or later"]]},
                             "B19013": {"lines": [["B19013_001", 0, "Median household income (in 2024 inflation-adjusted dollars)"]]},
                             "B08301": {"lines": [["B08301_010", 1, "Public transportation"]]}}}
        earlier = {"tables": {"B25034": {"five_year": True, "lines": [["B25034_002", None, "Built 2014 or later"]]},
                              "B19013": {"five_year": True, "lines": [["B19013_001", None, "MEDIAN HOUSEHOLD INCOME (IN 2019 INFLATION-ADJUSTED DOLLARS)"]]},
                              "B08301": {"five_year": True, "lines": [["B08301_010", None, "Public transportation (excluding taxicab):"]]}}}
        self.assertEqual(acs.comparability(latest, earlier, "count", "B25034_002", "B25034"), "years_move")
        self.assertEqual(acs.comparability(latest, earlier, "dollars", "B19013_001", "B19013"), "dollars")
        self.assertIsNone(acs.comparability(latest, earlier, "count", "B08301_010", "B08301"))
        self.assertIsNone(acs.comparability(latest, {"tables": {}}, "count", "B25034_002", "B25034"))

    def test_the_summarys_margins_follow_censuss_formulas(self):
        config = {"reliability": {"high": 15, "caution": 30},
                  "summary": {"share": {"share": ["X"], "of": ["Y"]}, "sum": {"sum": ["A", "B", "C"]}, "value": {"value": "A"}}}
        values = {"X": (2126, 309), "Y": (7151, 306), "A": (10, 5), "B": (0, 19), "C": (0, 12)}
        found = acs.summary(values, config)
        self.assertEqual(found["share"], (29.7, 4.1, "high"))  # CV 8.5%
        # Only the largest margin among the zero parts counts
        self.assertAlmostEqual(found["sum"][1], (5 ** 2 + 19 ** 2) ** 0.5)
        self.assertEqual(found["value"][2], "low")  # CV 30.4%
        self.assertEqual(acs.reliability(100, 0, config), "high")
        self.assertEqual(acs.reliability(0, 19, config), "low")

    def test_the_variables_and_views_fit(self):
        variables = acs.read_variables()
        self.assertEqual(len(variables), 1195)
        self.assertEqual({v["variable"].split("_")[0] for v in variables}, set(CONFIG["tables"]))
        self.assertTrue(all(term in {v["variable"] for v in variables}
                            for measure in CONFIG["summary"].values() for term in acs.summary_terms(measure)))
        self.assertEqual(len(acs.view_statements(CONFIG, variables)), 2 * len(acs.view_names(CONFIG)))


def _values(conn, level, place_id, year):
    where = {"town": "e.town_id_fk = :place", "district": "e.district_id_fk = :place", "state": "TRUE"}[level]
    return {code: (None if e is None else float(e), None if m is None else float(m)) for code, e, m in conn.execute(text(
        f"SELECT v.code, e.estimate, e.moe FROM {level}_acs_estimate e JOIN acs_variable v ON v.id = e.variable_id_fk "
        f"WHERE {where} AND e.release_year = :year"), {"place": place_id, "year": year}).all()}


class AcsLoadTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with engine.connect() as conn:
            cls.conway = conn.execute(text("SELECT id FROM town WHERE name = 'Conway'")).scalar()
            cls.conway_district = conn.execute(text("SELECT id FROM district WHERE name = 'Conway'")).scalar()

    def test_every_town_district_and_release_is_loaded(self):
        with engine.connect() as conn:
            self.assertEqual(conn.execute(text("SELECT count(*) FROM acs_town")).scalar(), 236)
            self.assertEqual(dict(conn.execute(text("SELECT census_type, count(*) FROM acs_district GROUP BY 1")).all()),
                             {"elementary": 88, "secondary": 9, "unified": 82})
            variables = dict(conn.execute(text("SELECT release_year, count(*) FROM acs_variable_release GROUP BY 1")).all())
            self.assertEqual(variables[2024], 1195)
            self.assertEqual(variables[2019], 1155)  # household language wasn't published for towns; two lines changed
            # Census gives no per capita income for Millsfield, which has a handful of residents
            missing = {"town": 1}
            for level, places in (("town", 236), ("district", 179), ("state", 1)):
                counts = dict(conn.execute(text(f"SELECT release_year, count(*) FROM {level}_acs_estimate GROUP BY 1")).all())
                self.assertEqual(counts, {year: places * n - missing.get(level, 0) for year, n in variables.items()}, level)

    def test_conways_figures(self):
        with engine.connect() as conn:
            income = dict(conn.execute(text(
                "SELECT release_year, median_household_income FROM town_acs_income WHERE town_id_fk = :t"), {"t": self.conway}).all())
            self.assertEqual(income, {2024: 64385, 2019: 62198})
            seasonal, moe = conn.execute(text(
                "SELECT vacant_seasonal, vacant_seasonal_moe FROM town_acs_housing WHERE town_id_fk = :t AND release_year = 2024"),
                {"t": self.conway}).one()
            self.assertEqual((seasonal, moe), (2126, 309))
            # Household language wasn't in the 2015-2019 release for towns
            self.assertEqual(dict(conn.execute(text(
                "SELECT release_year, b16002_001 IS NULL FROM town_acs_race_language WHERE town_id_fk = :t"), {"t": self.conway}).all()),
                {2024: False, 2019: True})
            # A one-town district has the town's figures
            self.assertEqual(conn.execute(text(
                "SELECT population FROM district_acs_population WHERE district_id_fk = :d AND release_year = 2024"),
                {"d": self.conway_district}).scalar(), 10141)

    def test_the_summary_views_match_the_formulas(self):
        with engine.connect() as conn:
            for level, place in (("town", self.conway), ("state", None)):
                for year in (2024, 2019):
                    expected = acs.summary(_values(conn, level, place, year), CONFIG)
                    where = "town_id_fk = :place AND " if level == "town" else ""
                    row = conn.execute(text(f"SELECT * FROM {level}_acs_summary WHERE {where}release_year = :year"),
                                       {"place": place, "year": year}).mappings().one()
                    for name, (value, moe, reliability) in expected.items():
                        found = (row[name], row[f"{name}_moe"], row[f"{name}_reliability"])
                        if value is None:
                            self.assertIsNone(found[0], f"{level} {year} {name}")
                            continue
                        self.assertAlmostEqual(float(found[0]), value, places=1, msg=f"{level} {year} {name}")
                        if moe is not None:
                            self.assertAlmostEqual(float(found[1]), round(moe, 1), places=1, msg=f"{level} {year} {name} moe")
                        self.assertEqual(found[2], reliability, f"{level} {year} {name} reliability")
            seasonal = conn.execute(text("SELECT seasonal_pct, seasonal_pct_moe, under_6_poverty_pct_reliability "
                                         "FROM town_acs_summary WHERE town_id_fk = :t AND release_year = 2024"), {"t": self.conway}).one()
            self.assertEqual((float(seasonal[0]), float(seasonal[1]), seasonal[2]), (29.7, 4.1, "low"))

    def test_elementary_and_unified_districts_cover_the_state_once(self):
        with engine.connect() as conn:
            covered = conn.execute(text("""
                SELECT sum(p.children_under_18) FROM district_acs_children p
                JOIN acs_district d ON d.district_id_fk = p.district_id_fk
                WHERE p.release_year = 2024 AND d.census_type IN ('elementary', 'unified')
            """)).scalar()
            state = conn.execute(text("SELECT children_under_18 FROM state_acs_children WHERE release_year = 2024")).scalar()
        self.assertEqual(state, 254480)
        self.assertLessEqual(state - covered, 10)


class AcsApiTests(unittest.TestCase):
    """Against the loaded database (the app needs the backend's image: python -m unittest in Docker)"""

    @classmethod
    def setUpClass(cls):
        from fastapi.testclient import TestClient
        from app.core.config import settings
        from app.main import app
        cls.api, cls.prefix = TestClient(app), f"{settings.API_V1_STR}/acs"
        with engine.connect() as conn:
            cls.conway = conn.execute(text("SELECT id FROM town WHERE name = 'Conway'")).scalar()
            cls.souhegan = conn.execute(text("SELECT id FROM district WHERE name = 'Souhegan Cooperative'")).scalar()

    def get(self, path, status=200, **params):
        response = self.api.get(f"{self.prefix}/{path}", params=params)
        self.assertEqual(response.status_code, status, response.text)
        return response.json()

    def test_the_lists_describe_releases_topics_values_and_measures(self):
        self.assertEqual([(r["year"], r["period"]) for r in self.get("release")], [(2019, "2015-2019"), (2024, "2020-2024")])
        topics = self.get("topic")
        self.assertEqual(len(topics), 10)
        self.assertIn("B25004", [t["code"] for t in next(t for t in topics if t["code"] == "housing")["tables"]])
        housing = self.get("variable", topic="housing", tier="core")
        self.assertEqual(len(housing), 28)
        seasonal = next(v for v in housing if v["code"] == "B25004_006")
        self.assertEqual((seasonal["column_name"], seasonal["unit"], [r["year"] for r in seasonal["releases"]]),
                         ("vacant_seasonal", "count", [2024, 2019]))
        measures = self.get("measure")
        self.assertEqual(len(measures), 40)
        self.assertEqual({m["name"]: m["unit"] for m in measures}["seasonal_pct"], "percent")
        self.assertTrue(all(m["label"] and m["description"] for m in measures))

    def test_a_towns_summary_with_its_change_since_2015_2019(self):
        [conway] = self.get("town/summary", town_id=self.conway, compare_to=2019)
        self.assertEqual((conway["town_name"], conway["release_year"], conway["period"]), ("Conway", 2024, "2020-2024"))
        seasonal = conway["measures"]["seasonal_pct"]
        self.assertEqual((seasonal["value"], seasonal["moe"], seasonal["reliability"]), (29.7, 4.1, "high"))
        self.assertEqual((seasonal["compare"]["release_year"], seasonal["compare"]["value"], seasonal["compare"]["change"]),
                         (2019, 31.0, -1.3))
        self.assertFalse(seasonal["compare"]["significant"])  # 1.3 points against margins of 4.1 and 4.6
        income = conway["measures"]["median_household_income"]
        self.assertEqual((income["value"], income["compare"]["value"]), (64385, 62198))
        self.assertEqual(list(conway["measures"]), [m["name"] for m in self.get("measure")])
        # Overlapping or unknown releases aren't compared
        self.get("town/summary", status=422, compare_to=2022)

    def test_summary_filters(self):
        self.assertEqual(len(self.get("town/summary")), 236 * 2)
        self.assertEqual(len(self.get("town/summary", release=2024)), 236)
        souhegan_towns = self.get("town/summary", release=2024, district_id=self.souhegan)
        self.assertEqual(sorted(t["town_name"] for t in souhegan_towns), ["Amherst", "Mont Vernon"])
        self.assertEqual(len(self.get("district/summary", release=2024, census_type="secondary")), 9)
        [state] = self.get("state/summary", release=2024, compare_to=2019)
        self.assertEqual(state["measures"]["population"]["value"], 1394868)
        self.assertTrue(state["measures"]["population"]["compare"]["significant"])  # controlled: no sampling error

    def test_a_topics_values(self):
        [conway] = self.get("town/housing", town_id=self.conway, release=2024)
        self.assertEqual(len(conway["values"]), 28)
        self.assertEqual(conway["values"]["vacant_seasonal"], {"estimate": 2126, "moe": 309})
        [conway] = self.get("town/housing", town_id=self.conway, release=2024, tier="all")
        self.assertEqual(len(conway["values"]), 164)
        rows = self.get("town/housing", variables="vacant_seasonal,housing_units")
        self.assertEqual((len(rows), list(rows[0]["values"])), (236 * 2, ["vacant_seasonal", "housing_units"]))
        # Every town, every value, no filter
        self.assertEqual(len(self.get("town/poverty", tier="all")), 236 * 2)
        [district] = self.get("district/children", district_id=self.souhegan, release=2024)
        self.assertEqual(district["census_type"], "secondary")
        self.assertEqual(len(self.get("state/income")), 2)
        self.get("town/housing", status=422, variables="vacant_seasonal,no_such_value")
        self.get("town/weather", status=404)


if __name__ == "__main__":
    unittest.main()
