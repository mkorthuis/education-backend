"""
Tests for the private schools' Form 990 load, run against the local database after `alembic upgrade head`:

    docker exec -w /app education-backend-backend-1 python -m unittest app.tests.test_private_990 -v
"""
import json
import os
import tempfile
import unittest

from sqlalchemy import text

from app.core.db import engine
from app.etl import private_990
from app.etl.core import config_path, load_config


def return_xml(form: str, main: str, schedules: str = "") -> bytes:
    """A return as the IRS e-file data gives it, with just the parts the parser reads"""
    return f"""<?xml version="1.0" encoding="utf-8"?>
<Return xmlns="http://www.irs.gov/efile">
  <ReturnHeader>
    <TaxPeriodEndDt>2025-06-30</TaxPeriodEndDt>
    <ReturnTypeCd>{form}</ReturnTypeCd>
    <Filer><EIN>020000001</EIN><BusinessName><BusinessNameLine1Txt>Example  Academy</BusinessNameLine1Txt></BusinessName></Filer>
    <PreparerFirmGrp><PreparerFirmName><BusinessNameLine1Txt>An Accounting Firm</BusinessNameLine1Txt></PreparerFirmName></PreparerFirmGrp>
  </ReturnHeader>
  <ReturnData>{main}{schedules}</ReturnData>
</Return>""".encode()


