"""
Location master data, from the state's school list, district/town list and SAU list:
region, school_type, grades, town, sau, sau_staff, district, school and the
town_district_xref, school_grade_xref and district_grade_xref links.

Towns, SAUs, districts and schools keep the state's ids. Each year's files are a
snapshot of the current lists, so a load adds and updates rows but never deletes a
school, district, SAU or town (closed schools keep their history). SAU staff and the
grade/district links of everything in the files are replaced by the snapshot.

Districts and schools in the latest configured year's lists are marked is_current;
the API lists only those.
"""
import logging
from typing import Iterable, Optional

import pandas as pd
from sqlalchemy import text
from sqlalchemy.engine import Connection

from app.etl.core import (
    configured_years, load_config, refresh_dependent_views, replace_rows, upsert_rows, year_file
)

logger = logging.getLogger("app.etl")

CONFIG = "generate_schools_config.yaml"

# Fixed lookups; schools refer to them by these ids
GRADES = {
    'P': (1, 'Preschool'), 'K': (2, 'Kindergarten'),
    '1': (3, 'Grade 1'), '2': (4, 'Grade 2'), '3': (5, 'Grade 3'), '4': (6, 'Grade 4'),
    '5': (7, 'Grade 5'), '6': (8, 'Grade 6'), '7': (9, 'Grade 7'), '8': (10, 'Grade 8'),
    '9': (11, 'Grade 9'), '10': (12, 'Grade 10'), '11': (13, 'Grade 11'), '12': (14, 'Grade 12'),
    'PG': (15, 'Post Graduate'),
}
REGIONS = {
    'South Central': 1, 'Lakes Region': 2, 'Southeast': 3, 'North Country': 4, 'Southwest': 5, 'Unknown': 6,
}
SCHOOL_TYPES = {
    'Public School': 1,
    'Interstate School': 2,
    'Charter Schools approved by the state': 3,
    'Joint Maintenance Agreement': 4,
    'Public Academy': 5,
    'Other Private Schools': 6,
    'Christian School': 7,
    'In-State Spec Ed and Other Private': 8,
    'In-State Private Special Education': 9,
    'Parochial School': 10,
    'Prep School': 11,
}
# Villages in school/SAU addresses that are not towns of their own
VILLAGE_TOWNS = {
    'groveton': 'northumberland',
    'contoocook': 'hopkinton',
    'woodsville': 'haverhill',
    'meriden': 'plainfield',
    'sanbornville': 'wakefield',
    'suncook': 'pembroke',
}

SAU_COLUMNS = ("id", "name", "address1", "address2", "town", "town_id_fk", "state", "zip", "phone", "fax", "webpage")
SAU_STAFF_COLUMNS = ("sau_id_fk", "first_name", "last_name", "title", "admin_type", "email")
DISTRICT_COLUMNS = ("id", "name", "sau_id_fk", "is_public")
SCHOOL_COLUMNS = (
    "id", "name", "sau_id_fk", "district_id_fk", "region_id_fk", "school_type_id_fk",
    "principal_first_name", "principal_last_name", "address1", "address2", "city", "town_id_fk",
    "state", "zip", "phone", "fax", "email", "county", "webpage",
)


def _text(value):
    """A text value, or None when blank."""
    return None if pd.isna(value) or value == '' else str(value)


def _text_not_null(value):
    """A text value, or '' when blank (for NOT NULL columns)."""
    return '' if pd.isna(value) or value == '' else str(value)


def _id(value):
    """An integer id, or None. A blank (NaN) id raises."""
    return None if value is None else int(value)


def parse_grade_span(grade_span) -> list:
    """Grade ids of a span such as "P K 1-8", sorted and without duplicates."""
    if pd.isna(grade_span) or grade_span == '':
        return []
    grade_ids = set()
    for part in grade_span.split():
        if part in GRADES:
            grade_ids.add(GRADES[part][0])
        elif '-' in part:
            start, end = part.split('-')
            if start in GRADES and end in GRADES:
                grade_ids.update(range(GRADES[start][0], GRADES[end][0] + 1))
    return sorted(grade_ids)


