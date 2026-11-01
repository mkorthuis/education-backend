"""Education Freedom Account (EFA) membership by town, from the state's yearly EFA workbooks."""
import logging
import re
from decimal import Decimal
from typing import Iterable, Optional

import pandas as pd
from sqlalchemy.engine import Connection

from app.etl.core import (
    configured_years, existing_ids, load_config, lookup_ids, refresh_dependent_views, upsert_rows, year_file
)

logger = logging.getLogger("app.etl")

CONFIG = "generate_education_freedom_accounts.yaml"
# No later migration renames or reshapes these tables, so the migration and the CLI use the
# same names; the CLI path also refreshes the materialized view built on the entries.
TYPE_TABLE = "education_freedom_account_entry_type"
TYPE_VALUE_TABLE = "education_freedom_account_entry_type_value"
ENTRY_TABLE = "education_freedom_account_entry"
TYPE_FK = "education_freedom_account_entry_type_id_fk"

# Layout of the workbook: entry type names in row 3 (0-indexed 1) from column G on, every
# other column; each type's per-student amount sits two rows down, one column to the right.
# Towns are the rows with an integer location number in column E.
FIRST_TYPE_COLUMN = 6
TYPE_ROW = 1
AMOUNT_ROW = 3
TOWN_COLUMN = 4


def clean_value(value) -> Optional[Decimal]:
    """A cell as a number: $, commas and other symbols removed; blank cells are None."""
    if pd.isna(value) or value == "":
        return None
    cleaned = re.sub(r"[^0-9.-]", "", str(value))
    # Anything that isn't a plain number after cleaning (e.g. "-") raises
    return Decimal(cleaned) if cleaned != "" else None


def parse_year(df: pd.DataFrame) -> tuple:
    """
    The entry types in one year's workbook and the town entries, in file order.

    Returns ([(name, amount)], [(town_id, name, value)]). A type whose amount cell is
    blank (e.g. the totals and payment columns) is not an entry type. Blank cells in
    town rows are skipped.
    """
    types, type_columns = [], []
    for col in range(FIRST_TYPE_COLUMN, len(df.columns) - 1, 2):
        name = df.iloc[TYPE_ROW, col]
        if pd.isna(name) or name == "":
            continue
        amount = clean_value(df.iloc[AMOUNT_ROW, col + 1])
        if amount is not None:
            types.append((str(name).strip(), amount))
            type_columns.append((str(name).strip(), col))

    entries = []
    for _, row in df.iterrows():
        town_id = row.iloc[TOWN_COLUMN]
        if pd.notna(town_id) and isinstance(town_id, (int, float)) and town_id == int(town_id):
            for name, col in type_columns:
                value = clean_value(row.iloc[col])
                if value is not None:
                    entries.append((int(town_id), name, value))
    return types, entries


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """
    Load the given years (default: every configured year) into the three EFA tables.

    Entry types are matched by name. A type not yet in the table gets the next id
    explicitly, as the original migration numbered them (1, 2, ... in order of first
    appearance); the id sequence is never used.
    """
    config = load_config(CONFIG)
    known_towns = existing_ids(conn, "town")
    type_ids = lookup_ids(conn, TYPE_TABLE)
    next_id = max(type_ids.values(), default=0) + 1

    type_rows, type_value_rows, entry_rows, unknown_towns = {}, [], [], set()
    for year in configured_years(config["file_settings"], years):
        types, entries = parse_year(pd.read_excel(year_file(config["file_settings"], year)))
        for name, amount in types:
            if name not in type_ids:
                type_ids[name] = next_id
                next_id += 1
            type_rows[name] = (type_ids[name], name, name)
            type_value_rows.append((type_ids[name], year, amount))
        # Entries take their type's id by name (the original used the type's position in each
        # year's file, which is the same for every file so far)
        for town_id, name, value in entries:
            if town_id in known_towns:
                entry_rows.append((town_id, year, type_ids[name], value))
            else:
                unknown_towns.add((year, town_id))

    if unknown_towns:
        # Towns missing from the town table are skipped, as the original migration did
        town_ids = sorted({town_id for _, town_id in unknown_towns})
        logger.warning(f"Skipped {len(unknown_towns)} town-years for {len(town_ids)} towns "
                       f"not in the town table: {town_ids}")

    return {
        TYPE_TABLE: upsert_rows(conn, TYPE_TABLE, ("id", "name", "description"), ("id",),
                                sorted(type_rows.values())),
        TYPE_VALUE_TABLE: upsert_rows(conn, TYPE_VALUE_TABLE, (TYPE_FK, "year", "value"), (TYPE_FK, "year"),
                                      type_value_rows),
        ENTRY_TABLE: upsert_rows(conn, ENTRY_TABLE, ("town_id_fk", "year", TYPE_FK, "value"),
                                 ("town_id_fk", "year", TYPE_FK), entry_rows),
        "views_refreshed": refresh_dependent_views(conn, ENTRY_TABLE),
    }
