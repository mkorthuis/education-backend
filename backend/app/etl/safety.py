"""
School safety data from the state's yearly safety workbooks: restraints and seclusions,
harassment, bullying, discipline, serious safety incidents and truancy.

Loads the ten school_* safety tables. The state_* and district_* totals summed from them
(first built by migrations 8ed3c152c0c4 and aed3c152c0c6) are rebuilt for the loaded years
when run from the command.
"""
import logging
from typing import Iterable, Optional

import pandas as pd
from sqlalchemy import text
from sqlalchemy.engine import Connection

from app.etl.core import (
    configured_years, existing_ids, load_config, lookup_ids, refresh_dependent_views, upsert_rows, year_file
)

logger = logging.getLogger("app.etl")

CONFIG = "generate_school_safety_data.yaml"

# School table -> (its type table without prefix, value columns). The type tables were created
# as school_<type> (99baf2d34ef7) and renamed to safety_<type> (bed3c152c0c7); the id columns
# pointing at them kept their school_<type>_id_fk names.
TABLES = {
    "school_truancy": (None, ("count",)),
    "school_safety": ("safety_type", ("count",)),
    "school_discipline_incident": ("discipline_incident_type", ("count",)),
    "school_discipline_count": ("discipline_count_type", ("count",)),
    "school_bullying": ("bullying_type", ("reported", "investigated_actual")),
    "school_bullying_classification": ("bullying_classification_type", ("count",)),
    "school_bullying_impact": ("bullying_impact_type", ("count",)),
    "school_harassment": ("harassment_classification", ("incident_count", "student_impact_count",
                                                        "student_engaged_count")),
    "school_restraint": (None, ("generated", "active_investigation", "closed_investigation",
                                "bodily_injury", "serious_injury")),
    "school_seclusion": (None, ("generated", "active_investigation", "closed_investigation")),
}

# school_safety keeps only counts above zero; every other table stores zeros too. This is how
# the data was first loaded and is pending a decision (review item S7), so keep it as is.
SKIP_ZERO_COUNTS = {"school_safety"}


def _typed(table: str, offset: int, names: list) -> list:
    """One output per type name, each reading the column after the previous one."""
    return [(table, name, (offset + i,)) for i, name in enumerate(names)]


# The kinds of sheet, matched by keyword in this order, and the rows each sheet row gives, in
# insert order: (table, type name, value column offsets from the school id column). An offset
# of None stores 0.
SHEETS = {
    "truancy": [("school_truancy", None, (3,))],
    # Incidents, students impacted and students engaged sit five columns apart
    "harassment": [("school_harassment", name, (offset, offset + 5, offset + 10)) for offset, name in enumerate([
        "Gender", "Sexual Orientation", "Race, Color or National Origin", "Disability",
        "Physical Characteristics (other than race)",
    ], start=3)],
    # Reported and investigated sit two columns apart
    "bullying": [("school_bullying", name, (offset, offset + 2))
                 for offset, name in enumerate(["Bullying (of any kind)", "Cyber-bullying"], start=3)]
    + _typed("school_bullying_classification", 7, [
        "Gender", "Sexual Orientation", "Race, Color or National Origin", "Disability",
        "Physical Characteristics", "Any Other Basis",
    ])
    + _typed("school_bullying_impact", 13, [
        "Were a Single Significant Event", "Were a Pattern of Deliberate Harmful Events",
        "Included Physical Harm", "Included Property Damage", "Used Social/ Emotional Alienation",
        "Interfered with Educational Opportunities", "Disrupted School Operations",
    ]),
    "restraint": [("school_restraint", None, (3, 4, 5, 6, 7)), ("school_seclusion", None, (8, 9, 10))],
    "discipline": _typed("school_discipline_incident", 3, [
        "Violent Incidents With Physical Injury Requiring Professional Medical Attention",
        "Violent Incidents, including Harassment & Bullying (Without Physical Injury)",
        "Weapons Possession", "Illicit Drugs", "Alcohol",
        "Other Incidents Related to Drug or Alcohol Use, Violence or Weapons Possession",
        "Disruption", "Defiance", "Inappropriate Language", "All Other Incidents",
    ])
    + _typed("school_discipline_count", 13, [
        "Who Received In-School Suspensions", "Who Received Out-of-School Suspensions", "Who Were Expelled",
    ]),
    "safety": _typed("school_safety", 3, [
        "Handgun Incidents", "Rifles/ Shotguns Incidents",
        "Firearms Incidents Including More Than One Type of Weapon or Firearm", "Other Firearms Incidents",
        "Homicides", "First Degree Assaults", "Aggravated Felonious Sexual Assaults", "Arsons", "Robberies",
        "Firearms Possessions or Sales",
    ]),
}

