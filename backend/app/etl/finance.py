"""
District finances from the DOE-25 annual financial reports (one workbook per district and year).

Loads the entry, category and fund types from the config (their ids are fixed: the frontend
uses them), one doe_form per district and year, its balance sheet, revenue and expenditure
values, and its average daily membership (doe_form_adm).
"""
import logging
import os
from collections import Counter
from typing import Iterable, Optional, Sequence

import openpyxl
import pandas as pd
from sqlalchemy import text
from sqlalchemy.engine import Connection

from app.etl.cache import cached, fingerprint
from app.etl.core import (
    CONFIG_DIR, config_path, configured_years, load_config, refresh_dependent_views, upsert_rows
)

logger = logging.getLogger("app.etl")

CONFIG = "generate_finance_config.yaml"
FORM_TABLE = "doe_form"
FORM_COLUMNS = ("district_id_fk", "year")
ADM_TABLE = "doe_form_adm"
ADM_COLUMNS = ("doe_form_id_fk", "elementary", "middle", "high", "total")

# The three statements of the form: their config section, and the config keys of their
# super-category and category types (entry and fund types are <name>_entry_type and <name>_fund_type)
STATEMENTS = {
    "balance": ("initial_data", "balance_entry_super_category_type", "balance_entry_category_type"),
    "revenue": ("revenue_data", "revenue_super_category_type", "revenue_category_type"),
    "expenditure": ("expenditure_data", "expenditure_super_category_type", "expenditure_category_type"),
}
VALUE_TABLES = {"balance": "balance_sheet", "revenue": "revenue", "expenditure": "expenditure"}

with open(__file__, "rb") as _source, open(os.path.join(CONFIG_DIR, CONFIG), "rb") as _config:
    # Parsed forms are cached; any change to this code, the config or the readers invalidates them
    PARSER_FINGERPRINT = fingerprint(_source.read(), _config.read(), pd.__version__, openpyxl.__version__)


def statement_types(config: dict, name: str) -> dict:
    """The entry, category, super-category and fund type rows of one statement, keyed by table."""
    section, super_category_key, category_key = STATEMENTS[name]
    settings = config[section]
    return {
        f"{name}_entry_super_category_type": (
            ("id", "name"),
            [(id_, type_name) for id_, type_name in settings[super_category_key]]),
        f"{name}_entry_category_type": (
            ("id", "name", f"{name}_entry_super_category_type_id_fk"),
            [tuple(row) for row in settings[category_key]]),
        f"{name}_entry_type": (
            ("id", "name", "page", "line", "account_no", f"{name}_entry_category_type_id_fk"),
            [(e[0], e[1], str(e[2]), str(e[3]), str(e[4]), e[5]) for e in settings[f"{name}_entry_type"]]),
        f"{name}_fund_type": (
            ("id", "state_id", "state_name"),
            [(id_, str(state_id), state_name) for id_, state_id, state_name, _ in settings[f"{name}_fund_type"]]),
    }


def district_file(config: dict, district_name: str, year: int) -> str:
    """A district's DOE-25 workbook for a year, named after the district (e.g. "oyster-river-coop")."""
    slug = (district_name.lower()
            .replace(' school district', '')
            .replace(' (carroll county)', '')
            .replace('oyster river cooperative', 'oyster river coop')
            .replace("'", '')
            .strip()
            .replace(' ', '-'))
    pattern = config["file_settings"]["default_input"]
    return config_path(pattern.replace("****", str(year)).replace("{district}", slug))


def parse_values(df: pd.DataFrame, config: dict, name: str, year: int, skipped: Counter) -> list:
    """
    One statement's values as (entry_type_id, fund_type_id, value), in config order.

    An entry's row is the first whose title (column A), page, line and account number match the
    config; entries limited to other years are not looked up. Blank, zero and non-numeric cells
    (the forms fill unused cells with dots) are skipped. Expenditures are rounded to cents.
    """
    section = config[STATEMENTS[name][0]]
    keys = zip(*(df.iloc[:, i].astype(str).str.strip() for i in (0, 1, 2, 4)))
    positions = {}
    for position, key in enumerate(keys):
        positions.setdefault(key, position)

    values = []
    for entry in section[f"{name}_entry_type"]:
        if len(entry) > 7 and year not in entry[7]:
            continue
        entry_id, _, page, line, account_no, _, title = entry[:7]
        position = positions.get((title.strip(), str(page), str(line), str(account_no) if account_no else 'nan'))
        if position is None:
            skipped[f"{name} lines not found"] += 1
            continue
        for fund_id, _, _, column_letter in section[f"{name}_fund_type"]:
            cell = df.iloc[position, ord(column_letter) - ord('A')]
            if pd.isna(cell):
                continue
            try:
                value = float(str(cell).replace(',', ''))
            except ValueError:
                skipped[f"{name} non-numeric cells"] += 1
                continue
            if value != 0:
                values.append((entry_id, fund_id, round(value, 2) if name == "expenditure" else value))
    return values


