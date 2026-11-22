"""
Tests for the EFA provider load (where Education Freedom Account money and students go), run against
the local database after `alembic upgrade head`:

    docker exec -w /app education-backend-backend-1 python -m unittest app.tests.test_education_freedom_account_provider -v
"""
import csv
import os
import tempfile
import unittest
from decimal import Decimal

from sqlalchemy import text

from app.core.db import engine
from app.etl import education_freedom_account_provider
from app.etl.core import config_path, load_config

CONFIG = load_config(education_freedom_account_provider.CONFIG)
DIRECTORY = config_path(CONFIG["directory"])


class EducationFreedomAccountCategoryTests(unittest.TestCase):
    def codes(self, published):
        return education_freedom_account_provider.classify(published, CONFIG["categories"])

    def test_categories_as_published_in_the_scans(self):
        cases = {
            "Tuition and fees ata private school": ("private_school",),
            "Tuition and fees at a private school, School uniforms": ("private_school", "uniforms"),
            "Textbooks, curriculum, or other instructional and supplemental materials oronline instruction required by": ("curriculum",),
            # Half hidden by the shaded bar it's printed on
            ".... devices": ("technology",),
            "limitedto, occupational, behavioral, physical, speech- language, and audiology therapies": ("therapies",),
            "placement examinations, examinations related to college or university admission": ("exams",),
            "services provided by a district public school, chartered public school, public academy, or independent school": ("public_school_classes",),
            "Educatio nal software and applications & School uniforms": ("uniforms", "software"),
            "Tuition and fees for non-public / private online learning progr:": ("online_programs",),
            "Educational Programs; Tuition and fees for summer education programs and specialized education programs": ("education_programs",),
            "Tuition and fees atan institution of higher education": ("higher_education",),
            "Tuition and fees ata career or technical school and related instructional materials": ("career_technical",),
        }
        self.assertEqual({published: self.codes(published) for published in cases}, cases)

    def test_a_category_none_of_the_rules_name_stops_the_load(self):
        with self.assertRaises(ValueError):
            self.codes("Gift cards")


class EducationFreedomAccountReadTests(unittest.TestCase):
    def year(self, rows, grand_total):
        with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["year", "line_no", "category", "category_total", "provider", "amount"])
            writer.writerows(rows)
        try:
            return education_freedom_account_provider.read_year(f.name, 2025, Decimal(grand_total))
        finally:
            os.unlink(f.name)

    def test_lines_that_add_up_to_their_category_and_the_grand_total(self):
        lines = self.year([(2025, 1, "Tutoring services", "30.00", "CL Tutor", "20.00"),
                           (2025, 2, "Tutoring services", "30.00", "CL Tutor", "10.00"),
                           (2025, 3, "School uniforms", "5.00", "LANDS END", "5.00")], "35.00")
        self.assertEqual([line["amount"] for line in lines], [Decimal("20.00"), Decimal("10.00"), Decimal("5.00")])

    def test_lines_that_dont_add_up_stop_the_load(self):
        with self.assertRaises(ValueError):
            self.year([(2025, 1, "Tutoring services", "30.00", "CL Tutor", "20.00")], "30.00")
        with self.assertRaises(ValueError):
            self.year([(2025, 1, "Tutoring services", "20.00", "CL Tutor", "20.00")], "25.00")

    def test_a_providers_name_from_its_latest_listing_not_in_capitals(self):
        self.assertEqual(education_freedom_account_provider.display_name(["Trinity Christian School of Concord", "TRINITY CHRISTIAN SCHOOL CONCORD"]),
                         "Trinity Christian School of Concord")
        self.assertEqual(education_freedom_account_provider.display_name(["MOUNT ROYALACADEMY", "MOUNT  ROYAL ACADEMY"]), "MOUNT ROYAL ACADEMY")


class EducationFreedomAccountAssetTests(unittest.TestCase):
    def test_every_year_adds_up_to_its_report(self):
        lines = {year: len(education_freedom_account_provider.read_year(os.path.join(DIRECTORY, CONFIG["expenditure_input"].replace("****", str(year))),
                                                  year, Decimal(str(CONFIG["grand_totals"][year]))))
                 for year in range(CONFIG["year_start"], CONFIG["year_end"] + 1)}
        self.assertEqual(lines, {2022: 932, 2023: 1404, 2024: 2234, 2025: 2092})

    def test_the_served_list_and_the_school_matches(self):
        served = education_freedom_account_provider.read_served(os.path.join(DIRECTORY, CONFIG["served_files"][2025]), 2025)
        self.assertEqual((len(served), sum(row["students"] for row in served)), (225, 10158))
        matches = education_freedom_account_provider.read_matches(os.path.join(DIRECTORY, CONFIG["school_match_file"]))
        self.assertEqual(matches["CONCORDCHRISTIANACADEMY"], 20290)


class EducationFreedomAccountDatabaseTests(unittest.TestCase):
    """Against the loaded database"""

    def query(self, sql, **params):
        with engine.connect() as conn:
            return conn.execute(text(sql), params).fetchall()

    def test_each_year_as_its_report_totals_it(self):
        totals = dict(self.query("SELECT year, sum(amount) FROM education_freedom_account_expenditure GROUP BY year"))
        self.assertEqual(totals, {year: Decimal(str(total)) for year, total in CONFIG["grand_totals"].items()})
        tuition = self.query("""
            SELECT sum(e.amount) FROM education_freedom_account_expenditure e JOIN education_freedom_account_category c ON c.id = e.category_id
            WHERE e.year = 2025 AND c.code = 'private_school'
        """)
        self.assertEqual(tuition[0][0], Decimal("11501321.84"))

    def test_a_schools_tuition_each_year(self):
        rows = self.query("""
            SELECT e.year, sum(e.amount) FROM education_freedom_account_expenditure e JOIN education_freedom_account_provider p ON p.id = e.provider_id
            JOIN education_freedom_account_category c ON c.id = e.category_id
            WHERE p.school_id_fk = 20290 AND c.code = 'private_school' GROUP BY e.year ORDER BY e.year
        """)
        self.assertEqual([tuple(row) for row in rows], [(2022, Decimal("197762.57")), (2023, Decimal("370783.22")),
                                                        (2024, Decimal("541719.94")), (2025, Decimal("475929.36"))])

    def test_providers_listed_by_initials_keep_each_line(self):
        rows = self.query("""
            SELECT s.students FROM education_freedom_account_served s JOIN education_freedom_account_provider p ON p.id = s.provider_id
            WHERE p.name_key = 'CLTUTOR' ORDER BY s.line_no
        """)
        self.assertEqual([row[0] for row in rows], [23, 15])


if __name__ == "__main__":
    unittest.main()
