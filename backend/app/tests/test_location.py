"""
Tests for the school list's types and the kind of each district (a school district, a charter
school's board or a private school's operator), and the API's filters on them. The API tests
run against the local database after `alembic upgrade head`:

    docker exec -w /app education-backend-backend-1 python -m unittest app.tests.test_location -v
"""
import unittest

import pandas as pd
from fastapi.testclient import TestClient

from app.core.config import settings
from app.etl import location
from app.main import app

CONFIG = location.load_config(location.CONFIG)


def school_list(*rows):
    """A school list laid out as the config maps it, from (district id, district name, school id, school name, type code)."""
    mappings = CONFIG['column_mappings']
    width = max(mappings.values()) + 1
    frame = []
    for district_id, district_name, school_id, school_name, type_code in rows:
        row = [None] * width
        row[mappings['district_id']], row[mappings['district_name']] = district_id, district_name
        row[mappings['school_id']], row[mappings['school_name']] = school_id, school_name
        # The description changes from year to year; only the code counts
        row[mappings['school_type']], row[mappings['school_type_desc']] = type_code, f"Renamed {type_code}"
        frame.append(row)
    return pd.DataFrame(frame)


def parse(*rows):
    """The schools and districts parse_schools makes of the rows, with Concord (111) on the district list."""
    districts = {111: {'name': 'Concord', 'sau_id': 8, 'grade_ids': [], 'is_public': True, 'kind': 'district'}}
    schools = location.parse_schools(school_list(*rows), CONFIG, districts, {}, location.TownMatcher({}))
    return schools, districts


class SchoolListParseTests(unittest.TestCase):
    def test_a_schools_type_comes_from_the_states_code(self):
        schools, _ = parse((111, "Concord", 20080, "Concord High School", "PU"), (703, "North Country Charter Academy", 28395, "NCCA (H)", "CRS"))
        type_ids = {school_id: school['row'][location.SCHOOL_COLUMNS.index("school_type_id_fk")] for school_id, school in schools.items()}
        self.assertEqual(type_ids, {20080: 1, 28395: 3})

    def test_operators_off_the_district_list_take_their_schools_kind(self):
        _, districts = parse(
            (111, "Concord", 20080, "Concord High School", "PU"),
            (703, "North Country Charter Academy", 28395, "NCCA (H)", "CRS"),
            (703, "North Country Charter Academy", 28505, "NCCA (M)", "CRS"),
            (1006, "Diocese of Manchester", 99001, "A Parochial School", "PA"),
        )
        self.assertEqual({district_id: (d['is_public'], d['kind']) for district_id, d in districts.items()},
                         {111: (True, 'district'), 703: (False, 'charter'), 1006: (False, 'private')})

    def test_a_type_code_the_loader_doesnt_know_stops_the_load(self):
        with self.assertRaisesRegex(ValueError, "'ZZ'"):
            parse((111, "Concord", 20080, "Concord High School", "ZZ"))


class LocationApiTests(unittest.TestCase):
    """Against the loaded database"""

    @classmethod
    def setUpClass(cls):
        cls.api = TestClient(app)

    def get(self, path, **params):
        response = self.api.get(f"{settings.API_V1_STR}/{path}", params=params)
        self.assertEqual(response.status_code, 200, response.text)
        return response.json()

    def test_every_current_school_has_a_type_and_a_kind(self):
        schools = self.get("location/school")
        self.assertEqual([s["name"] for s in schools if not s["school_type"]], [])
        self.assertEqual({s["kind"] for s in schools}, {"district", "charter", "private"})
        # A charter school is one of the state's charter schools and has a charter board
        for school in schools:
            self.assertEqual(school["kind"] == "charter", school["school_type"]["code"] == "CRS", school["name"])

    def test_charter_schools_and_their_boards(self):
        charters = self.get("location/school", kind="charter")
        latest = location.read_year(CONFIG, int(CONFIG['file_settings']['year_end']))
        listed = [row for row in latest['school'] if row[location.SCHOOL_COLUMNS.index("school_type_id_fk")] == 3]
        self.assertEqual(len(charters), len(listed))
        boards = self.get("location/district", kind="charter")
        self.assertEqual({d["id"] for d in boards}, {s["district_id"] for s in charters})
        self.assertFalse(any(d["is_public"] for d in boards))
        # The school districts the site lists are all districts
        self.assertEqual({d["kind"] for d in self.get("location/district", is_public=True)}, {"district"})

    def test_a_new_school_lists_the_figures_it_has_none_of_yet(self):
        breakthrough = self.get("location/school/29300")
        self.assertEqual(breakthrough["open_date"], "2026-09-01")
        self.assertEqual(breakthrough["not_yet_reported"], ["enrollment", "test_scores", "graduation", "safety"])
        # Opened July 2025: its spring 2026 tests are in, its 2025-26 enrollment and safety figures aren't, and
        # without a grade 12 it has no graduation to wait for
        north_star = next(s for s in self.get("location/school", kind="charter") if s["name"].startswith("North Star Academy"))
        self.assertEqual(north_star["not_yet_reported"], ["enrollment", "safety"])
        # A long-standing school has figures in every topic
        self.assertEqual(self.get("location/school/20285")["not_yet_reported"], [])

    def test_district_ranks_can_leave_out_charter_boards(self):
        boards = {d["id"] for d in self.get("location/district", kind="charter")}
        params = dict(year=2026, assessment_subject_id=1, assessment_subgroup_id=1, grade_id=999)
        every = {row["district_id"] for row in self.get("assessment/district", **params)}
        districts = {row["district_id"] for row in self.get("assessment/district", district_kind="district", **params)}
        self.assertTrue(every & boards, "charter boards have district rows")
        self.assertFalse(districts & boards)
        self.assertEqual(districts, every - boards - {d["id"] for d in self.get("location/district", kind="private")})


if __name__ == "__main__":
    unittest.main()
