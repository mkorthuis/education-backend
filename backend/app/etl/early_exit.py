"""High school early exit and dropout counts and rates, from the state's "early-exit-dropout-rates-HS" workbooks."""
import logging
from decimal import ROUND_HALF_UP, Decimal
from typing import Iterable, Optional

import pandas as pd
from sqlalchemy.engine import Connection

from app.etl.core import configured_years, load_config, refresh_dependent_views, upsert_rows, year_file
from app.etl.outcome_common import Schools, cell, clean_numeric

logger = logging.getLogger("app.etl")

CONFIG = "school_early_exit_config.yaml"
SCHOOL_TABLE = "school_early_exit"
STATE_TABLE = "state_early_exit"
# Config column_mappings keys, in table column order
FIELDS = (
    "adjusted_fall_enrollment", "earned_hiset", "enrolled_in_college", "dropped_out", "missing",
    "annual_early_exit_percentage", "4_year_early_exit_percentage",
    "annual_dropout_percentage", "4_year_dropout_percentage",
)
COUNT_FIELDS = FIELDS[:5]
PERCENTAGE_FIELDS = FIELDS[5:]
VALUE_COLUMNS = tuple(field.replace("4_year", "four_year") for field in FIELDS)
SCHOOL_COLUMNS = ("school_id_fk", "year") + VALUE_COLUMNS
STATE_COLUMNS = ("year",) + VALUE_COLUMNS


def round_four_decimal(value):
    if value is None:
        return None
    return float(Decimal(str(value)).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP))


def row_values(row: pd.Series, year: int, mappings: dict, is_state: bool) -> tuple:
    """The nine value columns of one school or state row; counts as int, rates rounded to 4 places."""
    values = []
    for field in FIELDS:
        position = mappings[field]
        # Files up to 2019 have the rates one column further left
        if year <= 2019 and field in PERCENTAGE_FIELDS:
            position -= 1
        value = clean_numeric(cell(row, position))
        if year <= 2019 and not is_state and field in ("adjusted_fall_enrollment", "missing"):
            # Left empty for schools in files up to 2019, as the original migration did
            value = None
        elif field in COUNT_FIELDS:
            value = int(float(value)) if value is not None else None
        else:
            value = round_four_decimal(value)
        values.append(value)
    return tuple(values)


def parse_year(df: pd.DataFrame, year: int, config: dict, schools: Schools) -> tuple:
    """
    (school_rows, state_row, repeated, no_values) from one year's workbook, in file order.

    The state row is the one flagged "State Total" (column F up to 2019, column D after);
    if there are several, the last wins. Schools are identified by id (column E) up to
    2019 and by name after. Unknown schools, repeated schools (the first row wins) and
    schools whose values are all blank or zero are skipped.
    """
    mappings = config["column_mappings"]
    school_rows, state_row, seen = [], None, set()
    repeated = no_values = 0

    for _, row in df.iterrows():
        flag = cell(row, 5 if year <= 2019 else 3)
        if isinstance(flag, str) and flag.strip().lower() == "state total":
            state_row = (year,) + row_values(row, year, mappings, is_state=True)
            continue

        raw_name = cell(row, mappings["school_name"])
        name = str(raw_name).strip() if raw_name is not None else ""
        if pd.isna(raw_name) or name == "":
            continue

        if year > 2019:
            school_id = schools.by_name(name, year)
        else:
            try:
                school_id = schools.by_id(int(float(name)), year)
            except (ValueError, TypeError):
                # Not a school row (headers, notes)
                continue
        if not school_id:
            continue
        if school_id in seen:
            repeated += 1
            continue
        seen.add(school_id)

        values = row_values(row, year, mappings, is_state=False)
        if not any(value is not None and value != 0 for value in values):
            no_values += 1
            continue
        school_rows.append((school_id, year) + values)
    return school_rows, state_row, repeated, no_values


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the given years (default: every configured year) into school_early_exit and state_early_exit."""
    config = load_config(CONFIG)
    schools = Schools(conn)

    school_rows, state_rows = [], []
    repeated = no_values = 0
    for year in configured_years(config["file_settings"], years):
        df = pd.read_excel(year_file(config["file_settings"], year))
        year_rows, state_row, year_repeated, year_no_values = parse_year(df, year, config, schools)
        school_rows.extend(year_rows)
        if state_row is not None:
            state_rows.append(state_row)
        repeated += year_repeated
        no_values += year_no_values

    if not school_rows and not state_rows:
        raise ValueError("No early exit data found in the input files")
    schools.warn("Early exit", repeated, no_values)

    counts = {
        SCHOOL_TABLE: upsert_rows(conn, SCHOOL_TABLE, SCHOOL_COLUMNS, ("school_id_fk", "year"), school_rows),
        STATE_TABLE: upsert_rows(conn, STATE_TABLE, STATE_COLUMNS, ("year",), state_rows),
    }
    counts["views_refreshed"] = refresh_dependent_views(conn, SCHOOL_TABLE)
    return counts