class Private990ParseTests(unittest.TestCase):
    def test_a_990s_figures_with_its_tuition_lines_and_endowment(self):
        parsed = private_990.parse_return(return_xml("990", """
            <IRS990>
              <FormationYr>1991</FormationYr>
              <MissionDesc>An independent   day school.</MissionDesc>
              <TotalEmployeeCnt>41</TotalEmployeeCnt>
              <TotalVolunteersCnt>18</TotalVolunteersCnt>
              <IndivRcvdGreaterThan100KCnt>3</IndivRcvdGreaterThan100KCnt>
              <CYContributionsGrantsAmt>600</CYContributionsGrantsAmt>
              <CYProgramServiceRevenueAmt>3000</CYProgramServiceRevenueAmt>
              <PYTotalRevenueAmt>3500</PYTotalRevenueAmt><CYTotalRevenueAmt>3700</CYTotalRevenueAmt>
              <PYTotalExpensesAmt>3600</PYTotalExpensesAmt><CYTotalExpensesAmt>3800</CYTotalExpensesAmt>
              <CYSalariesCompEmpBnftPaidAmt>2400</CYSalariesCompEmpBnftPaidAmt>
              <TotalAssetsEOYAmt>11000</TotalAssetsEOYAmt><TotalLiabilitiesEOYAmt>1000</TotalLiabilitiesEOYAmt>
              <NetAssetsOrFundBalancesEOYAmt>10000</NetAssetsOrFundBalancesEOYAmt>
              <ProgramServiceRevenueGrp><Desc>Net tuition and fees</Desc><BusinessCd>611110</BusinessCd><TotalRevenueColumnAmt>2800</TotalRevenueColumnAmt></ProgramServiceRevenueGrp>
              <ProgramServiceRevenueGrp><Desc>Summer camp</Desc><TotalRevenueColumnAmt>100</TotalRevenueColumnAmt></ProgramServiceRevenueGrp>
              <NetGainOrLossInvestmentsGrp><TotalRevenueColumnAmt>-25</TotalRevenueColumnAmt></NetGainOrLossInvestmentsGrp>
              <TotalFunctionalExpensesGrp><TotalAmt>3800</TotalAmt><ProgramServicesAmt>2600</ProgramServicesAmt>
                <ManagementAndGeneralAmt>1150</ManagementAndGeneralAmt><FundraisingAmt>50</FundraisingAmt></TotalFunctionalExpensesGrp>
              <LandBldgEquipBasisNetGrp><BOYAmt>9000</BOYAmt><EOYAmt>9400</EOYAmt></LandBldgEquipBasisNetGrp>
            </IRS990>""", """<IRS990ScheduleD><CYEndwmtFundGrp><EndYearBalanceAmt>1800</EndYearBalanceAmt></CYEndwmtFundGrp>
              <BoardDesignatedBalanceEOYPct>0.31290</BoardDesignatedBalanceEOYPct><PrmnntEndowmentBalanceEOYPct>0.65980</PrmnntEndowmentBalanceEOYPct>
            </IRS990ScheduleD>"""), "1")
        # The filer's name, not the preparer's
        self.assertEqual((parsed["ein"], parsed["tax_period_end"], parsed["form"], parsed["name_as_filed"]),
                         ("020000001", "2025-06-30", "990", "Example Academy"))
        self.assertEqual((parsed["total_revenue"], parsed["prior_total_revenue"], parsed["total_expenses"], parsed["prior_total_expenses"]),
                         (3700, 3500, 3800, 3600))
        self.assertEqual((parsed["program_expenses"], parsed["management_expenses"], parsed["fundraising_expenses"]), (2600, 1150, 50))
        self.assertEqual((parsed["investment_gains"], parsed["land_buildings_equipment_eoy"], parsed["tax_exempt_bonds_eoy"]), (-25, 9400, None))
        self.assertEqual(parsed["lines"], [{"description": "Net tuition and fees", "business_code": "611110", "amount": 2800},
                                           {"description": "Summer camp", "business_code": None, "amount": 100}])
        self.assertEqual((parsed["endowment_eoy"], parsed["endowment_board_designated_share"], parsed["endowment_permanent_share"],
                          parsed["endowment_term_share"]), (1800, 0.3129, 0.6598, None))
        self.assertEqual((parsed["employees"], parsed["volunteers"], parsed["paid_over_100k"], parsed["government_grants"]), (41, 18, 3, None))
        self.assertEqual((parsed["founded"], parsed["mission"]), (1991, "An independent day school."))

    def test_a_990_ez_has_no_prior_year_or_employee_count(self):
        parsed = private_990.parse_return(return_xml("990EZ", """
            <IRS990EZ>
              <PrimaryExemptPurposeTxt>CATHOLIC EDUCATION</PrimaryExemptPurposeTxt>
              <ContributionsGiftsGrantsEtcAmt>50</ContributionsGiftsGrantsEtcAmt>
              <ProgramServiceRevenueAmt>150</ProgramServiceRevenueAmt>
              <TotalRevenueAmt>200</TotalRevenueAmt><TotalExpensesAmt>180</TotalExpensesAmt>
              <Form990TotalAssetsGrp><BOYAmt>90</BOYAmt><EOYAmt>110</EOYAmt></Form990TotalAssetsGrp>
              <SumOfTotalLiabilitiesGrp><BOYAmt>10</BOYAmt><EOYAmt>20</EOYAmt></SumOfTotalLiabilitiesGrp>
              <NetAssetsOrFundBalancesGrp><BOYAmt>80</BOYAmt><EOYAmt>90</EOYAmt></NetAssetsOrFundBalancesGrp>
            </IRS990EZ>"""), "2")
        self.assertEqual((parsed["form"], parsed["total_revenue"], parsed["total_expenses"], parsed["total_assets_eoy"],
                          parsed["total_liabilities_eoy"], parsed["net_assets_eoy"]), ("990EZ", 200, 180, 110, 20, 90))
        self.assertEqual((parsed["prior_total_revenue"], parsed["employees"], parsed["program_expenses"], parsed["lines"]), (None, None, None, []))
        self.assertEqual(parsed["mission"], "CATHOLIC EDUCATION")

    def test_another_kind_of_return_stops_the_fetch(self):
        with self.assertRaises(ValueError):
            private_990.parse_return(return_xml("990PF", "<IRS990PF/>"), "3")