def parse_saus(df: pd.DataFrame) -> dict:
    """SAUs and their staff from the SAU list; rows without a numeric SAU id are headers."""
    saus = {}
    for _, row in df.iterrows():
        try:
            sau_id = int(row[0])
        except (ValueError, TypeError):
            continue
        if sau_id not in saus:
            saus[sau_id] = {
                'name': row[1], 'address1': row[8], 'address2': row[9], 'town': row[10], 'state': row[12],
                'zip': row[13], 'phone': row[14], 'fax': row[15], 'webpage': row[17], 'staff': [],
            }
        # A row with a first or last name is a staff member
        if pd.notna(row[5]) or pd.notna(row[7]):
            saus[sau_id]['staff'].append({
                'admin_type': row[2], 'title': row[3], 'first_name': row[5], 'last_name': row[7], 'email': row[16],
            })
    return saus


def parse_districts_and_towns(df: pd.DataFrame, saus: dict):
    """
    Districts and towns from the district/town list, one row per district and town.

    A district takes its SAU and grade span from its first row. A town's districts are
    listed in file order. SAUs missing from the SAU list are added with their name only.
    """
    districts, towns = {}, {}
    for _, row in df.iterrows():
        district_id, town_id = row['District Id'], row['Town Id']
        sau_id = row.get('SAUId')

        if sau_id and not pd.isna(sau_id) and sau_id not in saus:
            saus[sau_id] = {'name': row.get('SAU'), 'staff': []}

        if district_id not in districts and not pd.isna(district_id):
            districts[district_id] = {
                'name': row['District'],
                'sau_id': sau_id if not pd.isna(sau_id) else None,
                'grade_ids': parse_grade_span(row.get('Grade Span')),
                'is_public': True,
            }

        if pd.isna(town_id):
            continue
        if town_id not in towns:
            towns[town_id] = {'name': row['Town'], 'district_ids': []}
        if not pd.isna(district_id) and district_id not in towns[town_id]['district_ids']:
            towns[town_id]['district_ids'].append(district_id)
    return districts, towns


class TownMatcher:
    """Finds the town of a city name in an address, counting the names it had to guess or could not match."""

    def __init__(self, towns: dict):
        self.towns = [(town_id, town['name'].lower().strip()) for town_id, town in towns.items()]
        self.villages, self.partial, self.unmatched = set(), set(), set()

    def find(self, city_name):
        if pd.isna(city_name) or city_name == '':
            return None
        city = city_name.lower().strip()

        if city in VILLAGE_TOWNS:
            self.villages.add(city_name)
            for town_id, town in self.towns:
                if town == VILLAGE_TOWNS[city]:
                    return town_id

        for town_id, town in self.towns:
            if town == city:
                return town_id

        # Otherwise the first town named by the city's first or last word, e.g. "North Conway" -> Conway
        words = city.split()
        if len(words) > 1:
            for town_id, town in self.towns:
                if town == words[0] or town == words[-1]:
                    self.partial.add(city_name)
                    return town_id

        self.unmatched.add(city_name)
        return None

    def report(self, year: int):
        if self.villages or self.partial:
            logger.info(f"{year}: matched {len(self.villages)} village names and {len(self.partial)} city names "
                        f"by one word to towns: {sorted(self.villages | self.partial)}")
        if self.unmatched:
            logger.warning(f"{year}: no town found for {len(self.unmatched)} city names, "
                           f"left without a town: {sorted(self.unmatched)}")


