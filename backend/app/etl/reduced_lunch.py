"""
Free and reduced-price lunch eligibility by school, district and for the state, from the state's
"Free Reduced K-12 School Lunch Eligibility Rates by School" workbooks (counts as of October 1).
"""
import logging
from typing import Iterable, Optional

import pandas as pd
from sqlalchemy.engine import Connection

from app.etl.core import (
    configured_years, existing_ids, known_school_ids, load_config, upsert_rows, whole_number, year_file
)

logger = logging.getLogger("app.etl")

CONFIG = "reduced_lunch_config.yaml"
SCHOOL_TABLE = "school_reduced_lunch"
DISTRICT_TABLE = "district_reduced_lunch"
STATE_TABLE = "state_reduced_lunch"
VALUE_COLUMNS = ("enrollment", "eligible")
SCHOOL_COLUMNS = ("school_id_fk", "year") + VALUE_COLUMNS
DISTRICT_COLUMNS = ("district_id_fk", "year") + VALUE_COLUMNS
STATE_COLUMNS = ("year",) + VALUE_COLUMNS


def parse_year(df: pd.DataFrame, year: int, config: dict) -> tuple:
    """
    (school_rows, district_rows, state_row) from one year's workbook, in file order.

    A school row has a whole number in the School # column. A district's counts are the sum of
    its schools' rows; the file prints that sum as a "District Total:" row only for districts
    with more than one school, and those rows are checked against it. The state row is the one
    labelled "Total State Average" (every public school, including academies, charter and
    interstate schools).
    """
    columns = config["column_mappings"]
    school_rows, district_totals, printed_totals, state_row = [], {}, {}, None
    for _, row in df.iterrows():
        label = str(row.iloc[columns["school_name"]]).strip() if pd.notna(row.iloc[columns["school_name"]]) else ""
        enrollment = whole_number(row.iloc[columns["enrollment"]])
        eligible = whole_number(row.iloc[columns["eligible"]])
        if label == config["state_label"]:
            state_row = (year, enrollment, eligible)
            continue
        district_id = whole_number(row.iloc[columns["district_id"]])
        school_id = whole_number(row.iloc[columns["school_id"]])
        if district_id is None or enrollment is None or eligible is None:
            continue
        if school_id is None:
            if label.startswith("District Total"):
                printed_totals[district_id] = (enrollment, eligible)
            continue
        school_rows.append((school_id, district_id, year, enrollment, eligible))
        total = district_totals.setdefault(district_id, [0, 0])
        total[0] += enrollment
        total[1] += eligible

    if state_row is None:
        raise ValueError(f"Reduced lunch file for {year} has no '{config['state_label']}' row")
    mismatched = sorted(district_id for district_id, total in printed_totals.items()
                        if tuple(district_totals.get(district_id, ())) != total)
    if mismatched:
        logger.warning(f"Reduced lunch {year}: district totals differ from their schools' sum for districts {mismatched}")
    district_rows = [(district_id, year, total[0], total[1]) for district_id, total in district_totals.items()]
    return school_rows, district_rows, state_row


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the given years (default: every configured year) into the school, district and state tables."""
    config = load_config(CONFIG)
    schools = known_school_ids(conn)
    districts = existing_ids(conn, "district")

    school_rows, district_rows, state_rows = [], [], []
    unknown_schools, unknown_districts = set(), set()
    for year in configured_years(config["file_settings"], years):
        df = pd.read_excel(year_file(config["file_settings"], year), header=None)
        year_schools, year_districts, state_row = parse_year(df, year, config)
        for school_id, _district_id, *values in year_schools:
            if school_id in schools:
                school_rows.append((schools[school_id], *values))
            else:
                unknown_schools.add(school_id)
        for row in year_districts:
            if row[0] in districts:
                district_rows.append(row)
            else:
                unknown_districts.add(row[0])
        state_rows.append(state_row)

    # Schools and districts that have since closed and aren't in the database are skipped
    if unknown_schools:
        logger.warning(f"Skipped reduced lunch rows for {len(unknown_schools)} schools not in the school table: "
                       f"{sorted(unknown_schools)}")
    if unknown_districts:
        logger.warning(f"Skipped reduced lunch rows for districts not in the district table: {sorted(unknown_districts)}")

    return {
        SCHOOL_TABLE: upsert_rows(conn, SCHOOL_TABLE, SCHOOL_COLUMNS, ("school_id_fk", "year"), school_rows),
        DISTRICT_TABLE: upsert_rows(conn, DISTRICT_TABLE, DISTRICT_COLUMNS, ("district_id_fk", "year"), district_rows),
        STATE_TABLE: upsert_rows(conn, STATE_TABLE, STATE_COLUMNS, ("year",), state_rows),
    }
