"""
Tests for the adequacy aid load, run against the local database after `alembic upgrade head`:

    docker exec -w /app education-backend-backend-1 python -m unittest app.tests.test_adequacy_aid -v
"""
import unittest

from sqlalchemy import text

from app.core.db import engine
from app.etl import adequacy_aid
from app.etl.core import load_config
from app.etl.formula import evaluate, names

CONFIG = load_config(adequacy_aid.CONFIG)
CONWAY, AMHERST, MONT_VERNON, SOUHEGAN = 113, 17, 367, 493


class FormulaTests(unittest.TestCase):
    def test_arithmetic_comparisons_and_functions(self):
        values = {"a": 926.6644, "rate": 4351, "swept": 3795601, "cost": 5244357.52}
        self.assertAlmostEqual(evaluate("a * rate", values), 4031916.80, places=1)
        self.assertAlmostEqual(evaluate("max(0, cost - swept)", values), 1448756.52, places=2)
        self.assertEqual(evaluate("max(0, swept - cost)", values), 0)
        self.assertEqual(evaluate("clamp(0.00221069 * (7003972 - 11550306), 0, 11730)", {}), 0)
        self.assertEqual(evaluate("(swept <= cost) * 10", values), 10)
        self.assertEqual(names("frl_adm * clamp(eng_factor * (eng_ceiling - ev_per_frl_pupil), 0, eng_max_per_pupil)"),
                         {"frl_adm", "eng_factor", "eng_ceiling", "ev_per_frl_pupil", "eng_max_per_pupil"})

    def test_anything_else_is_refused(self):
        for formula in ("__import__('os').system('true')", "a.real", "[a]", "a if a else 1", "lambda: 1", "open('x')", "'a'"):
            with self.assertRaises((ValueError, KeyError, SyntaxError), msg=formula):
                evaluate(formula, {"a": 1})
        with self.assertRaises(KeyError):
            evaluate("unknown * 2", {})


class AdequacyAidParseTests(unittest.TestCase):
    def test_every_years_steps_use_its_own_components_and_parameters(self):
        for year, settings in CONFIG["years"].items():
            known = set(settings["summary"]["columns"]) | set(settings["parameters"])
            for step in settings["steps"]:
                self.assertIn(step["component"], settings["summary"]["columns"], f"FY{year} {step['component']}")
                if step.get("formula"):
                    self.assertLessEqual(names(step["formula"]), known, f"FY{year} {step['component']}")

    def test_conways_fy2027_calculation_from_the_workbook(self):
        towns, lettered, state = adequacy_aid.read_summary(CONFIG, 2027)
        conway = towns[CONWAY]
        self.assertEqual((conway["resident_adm_base"], conway["base_adequacy_aid"], conway["swept"], conway["adequacy_grant"]),
                         (926.6644, 4031916.8, 3795601, 1786171.26))
        self.assertEqual(len(lettered), 15)  # the unincorporated places below the towns
        self.assertGreater(adequacy_aid.check_steps(CONFIG, 2027, towns), 3000)

    def test_a_split_towns_shares_add_up_and_the_dresden_number_is_fixed(self):
        shares = {(d, t): (g, s) for d, t, _, g, s in adequacy_aid.read_split(CONFIG, 2027)}
        self.assertEqual(shares[(SOUHEGAN, AMHERST)], (1665656.45, 1136067))
        self.assertEqual(shares[(SOUHEGAN, MONT_VERNON)], (487447.36, 170534))
        fy2020 = adequacy_aid.read_split(CONFIG, 2020)
        self.assertIn((142, 233), {(d, t) for d, t, *_ in fy2020})  # Dresden (Hanover): town 0 in the DOE's file
        self.assertNotIn(0, {t for _, t, *_ in fy2020})


