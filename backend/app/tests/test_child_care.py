"""
Tests for the child care load and API, run against the local database after `alembic upgrade head`:

    docker exec -w /app education-backend-backend-1 python -m unittest app.tests.test_child_care -v
"""
import unittest
from datetime import date, time
from decimal import Decimal

from fastapi.testclient import TestClient
from sqlalchemy import text

from app.core.config import settings
from app.core.db import engine
from app.etl import child_care
from app.etl.core import load_config
from app.main import app

CONFIG = load_config(child_care.CONFIG)
HEADINGS = child_care.page_lists(CONFIG)


def provider(record_id, name, number, record_type="Licensed Group Child Care Program", **fields):
    return {"Id": record_id, "Name": name, "License_Number__c": number, "Capacity__c": 20,
            "RecordType": {"Name": record_type}, **fields}


# A program page, trimmed, with the portal's markup for each section
PAGE = (
    '<span class="slds-text-heading fontStyleName ">Little Learners</span>'
    '<span class="fontStyleSub"> &nbsp;Email</span><span> <p class=" fontStyle slds-p-top_x-small">'
    'The provider has chosen not to display the email address.</p> <br /></span>'
    '<span class="fontStyleSub">Availability</span> <p class="fontStyle slds-p-top_x-small">Accepting Children on Wait List</p>'
    '<h3 class="fontStyleSub" id="ProgramInformation">Program Information</h3>'
    '<div> <span class="main-label">Main Contact: </span> Robyn Andersen, Jo Smith </div>'
    '<div> <span class="main-label">This is a Head Start Program: </span> Yes </div>'
    '<div> <span class="main-label">Capacity:</span> 6 </div>'
    '<div> <span class="main-label">This is an Early Head Start Program: </span> </div>'
    '<div> <h3 class="fontStyleSub" id="Schedules">Hours of Operation and Rates</h3><span>Last Updated: 03/05/2026</span> </div>'
    '<div class="panel panel-default schedulePanel"> <h4>Days</h4> <table><tbody>'
    ' <tr> <td>Monday</td> <td>08:00 AM</td> <td>04:00 PM</td> </tr>'
    ' <tr> <td>Friday</td> <td>08:00 AM</td> <td>12:30 PM</td> </tr> </tbody></table>'
    '<h4 class="heading-for-h4 slds-m-top_large" style="font-weight:600;">Fees</h4> <table> <thead> <tr class="cc-table-head">'
    ' <th>Age Group</th> <th>Hourly</th> <th>Daily</th> <th>Weekly</th> <th>Monthly</th> </tr> </thead> <tbody>'
    ' <tr> <td><b>Toddler</b></td> <td></td> <td></td> <td>$1,250.00</td> <td></td> </tr>'
    ' <tr> <td><b>Preschool</b></td> <td></td> <td>$60.00</td> <td></td> <td></td> </tr> </tbody> </table> </div>'
    # A second schedule that repeats the first, and a third with only rates
    '<div class="panel panel-default schedulePanel"> <h4>Days</h4> <table><tbody>'
    ' <tr> <td>Monday</td> <td>08:00 AM</td> <td>04:00 PM</td> </tr>'
    ' <tr> <td>Friday</td> <td>08:00 AM</td> <td>12:30 PM</td> </tr> </tbody></table>'
    '<h4 class="heading-for-h4 slds-m-top_large" style="font-weight:600;">Fees</h4> <table> <thead> <tr class="cc-table-head">'
    ' <th>Age Group</th> <th>Hourly</th> <th>Daily</th> <th>Weekly</th> <th>Monthly</th> </tr> </thead> <tbody>'
    ' <tr> <td><b>Toddler</b></td> <td></td> <td></td> <td>$1,250.00</td> <td></td> </tr>'
    ' <tr> <td><b>Preschool</b></td> <td></td> <td>$60.00</td> <td></td> <td></td> </tr> </tbody> </table> </div>'
    '<div class="panel panel-default schedulePanel"> <h4 class="heading-for-h4 slds-m-top_large">Fees</h4> <table> <thead>'
    ' <tr class="cc-table-head"> <th>Age Group</th> <th>Hourly</th> <th>Daily</th> <th>Weekly</th> <th>Monthly</th> </tr>'
    ' </thead> <tbody> <tr> <td><b>Preschool</b></td> <td></td> <td>$52.00</td> <td></td> <td></td> </tr> </tbody> </table> </div>'
    '<div class="paddingBottom" id="InspectionMonitoring"> <table><tbody>'
    ' <tr> <td data-label="Visit Date"> 06/23/2025 </td> <td data-label="Type of Visit"> Monitoring Visit </td>'
    ' <td data-label="Level of Compliance"> 173 / 175 </td>'
    ' <td data-label="Details"> <a onClick="getNonComplianceItem(\'a4lcs00000IxQIfAAN\');">View Detail</a> </td>'
    ' <td data-label="Visit Documents"> </td> </tr>'
    ' <tr> <td data-label="Visit Date"> 03/01/2023 </td> <td data-label="Type of Visit"> Renewal Visit </td>'
    ' <td data-label="Level of Compliance"> </td> <td data-label="Details"> </td>'
    ' <td data-label="Visit Documents"> <a href="/nhccis/servlet/doc?id=1&amp;v=2">Visit</a> </td> </tr> </tbody></table></div>'
    '<h3 class="fontStyleSub" id="AgesServed">Vacancies</h3> <span>Last Updated: 10/05/2026</span>'
    '<p>Infant: 6 weeks through 12 months.</p> <td> <span class="main-label">Infant: </span>1 </td>'
    ' <td> <span class="main-label">Toddler: </span>0 </td> <td> <span class="main-label">Preschool: </span> </td>'
    ' <td> <span class="main-label">School Age: </span>10 </td>'
    '<h3 id="CCRR">CCR&amp;R</h3>'
    '<h3 class="fontStyleSub" id="QRISRating">QRIS Recognition</h3> <div class="main-label slds-m-bottom_small">Endorsements: </div>'
    '<span><img src="/nhccis/resource/1645599127000/GSQ_Badge" width="100px" /></span>'
    '<h3 class="fontStyleSub" id="OtherInformation">Other Information</h3><span>Last Updated: 05/17/2025</span>'
    '<tr> <td> <span class="main-label">ENVIRONMENT: </span> </td> <td> <div class="wordBreak "> NO CAT, NO TV USE </div> </td> </tr>'
    '<tr> <td> <span class="main-label"> MEALS: </span> </td> <td> <div class="wordBreak">'
    ' PARENT PROVIDES LUNCH;REFRIGERATION IS AVAILABLE, ON REQUEST </div> </td> </tr>'
    '<tr> <td> <span class="main-label"> TYPE OF CARE: </span> </td> <td> <div class="wordBreak"> Licensed Family Child Care Program </div> </td> </tr>'
)


