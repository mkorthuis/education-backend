"""State totals of expenditure and average daily membership, from the state's "State Expenditures" files."""
import logging
import re
from typing import Iterable, Optional

import pandas as pd
from sqlalchemy.engine import Connection

from app.etl.core import configured_years, load_config, refresh_dependent_views, upsert_rows, year_file

logger = logging.getLogger("app.etl")

CONFIG = "state_expenditure_config.yaml"
# Migration 456acd975efb created this table as expenditure_state_total; 49358ad1275f renamed it to
# expenditure_state_rollup (and reused the old name for per-entry state totals). The migration
# passes the old name, the command uses the current one.
EXPENDITURE_TABLE = "expenditure_state_rollup"
EXPENDITURE_COLUMNS = ("year", "operating_elementary", "operating_middle", "operating_high", "operating_total",
                       "current_elementary", "current_middle", "current_high", "current_total", "total")
ENROLLMENT_TABLE = "state_enrollment_level"
ENROLLMENT_COLUMNS = ("year", "elementary", "middle", "high", "total")
KEY = ("year",)

# Rows are found by the start of their first cell; the first matching row wins. Values are in
# columns B, D, F and H (elementary, middle, high, total). "Total Expenditures" takes column H only;
# its first match is "Total Expenditures for Elementary and Secondary Education".
OPERATING = "Operating Expenses for Public Schools"
CURRENT = "Elem and Secondary Current Expenses"
TOTAL = "Total Expenditures"
ENROLLMENT = "Average daily membership"
LEVEL_POSITIONS = (1, 3, 5, 7)


def clean_number(value) -> Optional[float]:
    """A number from a cell, keeping only digits and the decimal point (so "$1,234 " is 1234.0)."""
    if pd.isna(value):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    cleaned = re.sub(r'[^\d.]', '', str(value))
    return float(cleaned) if cleaned else None


def parse_year(df: pd.DataFrame, year: int) -> tuple:
    """The year's expenditure row and enrollment row, in table column order."""
    found = {}
    for _, row in df.iterrows():
        if pd.isna(row.iloc[0]):
            continue
        label = str(row.iloc[0]).strip()
        for section in (OPERATING, CURRENT, TOTAL, ENROLLMENT):
            if section not in found and label.startswith(section):
                found[section] = [clean_number(row.iloc[i]) for i in LEVEL_POSITIONS]
                break
        if len(found) == 4:
            break

    missing = [section for section in (OPERATING, CURRENT, TOTAL, ENROLLMENT) if section not in found]
    if missing:
        # Kept from the original migration: the missing values are loaded as NULL
        logger.warning(f"State expenditure {year}: rows not found, values left empty: {missing}")
    none = [None] * 4
    expenditure = (year, *found.get(OPERATING, none), *found.get(CURRENT, none), found.get(TOTAL, none)[3])
    enrollment = (year, *found.get(ENROLLMENT, none))
    return expenditure, enrollment


def load(conn: Connection, years: Optional[Iterable[int]] = None, expenditure_table: str = EXPENDITURE_TABLE,
         enrollment_table: str = ENROLLMENT_TABLE) -> dict:
    """Load the given years (default: every configured year) into the state expenditure and enrollment tables."""
    config = load_config(CONFIG)
    expenditure_rows, enrollment_rows = [], []
    for year in configured_years(config["file_settings"], years):
        expenditure, enrollment = parse_year(pd.read_csv(year_file(config["file_settings"], year)), year)
        expenditure_rows.append(expenditure)
        enrollment_rows.append(enrollment)

    counts = {
        expenditure_table: upsert_rows(conn, expenditure_table, EXPENDITURE_COLUMNS, KEY, expenditure_rows),
        enrollment_table: upsert_rows(conn, enrollment_table, ENROLLMENT_COLUMNS, KEY, enrollment_rows),
    }
    counts["views_refreshed"] = (refresh_dependent_views(conn, expenditure_table)
                                 + refresh_dependent_views(conn, enrollment_table))
    return counts
