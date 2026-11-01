"""
District and state staff counts (FTE) by staff type, from the state's "FTE Staff" workbooks.

Also holds the parsing helpers shared by the teacher education, salary and salary band loaders.
"""
import logging
import os
import re
from collections import Counter
from decimal import ROUND_HALF_UP, Decimal
from typing import Iterable, Optional

import pandas as pd
from sqlalchemy.engine import Connection

from app.etl.core import config_path, configured_years, existing_ids, load_config, upsert_rows, year_file

logger = logging.getLogger("app.etl")

CONFIG = "district_staff_config.yaml"
DISTRICT_TABLE = "district_staff"
DISTRICT_COLUMNS = ("school_staff_type_id_fk", "district_id_fk", "year", "value")
DISTRICT_KEY = ("school_staff_type_id_fk", "district_id_fk", "year")
STATE_TABLE = "state_staff"
STATE_COLUMNS = ("school_staff_type_id_fk", "year", "value")
STATE_KEY = ("school_staff_type_id_fk", "year")

# Config column -> school_staff_type.id
STAFF_TYPES = {
    "teacher_count": 1,              # Teacher
    "instruction_support_count": 2,  # Instruction Support
    "librarian_count": 3,            # Librarian
    "specialist_count": 4,           # Specialist
    "admin_support_count": 5,        # Admin Support
    "other_support_count": 6,        # All Other Support
}


def parse_int(value) -> Optional[int]:
    """A whole number, or the digits of a string ("District # 123" -> 123); None otherwise."""
    if pd.isna(value):
        return None
    if isinstance(value, (int, float)):
        return int(value) if float(value).is_integer() else None
    if isinstance(value, str):
        digits = re.sub(r"[^0-9]", "", value)
        return int(digits) if digits else None
    return None


def parse_salary(value) -> Optional[float]:
    """A number, or a string with currency symbols and thousands separators removed; None otherwise."""
    if pd.isna(value):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        digits = re.sub(r"[^0-9\.]", "", value.replace(",", ""))
        try:
            return float(digits) if digits else None
        except ValueError:  # e.g. "1.2.3"
            return None
    return None


def round_two(value: float) -> float:
    """Round half up to two decimals."""
    return float(Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def valid_salary(value) -> Optional[float]:
    """A positive salary rounded to two decimals; None (row skipped) otherwise."""
    salary = parse_salary(value)
    if salary is None or salary <= 0:
        return None
    return round_two(salary)


def cell(row: pd.Series, position: int):
    """The value at a column position, or None when the sheet has fewer columns."""
    return row.iloc[position] if position < len(row) else None


def is_state_row(row: pd.Series, settings: dict) -> bool:
    """Whether the row's state column contains the state totals label (case-insensitive)."""
    value = cell(row, settings["state_column_index"])
    return isinstance(value, str) and settings["state_identifier_text"].lower() in value.lower()


def year_file_any_extension(file_settings: dict, year: int) -> str:
    """Like core.year_file, for patterns without an extension: the first of `extensions` that exists."""
    stem = file_settings["default_input"].replace("****", str(year))
    for extension in file_settings["extensions"]:
        path = config_path(stem + extension)
        if os.path.exists(path):
            return path
    raise FileNotFoundError(f"Input file for {year} not found: {config_path(stem)}{file_settings['extensions']}")


def skip_district(skips: Counter, district_id: int) -> None:
    """Count a row skipped because its district is not in the district table."""
    skips[("district", district_id)] += 1


def log_skips(skips: Counter, what: str) -> None:
    """One warning with the number of rows skipped for each reason."""
    parts = [f"{count} {reason}" for reason, count in skips.items() if isinstance(reason, str)]
    districts = sorted(key[1] for key in skips if isinstance(key, tuple))
    if districts:
        count = sum(skips[("district", district_id)] for district_id in districts)
        parts.append(f"{count} rows for {len(districts)} districts not in the district table: {districts}")
    if parts:
        logger.warning(f"{what}: skipped " + ", ".join(parts))


def staff_count(value) -> Optional[float]:
    """A staff count as float; None for blank, zero or non-numeric cells, which are skipped."""
    if pd.isna(value) or value == 0:
        return None
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def parse_year(df: pd.DataFrame, year: int, config: dict, districts: set, skips: Counter) -> tuple:
    """
    (district rows, state rows) from one year's sheet, in file order.

    The state totals row is the one labelled "State Total"; every other row is a district
    row when its district column holds a number. Blank, zero and non-numeric counts are skipped.
    """
    columns = config["column_mappings"]
    district_rows, state_rows = [], []
    for _, row in df.iterrows():
        counts = [(staff_type, staff_count(row.iloc[columns[column]])) for column, staff_type in STAFF_TYPES.items()]
        if is_state_row(row, config["state_data_settings"]):
            state_rows += [(staff_type, year, value) for staff_type, value in counts if value is not None]
            continue
        # Rows without a number in the district column are headings, notes and blank lines
        district_id = parse_int(row.iloc[columns["district_id"]])
        if district_id is None:
            continue
        if district_id not in districts:
            skip_district(skips, district_id)
        else:
            district_rows += [(staff_type, district_id, year, value) for staff_type, value in counts if value is not None]
    return district_rows, state_rows


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the given years (default: every configured year) into district_staff and state_staff."""
    config = load_config(CONFIG)
    file_settings = config["file_settings"]
    districts = existing_ids(conn, "district")

    district_rows, state_rows = [], []
    skips = Counter()
    for year in configured_years(file_settings, years):
        path = year_file(file_settings, year)
        df = pd.read_excel(path, sheet_name=file_settings["sheet_name"], skiprows=file_settings["start_row"] - 1)
        year_district_rows, year_state_rows = parse_year(df, year, config, districts, skips)
        if not year_district_rows or not year_state_rows:
            raise ValueError(f"No district or state staff counts found in {path}; has the layout changed?")
        district_rows += year_district_rows
        state_rows += year_state_rows
    log_skips(skips, "Staff counts")

    return {
        DISTRICT_TABLE: upsert_rows(conn, DISTRICT_TABLE, DISTRICT_COLUMNS, DISTRICT_KEY, district_rows),
        STATE_TABLE: upsert_rows(conn, STATE_TABLE, STATE_COLUMNS, STATE_KEY, state_rows),
    }