# 2016 has no serious injury column, so the seclusion columns start one earlier
SHEETS_2016 = {**SHEETS, "restraint": [("school_restraint", None, (3, 4, 5, 6, None)),
                                       ("school_seclusion", None, (7, 8, 9))]}


def type_column(type_table: str) -> str:
    return f"school_{type_table}_id_fk"


def key_columns(table: str) -> tuple:
    """The table's unique key: school, year and, for typed tables, the type."""
    type_table, _ = TABLES[table]
    return ("school_id_fk", "year") + ((type_column(type_table),) if type_table else ())


def resolve_types(sheets: dict, type_ids: dict) -> dict:
    """The sheet layouts with type names replaced by their ids; a name missing from its type table raises."""
    missing = [(table, name) for outputs in sheets.values() for table, name, _ in outputs
               if name is not None and name not in type_ids[table]]
    if missing:
        raise ValueError(f"Types missing from the type tables: {missing}")
    return {kind: [(table, None if name is None else type_ids[table][name], offsets) for table, name, offsets in outputs]
            for kind, outputs in sheets.items()}


def clean_count(value) -> int:
    """A cell as an integer, read the way the original migration did: digits and dots only, otherwise 0."""
    if pd.isna(value):
        return 0
    digits = "".join(c for c in str(value).strip() if c.isdigit() or c == ".")
    try:
        return int(float(digits))
    except ValueError:
        return 0


def find_sheets(workbook: pd.ExcelFile, path: str) -> dict:
    """Sheet name for each kind of data, matched by keyword (some years spell it "Harrassment")."""
    found = {}
    for sheet_name in workbook.sheet_names:
        name = sheet_name.lower().replace("harrassment", "harassment")
        kind = next((kind for kind in SHEETS if kind in name), None)
        if kind is None:
            continue
        if kind in found:
            raise ValueError(f"{path}: sheets {found[kind]!r} and {sheet_name!r} both look like {kind} data")
        found[kind] = sheet_name
    missing = [kind for kind in SHEETS if kind not in found]
    if missing:
        raise ValueError(f"{path}: no sheet found for {missing} (sheets: {workbook.sheet_names})")
    return found


def parse_sheet(df: pd.DataFrame, sheet_name: str, outputs: list, year: int,
                known_schools: set, unknown_schools: set) -> list:
    """
    (table, row) pairs from one sheet, in sheet order.

    The header row has "SAU" in its first column and the school id column is the first one
    whose header mentions "school"; the counts are found by offset from it. Rows without a
    school id (blank and note rows) are skipped, and so are schools missing from the school
    table (collected in unknown_schools).
    """
    header = next((i for i, value in enumerate(df.iloc[:, 0]) if isinstance(value, str) and "sau" in value.lower()),
                  None)
    if header is None:
        raise ValueError(f"{year} sheet {sheet_name!r}: no header row with 'SAU' in the first column")
    school_column = next((i for i, value in enumerate(df.iloc[header]) if isinstance(value, str)
                          and "school" in value.lower()), None)
    if school_column is None:
        raise ValueError(f"{year} sheet {sheet_name!r}: no school id column in the header row")
    last_offset = max(offset for _, _, offsets in outputs for offset in offsets if offset is not None)
    if school_column + last_offset >= df.shape[1]:
        raise ValueError(f"{year} sheet {sheet_name!r}: expected {last_offset} columns after the school id column, "
                         f"found {df.shape[1] - school_column - 1}")

    rows = []
    for _, row in df.iloc[header + 1:].iterrows():
        school_id = clean_count(row.iloc[school_column])
        if school_id == 0:
            continue
        if school_id not in known_schools:
            unknown_schools.add((year, school_id))
            continue
        counts = [clean_count(value) for value in row.iloc[school_column:]]
        for table, type_id, offsets in outputs:
            values = tuple(0 if offset is None else counts[offset] for offset in offsets)
            rows.append((table, (school_id, year) + ((type_id,) if type_id is not None else ()) + values))
    return rows