def parse_adm(df: pd.DataFrame, skipped: Counter) -> Optional[tuple]:
    """
    Average daily membership (elementary, middle, high, total) from columns F-I of the first
    "AVE DAILY MEMBERSHIP" row; empty cells count as 0. None when the row is missing, or when a
    cell holds text that isn't a number (the original migration left those forms without ADM).
    """
    rows = df[df.iloc[:, 0].astype(str).str.strip().str.lower() == "ave daily membership"]
    if rows.empty:
        skipped["forms without an ADM row"] += 1
        return None
    cells = [rows.iloc[0, i] for i in (5, 6, 7, 8)]
    try:
        return tuple(0.0 if pd.isna(cell) else float(cell.replace(',', '')) if isinstance(cell, str) else float(cell)
                     for cell in cells)
    except ValueError:
        skipped["forms without ADM: text in an ADM cell"] += 1
        return None


def parse_form(path: str, config: dict, district_id: int, year: int, skipped: Counter) -> Optional[dict]:
    """
    One district's DOE-25 for a year: its values per statement and its ADM.

    The district number is in cell B2. When it is blank the file is taken as the district's;
    when it names another district the form is skipped, as the original migration did.
    """
    df = pd.read_excel(path, sheet_name=config["file_settings"]["sheet_name"], engine="openpyxl")
    file_district_id = df.iloc[0, 1]
    if pd.isna(file_district_id):
        skipped["forms without a district number (file name used)"] += 1
    elif int(file_district_id) != district_id:
        # Typos in the file's district number; the form is skipped, as the original migration did
        skipped[f"forms skipped, {os.path.basename(path)} has district number {int(file_district_id)}"] += 1
        return None

    form = {name: parse_values(df, config, name, year, skipped) for name in STATEMENTS}
    form["adm"] = parse_adm(df, skipped)
    return form


def parse_form_cached(path: str, config: dict, district_id: int, year: int, skipped: Counter) -> Optional[dict]:
    """
    parse_form, cached on disk (app.etl.cache): reading the workbooks is most of a finance load.

    The cache key covers the workbook's contents, this module's code, the config file, the
    pandas and openpyxl versions, the district and the year, so any change re-reads the file.
    """
    def compute():
        form_skipped = Counter()
        return {"form": parse_form(path, config, district_id, year, form_skipped), "skipped": dict(form_skipped)}

    result = cached("finance", path, fingerprint(PARSER_FINGERPRINT, district_id, year), compute)
    skipped.update(result["skipped"])
    form = result["form"]
    if form is None:
        return None
    # JSON stores tuples as lists
    form = {name: [tuple(value) for value in values] for name, values in form.items() if name != "adm"} | {
        "adm": tuple(form["adm"]) if form["adm"] is not None else None}
    return form


def delete_other_rows(conn: Connection, table: str, key_columns: Sequence[str], rows: Sequence[tuple],
                      form_ids: Sequence[int]) -> int:
    """
    Delete the rows of the given forms whose key is not in `rows` (e.g. a value that is now zero),
    so a reloaded form holds exactly what its file holds. Generic helper kept here: core has no
    "replace within scope by key" operation that keeps ids of unchanged rows.
    """
    keys = list(zip(*[row[:len(key_columns)] for row in rows])) or [[] for _ in key_columns]
    unnest = ", ".join(f"CAST(:k{i} AS int[])" for i in range(len(key_columns)))
    match = " AND ".join(f"k.c{i} = t.{column}" for i, column in enumerate(key_columns))
    deleted = conn.execute(text(f"""
        DELETE FROM {table} t
        WHERE t.doe_form_id_fk = ANY(:form_ids)
          AND NOT EXISTS (SELECT 1 FROM unnest({unnest}) AS k({", ".join(f"c{i}" for i in range(len(key_columns)))})
                          WHERE {match})
    """), {"form_ids": list(form_ids), **{f"k{i}": list(values) for i, values in enumerate(keys)}}).rowcount
    if deleted:
        logger.info(f"{table}: {deleted} rows no longer in the files deleted")
    return deleted


