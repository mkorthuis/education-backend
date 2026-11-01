"""
Teacher salary bands (minimum and maximum salary, steps) per district, from the state's
"Teacher Starting Salary" workbooks. The state_teacher_salary_band materialized view averages them.
"""
import logging
import re
from collections import Counter
from typing import Iterable, Optional

import pandas as pd
from sqlalchemy.engine import Connection

from app.etl.core import configured_years, existing_ids, load_config, refresh_dependent_views, upsert_rows
from app.etl.staff import log_skips, parse_int, skip_district, valid_salary, year_file_any_extension

logger = logging.getLogger("app.etl")

CONFIG = "district_teacher_salary_band_config.yaml"
TABLE = "district_teacher_salary_band"
COLUMNS = ("district_id_fk", "teacher_salary_band_type_id_fk", "year", "min_salary", "max_salary", "steps")
KEY = ("district_id_fk", "teacher_salary_band_type_id_fk", "year")


def normalize_band_name(name: str) -> str:
    """Uppercase without periods or spaces, PLUS as +, Bachelor(s)/Master(s) as BA/MA: "B.A. plus 15" -> "BA+15"."""
    name = name.upper().replace(".", "")
    name = name.replace(" PLUS ", "+").replace("PLUS", "+")
    name = name.replace(" ", "")
    name = re.sub(r"^BACHELOR(S)?(\+|$)", r"BA\2", name)
    return re.sub(r"^MASTER(S)?(\+|$)", r"MA\2", name)


def parse_year(df: pd.DataFrame, year: int, config: dict, districts: set, skips: Counter) -> list:
    """
    Rows from one year's sheet, in file order; the first row for a district and band wins.

    Rows without a band the config maps, or without a positive minimum and maximum salary, are
    skipped. Steps that are missing, fractional or not positive are stored as NULL.
    """
    columns = config["column_mappings"]
    bands = {normalize_band_name(name): band_id for name, band_id in config["salary_band_mapping"].items()}
    rows, seen = [], set()
    for _, row in df.iterrows():
        # Rows without a number in the district column are headings, notes and blank lines
        district_id = parse_int(row.iloc[columns["district_id"]])
        if district_id is None:
            continue
        if district_id not in districts:
            skip_district(skips, district_id)
            continue
        band = row.iloc[columns["salary_band_type"]]
        if pd.isna(band):
            skips["rows without a band"] += 1
            continue
        band_id = bands.get(normalize_band_name(str(band)))
        if band_id is None:
            skips[f"rows with unknown band {str(band)!r}"] += 1
            continue
        if (district_id, band_id) in seen:
            continue
        min_salary = valid_salary(row.iloc[columns["min_salary"]])
        max_salary = valid_salary(row.iloc[columns["max_salary"]])
        if min_salary is None or max_salary is None:
            skips["rows without a minimum or maximum salary"] += 1
            continue
        steps = parse_int(row.iloc[columns["steps"]])
        if steps is not None and steps <= 0:
            steps = None
        rows.append((district_id, band_id, year, min_salary, max_salary, steps))
        seen.add((district_id, band_id))
    return rows


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the given years (default: every configured year) into district_teacher_salary_band."""
    config = load_config(CONFIG)
    file_settings = config["file_settings"]
    districts = existing_ids(conn, "district")

    rows, skips = [], Counter()
    for year in configured_years(file_settings, years):
        path = year_file_any_extension(file_settings, year)
        year_rows = parse_year(pd.read_excel(path, skiprows=file_settings["start_row"] - 1), year, config, districts, skips)
        if not year_rows:
            raise ValueError(f"No salary bands found in {path}; has the layout changed?")
        rows += year_rows
    log_skips(skips, "Teacher salary bands")

    counts = upsert_rows(conn, TABLE, COLUMNS, KEY, rows)
    # The state_teacher_salary_band view; it does not exist yet when the migration loads the table
    counts["views_refreshed"] = refresh_dependent_views(conn, TABLE)
    return counts