class Private990LinkTests(unittest.TestCase):
    def read(self, *rows):
        with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False) as f:
            f.write("school_id,school_name,status,ein,filer_name,note\n" + "".join(",".join(row) + "\n" for row in rows))
        try:
            return private_990.read_link(f.name)
        finally:
            os.unlink(f.name)

    def test_each_case_with_its_filer(self):
        rows = self.read(("20290", "Concord Christian Academy", "own_return", "205009013", "Concord Christian Academy", ""),
                         ("20150", "Claremont Christian Academy", "no_irs_record", "", "", ""))
        self.assertEqual(rows[0], {"school_id": 20290, "status": "own_return", "ein": "205009013",
                                   "filer_name": "Concord Christian Academy", "note": None})
        self.assertIsNone(rows[1]["ein"])

    def test_a_bad_row_stops_the_load(self):
        for row in (("1", "A", "files", "", "", ""),                     # unknown status
                    ("1", "A", "own_return", "2050", "", ""),             # not nine digits
                    ("1", "A", "operator_return", "", "", "")):           # files, but no EIN
            with self.assertRaises(ValueError, msg=row):
                self.read(row)
        with self.assertRaises(ValueError):
            self.read(("1", "A", "no_irs_record", "", "", ""), ("1", "A", "no_irs_record", "", "", ""))


class Private990OrganizationTests(unittest.TestCase):
    def link(self, ein, name, school_id=1):
        return {"school_id": school_id, "status": "operator_return", "ein": ein, "filer_name": name, "note": None}

    def test_each_ein_once_with_its_latest_founding_year_and_mission(self):
        rows = private_990.organizations(
            [self.link("020347622", "Strafford Learning Center", 1), self.link("020347622", "Strafford Learning Center", 2),
             {"school_id": 3, "status": "no_irs_record", "ein": None, "filer_name": None, "note": None}],
            [{"ein": "020347622", "tax_period_end": "2024-06-30", "founded": 1978, "mission": "Old mission"},
             {"ein": "020347622", "tax_period_end": "2025-06-30", "founded": None, "mission": "Current mission"}])
        self.assertEqual(rows, [("020347622", "Strafford Learning Center", 1978, "Current mission")])

    def test_an_ein_with_two_names_stops_the_load(self):
        with self.assertRaises(ValueError):
            private_990.organizations([self.link("020347622", "Strafford Learning Center", 1), self.link("020347622", "SLC", 2)], [])


class Private990CategoryTests(unittest.TestCase):
    rules = load_config(private_990.CONFIG)["revenue_line_categories"]

    def test_lines_as_filers_word_them(self):
        cases = {
            "Tuition and fees": "tuition", "NON-MEMBER DISTRICT TUITI": "tuition", "Tuition, room and boar": "tuition",
            "John Powers School": "school_program", "RLA": "school_program", "Academy": "school_program",
            "Room & Board Income": "room_and_board", "Board and care": "human_services",
            "Childrens' Services and Schools": "human_services", "Medicare/Medicaid Payments": "human_services",
            "Summer camp": "summer_auxiliary", "AUX.& SUMMER PROGRAMS": "summer_auxiliary",
            "After school program": "extended_care", "Extended school programs": "extended_care",
            "School activity revenue": "student_activities", "Application fees": "student_activities",
            "Transportation services": "transportation", "Income revenues OT": "therapy_tutoring", "Tutoring fees": "therapy_tutoring",
            "Building rental": "rental", "Program services": "unspecified_program", "Fee for service": "unspecified_program",
            "Miscellaneous": "other", "Bad debts": "other",
        }
        self.assertEqual({d: private_990.categorize(d, self.rules) for d in cases}, cases)

    def test_every_rule_names_a_category_the_table_allows(self):
        self.assertTrue({rule["category"] for rule in self.rules} <= set(private_990.CATEGORIES))


