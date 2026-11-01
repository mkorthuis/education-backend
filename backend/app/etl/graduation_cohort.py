"""Four-year graduation cohort counts by school and for the state, from the "Cohort Counts By School" workbooks."""
import logging
from typing import Iterable, Optional

import pandas as pd
from sqlalchemy.engine import Connection

from app.etl.core import configured_years, load_config, refresh_dependent_views, upsert_rows, year_file
from app.etl.outcome_common import Schools, cell, clean_numeric

logger = logging.getLogger("app.etl")

CONFIG = "cohort_graduation_config.yaml"
SCHOOL_TABLE = "school_graduation_cohort"
STATE_TABLE = "state_graduation_cohort"
# Config column_mappings keys, in the order of the tables' value columns
FIELDS = ("cohort_size", "cohort_graduated", "earned_hiset", "dropped_out")
VALUE_COLUMNS = ("cohort_size", "graduate", "earned_hiset", "dropped_out")
SCHOOL_COLUMNS = ("school_id_fk", "year") + VALUE_COLUMNS
STATE_COLUMNS = ("year",) + VALUE_COLUMNS


def row_values(row: pd.Series, mappings: dict) -> tuple:
    """The four counts of one school or state row, as int (blank -> None)."""
    values = (clean_numeric(cell(row, mappings[field])) for field in FIELDS)
    return tuple(int(float(value)) if value is not None else None for value in values)


def parse_year(df: pd.DataFrame, year: int, config: dict, schools: Schools) -> tuple:
    """
    (school_rows, state_row, repeated, no_values) from one year's workbook, in file order.

    The state row has "State Total" in the school name column (D); if there are several,
    the last wins. Schools are identified by name; unknown schools, repeated schools (the
    first row wins) and schools whose counts are all blank or zero are skipped.
    """
    mappings = config["column_mappings"]
    school_rows, state_row, seen = [], None, set()
    repeated = no_values = 0

    for _, row in df.iterrows():
        raw_name = cell(row, mappings["school_name"])
        name = str(raw_name).strip() if raw_name is not None else ""
        if name.lower() == "state total":
            state_row = (year,) + row_values(row, mappings)
            continue
        if pd.isna(raw_name) or name == "":
            continue

        school_id = schools.by_name(name, year)
        if not school_id:
            continue
        if school_id in seen:
            repeated += 1
            continue
        seen.add(school_id)

        values = row_values(row, mappings)
        if not any(value is not None and value != 0 for value in values):
            no_values += 1
            continue
        school_rows.append((school_id, year) + values)
    return school_rows, state_row, repeated, no_values


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the given years (default: every configured year) into school_graduation_cohort and state_graduation_cohort."""
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
        raise ValueError("No graduation cohort data found in the input files")
    schools.warn("Graduation cohort", repeated, no_values)

    counts = {
        SCHOOL_TABLE: upsert_rows(conn, SCHOOL_TABLE, SCHOOL_COLUMNS, ("school_id_fk", "year"), school_rows),
        STATE_TABLE: upsert_rows(conn, STATE_TABLE, STATE_COLUMNS, ("year",), state_rows),
    }
    # district_graduation_cohort, once the migration has created it
    counts["views_refreshed"] = refresh_dependent_views(conn, SCHOOL_TABLE)
    return counts