def parse_schools(df: pd.DataFrame, config: dict, districts: dict, saus: dict, matcher: TownMatcher) -> dict:
    """
    Schools from the school list, keyed by school id.

    SAUs and districts the other lists don't have are added (districts as not public).
    A blank region leaves the school without a region.
    """
    mappings = config['column_mappings']
    schools = {}
    for _, row in df.iterrows():
        def value(column_name):
            column_index = mappings.get(column_name)
            return None if column_index is None else row.get(column_index)

        school_id = value('school_id')
        if pd.isna(school_id):
            continue

        sau_id = value('sau_id')
        if sau_id and sau_id not in saus and not pd.isna(sau_id):
            saus[sau_id] = {'name': value('sau_name') or f'SAU {sau_id}'}

        district_id = value('district_id')
        if district_id and district_id not in districts and not pd.isna(district_id):
            grade_span = value('grade_span')
            districts[district_id] = {
                'name': value('district_name') or '',
                'sau_id': sau_id if not pd.isna(sau_id) else None,
                'grade_ids': parse_grade_span(grade_span) if grade_span else [],
                'is_public': False,
            }

        schools[school_id] = {
            'row': (
                _id(school_id), _text(value('school_name')), _id(sau_id), _id(district_id),
                REGIONS.get(value('region_name') or 'Unknown'), SCHOOL_TYPES.get(value('school_type_desc')),
                _text(value('principal_first_name')), _text(value('principal_last_name')),
                _text(value('address1')), _text(value('address2')), _text(value('city')),
                matcher.find(value('city')),
                _text(value('state')), _text(value('zip')), _text(value('phone')), _text(value('fax')),
                _text(value('email')), _text(value('county')), _text(value('webpage')),
            ),
            'grade_ids': parse_grade_span(value('grade_span')),
        }
    return schools


def read_year(config: dict, year: int) -> dict:
    """Rows for every table from one year's three files, in the original insert order."""
    settings = config['file_settings']
    sau_file, school_file = settings['sau_file'], settings['school_file']
    saus = parse_saus(pd.read_excel(year_file(sau_file, year), header=None, skiprows=sau_file['start_row']))
    districts, towns = parse_districts_and_towns(pd.read_csv(year_file(settings['district_file'], year)), saus)

    matcher = TownMatcher(towns)
    sau_towns = {sau_id: matcher.find(sau.get('town')) for sau_id, sau in saus.items()}
    school_df = pd.read_excel(year_file(school_file, year), header=None, skiprows=school_file['start_row'])
    schools = parse_schools(school_df, config, districts, saus, matcher)
    matcher.report(year)

    return {
        'town': [(_id(town_id), _text(town['name'])) for town_id, town in towns.items()],
        'sau': [
            (_id(sau_id), _text_not_null(sau.get('name', '')), _text(sau.get('address1')), _text(sau.get('address2')),
             _text(sau.get('town')), sau_towns.get(sau_id), _text(sau.get('state')), _text(sau.get('zip')),
             _text(sau.get('phone')), _text(sau.get('fax')), _text(sau.get('webpage')))
            for sau_id, sau in saus.items()
        ],
        'sau_staff': [
            (_id(sau_id), _text_not_null(staff['first_name']), _text_not_null(staff['last_name']),
             _text(staff['title']), str(staff['admin_type']), _text(staff['email']))
            for sau_id, sau in saus.items() for staff in sau.get('staff', [])
        ],
        'district': [
            (_id(district_id), _text_not_null(district['name']), _id(district['sau_id']), district['is_public'])
            for district_id, district in districts.items()
        ],
        'town_district_xref': [
            (_id(town_id), _id(district_id)) for town_id, town in towns.items() for district_id in town['district_ids']
        ],
        'region': [(region_id, name) for name, region_id in REGIONS.items()],
        'school_type': [(type_id, name) for name, type_id in SCHOOL_TYPES.items()],
        'grades': list(GRADES.values()),
        'school': [school['row'] for school in schools.values()],
        'school_grade_xref': [
            (_id(school_id), grade_id) for school_id, school in schools.items() for grade_id in school['grade_ids']
        ],
        'district_grade_xref': [
            (_id(district_id), grade_id)
            for district_id, district in districts.items() for grade_id in district['grade_ids']
        ],
        # Owners whose links the snapshot replaces
        'owners': {
            'school_grade_xref': [_id(school_id) for school_id in schools],
            'district_grade_xref': [_id(district_id) for district_id in districts],
        },
    }


