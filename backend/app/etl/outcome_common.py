"""Parsing helpers shared by the outcome loaders (early exit, post-graduation, graduation cohort)."""
import logging
import re
from typing import Optional

import pandas as pd
from sqlalchemy import text
from sqlalchemy.engine import Connection

from app.etl.core import known_school_ids

logger = logging.getLogger("app.etl")


def cell(row: pd.Series, position: int):
    """The value at a column position, or None when the row is shorter."""
    return row.iloc[position] if len(row) > position else None


def clean_numeric(value):
    """A cell as a float with any non-numeric characters stripped ("12.5%" -> 12.5), else None."""
    if pd.isna(value) or value == "":
        return None
    if isinstance(value, (int, float)):
        return float(value)
    cleaned = re.sub(r"[^0-9.-]", "", str(value))
    try:
        return float(cleaned) if cleaned else None
    except ValueError:
        return None


class Schools:
    """
    Finds rows' schools in the school table, fetched once, and collects what it could not match.

    Names are matched as lower(trim(name)). The original loaders used
    "WHERE lower(trim(name)) = ... LIMIT 1", which returns the first match in table order,
    so for a name shared by several schools the first one in table order is used here too.
    """

    def __init__(self, conn: Connection):
        self.ids = known_school_ids(conn)
        self.names, self.shared_names = {}, set()
        for name, school_id in conn.execute(text("SELECT lower(trim(name)), id FROM school ORDER BY ctid")):
            if name in self.names:
                self.shared_names.add(name)
            else:
                self.names[name] = school_id
        self.unknown = set()
        self.shared_matched = set()

    def by_id(self, school_id: Optional[int], year: int) -> Optional[int]:
        if school_id in self.ids:
            return self.ids[school_id]
        self.unknown.add((year, school_id))
        return None

    def by_name(self, name: str, year: int) -> Optional[int]:
        key = name.lower()
        if key in self.shared_names:
            self.shared_matched.add(name)
        if key in self.names:
            return self.names[key]
        self.unknown.add((year, name))
        return None

    def warn(self, dataset: str, repeated: int, no_values: int) -> None:
        """One warning for the rows skipped as unknown, repeated or empty, as the original loaders did."""
        if self.unknown or repeated or no_values:
            schools = sorted({str(school) for _, school in self.unknown})
            logger.warning(f"{dataset}: skipped {len(self.unknown)} school-years for {len(schools)} schools not "
                           f"in the school table {schools}, {repeated} repeated school rows within a year, "
                           f"{no_values} school rows without values")
        if self.shared_matched:
            logger.warning(f"{dataset}: matched names shared by several schools to the first one: "
                           f"{sorted(self.shared_matched)}")
