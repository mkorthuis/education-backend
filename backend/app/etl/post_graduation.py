"""Where high school completers went after graduating, by school and for the state, from the "Completers" workbooks."""
import logging
from typing import Iterable, Optional

import pandas as pd
from sqlalchemy.engine import Connection

from app.etl.core import (
    configured_years, load_config, lookup_ids, refresh_dependent_views, upsert_rows, year_file
)
from app.etl.outcome_common import Schools, cell, clean_numeric

logger = logging.getLogger("app.etl")

CONFIG = "post_graduation_outcomes_config.yaml"
TYPE_TABLE = "post_graduation_type"
SCHOOL_TABLE = "school_post_graduation"
STATE_TABLE = "state_post_graduation"
SCHOOL_COLUMNS = ("school_id_fk", "year", "post_graduation_type_id_fk", "value")
STATE_COLUMNS = ("year", "post_graduation_type_id_fk", "value")

# (config percentages key, name, description), in the order the original migration inserted them
OUTCOME_TYPES = (
    ("4_year_college", "4 Year College", "Entering Four Year Colleges & Universities"),
    ("gt_4_year_college", "Less 4 Year College", "Entering Less Than Four Years"),
    ("addl_high_school", "Addl. High School", "Returning To Secondary Schools For Post Graduate Study"),
    ("employed", "Employed", "Employed"),
    ("armed_forces", "Armed Forces", "Armed Forces"),
    ("unemployed", "Unemployed", "Unemployed"),
    ("unknown", "Unknown", "Status Unknown"),
)


def outcome_counts(row: pd.Series, mappings: dict, type_ids: dict) -> list:
    """
    (type_id, count) pairs of one row: each outcome percentage times the row's total students.

    Rows without a positive total, and outcomes whose percentage or rounded count is blank
    or not positive, give nothing. Fractions (<= 1) are read as percentages / 100.
    """
    total_students = clean_numeric(cell(row, mappings["total_students"]))
    if total_students is None or total_students <= 0:
        return []
    total_students = int(float(total_students))

    counts = []
    for key, position in mappings["percentages"].items():
        percentage = clean_numeric(cell(row, position))
        if percentage is None or percentage <= 0:
            continue
        if percentage <= 1:
            percentage *= 100
        count = int(round(total_students * (percentage / 100)))
        if count > 0:
            counts.append((type_ids[key], count))
    return counts


def parse_year(df: pd.DataFrame, year: int, config: dict, type_ids: dict, schools: Schools) -> tuple:
    """
    (school_rows, state_rows, repeated, no_values) from one year's workbook, in file order.

    State rows are flagged "State Total" in column F. Schools are identified by id
    (column E); unknown schools and repeated schools (the first row wins) are skipped.
    """
    mappings = config["column_mappings"]
    school_rows, state_rows, seen = [], [], set()
    repeated = no_values = 0

    for _, row in df.iterrows():
        flag = cell(row, 5)
        if isinstance(flag, str) and flag.strip().lower() == "state total":
            state_rows.extend((year, type_id, count) for type_id, count in outcome_counts(row, mappings, type_ids))
            continue

        try:
            school_id = schools.by_id(int(cell(row, mappings["school_id"])), year)
        except (ValueError, TypeError):
            # Not a school row (headers, notes, blank lines)
            continue
        if not school_id:
            continue
        if school_id in seen:
            repeated += 1
            continue
        seen.add(school_id)

        counts = outcome_counts(row, mappings, type_ids)
        if not counts:
            no_values += 1
        school_rows.extend((school_id, year, type_id, count) for type_id, count in counts)
    return school_rows, state_rows, repeated, no_values


def load_types(conn: Connection) -> dict:
    """Insert the outcome types if missing; returns their ids by config key."""
    upsert_rows(conn, TYPE_TABLE, ("name", "description"), ("name",),
                [(name, description) for _, name, description in OUTCOME_TYPES])
    ids = lookup_ids(conn, TYPE_TABLE)
    return {key: ids[name] for key, name, _ in OUTCOME_TYPES}


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the given years (default: every configured year) into school_post_graduation and state_post_graduation."""
    config = load_config(CONFIG)
    type_ids = load_types(conn)
    schools = Schools(conn)

    school_rows, state_rows = [], []
    repeated = no_values = 0
    for year in configured_years(config["file_settings"], years):
        df = pd.read_excel(year_file(config["file_settings"], year))
        year_school_rows, year_state_rows, year_repeated, year_no_values = parse_year(
            df, year, config, type_ids, schools
        )
        school_rows.extend(year_school_rows)
        state_rows.extend(year_state_rows)
        repeated += year_repeated
        no_values += year_no_values

    if not school_rows and not state_rows:
        raise ValueError("No post-graduation data found in the input files")
    schools.warn("Post-graduation", repeated, no_values)

    counts = {
        SCHOOL_TABLE: upsert_rows(conn, SCHOOL_TABLE, SCHOOL_COLUMNS,
                                  ("school_id_fk", "year", "post_graduation_type_id_fk"), school_rows),
        STATE_TABLE: upsert_rows(conn, STATE_TABLE, STATE_COLUMNS, ("year", "post_graduation_type_id_fk"),
                                 state_rows),
    }
    counts["views_refreshed"] = refresh_dependent_views(conn, SCHOOL_TABLE)
    return counts