class ChildCareParseTests(unittest.TestCase):
    def test_shared_values_are_put_back(self):
        answer = {"s": 1, "v": [{"s": 2, "v": {"Id": "a", "RecordType": {"s": 3, "v": {"Name": "Group"}}}},
                                {"s": 4, "v": {"Id": "b", "RecordType": {"r": 3}}}]}
        self.assertEqual(child_care.dereference(answer),
                         [{"Id": "a", "RecordType": {"Name": "Group"}}, {"Id": "b", "RecordType": {"Name": "Group"}}])

    def test_a_page_list_keeps_commas_inside_parentheses(self):
        self.assertEqual(child_care._page_list("CIVIL SERVICE DISCOUNT (POLICE, FIRE, EMERGENCY), MILITARY ASSISTANCE, FIRE"),
                         ["CIVIL SERVICE DISCOUNT (POLICE, FIRE, EMERGENCY)", "MILITARY ASSISTANCE", "FIRE"])
        self.assertEqual(child_care._page_list("FULL DAY; PART DAY (MORNINGS, AFTERNOONS)"), ["FULL DAY", "PART DAY (MORNINGS, AFTERNOONS)"])

    def test_the_youngest_age_comes_in_weeks_or_in_years_and_months(self):
        self.assertEqual(child_care.min_age_months({"age_wks_lo__c": 6}), 1.4)
        self.assertEqual(child_care.min_age_months({"age_yrs_lo__c": 2, "age_mos_lo__c": 8}), 32)
        self.assertEqual(child_care.min_age_months({"age_yrs_lo__c": 4.8}), 57.6)
        self.assertIsNone(child_care.min_age_months({}))
        with self.assertRaises(ValueError):
            child_care.min_age_months({"age_wks_lo__c": 6, "age_mos_lo__c": 3})

    def test_age_groups_come_from_the_search_then_the_license_then_the_age_range(self):
        flags = child_care.age_group_flags
        # The program's own age groups win over its license
        self.assertEqual(flags(["School Age"], ["Infant/Toddler Program", "School Age Program"], 1.4, 144),
                         {"infant": False, "toddler": False, "preschool": False, "school_age": True, "age_groups_source": "listed"})
        self.assertEqual(flags([], ["Infant/Toddler Program", "Group child care center", "Preschool Program"], 1.4, 144),
                         {"infant": True, "toddler": True, "preschool": True, "school_age": False, "age_groups_source": "license"})
        # A family home, by its range: 18 months to 5 years is toddlers and preschoolers
        self.assertEqual(flags([], ["Family Child Care Home"], 18, 60),
                         {"infant": False, "toddler": True, "preschool": True, "school_age": False, "age_groups_source": "age_range"})
        self.assertEqual(flags([], ["Family Child Care Home"], 1.4, 144),
                         {"infant": True, "toddler": True, "preschool": True, "school_age": True, "age_groups_source": "age_range"})
        self.assertEqual(flags([], ["Facility"], None, None),
                         {"infant": None, "toddler": None, "preschool": None, "school_age": None, "age_groups_source": None})

    def test_fixed_lists_give_ids_and_an_unknown_value_stops_the_load(self):
        lists = child_care.fixed_lists(CONFIG)
        self.assertEqual(child_care.listed_id(lists, "regions", "Region 4 Greater Derry and Manchester"), 4)
        self.assertEqual(child_care.listed_id(lists, "counties", " Coos "), 4)
        self.assertIsNone(child_care.listed_id(lists, "quality_ratings", ""))
        with self.assertRaises(ValueError):
            child_care.listed_id(lists, "regions", "Region 4 Capitol Area")
        with self.assertRaises(ValueError):
            child_care.listed_id(lists, "availabilities", "Closed")

    def test_granite_steps_for_quality_steps_are_numbers(self):
        self.assertEqual([child_care.gsq_step(step) for step in ("Licensed", "Step 1", "Step 4", None)], [0, 1, 4, None])
        with self.assertRaises(ValueError):
            child_care.gsq_step("Step 5")

    def test_a_download_joins_the_search_results_to_the_provider_list(self):
        saved = {
            "providers": [
                provider("a", "Little  Learners", "CCCB-00001", ShippingStreet="Building 1: 85 Parker Street\r\nBuilding 2: 21 Durkee Street",
                         ShippingPostalCode="03446-", License_Type_From_Application__c="Infant/Toddler Program;Night Care Program;Night Care Program",
                         Issue_Date__c=1757635200000, Provider_Enrollment_Status_Formula__c="Active", age_wks_lo__c=6, age_yrs_hi__c=12,
                         QRIS_Rating__c="Licensed Plus", Qris_GSQ_Approved_Step__c="Step 3", Shipping_County__c="Cheshire",
                         Shipping_Region__c="Region 1 Greater Monadnock, Greater Sullivan and Upper County"),
                provider("b", "Youth Home", "RES-1", "Residential Child Care Program"),
            ],
            "search": [{"Id": "a", "Age_Group__c": "Toddler;Infant", "Infant__c": 8, "Toddler__c": 22, "License_Status__c": "Permit Issued",
                        "ShippingLatitude": 44.048197, "Enrolled_as_a_Preventive_and_Protective__c": "No"}],
        }
        [program] = child_care.parse_download(saved, CONFIG)
        self.assertEqual(program["name"], "Little Learners")
        self.assertEqual(program["street"], "Building 1: 85 Parker Street; Building 2: 21 Durkee Street")
        self.assertEqual(program["zip"], "03446")
        self.assertEqual(program["license_types"], ["Infant/Toddler Program", "Night Care Program"])
        self.assertEqual(program["license_issue_date"], date(2025, 9, 12))
        self.assertEqual((program["min_age_months"], program["max_age_months"]), (1.4, 144))
        self.assertEqual((program["infant"], program["preschool"], program["age_groups_source"]), (True, False, "listed"))
        self.assertEqual((program["capacity"], program["infant_capacity"], program["toddler_capacity"]), (20, 8, 22))
        self.assertEqual((program["license_status_id_fk"], program["accepts_scholarship"], program["preventive_protective_care"]),
                         (2, True, False))
        self.assertEqual((program["quality_rating_id_fk"], program["gsq_step"], program["county_id_fk"], program["region_id_fk"]),
                         (2, 3, 3, 1))

    def test_an_unknown_type_or_a_repeated_program_stops_the_load(self):
        with self.assertRaises(ValueError):
            child_care.parse_download({"providers": [provider("a", "A", "X-1", "Overnight Camp")], "search": []}, CONFIG)
        with self.assertRaises(ValueError):
            child_care.parse_download({"providers": [provider("a", "A", "X-1", Shipping_County__c="Essex")], "search": []}, CONFIG)
        with self.assertRaises(ValueError):
            child_care.parse_download({"providers": [provider("a", "A", "X-1"), provider("b", "B", "X-1")], "search": []}, CONFIG)

    def test_a_program_page_gives_its_hours_rates_visits_vacancies_and_lists(self):
        page = child_care.parse_page(PAGE, HEADINGS, "Little Learners")
        self.assertEqual((page["availability"], page["email_hidden"], page["main_contact"]),
                         ("Accepting Children on Wait List", True, "Robyn Andersen, Jo Smith"))
        self.assertEqual((page["head_start"], page["early_head_start"], page["capacity"]), (True, None, 6))
        self.assertEqual(page["hours"], [(1, 1, time(8), time(16)), (1, 5, time(8), time(12, 30))])
        # Schedules are numbered; one that repeats another is left out
        self.assertEqual(page["rates"], [(1, "Toddler", "weekly", Decimal("1250.00")), (1, "Preschool", "daily", Decimal("60.00")),
                                         (2, "Preschool", "daily", Decimal("52.00"))])
        # The later of the hours' and Other Information's Last Updated
        self.assertEqual(page["details_updated"], date(2026, 3, 5))
        self.assertEqual(page["inspections"], [
            {"review_date": date(2025, 6, 23), "review_type": "Monitoring Visit", "items_compliant": 173, "items_reviewed": 175,
             "visit_id": "a4lcs00000IxQIfAAN", "document_url": None},
            {"review_date": date(2023, 3, 1), "review_type": "Renewal Visit", "items_compliant": None, "items_reviewed": None,
             "visit_id": None, "document_url": "https://new-hampshire.my.site.com/nhccis/servlet/doc?id=1&v=2"},
        ])
        self.assertEqual(page["vacancies"], {"Infant": 1, "Toddler": 0, "Preschool": None, "School Age": 10})
        self.assertEqual(page["vacancies_updated"], date(2026, 10, 5))
        # A list separated by ";" keeps the commas inside its values
        # By their category's code; its type of care and endorsement badge are left out
        self.assertEqual(page["features"], {"environment": ["NO CAT", "NO TV USE"],
                                            "meals": ["PARENT PROVIDES LUNCH", "REFRIGERATION IS AVAILABLE, ON REQUEST"]})

    def test_a_page_that_says_to_ask_for_rates_has_none(self):
        start = PAGE.index('<div class="panel panel-default schedulePanel">')
        page = PAGE.replace(PAGE[start:PAGE.index('<div class="paddingBottom"')],
                            '<div class="panel panel-default schedulePanel"> <h4 class="heading-for-h4">Fees</h4> <table> <thead>'
                            ' <tr> <th><center>Please contact the child care provider for the rates.</center></th> </tr> </thead>'
                            ' </table> </div> <br /> ')
        parsed = child_care.parse_page(page, HEADINGS)
        self.assertEqual((parsed["hours"], parsed["rates"]), ([], []))

    def test_a_page_that_changed_stops_the_load(self):
        with self.assertRaises(ValueError):
            child_care.parse_page(PAGE.replace('id="AgesServed"', 'id="Openings"'), HEADINGS)
        with self.assertRaises(ValueError):
            child_care.parse_page(PAGE.replace("ENVIRONMENT:", "PETS:"), HEADINGS)

    def test_the_saved_downloads_check_out(self):
        programs = child_care.parse_download(child_care.read_file(CONFIG, date(2026, 11, 13)), CONFIG)
        self.assertEqual((len(programs), sum(p["capacity"] for p in programs)), (735, 48501))
        self.assertEqual({p["program_type"] for p in programs}, {t["name"] for t in CONFIG["program_types"].values()})


