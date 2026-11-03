"""School enrollment by grade, from the state's "School Enrollments by Grade Public" workbooks."""
import logging
from typing import Iterable, Optional

import pandas as pd
from sqlalchemy.engine import Connection

from app.etl.core import (
    configured_years, known_school_ids, load_config, refresh_dependent_views, upsert_rows, year_file
)

logger = logging.getLogger("app.etl")

CONFIG = "generate_enrollment_config.yaml"
TABLE = "school_enrollment"
COLUMNS = ("school_id_fk", "grade_id_fk", "year", "enrollment")
KEY = ("school_id_fk", "grade_id_fk", "year")


def parse_year(df: pd.DataFrame, year: int, config: dict) -> list:
    """
    Rows of (school_id, grade_id, year, enrollment) from one year's workbook, in file order.

    A row is a school when its first column (SAU number) is numeric. Blank and zero
    grade counts are skipped.
    """
    settings = config["excel_settings"]
    rows = []
    for _, row in df.iloc[settings["data_start_row"]:].iterrows():
        try:
            int(row.iloc[0])
        except (ValueError, TypeError):
            continue
        school_id = int(row.iloc[4])
        for grade, position in settings["grade_positions"].items():
            value = row.iloc[position]
            if pd.notna(value) and value > 0:
                rows.append((school_id, config["grade_mappings"][grade], year, int(value)))
    return rows


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the given years (default: every configured year) into school_enrollment."""
    config = load_config(CONFIG)
    known_schools = known_school_ids(conn)

    rows, unknown_schools = [], set()
    for year in configured_years(config["file_settings"], years):
        for row in parse_year(pd.read_excel(year_file(config["file_settings"], year)), year, config):
            if row[0] in known_schools:
                rows.append((known_schools[row[0]], *row[1:]))
            else:
                unknown_schools.add((year, row[0]))

    if unknown_schools:
        # Schools missing from the school list are skipped, as the original migration did
        school_ids = sorted({school_id for _, school_id in unknown_schools})
        logger.warning(f"Skipped {len(unknown_schools)} school-years for {len(school_ids)} schools "
                       f"not in the school table: {school_ids}")

    counts = upsert_rows(conn, TABLE, COLUMNS, KEY, rows)
    counts["views_refreshed"] = refresh_dependent_views(conn, TABLE)
    return counts
