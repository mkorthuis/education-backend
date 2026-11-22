"""
Tests for the private school endpoints a private school's page reads, run against the loaded database:

    docker exec -w /app education-backend-backend-1 python -m unittest app.tests.test_private_school_api -v
"""
import unittest

from fastapi.testclient import TestClient

from app.core.config import settings
from app.main import app

CCA = 20290  # Concord Christian Academy
BISHOP_BRADY = 20320  # a Catholic school, which files no Form 990 of its own
CONCORD_HIGH = 20285  # a public school


class PrivateSchoolApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api = TestClient(app)

    def get(self, path, **params):
        response = self.api.get(f"{settings.API_V1_STR}/{path}", params=params)
        self.assertEqual(response.status_code, 200, response.text)
        return response.json()

    def test_enrollment_by_year_with_its_grades(self):
        rows = self.get("enrollment/private-school", school_id=CCA)
        self.assertEqual([row["year"] for row in rows], list(range(2012, 2027)))
        latest = rows[-1]
        self.assertEqual(latest["total"], sum(g["enrollment"] for g in latest["grades"])
                         + latest["ungraded_elementary"] + latest["ungraded_secondary"])
        self.assertEqual(latest["grades"][0], {"grade_id": 1, "grade_name": "Preschool", "enrollment": 17})
        self.assertEqual(self.get("enrollment/private-school", school_id=CONCORD_HIGH), [])

    def test_survey_answers_with_grades(self):
        rows = self.get("enrollment/private-school/survey", school_id=CCA)
        self.assertEqual([row["year"] for row in rows], [2018, 2022, 2024])
        latest = rows[-1]
        self.assertEqual((latest["teachers_fte"], latest["students_per_teacher"], latest["to_four_year_college_pct"]), (27.8, 11.65, 73))
        self.assertEqual(sum(g["students"] for g in latest["grades"]), latest["students_with_preschool"])

    def test_990_filer_and_returns(self):
        [cca] = self.get("finance/private-school/990", school_id=CCA)
        self.assertEqual((cca["status"], cca["organization"]["name"]), ("own_return", "Concord Christian Academy"))
        latest = cca["returns"][-1]
        self.assertEqual((latest["tax_period_end"], latest["total_revenue"], latest["prior_total_revenue"]), ("2025-06-30", 4449722, 4137562))
        self.assertEqual(sum(line["amount"] for line in latest["revenue_lines"] if line["category"] == "tuition"), 3737361)
        [brady] = self.get("finance/private-school/990", school_id=BISHOP_BRADY)
        self.assertEqual((brady["status"], brady["returns"]), ("not_required_religious", []))
        self.assertEqual(len(self.get("finance/private-school/990")), 136)

    def test_tuition_with_its_rates(self):
        [cca] = self.get("finance/private-school/tuition", school_id=CCA)
        self.assertEqual((cca["year"], cca["status"], cca["with_aid"]), (2027, "published", "85% of students"))
        first = cca["rates"][0]
        self.assertEqual((first["band"], first["lowest_grade"], first["tuition"], first["required_fee"]), ("Kindergarten Readiness", "Preschool", 9700, 800))
        statuses = [row["status"] for row in self.get("finance/private-school/tuition", year=2027)]
        self.assertEqual(statuses.count("published"), 66)

    def test_efa_payments_and_students(self):
        [cca] = self.get("education-freedom-account/private-school", school_id=CCA)
        self.assertEqual([(p["year"], p["amount"]) for p in cca["payments"]],
                         [(2022, 197762.57), (2023, 370783.22), (2024, 541719.94), (2025, 475929.36)])
        self.assertEqual(cca["served"], [{"calendar_year": 2025, "students": 183}])
        self.assertEqual(self.get("education-freedom-account/private-school", school_id=CONCORD_HIGH), [])


if __name__ == "__main__":
    unittest.main()