class AdequacyAidLoadTests(unittest.TestCase):
    def query(self, sql, **params):
        with engine.connect() as conn:
            return conn.execute(text(sql), params).all()

    def test_every_year_town_and_district_is_loaded(self):
        years = dict(self.query("SELECT fiscal_year, status FROM adequacy_aid_year"))
        self.assertEqual(years, {**{y: "final" for y in range(2020, 2027)}, 2027: "estimate"})
        towns = dict(self.query("SELECT fiscal_year, count(DISTINCT town_id_fk) FROM town_adequacy_aid GROUP BY 1"))
        self.assertEqual(set(towns.values()), {237})
        shares = self.query("SELECT fiscal_year, count(*), count(*) FILTER (WHERE source = 'doe_split'), count(DISTINCT town_id_fk) "
                            "FROM district_adequacy_aid_share GROUP BY 1")
        self.assertEqual({(n, split, towns) for _, n, split, towns in shares}, {(265, 56, 237)})

    def test_each_towns_shares_add_up_to_its_grant_and_swept(self):
        self.assertEqual(self.query("""
            SELECT count(*) FROM (
                SELECT s.town_id_fk, s.fiscal_year, sum(s.adequacy_grant) g, sum(s.swept_retained) w
                FROM district_adequacy_aid_share s GROUP BY 1, 2
            ) x JOIN town_adequacy_aid_summary t ON t.town_id_fk = x.town_id_fk AND t.fiscal_year = x.fiscal_year
            WHERE abs(x.g - t.adequacy_grant) > 0.01 OR abs(x.w - t.swept) > 0.5
        """)[0][0], 0)

    def test_how_the_fy2027_calculation_works(self):
        rates = dict(self.query("SELECT code, value FROM adequacy_aid_parameter WHERE fiscal_year = 2027 AND code LIKE '%per_pupil'"))
        self.assertEqual({k: float(v) for k, v in rates.items() if k in ("base_per_pupil", "frl_per_pupil", "sped_per_pupil", "ell_per_pupil")},
                         {"base_per_pupil": 4351, "frl_per_pupil": 2441, "sped_per_pupil": 2229, "ell_per_pupil": 849})
        steps = self.query("SELECT s.step, c.code, s.formula FROM adequacy_aid_step s JOIN adequacy_aid_component c ON c.id = s.component_id_fk "
                           "WHERE s.fiscal_year = 2027 ORDER BY s.step")
        self.assertEqual(steps[0][1:], ("base_adequacy_aid", "resident_adm_base * base_per_pupil"))
        self.assertEqual(steps[-1][1], "final_total_state_grant")

    def test_conway_and_souhegan(self):
        [conway] = self.query("SELECT total_cost, swept, preliminary_grant, hold_harmless, adequacy_grant, total_state_aid "
                              "FROM town_adequacy_aid_summary WHERE town_id_fk = :t AND fiscal_year = 2027", t=CONWAY)
        self.assertEqual(tuple(float(v) for v in conway), (5244357.52, 3795601, 1448756.52, 337414.7448, 1786171.26, 5581772.26))
        [souhegan] = self.query("SELECT adequacy_grant, swept_retained, member_towns FROM district_adequacy_aid "
                                "WHERE district_id_fk = :d AND fiscal_year = 2027", d=SOUHEGAN)
        self.assertEqual((float(souhegan[0]), float(souhegan[1]), souhegan[2]), (2153103.81, 1306601, 2))

    def test_the_grant_matches_what_districts_report(self):
        [(reported, matching)] = self.query("""
            SELECT count(reported_adequacy_grant), count(*) FILTER (WHERE abs(reported_difference) < 1)
            FROM district_adequacy_aid WHERE fiscal_year BETWEEN 2020 AND 2025
        """)
        self.assertGreater(matching / reported, 0.98)
        [(difference,)] = self.query("SELECT reported_difference FROM district_adequacy_aid WHERE district_id_fk = :d AND fiscal_year = 2023", d=CONWAY)
        self.assertEqual(difference, 0)


class AdequacyAidApiTests(unittest.TestCase):
    """Against the loaded database (the app needs the backend's image: python -m unittest in Docker)"""

    @classmethod
    def setUpClass(cls):
        from fastapi.testclient import TestClient
        from app.core.config import settings
        from app.main import app
        cls.api, cls.prefix = TestClient(app), f"{settings.API_V1_STR}/finance/adequacy-aid"

    def get(self, path, status=200, **params):
        response = self.api.get(f"{self.prefix}/{path}", params=params)
        self.assertEqual(response.status_code, status, response.text)
        return response.json()

    def test_years_and_how_a_year_works(self):
        years = self.get("years")
        self.assertEqual([(y["fiscal_year"], y["status"]) for y in years][-2:], [(2026, "final"), (2027, "estimate")])
        formula = self.get("formula", year=2027)
        self.assertEqual({p["code"]: p["value"] for p in formula["parameters"]}["base_per_pupil"], 4351)
        self.assertEqual((formula["steps"][0]["code"], formula["steps"][0]["uses"]), ("base_adequacy_aid", ["base_per_pupil", "resident_adm_base"]))
        # Every name a formula uses is a parameter or a named part
        components = {c["code"]: c for c in formula["components"]}
        self.assertEqual((components["resident_adm_base"]["unit"], components["swept"]["role"]), ("count", "swept"))
        known = set(components) | {p["code"] for p in formula["parameters"]}
        self.assertLessEqual({name for s in formula["steps"] for name in s["uses"]} | {s["code"] for s in formula["steps"]}, known)
        self.get("formula", status=404, year=2019)

    def test_a_districts_calculation_has_every_year_and_its_towns(self):
        years = self.get(f"district/{SOUHEGAN}/calculation")
        self.assertEqual([y["fiscal_year"] for y in years], list(range(2020, 2028)))
        fy2027 = years[-1]
        self.assertEqual((fy2027["status"], fy2027["adequacy_grant"], fy2027["swept_retained"]), ("estimate", 2153103.81, 1306601))
        amherst = next(t for t in fy2027["towns"] if t["town_id"] == AMHERST)
        self.assertEqual((amherst["share"]["adequacy_grant"], amherst["share"]["source"]), (1665656.45, "doe_split"))
        base = amherst["steps"][0]
        self.assertEqual((base["code"], base["inputs"]), ("base_adequacy_aid", {"base_per_pupil": 4351, "resident_adm_base": 1779.5653}))
        self.assertAlmostEqual(base["inputs"]["base_per_pupil"] * base["inputs"]["resident_adm_base"], base["value"], places=1)
        self.assertEqual(sum(t["share"]["adequacy_grant"] for t in fy2027["towns"]), fy2027["adequacy_grant"])
        self.get("district/999999/calculation", status=404)

    def test_district_town_and_state_lists(self):
        districts = self.get("district", year=2023)
        conway = next(d for d in districts if d["district_id"] == CONWAY)
        self.assertEqual((conway["adequacy_grant"], conway["reported_difference"]), (3740927.99, 0))
        self.assertEqual(len(self.get("district")), 179 * 8)
        self.assertEqual(sorted(t["town_name"] for t in self.get("town", district_id=SOUHEGAN, year=2027)), ["Amherst", "Mont Vernon"])
        [conway_town] = self.get(f"town/{CONWAY}/calculation", year=2027)
        self.assertEqual((conway_town["totals"]["total_state_aid"], [d["district_id"] for d in conway_town["districts"]]), (5581772.26, [CONWAY]))
        state = self.get("state", year=2027)[0]
        self.assertEqual(state["values"]["adequacy_grant"], state["adequacy_grant"])


if __name__ == "__main__":
    unittest.main()