class Private990AssetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        config = load_config(private_990.CONFIG)
        directory = config_path(config["directory"])
        cls.link = private_990.read_link(os.path.join(directory, config["link_file"]))
        with open(os.path.join(directory, config["returns_file"])) as f:
            cls.saved = json.load(f)

    def test_every_private_school_has_its_case(self):
        counts = {status: sum(row["status"] == status for row in self.link) for status in private_990.STATUSES}
        self.assertEqual(counts, {"own_return": 44, "operator_return": 24, "postcard_only": 2,
                                  "not_required_religious": 27, "no_irs_record": 37, "placeholder": 2})

    def test_the_returns_are_the_filers_one_per_tax_year(self):
        returns = self.saved["returns"]
        filers = {row["ein"] for row in self.link if row["status"] in private_990.FILES_990}
        self.assertTrue({r["ein"] for r in returns} <= filers)
        self.assertEqual(len({(r["ein"], r["tax_period_end"]) for r in returns}), len(returns))
        # Concord Christian Academy's 2024-25 return, as its page gives it
        cca = next(r for r in returns if r["ein"] == "205009013" and r["tax_period_end"] == "2025-06-30")
        self.assertEqual((cca["total_revenue"], cca["prior_total_revenue"], cca["employees"], cca["founded"]),
                         (4449722, 4137562, 77, 2006))
        self.assertEqual(cca["lines"][0], {"description": "Tuition and fees", "business_code": "611110", "amount": 3737361})


class Private990DatabaseTests(unittest.TestCase):
    """Against the loaded database"""

    def query(self, sql, **params):
        with engine.connect() as conn:
            return conn.execute(text(sql), params).fetchall()

    def test_the_organizations_link_and_returns_are_loaded(self):
        link = dict(self.query("SELECT status, count(*) FROM school_990_link GROUP BY status"))
        self.assertEqual(sum(link.values()), 136)
        self.assertEqual(link["operator_return"], 24)
        # Every EIN in the link is an organization, with or without returns (a church school's has none)
        self.assertEqual(self.query("SELECT count(*) FROM private_org")[0][0],
                         self.query("SELECT count(DISTINCT ein) FROM school_990_link WHERE ein IS NOT NULL")[0][0])
        returns = self.query("SELECT count(*), count(DISTINCT ein) FROM private_org_990")[0]
        with open(os.path.join(config_path(load_config(private_990.CONFIG)["directory"]), "returns.json")) as f:
            saved = json.load(f)["returns"]
        self.assertEqual(tuple(returns), (len(saved), len({r["ein"] for r in saved})))
        self.assertEqual(self.query("SELECT count(*) FROM private_org_990_revenue_line")[0][0], sum(len(r["lines"]) for r in saved))

    def test_an_operator_return_covers_each_of_its_schools(self):
        # Strafford Learning Center runs four of the state's private schools
        schools = self.query("SELECT count(*) FROM school_990_link WHERE ein = '020347622' AND status = 'operator_return'")
        self.assertEqual(schools[0][0], 4)
        years = self.query("SELECT count(*) FROM private_org_990 WHERE ein = '020347622'")
        self.assertGreater(years[0][0], 0)

    def test_a_school_that_files_has_its_years_with_tuition_from_its_lines(self):
        rows = self.query("""
            SELECT o.name, o.founded, r.tax_period_end, r.total_revenue,
                   (SELECT sum(amount) FROM private_org_990_revenue_line WHERE return_id = r.id AND category = 'tuition')
            FROM school_990_link l JOIN private_org o ON o.ein = l.ein JOIN private_org_990 r ON r.ein = o.ein
            WHERE l.school_id_fk = 20290 ORDER BY r.tax_period_end
        """)
        self.assertGreaterEqual(len(rows), 2)
        self.assertEqual((rows[-1][0], rows[-1][1], str(rows[-1][2]), rows[-1][3], rows[-1][4]),
                         ("Concord Christian Academy", 2006, "2025-06-30", 4449722, 3737361))

    def test_a_church_school_has_its_organization_and_no_returns(self):
        # Bishop Brady High School: the Diocese of Manchester's, which needn't file
        rows = self.query("""
            SELECT l.status, o.name, (SELECT count(*) FROM private_org_990 r WHERE r.ein = o.ein)
            FROM school_990_link l JOIN private_org o ON o.ein = l.ein WHERE l.school_id_fk = 20320
        """)
        self.assertEqual((rows[0][0], rows[0][2]), ("not_required_religious", 0))


if __name__ == "__main__":
    unittest.main()