def rebuild_state_totals(conn: Connection, years: Sequence[int]) -> list:
    """
    Recompute revenue_state_total and expenditure_state_total (sums per entry type and year, built by
    migrations 745adf234bc3 and 49358ad1275f) for the given years. Skipped where those tables don't
    exist yet, or (before 49358ad1275f) when expenditure_state_total is still the older rollup table.
    """
    rebuilt = []
    for name, table in (("revenue", "revenue_state_total"), ("expenditure", "expenditure_state_total")):
        entry_column = f"{name}_entry_type_id_fk"
        if not conn.execute(text(
            "SELECT 1 FROM information_schema.columns WHERE table_name = :table AND column_name = :column"
        ), {"table": table, "column": entry_column}).first():
            continue
        # Same sums as the migrations that built the tables
        totals = f"""
            SELECT et.id AS entry_type_id, df.year, SUM(v.value) AS value
            FROM doe_form df
            JOIN {name} v ON v.doe_form_id_fk = df.id
            JOIN {name}_entry_type et ON v.{entry_column} = et.id
            JOIN {name}_entry_category_type ct ON et.{name}_entry_category_type_id_fk = ct.id
            JOIN {name}_entry_super_category_type st ON ct.{name}_entry_super_category_type_id_fk = st.id
            WHERE df.year = ANY(:years)
            GROUP BY et.id, df.year
        """
        params = {"years": list(years)}
        deleted = conn.execute(text(f"""
            DELETE FROM {table} t WHERE t.year = ANY(:years) AND NOT EXISTS (
                SELECT 1 FROM ({totals}) s WHERE s.entry_type_id = t.{entry_column} AND s.year = t.year)
        """), params).rowcount
        changed = conn.execute(text(f"""
            INSERT INTO {table} ({entry_column}, year, value)
            SELECT entry_type_id, year, value FROM ({totals}) s ORDER BY year, entry_type_id
            ON CONFLICT ({entry_column}, year) DO UPDATE SET value = EXCLUDED.value, date_updated = CURRENT_TIMESTAMP
            WHERE {table}.value IS DISTINCT FROM EXCLUDED.value
        """), params).rowcount
        logger.info(f"{table}: {changed} rows inserted or updated, {deleted} deleted")
        rebuilt.append(table)
    return rebuilt


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the types and the given years (default: every configured year) of DOE-25 forms."""
    config = load_config(CONFIG)
    years = configured_years(config["file_settings"], years)
    districts = conn.execute(text("SELECT id, name FROM district ORDER BY id")).all()

    # Read every form first, in the original order: by year, then district id
    forms, skipped, missing_files = [], Counter(), Counter()
    for year in years:
        found = 0
        for district_id, district_name in districts:
            path = district_file(config, district_name, year)
            if not os.path.exists(path):
                missing_files[year] += 1
                continue
            found += 1
            if os.path.basename(path) in config["file_settings"]["unreadable_files"].get(year, []):
                skipped["unreadable files (see config)"] += 1
                continue
            form = parse_form_cached(path, config, district_id, year, skipped)
            if form is not None:
                forms.append(((district_id, year), form))
        if not found:
            raise FileNotFoundError(f"No DOE-25 files found for {year}: {district_file(config, '<district>', year)}")

    if missing_files:
        # Districts without a file (charter schools, districts that did not exist yet) have no form
        logger.warning(f"DOE-25 files missing for {sum(missing_files.values())} district-years "
                       f"({dict(missing_files)}); skipped")
    if skipped:
        logger.warning("DOE-25 skips: " + "; ".join(f"{reason}: {count}" for reason, count in sorted(skipped.items())))

    counts = {}
    for name in STATEMENTS:
        for table, (columns, rows) in statement_types(config, name).items():
            counts[table] = upsert_rows(conn, table, columns, ("id",), rows)

    counts[FORM_TABLE] = upsert_rows(conn, FORM_TABLE, FORM_COLUMNS, FORM_COLUMNS, [key for key, _ in forms])
    form_ids = {(district_id, year): id_ for district_id, year, id_ in conn.execute(text(
        "SELECT district_id_fk, year, id FROM doe_form WHERE year = ANY(:years)"), {"years": years})}
    loaded_ids = [form_ids[key] for key, _ in forms]

    for name, table in VALUE_TABLES.items():
        columns = ("doe_form_id_fk", f"{name}_entry_type_id_fk", f"{name}_fund_type_id_fk", "value")
        rows = [(form_ids[key], *value) for key, form in forms for value in form[name]]
        counts[table] = upsert_rows(conn, table, columns, columns[:3], rows)
        counts[table]["deleted"] = delete_other_rows(conn, table, columns[:3], rows, loaded_ids)
    adm_rows = [(form_ids[key], *form["adm"]) for key, form in forms if form["adm"] is not None]
    counts[ADM_TABLE] = upsert_rows(conn, ADM_TABLE, ADM_COLUMNS, ADM_COLUMNS[:1], adm_rows)
    counts[ADM_TABLE]["deleted"] = delete_other_rows(conn, ADM_TABLE, ADM_COLUMNS[:1], adm_rows, loaded_ids)

    counts["views_refreshed"] = sorted({view for table in (FORM_TABLE, ADM_TABLE, *VALUE_TABLES.values())
                                        for view in refresh_dependent_views(conn, table)})
    counts["totals_rebuilt"] = rebuild_state_totals(conn, years)
    return counts
