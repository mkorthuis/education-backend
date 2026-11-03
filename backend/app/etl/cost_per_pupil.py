"""Cost per pupil by district and the state average, from the state's "Cost Per Pupil by District" files."""
import logging
from typing import Iterable, Optional

import pandas as pd
from sqlalchemy.engine import Connection

from app.etl.core import (
    configured_years, existing_ids, load_config, refresh_dependent_views, upsert_rows, year_file
)

logger = logging.getLogger("app.etl")

CONFIG = "generate_cost_per_pupil_config.yaml"
DISTRICT_TABLE = "district_cost_per_pupil"
DISTRICT_COLUMNS = ("district_id_fk", "year", "elementary", "middle", "high", "total")
DISTRICT_KEY = ("district_id_fk", "year")
STATE_TABLE = "state_cost_per_pupil"
STATE_COLUMNS = ("year", "elementary", "middle", "high", "total")
STATE_KEY = ("year",)

# Column headers of the four values, and their positions when a header is missing
COLUMN_LABELS = {"elementary": " Elementary ", "middle": " Middle ", "high": " High ", "total": " Total "}
DEFAULT_INDICES = {"elementary": 4, "middle": 5, "high": 6, "total": 7}


def is_district_id(value) -> bool:
    """Whether a DIST cell holds a district number."""
    if pd.isna(value) or value == '' or value == '-':
        return False
    try:
        int(float(value))
        return True
    except (ValueError, TypeError):
        return False


def parse_currency(value) -> Optional[int]:
    """A dollar amount as a whole number; None when blank or "-" (and for text that isn't a number)."""
    if pd.isna(value) or value == '' or value == '-':
        return None
    cleaned = value.replace('$', '').replace(',', '').replace(' ', '')
    if cleaned == '-' or cleaned == '':
        return None
    try:
        return int(float(cleaned))
    except ValueError:
        return None


def find_header_row(df: pd.DataFrame, year: int) -> int:
    """The header row: "DIST" in the first column and "School District" in the fourth (or, failing that, just "DIST")."""
    first_rows = range(min(25, df.shape[0]))
    for i in first_rows:
        if (isinstance(df.iloc[i, 0], str) and "DIST" in df.iloc[i, 0]
                and isinstance(df.iloc[i, 3], str) and "School District" in df.iloc[i, 3]):
            return i
    for i in first_rows:
        if isinstance(df.iloc[i, 0], str) and df.iloc[i, 0].strip() == "DIST":
            logger.warning(f"Cost per pupil {year}: header row found by DIST alone (row {i})")
            return i
    raise ValueError(f"Cost per pupil {year}: no header row with DIST in the first 25 rows")


def parse_year(df: pd.DataFrame, year: int) -> tuple:
    """
    District rows of (district_id, year, elementary, middle, high, total) in file order,
    and the state average row (year, elementary, middle, high, total) or None.

    Rows whose DIST cell isn't a number (titles, notes, the state average) are not districts.
    """
    header_row = find_header_row(df, year)
    column_names = [str(df.iloc[header_row, j]).strip() or f"Column_{j}" for j in range(df.shape[1])]
    data = df.iloc[header_row + 1:].reset_index(drop=True)
    columns = {level: column_names.index(label) if label in column_names else DEFAULT_INDICES[level]
               for level, label in COLUMN_LABELS.items()}

    def values(i):
        return tuple(parse_currency(data.iloc[i, j]) if j < data.shape[1] else None for j in columns.values())

    state_row = next((i for i in range(min(30, data.shape[0]))
                      if isinstance(data.iloc[i, 3], str) and "State Average" in data.iloc[i, 3]), None)
    state = (year, *values(state_row)) if state_row is not None else None
    if state is None:
        logger.warning(f"Cost per pupil {year}: no State Average row; no state value loaded")

    district_column = column_names.index("DIST") if "DIST" in column_names else 0
    districts = []
    for i in range(data.shape[0]):
        value = data.iloc[i, district_column]
        if i == state_row or not is_district_id(value):
            continue
        districts.append((int(float(value)), year, *values(i)))
    return districts, state


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the given years (default: every configured year) into district_cost_per_pupil and state_cost_per_pupil."""
    config = load_config(CONFIG)
    known_districts = existing_ids(conn, "district")
    aliases = config.get("district_id_aliases") or {}
    missing = sorted(set(aliases.values()) - known_districts)
    if missing:
        raise ValueError(f"{CONFIG} aliases district ids to ids that aren't in the database: {missing}")

    district_rows, state_rows, unknown_districts = [], [], set()
    for year in configured_years(config["file_settings"], years):
        districts, state = parse_year(pd.read_csv(year_file(config["file_settings"], year), dtype=str), year)
        if not districts and state is None:
            raise ValueError(f"Cost per pupil {year}: no district or state rows found")
        for row in districts:
            row = (aliases.get(row[0], row[0]), *row[1:])
            if row[0] in known_districts:
                district_rows.append(row)
            else:
                unknown_districts.add((year, row[0]))
        if state is not None:
            state_rows.append(state)

    if unknown_districts:
        # Districts missing from the district list are skipped, as the original migration did
        district_ids = sorted({district_id for _, district_id in unknown_districts})
        logger.warning(f"Skipped {len(unknown_districts)} district-years for {len(district_ids)} districts "
                       f"not in the district table: {district_ids}")

    counts = {
        DISTRICT_TABLE: upsert_rows(conn, DISTRICT_TABLE, DISTRICT_COLUMNS, DISTRICT_KEY, district_rows),
        STATE_TABLE: upsert_rows(conn, STATE_TABLE, STATE_COLUMNS, STATE_KEY, state_rows),
    }
    counts["views_refreshed"] = (refresh_dependent_views(conn, DISTRICT_TABLE)
                                 + refresh_dependent_views(conn, STATE_TABLE))
    return counts
