"""Town enrollment by grade, from the state's "Town Level Enrollment By Grade" workbooks."""
import logging
from typing import Iterable, Optional

import pandas as pd
from sqlalchemy.engine import Connection

from app.etl.core import (
    configured_years, existing_ids, load_config, refresh_dependent_views, upsert_rows, year_file
)

logger = logging.getLogger("app.etl")

CONFIG = "generate_town_enrollments.yaml"
TABLE = "town_enrollment"
COLUMNS = ("town_id_fk", "grade_id_fk", "year", "enrollment")
KEY = ("town_id_fk", "grade_id_fk", "year")
# Grade column headers and their grade ids: Kindergarten to Grade 12. From 2026 the report
# also has PS and PG columns; they are not loaded, so every year covers the same grades.
GRADE_HEADERS = {"KG": 2, **{f"G{grade}": grade + 2 for grade in range(1, 13)}}


def parse_year(df: pd.DataFrame, year: int) -> tuple:
    """
    Rows of (town_id, grade_id, year, enrollment) from one year's workbook, in file order,
    plus the number of grade values that are not numbers.

    A row is a town when its first column (Town ID) is a whole number. Blank and zero
    grade counts are skipped; other values are truncated to integers.
    """
    header = next((row for _, row in df.iterrows() if str(row.iloc[0]).strip() == "Town ID"), None)
    if header is None:
        raise ValueError(f"Town enrollment file for {year} has no 'Town ID' header row")
    grade_columns = {position: GRADE_HEADERS[str(label).strip()]
                     for position, label in enumerate(header) if str(label).strip() in GRADE_HEADERS}
    if len(grade_columns) != len(GRADE_HEADERS):
        raise ValueError(f"Town enrollment file for {year} is missing grade columns: "
                         f"{sorted(set(GRADE_HEADERS) - {str(label).strip() for label in header})}")
    rows, invalid = [], 0
    for _, row in df.iterrows():
        town_id = row.iloc[0]
        if not (pd.notna(town_id) and isinstance(town_id, (int, float)) and town_id == int(town_id)):
            continue
        for position, grade_id in grade_columns.items():
            value = row.iloc[position]
            if pd.isna(value) or value == "" or value == 0:
                continue
            try:
                enrollment = int(float(value))
            except (ValueError, TypeError):
                invalid += 1
                continue
            rows.append((int(town_id), grade_id, year, enrollment))
    return rows, invalid


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the given years (default: every configured year) into town_enrollment."""
    config = load_config(CONFIG)
    known_towns = existing_ids(conn, "town")
    known_grades = existing_ids(conn, "grades")

    rows, unknown, invalid = [], [], 0
    for year in configured_years(config["file_settings"], years):
        year_rows, year_invalid = parse_year(pd.read_excel(year_file(config["file_settings"], year)), year)
        invalid += year_invalid
        for row in year_rows:
            if row[0] in known_towns and row[1] in known_grades:
                rows.append(row)
            else:
                unknown.append(row)

    if invalid:
        logger.warning(f"Skipped {invalid} town enrollment values that are not numbers")
    if unknown:
        # Towns (or grades) missing from their lookup tables are skipped, as the original migration did
        town_ids = sorted({row[0] for row in unknown if row[0] not in known_towns})
        grade_ids = sorted({row[1] for row in unknown if row[1] not in known_grades})
        logger.warning(f"Skipped {len(unknown)} town enrollments for towns not in the town table: {town_ids}"
                       + (f" or grades not in the grades table: {grade_ids}" if grade_ids else ""))

    counts = upsert_rows(conn, TABLE, COLUMNS, KEY, rows)
    # town_enrollment_state is created by the migration after the first load, so it is refreshed only later
    counts["views_refreshed"] = refresh_dependent_views(conn, TABLE)
    return counts