class ChildCareLoadTests(unittest.TestCase):
    def test_every_program_has_a_town_and_the_views_add_up(self):
        with engine.connect() as conn:
            self.assertEqual(conn.execute(text("SELECT count(*) FROM child_care_program WHERE town_id_fk IS NULL")).scalar(), 0)
            for as_of, programs, capacity in conn.execute(text("SELECT as_of, programs, capacity FROM state_child_care")).all():
                for view in ("town_child_care", "district_child_care"):
                    self.assertEqual(conn.execute(text(f"SELECT sum(programs), sum(capacity) FROM {view} WHERE as_of = :as_of"),
                                                  {"as_of": as_of}).one(), (programs, capacity), view)

    def test_the_pages_fill_in_vacancies_hours_rates_and_visits(self):
        with engine.connect() as conn:
            read, programs = conn.execute(text(
                "SELECT count(*) FILTER (WHERE email_hidden IS NOT NULL), count(*) FROM child_care_program WHERE is_current")).one()
            self.assertGreaterEqual(read, programs * 0.95)
            for table in ("child_care_program_hours", "child_care_program_rate", "child_care_program_feature_xref", "child_care_inspection"):
                self.assertGreater(conn.execute(text(f"SELECT count(*) FROM {table}")).scalar(), 0, table)
            self.assertEqual(conn.execute(text(
                "SELECT count(*) FROM child_care_inspection WHERE items_compliant > items_reviewed")).scalar(), 0)
            self.assertIsNotNone(conn.execute(text(
                "SELECT infant_vacancies FROM state_child_care ORDER BY as_of DESC LIMIT 1")).scalar())

    def test_lookups_are_filled_and_every_license_type_is_a_feature(self):
        with engine.connect() as conn:
            for table, key in child_care.LISTS.items():
                self.assertEqual(dict(conn.execute(text(f"SELECT id, name FROM {key}")).all()), CONFIG[table], key)
            self.assertEqual({category_id: {"code": code, "name": name} for category_id, code, name in
                              conn.execute(text("SELECT id, code, name FROM child_care_feature_category"))},
                             CONFIG["feature_categories"])
            # Every category has values
            self.assertEqual(conn.execute(text("""
                SELECT count(*) FROM child_care_feature_category c
                WHERE NOT EXISTS (SELECT 1 FROM child_care_feature f WHERE f.category_id_fk = c.id)
            """)).scalar(), 0)
            self.assertEqual(conn.execute(text("""
                SELECT count(*) FROM child_care_program p WHERE NOT EXISTS (
                    SELECT 1 FROM child_care_program_feature_xref x JOIN child_care_feature f ON f.id = x.feature_id_fk
                    JOIN child_care_feature_category c ON c.id = f.category_id_fk
                    WHERE x.program_id_fk = p.id AND c.code = 'license_type')
            """)).scalar(), 3)  # three programs list no license type
            self.assertEqual(conn.execute(text("SELECT count(*) FROM child_care_inspection WHERE review_type_id_fk IS NULL")).scalar(), 0)
            # Every value is one a program lists, read whole
            self.assertEqual(conn.execute(text("""
                SELECT count(*) FROM child_care_feature f
                WHERE NOT EXISTS (SELECT 1 FROM child_care_program_feature_xref x WHERE x.feature_id_fk = f.id)
            """)).scalar(), 0)
            self.assertEqual(conn.execute(text(
                "SELECT count(*) FROM child_care_feature WHERE name = 'CIVIL SERVICE DISCOUNT (POLICE, FIRE, EMERGENCY)'")).scalar(), 1)

    def test_a_town_in_two_districts_counts_toward_the_one_with_kindergarten(self):
        with engine.connect() as conn:
            found = dict(conn.execute(text("""
                SELECT d.name, c.programs FROM district_child_care c JOIN district d ON d.id = c.district_id_fk
                WHERE c.as_of = (SELECT max(as_of) FROM state_child_care) AND d.name IN ('Amherst', 'Souhegan Cooperative')
            """)).all())
        self.assertIn("Amherst", found)
        self.assertNotIn("Souhegan Cooperative", found)


