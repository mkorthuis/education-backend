"""Average teacher salary, per district and statewide, from the state's "Teacher Average Salary" workbooks."""
import logging
import re
from collections import Counter
from typing import Iterable, Optional

import pandas as pd
from sqlalchemy import text
from sqlalchemy.engine import Connection

from app.etl.core import configured_years, existing_ids, load_config, upsert_rows
from app.etl.staff import cell, log_skips, parse_int, skip_district, valid_salary, year_file_any_extension

logger = logging.getLogger("app.etl")

CONFIG = "district_teacher_salary_config.yaml"
DISTRICT_TABLE = "district_teacher_average_salary"
DISTRICT_COLUMNS = ("district_id_fk", "year", "salary")
DISTRICT_KEY = ("district_id_fk", "year")
STATE_TABLE = "state_teacher_average_salary"
STATE_COLUMNS = ("year", "salary")
STATE_KEY = ("year",)


def is_state_label(value, label: str) -> bool:
    """Whether a cell starts with the state row's label (case-insensitive)."""
    return isinstance(value, str) and value.strip().lower().startswith(label.lower())


def clean_district_name(name) -> Optional[str]:
    """Lowercase, without a trailing "school district", "schools" or "sd", with single spaces."""
    if not isinstance(name, str):
        return None
    name = name.lower()
    name = re.sub(r"\s+school\s+district\s*$", "", name)
    name = re.sub(r"\s+schools\s*$", "", name)
    name = re.sub(r"\s+sd\s*$", "", name)
    return re.sub(r"\s+", " ", name.strip())


def district_ids_by_name(conn: Connection, names: set) -> dict:
    """
    Map cleaned names to the first district whose name contains them, in table order.

    This is the original migration's lookup (LIKE '%name%' ... LIMIT 1 with no ORDER BY, i.e. the
    first match in physical order, made explicit here with ctid), kept so fresh builds get the same
    rows. Physical order is load order as long as district rows are never updated in place. It is
    a loose match: e.g. "dover" finds Andover and "northwood" finds Coe-Brown Northwood Academy.
    """
    result = conn.execute(text("""
        SELECT DISTINCT ON (n.name) n.name, d.id
        FROM unnest(CAST(:names AS text[])) AS n(name)
        JOIN district d ON LOWER(d.name) LIKE '%' || n.name || '%'
            OR LOWER(d.name) LIKE '%' || n.name || ' school%'
            OR LOWER(d.name) LIKE '%' || n.name || ' sd%'
        ORDER BY n.name, d.ctid
    """), {"names": sorted(names)})
    return {name: district_id for name, district_id in result}


def parse_legacy_year(conn: Connection, df: pd.DataFrame, year: int, config: dict, skips: Counter) -> tuple:
    """
    (district rows, state rows) from a legacy sheet (up to legacy_year_end), in file order.

    Districts are named, not numbered: the name is in the first or second column, with the
    salary two columns to its right. Each row tries the first column, then the second. The
    first row matched to a district wins. Some sheets have only three columns, so the second
    position's salary column can be missing (read as blank).
    """
    columns = config["column_mappings"]
    positions = [(columns["legacy_district_name_col0"], columns["legacy_salary_col0"]),
                 (columns["legacy_district_name_col1"], columns["legacy_salary_col1"])]
    state_label = config["state_data_settings"]["legacy_state_identifier_text"]
    names = {clean_district_name(cell(row, name_column)) for _, row in df.iterrows() for name_column, _ in positions}
    district_ids = district_ids_by_name(conn, {name for name in names if name})

    district_rows, state_rows, seen = [], [], set()
    for _, row in df.iterrows():
        for name_column, salary_column in positions:
            name = cell(row, name_column)
            if not isinstance(name, str):
                continue
            if is_state_label(name, state_label):
                salary = valid_salary(cell(row, salary_column))
                if salary is None:
                    continue
                state_rows.append((year, salary))
                break
            district_id = district_ids.get(clean_district_name(name))
            if district_id is None:
                continue
            if district_id in seen:
                break
            salary = valid_salary(cell(row, salary_column))
            if salary is None:
                skips["district rows without a salary"] += 1
                continue
            district_rows.append((district_id, year, salary))
            seen.add(district_id)
            break
    return district_rows, state_rows


def parse_year(df: pd.DataFrame, year: int, config: dict, districts: set, skips: Counter) -> tuple:
    """(district rows, state rows) from a sheet with district ids, in file order; the first row for a district wins."""
    columns = config["column_mappings"]
    settings = config["state_data_settings"]
    district_rows, state_rows, seen = [], [], set()
    for _, row in df.iterrows():
        if is_state_label(cell(row, settings["modern_state_column_index"]), settings["modern_state_identifier_text"]):
            salary = valid_salary(row.iloc[columns["salary"]])
            if salary is None:
                skips["state rows without a salary"] += 1
            else:
                state_rows.append((year, salary))
            continue

        # Rows without a number in the district column are headings, notes and blank lines
        district_id = parse_int(row.iloc[columns["district_id"]])
        if district_id is None or district_id in seen:
            continue
        if district_id not in districts:
            skip_district(skips, district_id)
            continue
        salary = valid_salary(row.iloc[columns["salary"]])
        if salary is None:
            skips["district rows without a salary"] += 1
            continue
        district_rows.append((district_id, year, salary))
        seen.add(district_id)
    return district_rows, state_rows


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the given years (default: every configured year) into the district and state average salary tables."""
    config = load_config(CONFIG)
    file_settings = config["file_settings"]
    districts = existing_ids(conn, "district")

    district_rows, state_rows, skips = [], [], Counter()
    for year in configured_years(file_settings, years):
        path = year_file_any_extension(file_settings, year)
        df = pd.read_excel(path, skiprows=file_settings["start_row"] - 1)
        if year <= int(file_settings["legacy_year_end"]):
            year_district_rows, year_state_rows = parse_legacy_year(conn, df, year, config, skips)
        else:
            year_district_rows, year_state_rows = parse_year(df, year, config, districts, skips)
        if not year_district_rows or not year_state_rows:
            raise ValueError(f"No district or state average salary found in {path}; has the layout changed?")
        district_rows += year_district_rows
        state_rows += year_state_rows
    log_skips(skips, "Teacher average salary")

    return {
        DISTRICT_TABLE: upsert_rows(conn, DISTRICT_TABLE, DISTRICT_COLUMNS, DISTRICT_KEY, district_rows),
        STATE_TABLE: upsert_rows(conn, STATE_TABLE, STATE_COLUMNS, STATE_KEY, state_rows),
    }