def sync_links(conn: Connection, table: str, owner_column: str, other_column: str, owners: list, rows: list) -> dict:
    """
    Make an xref table hold exactly `rows` for the given owners: links no longer listed
    are deleted, new ones inserted in order (existing links keep their ids).
    """
    deleted = conn.execute(text(f"""
        DELETE FROM {table}
        WHERE {owner_column} = ANY(:owners)
          AND ({owner_column}, {other_column}) NOT IN (
              SELECT * FROM unnest(CAST(:owner_ids AS INTEGER[]), CAST(:other_ids AS INTEGER[])))
    """), {"owners": owners, "owner_ids": [r[0] for r in rows], "other_ids": [r[1] for r in rows]}).rowcount
    if deleted:
        logger.info(f"{table}: {deleted} links no longer listed deleted")
    counts = upsert_rows(conn, table, (owner_column, other_column), (owner_column, other_column), rows)
    counts["deleted"] = deleted
    return counts


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the given years' lists (default: every configured year, oldest first)."""
    config = load_config(CONFIG)
    counts = {}
    latest_year = int(config['file_settings']['year_end'])
    latest = None
    for year in configured_years(config['file_settings'], years):
        data = read_year(config, year)
        if year == latest_year:
            latest = data
        owners = data['owners']
        # Same table order as the original migration: parents before the rows that refer to them
        counts[year] = {
            'town': upsert_rows(conn, "town", ("id", "name"), ("id",), data['town']),
            'sau': upsert_rows(conn, "sau", SAU_COLUMNS, ("id",), data['sau']),
            # Staff have no key: the list replaces every SAU's staff
            'sau_staff': replace_rows(conn, "sau_staff", SAU_STAFF_COLUMNS, data['sau_staff'], where="TRUE"),
            'district': upsert_rows(conn, "district", DISTRICT_COLUMNS, ("id",), data['district']),
            # The district/town list is complete, so it replaces the links of every town,
            # including towns it no longer lists (e.g. Gonic, a village of Rochester, from 2026)
            'town_district_xref': sync_links(conn, "town_district_xref", "town_id_fk", "district_id_fk",
                                             conn.execute(text("SELECT id FROM town")).scalars().all(),
                                             data['town_district_xref']),
            'region': upsert_rows(conn, "region", ("id", "name"), ("id",), data['region']),
            'school_type': upsert_rows(conn, "school_type", ("id", "name"), ("id",), data['school_type']),
            'grades': upsert_rows(conn, "grades", ("id", "name"), ("id",), data['grades']),
            'school': upsert_rows(conn, "school", SCHOOL_COLUMNS, ("id",), data['school']),
            'school_grade_xref': sync_links(conn, "school_grade_xref", "school_id_fk", "grade_id_fk",
                                            owners['school_grade_xref'], data['school_grade_xref']),
            'district_grade_xref': sync_links(conn, "district_grade_xref", "district_id_fk", "grade_id_fk",
                                              owners['district_grade_xref'], data['district_grade_xref']),
        }
    counts["current"] = mark_current(conn, latest or read_year(config, latest_year))
    # The district views also read school, so they are refreshed with it
    counts["views_refreshed"] = refresh_dependent_views(conn, "school")
    return counts


def mark_current(conn: Connection, latest: dict) -> dict:
    """
    Set is_current on districts and schools: true for those in the latest lists, false for
    the rest. Skipped while the column does not exist yet (the migration that loads the
    lists runs before the one that adds it; that migration calls this itself).
    """
    counts = {}
    for table in ("district", "school"):
        has_column = conn.execute(text("""
            SELECT EXISTS (SELECT 1 FROM information_schema.columns
                           WHERE table_name = :table AND column_name = 'is_current')
        """), {"table": table}).scalar()
        if not has_column:
            continue
        ids = [row[0] for row in latest[table]]
        changed = conn.execute(text(f"""
            UPDATE {table} SET is_current = (id = ANY(:ids)), date_updated = CURRENT_TIMESTAMP
            WHERE is_current IS DISTINCT FROM (id = ANY(:ids))
        """), {"ids": ids}).rowcount
        former = conn.execute(text(f"SELECT count(*) FROM {table} WHERE NOT is_current")).scalar()
        logger.info(f"{table}: {len(ids)} current, {former} former ({changed} changed)")
        counts[table] = {"current": len(ids), "former": former, "changed": changed}
    return counts