class ChildCareApiTests(unittest.TestCase):
    """Against the loaded database"""

    @classmethod
    def setUpClass(cls):
        cls.api = TestClient(app)
        cls.programs = cls.api.get(f"{settings.API_V1_STR}/child-care/program").json()

    def get(self, path, status=200, **params):
        response = self.api.get(f"{settings.API_V1_STR}/child-care/{path}", params=params)
        self.assertEqual(response.status_code, status, response.text)
        return response.json()

    def test_the_towns_and_districts_add_up_to_the_state(self):
        [state] = self.get("state", as_of="2026-11-13")
        self.assertEqual((state["programs"], state["capacity"]), (735, 48501))
        for level in ("town", "district"):
            rows = self.get(level, as_of="2026-11-13")
            self.assertEqual((sum(r["programs"] for r in rows), sum(r["capacity"] for r in rows)), (735, 48501), level)
        self.assertEqual(self.get("state", as_of="2025-01-01"), [])
        self.get("state", status=422, as_of="2026-02-30")

    def test_a_districts_towns_and_programs(self):
        [souhegan] = [d for d in self.api.get(f"{settings.API_V1_STR}/location/district").json()
                      if d["name"] == "Souhegan Cooperative"]
        towns = {r["town_name"] for r in self.get("town", district_id=souhegan["id"])}
        self.assertEqual(towns, {"Amherst", "Mont Vernon"} & towns)
        programs = self.get("program", district_id=souhegan["id"])
        self.assertTrue(programs)
        self.assertEqual({p["town_name"] for p in programs}, towns)
        # Its towns' programs count toward the districts that teach their kindergarten
        self.assertEqual(self.get("district", district_id=souhegan["id"]), [])

    def test_a_hidden_email_is_returned_unless_asked_to_hide_it(self):
        hidden = [p for p in self.programs if p["email_hidden"]]
        self.assertGreater(sum(1 for p in hidden if p["email"]), 300)
        hiding = {p["id"]: p for p in self.get("program", hide_hidden_email=True)}
        self.assertFalse(any(hiding[p["id"]]["email"] for p in hidden))
        # Programs that show their email keep it
        self.assertEqual([p["email"] for p in self.programs if not p["email_hidden"]],
                         [hiding[p["id"]]["email"] for p in self.programs if not p["email_hidden"]])
        detail = next(p for p in hidden if p["email"])
        self.assertEqual(self.get(f"program/{detail['id']}")["email"], detail["email"])
        self.assertIsNone(self.get(f"program/{detail['id']}", hide_hidden_email=True)["email"])

    def test_program_filters(self):
        self.assertEqual(len(self.programs), 735)
        # By town, then name (in the database's order, which ignores case and spaces): each town's together
        towns = [p["town_name"] for p in self.programs]
        self.assertEqual(sum(1 for i, town in enumerate(towns) if i == 0 or town != towns[i - 1]), len(set(towns)))
        infant_openings = self.get("program", age_group="infant", has_vacancies=True)
        self.assertTrue(infant_openings)
        self.assertTrue(all(p["infant"] and p["infant_vacancies"] > 0 for p in infant_openings))
        accepting = self.get("program", availability_id=1)
        self.assertEqual({p["availability"] for p in accepting}, {"Accepting Children"})
        self.assertEqual(len(self.get("program", accepts_scholarship=True)), sum(p["accepts_scholarship"] for p in self.programs))
        self.get("program", status=422, age_group="baby")

    def test_a_programs_details(self):
        program = next(p for p in self.programs if p["provider_number"] == "CCCB-06853")
        detail = self.get(f"program/{program['id']}")
        self.assertEqual({key: detail[key] for key in program}, program)
        self.assertTrue(detail["source_url"].endswith("?id=" + detail["source_url"].split("=")[-1]))
        self.assertEqual([(h["day"], h["opens"], h["closes"]) for h in detail["hours"]][0], ("Monday", "07:00:00", "18:00:00"))
        self.assertEqual([(r["age_group"], r["period"]) for r in detail["rates"]], [("Preschool", "weekly"), ("School Age", "weekly")])
        self.assertEqual(detail["features"][0], {"category": "license_type", "category_name": "License Type",
                                                 "values": ["Group child care center", "Preschool Program", "School Age Program"]})
        dates = [i["review_date"] for i in detail["inspections"]]
        self.assertEqual(dates, sorted(dates, reverse=True))
        self.assertEqual([s["as_of"] for s in detail["snapshots"]], ["2026-11-13"])
        self.get("program/999999", status=404)


if __name__ == "__main__":
    unittest.main()
