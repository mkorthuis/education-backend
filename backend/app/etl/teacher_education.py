"""Teachers by highest degree, per district and statewide, from the state's "Teacher Attainment" workbooks."""
import logging
import re
from collections import Counter
from typing import Iterable, Optional

import pandas as pd
from sqlalchemy.engine import Connection

from app.etl.core import configured_years, existing_ids, load_config, upsert_rows, year_file
from app.etl.staff import is_state_row, log_skips, parse_int, round_two, skip_district

logger = logging.getLogger("app.etl")

CONFIG = "district_teacher_education_config.yaml"
DISTRICT_TABLE = "district_teacher_education"
DISTRICT_COLUMNS = ("teacher_type_id_fk", "district_id_fk", "year", "value")
DISTRICT_KEY = ("teacher_type_id_fk", "district_id_fk", "year")
STATE_TABLE = "state_teacher_education"
STATE_COLUMNS = ("teacher_type_id_fk", "year", "value")
STATE_KEY = ("teacher_type_id_fk", "year")

# Degree -> teacher_education_type.id, in the order rows are written
EDUCATION_TYPES = {
    "bachelor": 2,          # Bachelor
    "masters": 3,           # Masters
    "beyond_masters": 4,    # Beyond Masters
    "none": 1,              # None
}


def parse_percentage(value) -> Optional[float]:
    """A percentage (0-100). Strings below 1 are taken as fractions ("0.25" -> 25); None if unparseable."""
    if pd.isna(value):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        digits = re.sub(r"[^0-9\.]", "", value.replace(",", "."))
        try:
            result = float(digits) if digits else None
        except ValueError:  # e.g. "1.2.3"
            return None
        if result is not None and 0 < result < 1:
            result = result * 100
        return result
    return None


def total_teachers(value) -> float:
    """The teacher count; 0 (row skipped) for blank or non-numeric cells such as "Did Not Report"."""
    if pd.isna(value):
        return 0
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0


def teachers_by_degree(row: pd.Series, columns: dict) -> Optional[list]:
    """
    [(teacher_type_id, teachers)] for one row; None when the row has no teacher count.

    Teachers per degree are the percentages times the total, rounded to two decimals; teachers
    with no degree are the remainder, unless it is within 0.1 (rounding). Zero values are left out.
    """
    total = total_teachers(row.iloc[columns["total_teachers"]])
    if pd.isna(total) or total <= 0:
        return None
    values = {}
    for degree in ("bachelor", "masters", "beyond_masters"):
        percent = parse_percentage(row.iloc[columns[f"{degree}_percent"]])
        values[degree] = round_two((percent / 100) * total) if not pd.isna(percent) and percent > 0 else 0
    with_degree = sum(values.values())
    values["none"] = 0 if abs(with_degree - total) <= 0.1 else round_two(total - with_degree)
    return [(EDUCATION_TYPES[degree], value) for degree, value in values.items() if value > 0]


def parse_year(df: pd.DataFrame, year: int, config: dict, districts: set, skips: Counter) -> tuple:
    """(district rows, state rows) from one year's sheet, in file order; the first row for a district wins."""
    columns = config["column_mappings"]
    district_rows, state_rows, seen = [], [], set()
    for _, row in df.iterrows():
        if is_state_row(row, config["state_data_settings"]):
            values = teachers_by_degree(row, columns)
            if values is None:
                skips["state rows without a teacher count"] += 1
            else:
                state_rows += [(type_id, year, value) for type_id, value in values]
            continue

        # Rows without a number in the district column are headings, notes and blank lines
        district_id = parse_int(row.iloc[columns["district_id"]])
        if district_id is None or district_id in seen:
            continue
        if district_id not in districts:
            skip_district(skips, district_id)
            continue
        values = teachers_by_degree(row, columns)
        if values is None:
            skips["district rows without a teacher count"] += 1
            continue
        district_rows += [(type_id, district_id, year, value) for type_id, value in values]
        seen.add(district_id)
    return district_rows, state_rows


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the given years (default: every configured year) into the district and state teacher education tables."""
    config = load_config(CONFIG)
    file_settings = config["file_settings"]
    districts = existing_ids(conn, "district")

    district_rows, state_rows, skips = [], [], Counter()
    for year in configured_years(file_settings, years):
        path = year_file(file_settings, year)
        df = pd.read_excel(path, sheet_name=file_settings["sheet_name"], skiprows=file_settings["start_row"] - 1)
        year_district_rows, year_state_rows = parse_year(df, year, config, districts, skips)
        if not year_district_rows or not year_state_rows:
            raise ValueError(f"No district or state teacher education found in {path}; has the layout changed?")
        district_rows += year_district_rows
        state_rows += year_state_rows
    log_skips(skips, "Teacher education")

    return {
        DISTRICT_TABLE: upsert_rows(conn, DISTRICT_TABLE, DISTRICT_COLUMNS, DISTRICT_KEY, district_rows),
        STATE_TABLE: upsert_rows(conn, STATE_TABLE, STATE_COLUMNS, STATE_KEY, state_rows),
    }
