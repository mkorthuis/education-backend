"""
Average class size by grade band (grades 1-2, 3-4, 5-8), from the state's
"District Average Class Size" and "School Average Class Size" workbooks.

The district workbooks load district_class_size and state_class_size (the
"State Average" row); the school workbooks load school_class_size. No later
migration renames or reshapes these tables, so the same table names work at the
loading migrations' point in the chain and on the current schema.
"""
import logging
import re
from decimal import Decimal, ROUND_HALF_UP
from typing import Iterable, Optional

import pandas as pd
from sqlalchemy import text
from sqlalchemy.engine import Connection

from app.etl.core import (
    configured_years, existing_ids, load_config, refresh_dependent_views, upsert_rows, year_file
)

logger = logging.getLogger("app.etl")

DISTRICT_CONFIG = "district_average_class_size_config.yaml"
SCHOOL_CONFIG = "school_average_class_size_config.yaml"
GRADE_BANDS = ("grade_1_2", "grade_3_4", "grade_5_8")


def clean_numeric(value) -> Optional[float]:
    """A cell as a float, ignoring characters other than digits, "." and "-"; blank or text-only cells are None."""
    if pd.isna(value) or value == "":
        return None
    if isinstance(value, (int, float)):
        return float(value)
    cleaned = re.sub(r"[^0-9.-]", "", str(value))
    return float(cleaned) if cleaned else None