def rebuild_totals(conn: Connection, years: list) -> dict:
    """
    Rebuild the years' state_* and district_* totals from the school rows.

    Same sums as migrations 8ed3c152c0c4 (state) and aed3c152c0c6 (district). The years'
    total rows are deleted and inserted again, so they get new ids.
    """
    counts = {}
    for school_table, (type_table, values) in TABLES.items():
        type_columns = [type_column(type_table)] if type_table else []
        sums = [f"SUM(t.{c})" for c in values]
        name = school_table.removeprefix("school_")
        for level, level_keys, join in (
            ("state", [], ""),
            ("district", ["s.district_id_fk"], "JOIN school s ON t.school_id_fk = s.id"),
        ):
            table = f"{level}_{name}"
            keys = level_keys + ["t.year"] + [f"t.{c}" for c in type_columns]
            columns = [key.split(".")[1] for key in keys] + list(values)
            deleted = conn.execute(text(f"DELETE FROM {table} WHERE year = ANY(:years)"), {"years": years}).rowcount
            inserted = conn.execute(text(f"""
                INSERT INTO {table} ({", ".join(columns)})
                SELECT {", ".join(keys + sums)}
                FROM {school_table} t {join}
                WHERE t.year = ANY(:years)
                GROUP BY {", ".join(keys)}
            """), {"years": years}).rowcount
            counts[table] = {"deleted": deleted, "inserted": inserted}
            logger.info(f"{table}: {deleted} deleted, {inserted} inserted")
    return counts


def load(
    conn: Connection,
    years: Optional[Iterable[int]] = None,
    type_table_prefix: str = "safety_",
    rebuild_state_district: bool = True,
) -> dict:
    """
    Load the given years (default: every configured year) into the school_* safety tables.

    The data migration runs before the type tables are renamed and before the state and
    district tables exist, so it passes type_table_prefix="school_" and
    rebuild_state_district=False. The command uses the defaults: current table names, and
    the loaded years' state/district totals rebuilt. Materialized views on these tables are
    refreshed when they exist (not yet during the data migration).
    """
    config = load_config(CONFIG)
    known_schools = existing_ids(conn, "school")

    type_ids = {table: lookup_ids(conn, type_table_prefix + type_table)
                for table, (type_table, _) in TABLES.items() if type_table}

    years = configured_years(config["file_settings"], years)
    rows = {table: [] for table in TABLES}
    unknown_schools, zero_counts = set(), 0
    for year in years:
        sheets = resolve_types(SHEETS_2016 if year == 2016 else SHEETS, type_ids)
        path = year_file(config["file_settings"], year)
        workbook = pd.ExcelFile(path)
        for kind, sheet_name in find_sheets(workbook, path).items():
            df = pd.read_excel(workbook, sheet_name=sheet_name)
            for table, row in parse_sheet(df, sheet_name, sheets[kind], year, known_schools, unknown_schools):
                if table in SKIP_ZERO_COUNTS and row[-1] <= 0:
                    zero_counts += 1
                    continue
                rows[table].append(row)

    if unknown_schools:
        # Schools missing from the school list are skipped, as the original migration did
        school_ids = sorted({school_id for _, school_id in unknown_schools})
        logger.warning(f"Skipped {len(unknown_schools)} school-years for {len(school_ids)} schools "
                       f"not in the school table: {school_ids}")
    logger.info(f"school_safety: {zero_counts} zero counts not stored")

    counts = {table: upsert_rows(conn, table, key_columns(table) + TABLES[table][1], key_columns(table), table_rows)
              for table, table_rows in rows.items()}
    if rebuild_state_district:
        counts["state_district_totals"] = rebuild_totals(conn, years)
    counts["views_refreshed"] = [view for table in TABLES for view in refresh_dependent_views(conn, table)]
    return counts
