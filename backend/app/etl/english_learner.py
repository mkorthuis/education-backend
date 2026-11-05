"""
English learners by district and for the state, from the state's "Limited English Proficiency
Enrollment" workbooks (counts as of October 1). The state reports English learners by district only.
"""
import logging
from typing import Iterable, Optional

import pandas as pd
from sqlalchemy.engine import Connection

from app.etl.core import configured_years, existing_ids, load_config, upsert_rows, whole_number, year_file

logger = logging.getLogger("app.etl")

CONFIG = "english_learner_config.yaml"
DISTRICT_TABLE = "district_english_learner"
STATE_TABLE = "state_english_learner"
VALUE_COLUMNS = ("enrollment", "eligible", "monitor")
DISTRICT_COLUMNS = ("district_id_fk", "year") + VALUE_COLUMNS
STATE_COLUMNS = ("year",) + VALUE_COLUMNS


def parse_year(df: pd.DataFrame, year: int, config: dict) -> tuple:
    """
    (district_rows, state_row) from one year's workbook, in file order.

    A district row has a whole number in the District # column; the state row is labelled
    "State Total" in the District Name column.
    """
    columns = config["column_mappings"]
    district_rows, state_row = [], None
    for _, row in df.iterrows():
        values = tuple(whole_number(row.iloc[columns[name]]) for name in VALUE_COLUMNS)
        name = row.iloc[columns["district_name"]]
        if pd.notna(name) and str(name).strip() == config["state_label"]:
            state_row = (year, *values)
            continue
        district_id = whole_number(row.iloc[columns["district_id"]])
        if district_id is not None and values[0] is not None:
            district_rows.append((district_id, year, *values))
    if state_row is None:
        raise ValueError(f"English learner file for {year} has no '{config['state_label']}' row")
    return district_rows, state_row


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the given years (default: every configured year) into the district and state tables."""
    config = load_config(CONFIG)
    districts = existing_ids(conn, "district")

    district_rows, state_rows, unknown = [], [], set()
    for year in configured_years(config["file_settings"], years):
        df = pd.read_excel(year_file(config["file_settings"], year), header=None)
        year_districts, state_row = parse_year(df, year, config)
        for row in year_districts:
            if row[0] in districts:
                district_rows.append(row)
            else:
                unknown.add(row[0])
        state_rows.append(state_row)

    # Districts that have since closed and aren't in the database are skipped
    if unknown:
        logger.warning(f"Skipped English learner rows for districts not in the district table: {sorted(unknown)}")

    return {
        DISTRICT_TABLE: upsert_rows(conn, DISTRICT_TABLE, DISTRICT_COLUMNS, ("district_id_fk", "year"), district_rows),
        STATE_TABLE: upsert_rows(conn, STATE_TABLE, STATE_COLUMNS, ("year",), state_rows),
    }
