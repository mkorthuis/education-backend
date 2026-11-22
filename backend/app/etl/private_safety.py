"""
Restraints and seclusions at private (nonpublic) schools, from NHED's restraint and seclusion
reports, into private_school_restraint_seclusion.

Kept apart from school_restraint and school_seclusion on purpose. Those tables are the public
schools' (from the School Safety Data Collection, which lists no private school), and the state and
district totals, the safety enrollment views and the Ask's statewide rates are sums over every row
in them. Private schools report their own figures, where the public schools' are certified by
superintendents, and the reports carry each school's enrollment.

Each year is a CSV copied from that year's PDF report (see private_school_restraint_seclusion_config.yaml),
and must add up to the report's printed nonpublic totals before anything is written.
"""
import logging
from typing import Iterable, Optional

import pandas as pd
from sqlalchemy.engine import Connection

from app.etl.core import configured_years, known_school_ids, load_config, upsert_rows, whole_number, year_file

logger = logging.getLogger("app.etl")

CONFIG = "private_school_restraint_seclusion_config.yaml"
TABLE = "private_school_restraint_seclusion"
# The report's columns, in the CSVs and the table alike
COUNTS = (
    "restraint_reports", "restraints_bodily_harm", "restraints_serious_injury_or_death",
    "restraint_investigations_active", "restraint_investigations_closed",
    "seclusion_reports", "seclusion_investigations_active", "seclusion_investigations_closed",
)
VALUES = ("enrollment", *COUNTS)


def check_totals(df: pd.DataFrame, expected: dict, path: str) -> None:
    """Stop the load when a year's rows don't add up to its report's printed totals."""
    wrong = {column: (int(df[column].fillna(0).sum()), total) for column, total in expected.items()
             if int(df[column].fillna(0).sum()) != total}
    if wrong:
        raise ValueError(f"{path}: rows don't add up to the report's totals (rows, report): {wrong}")


def parse_year(df: pd.DataFrame, year: int, known_schools: dict, path: str) -> tuple:
    """
    Rows of (school_id, year, enrollment, *counts) from one year's CSV, the school-years not in the
    school table, and the schools that reported no counts.

    Ids go through known_school_ids, so a renumbered school's earlier rows load under its current
    id. A row with no number in any count cell isn't stored: as for the public schools, a missing
    row means no data, never zero incidents. A school listed twice stops the load.
    """
    rows, seen, unknown, not_reported = [], set(), set(), set()
    for record in df.to_dict("records"):
        if whole_number(record["year"]) != year:
            raise ValueError(f"{path}: a row for {record['year']} in the {year} file")
        state_id = whole_number(record["school_id"])
        school_id = known_schools.get(state_id)
        if school_id is None:
            unknown.add((year, state_id))
            continue
        if school_id in seen:
            raise ValueError(f"{path}: school {school_id} listed twice")
        seen.add(school_id)
        values = [whole_number(record[column]) for column in VALUES]
        if all(value is None for value in values[1:]):
            not_reported.add((year, school_id))
            continue
        rows.append((school_id, year, *values))
    return rows, unknown, not_reported


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the given years (default: every configured year) into private_school_restraint_seclusion."""
    config = load_config(CONFIG)
    known_schools = known_school_ids(conn)
    rows, unknown, not_reported = [], set(), set()
    for year in configured_years(config["file_settings"], years):
        path = year_file(config["file_settings"], year)
        df = pd.read_csv(path)
        check_totals(df, config["expected_totals"][year], path)
        year_rows, year_unknown, year_not_reported = parse_year(df, year, known_schools, path)
        rows += year_rows
        unknown |= year_unknown
        not_reported |= year_not_reported

    if unknown:
        # Schools that have closed or aren't on the state's school list, skipped as the public loader skips them
        school_ids = sorted({school_id for _, school_id in unknown})
        logger.warning(f"Skipped {len(unknown)} school-years for {len(school_ids)} schools "
                       f"not in the school table: {school_ids}")
    if not_reported:
        logger.warning(f"Skipped {len(not_reported)} school-years with no counts: {sorted(not_reported)}")

    columns = ("school_id_fk", "year", *VALUES)
    return {TABLE: upsert_rows(conn, TABLE, columns, ("school_id_fk", "year"), rows)}