def round_two_decimal(value: Optional[float]) -> Optional[float]:
    """Round to two decimal places, halves up."""
    if value is None:
        return None
    return float(Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def grade_values(row: pd.Series, mappings: dict) -> Optional[tuple]:
    """The three grade band averages of a row, or None when none of them is above zero."""
    values = tuple(
        round_two_decimal(clean_numeric(row.iloc[mappings[band]] if len(row) > mappings[band] else None))
        for band in GRADE_BANDS
    )
    if not any(value is not None and value > 0 for value in values):
        return None
    return values


def parse_district_year(df: pd.DataFrame, year: int, config: dict, known_districts: set) -> tuple:
    """
    District rows of (district_id, year, grade_1_2, grade_3_4, grade_5_8) from one year's
    workbook, in file order, and the ids of districts not in the district table.

    A row is a district when its district id column is numeric. Only the first row
    of each district counts, even when it is skipped (unknown district, no values).
    """
    mappings = config["column_mappings"]
    rows, seen, unknown = [], set(), set()
    for _, row in df.iterrows():
        raw_id = row.iloc[mappings["district_id"]] if len(row) > mappings["district_id"] else None
        try:
            district_id = int(float(raw_id)) if pd.notna(raw_id) else None
        except (ValueError, TypeError):
            district_id = None
        if district_id is None or district_id in seen:
            continue
        seen.add(district_id)
        if district_id not in known_districts:
            unknown.add(district_id)
            continue
        values = grade_values(row, mappings)
        if values is not None:
            rows.append((district_id, year, *values))
    return rows, unknown


def parse_state_year(df: pd.DataFrame, year: int, config: dict) -> Optional[tuple]:
    """The (year, grade_1_2, grade_3_4, grade_5_8) row from the first "State Average" row, if it has values."""
    settings = config["state_row_identifier"]
    identifier = settings["identifier_text"].lower().strip()
    for _, row in df.iterrows():
        cell = row.iloc[settings["column_index"]] if len(row) > settings["column_index"] else None
        if isinstance(cell, str) and cell.strip().lower() == identifier:
            values = grade_values(row, config["column_mappings"])
            return (year, *values) if values is not None else None
    return None


def school_ids_by_name(conn: Connection) -> tuple:
    """
    School ids by (district id, lower-cased trimmed name), and by name alone for names that
    belong to only one school.

    A few names belong to more than one school ("Memorial School" in Bedford and Sanborn
    Regional, "Maple Avenue School" in Claremont and Goffstown), so a name alone can't tell
    them apart.
    """
    by_district, by_name, schools_per_name = {}, {}, {}
    for school_id, district_id, name in conn.execute(text(
        "SELECT id, district_id_fk, lower(trim(name)) FROM school ORDER BY id"
    )):
        by_district.setdefault((district_id, name), school_id)
        by_name.setdefault(name, school_id)
        schools_per_name[name] = schools_per_name.get(name, 0) + 1
    unique_names = {name: school_id for name, school_id in by_name.items() if schools_per_name[name] == 1}
    return by_district, unique_names


def parse_school_year(df: pd.DataFrame, year: int, config: dict, school_ids: tuple) -> tuple:
    """
    School rows of (school_id, year, grade_1_2, grade_3_4, grade_5_8) from one year's
    workbook, in file order, and the names not found in the school table.

    Schools are matched by the row's district id and name, ignoring case and surrounding
    spaces, then by name alone when only one school has it (e.g. a school that has since
    moved to another district). Only the first row matched to each school counts, even when
    it has no values.
    """
    mappings = config["column_mappings"]
    by_district, unique_names = school_ids
    rows, seen, unknown = [], set(), set()
    for _, row in df.iterrows():
        raw_name = row.iloc[mappings["school_name"]] if len(row) > mappings["school_name"] else None
        if pd.isna(raw_name) or str(raw_name).strip() == "":
            continue
        name = str(raw_name).strip()
        raw_district = row.iloc[mappings["district_id"]] if len(row) > mappings["district_id"] else None
        try:
            district_id = int(float(raw_district)) if pd.notna(raw_district) else None
        except (ValueError, TypeError):
            district_id = None
        school_id = by_district.get((district_id, name.lower()), unique_names.get(name.lower()))
        if school_id is None:
            unknown.add(name)
            continue
        if school_id in seen:
            continue
        seen.add(school_id)
        values = grade_values(row, mappings)
        if values is not None:
            rows.append((school_id, year, *values))
    return rows, unknown


def load_district(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the given years (default: every configured year) into district_class_size and state_class_size."""
    config = load_config(DISTRICT_CONFIG)
    known_districts = existing_ids(conn, "district")

    district_rows, state_rows, unknown, no_state = [], [], set(), []
    for year in configured_years(config["file_settings"], years):
        df = pd.read_excel(year_file(config["file_settings"], year))
        rows, year_unknown = parse_district_year(df, year, config, known_districts)
        district_rows.extend(rows)
        unknown.update((year, district_id) for district_id in year_unknown)
        state_row = parse_state_year(df, year, config)
        if state_row is not None:
            state_rows.append(state_row)
        else:
            no_state.append(year)

    if not district_rows and not state_rows:
        raise ValueError("No district or state class size rows found")
    if unknown:
        # Districts missing from the district list are skipped, as the original migration did
        district_ids = sorted({district_id for _, district_id in unknown})
        logger.warning(f"Skipped {len(unknown)} district-years for {len(district_ids)} districts "
                       f"not in the district table: {district_ids}")
    if no_state:
        logger.warning(f"No state average class size for {no_state}")

    columns = ("district_id_fk", "year", *GRADE_BANDS)
    counts = {"district_class_size": upsert_rows(conn, "district_class_size", columns,
                                                 ("district_id_fk", "year"), district_rows)}
    counts["state_class_size"] = upsert_rows(conn, "state_class_size", ("year", *GRADE_BANDS),
                                             ("year",), state_rows)
    counts["views_refreshed"] = (refresh_dependent_views(conn, "district_class_size")
                                 + refresh_dependent_views(conn, "state_class_size"))
    return counts


def load_school(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the given years (default: every configured year) into school_class_size."""
    config = load_config(SCHOOL_CONFIG)
    school_ids = school_ids_by_name(conn)

    school_rows, unknown = [], set()
    for year in configured_years(config["file_settings"], years):
        df = pd.read_excel(year_file(config["file_settings"], year))
        rows, year_unknown = parse_school_year(df, year, config, school_ids)
        school_rows.extend(rows)
        unknown.update((year, name) for name in year_unknown)

    if not school_rows:
        raise ValueError("No school class size rows found")
    if unknown:
        # Names that match no school (including the sheet's header and footer rows) are skipped,
        # as the original migration did
        names = sorted({name for _, name in unknown})
        logger.warning(f"Skipped {len(unknown)} school-years for {len(names)} names "
                       f"not in the school table: {names}")

    counts = upsert_rows(conn, "school_class_size", ("school_id_fk", "year", *GRADE_BANDS),
                         ("school_id_fk", "year"), school_rows)
    counts["views_refreshed"] = refresh_dependent_views(conn, "school_class_size")
    return counts


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the given years (default: every configured year) into the district, state and school tables."""
    return {"district": load_district(conn, years), "school": load_school(conn, years)}
