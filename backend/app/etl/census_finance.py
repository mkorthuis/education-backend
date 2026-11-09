"""
School system revenue by state, from the Census Bureau's Annual Survey of School System Finances
(see census_finance_config.yaml): each state's revenue from federal, state and local sources by
item (Title I, property taxes, ...), into census_state_revenue, and the fall enrollment Census uses
for its per-pupil amounts, into census_state_enrollment. Amounts are thousand dollars, as Census
publishes them.

`fetch` downloads each year's school-system file and summary tables, adds the school systems up by
state, checks each state's federal, state and local totals against Census's Table 1, and saves the
state figures under assets/census-finance/; `load` reads those files.
"""
import hashlib
import json
import logging
import os
import re
import tempfile
import warnings
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from typing import Iterable, List, Optional
from urllib.request import urlopen

import pandas as pd
from sqlalchemy.engine import Connection

from app.etl.core import config_path, configured_years, load_config, lookup_ids, upsert_rows

logger = logging.getLogger("app.etl")

CONFIG = "census_finance_config.yaml"
SOURCES = ("federal", "state", "local")
# Each source's items sit between these columns in the school-system file's header
SOURCE_COLUMNS = {"federal": ("TFEDREV", "TSTREV"), "state": ("TSTREV", "TLOCREV"), "local": ("TLOCREV", "TOTALEXP")}
REVENUE_TABLE = "census_state_revenue"
ENROLLMENT_TABLE = "census_state_enrollment"
PARALLEL_DOWNLOADS = 4
# Census's mark for "not applicable" in its tables: the District of Columbia's state revenue, since
# DC has no separate state government
NOT_APPLICABLE = "(X)"


def file_name(year: int) -> str:
    return f"census-finance-{year}.json"


def _download(url: str, path: str) -> str:
    """Save a file and return its SHA-256."""
    with urlopen(url, timeout=600) as response:
        data = response.read()
    with open(path, "wb") as f:
        f.write(data)
    return hashlib.sha256(data).hexdigest()


def read_district_file(path: str) -> pd.DataFrame:
    """Every school system's data items, as text. The text files end each row with a comma."""
    if path.endswith(".txt"):
        return pd.read_csv(path, index_col=False, dtype=str, encoding="latin-1", keep_default_na=False)
    return pd.read_excel(path, dtype=str, keep_default_na=False)


def state_revenue(df: pd.DataFrame, config: dict) -> dict:
    """{place code: {item code: thousand dollars}} for every state and the nation, adding up the school
    systems. Items in excluded_items are left out."""
    header = list(df.columns)
    items, excluded = config["items"], set(config["excluded_items"])
    codes = []
    for source, (start, end) in SOURCE_COLUMNS.items():
        for code in header[header.index(start) + 1: header.index(end)]:
            if code in excluded:
                continue
            if code not in items:
                raise ValueError(f"Revenue item {code} isn't in {CONFIG}")
            if items[code]["source"] != source:
                raise ValueError(f"Revenue item {code} is {source} revenue in the file, {items[code]['source']} in {CONFIG}")
            codes.append(code)

    unknown = sorted(set(df["STATE"]) - set(config["states"]))
    if unknown:
        raise ValueError(f"State codes not in {CONFIG}: {unknown}")
    # Census's state codes are alphabetical, not FIPS; check them against the systems' NCES ids
    prefixes = df[df["NCESID"].str.len() >= 2].assign(prefix=lambda d: d["NCESID"].str[:2]).groupby("STATE")["prefix"]
    for state, found in prefixes.agg(lambda s: Counter(s).most_common(1)[0][0]).items():
        if found != config["states"][state]["fips"]:
            raise ValueError(f"State code {state} looks like FIPS {found}, not {config['states'][state]['fips']}")

    amounts = df[codes].apply(pd.to_numeric, errors="raise").groupby(df["STATE"]).sum()
    revenue = {config["states"][state]["code"]: {code: int(row[code]) for code in codes} for state, row in amounts.iterrows()}
    revenue[config["nation"]["code"]] = {code: int(amounts[code].sum()) for code in codes}
    return revenue


def _label(value) -> str:
    """A table row's place name without its dot leaders and footnote numbers."""
    return re.sub(r"[\s.\d]+$", "", str(value).strip())


def _places(config: dict) -> dict:
    """{name in the tables: place code}"""
    places = {state["name"]: state["code"] for state in config["states"].values()}
    places[config["nation"]["name"]] = config["nation"]["code"]
    return places


def _table(path: str, sheet: str) -> tuple:
    """A summary table, its rows by place code, and the row where the places start."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        df = pd.read_excel(path, sheet_name=sheet, header=None)
    first = next(i for i, value in enumerate(df.iloc[:, 0]) if _label(value) == "United States")
    return df, first


def _heading(df: pd.DataFrame, column: int, first: int) -> str:
    return " ".join(str(v) for v in df.iloc[:first, column] if str(v) != "nan").lower()


def _rows(df: pd.DataFrame, first: int, config: dict) -> dict:
    places = _places(config)
    rows = {places[_label(row[0])]: row for row in df.iloc[first:].itertuples(index=False) if _label(row[0]) in places}
    missing = sorted(set(places.values()) - set(rows))
    if missing:
        raise ValueError(f"Places missing from the table: {missing}")
    return rows


def _amount(value) -> int:
    """A table cell as a whole number; "not applicable" is none"""
    return 0 if str(value).strip() == NOT_APPLICABLE else int(value)


def published_totals(path: str, config: dict) -> dict:
    """{place code: {source: thousand dollars}} from Table 1."""
    df, first = _table(path, config["summary_sheet"])
    for source, column in config["summary_columns"].items():
        if source not in _heading(df, column, first):
            raise ValueError(f"Table 1 column {column} isn't {source} revenue: {_heading(df, column, first)!r}")
    return {code: {source: _amount(row[column]) for source, column in config["summary_columns"].items()}
            for code, row in _rows(df, first, config).items()}


def published_enrollment(path: str, sheet: str, year: int, config: dict) -> dict:
    """{place code: fall enrollment} from the population, enrollment and income table."""
    df, first = _table(path, sheet)
    column = config["enrollment_column"]
    heading = _heading(df, column, first)
    if "enrollment" not in heading or str(year) not in heading:
        raise ValueError(f"Column {column} of table {sheet} isn't {year} enrollment: {heading!r}")
    return {code: int(row[column]) for code, row in _rows(df, first, config).items()}


def check(revenue: dict, totals: dict, year: int, config: dict) -> None:
    """Each place's federal, state and local totals must equal Census's Table 1, apart from the
    Table 1 cells the config lists as wrong."""
    sources = {code: item["source"] for code, item in config["items"].items()}
    errors = (config.get("table_1_errors") or {}).get(year, {})
    differences = []
    for place, published in totals.items():
        for source in SOURCES:
            added = sum(amount for code, amount in revenue[place].items() if sources[code] == source)
            if errors.get(place, {}).get(source) == published[source]:
                logger.warning(f"Census {year}: Table 1's {place} {source} revenue ({published[source]}) is a known error; "
                               f"the school systems add up to {added}")
                continue
            if added != published[source]:
                differences.append(f"{place} {source}: {added} added up, {published[source]} published")
    if differences:
        raise ValueError("School-system sums don't match Census's Table 1: " + "; ".join(differences[:10]))


def _write(path: str, year: int, files: List[dict], revenue: dict, enrollment: dict) -> None:
    """A saved year: where it came from, each place's enrollment, then one place's revenue per line."""
    header = json.dumps({"source": "U.S. Census Bureau, Annual Survey of School System Finances", "year": year,
                         "fetched": date.today().isoformat(), "files": files,
                         "checked": "Each place's federal, state and local totals equal Census's Table 1",
                         "units": "thousand dollars", "enrollment": enrollment})
    lines = ",\n".join(f'"{place}":{json.dumps(items, separators=(",", ":"))}' for place, items in revenue.items())
    with open(path, "w") as f:
        f.write(f'{header[:-1]}, "revenue": {{\n{lines}\n}}}}\n')


def fetch_year(year: int, config: dict, directory: str) -> int:
    settings = config["years"][year]
    base = config["source_url"].format(year=year)
    with tempfile.TemporaryDirectory() as scratch:
        names = (settings["district_file"], settings["tables_file"])
        with ThreadPoolExecutor(2) as pool:
            hashes = list(pool.map(lambda name: _download(base + name, os.path.join(scratch, name)), names))
        files = [{"name": name, "url": base + name, "sha256": sha} for name, sha in zip(names, hashes)]
        district = read_district_file(os.path.join(scratch, settings["district_file"]))
        tables = os.path.join(scratch, settings["tables_file"])
        revenue = state_revenue(district, config)
        check(revenue, published_totals(tables, config), year, config)
        enrollment = published_enrollment(tables, settings["enrollment_sheet"], year, config)
    _write(os.path.join(directory, file_name(year)), year, files, revenue, enrollment)
    logger.info(f"Census school finance {year}: {len(district)} school systems, {len(revenue)} places, totals match Table 1")
    return len(revenue)


def fetch(years: Optional[Iterable[int]] = None) -> dict:
    """Download and save the given years (default: every configured year)."""
    config = load_config(CONFIG)
    years = configured_years(config["file_settings"], years)
    directory = config_path(config["file_settings"]["directory"])
    os.makedirs(directory, exist_ok=True)
    with ThreadPoolExecutor(PARALLEL_DOWNLOADS) as pool:
        places = list(pool.map(lambda year: fetch_year(year, config, directory), years))
    return {file_name(year): count for year, count in zip(years, places)}


def read_file(path: str) -> dict:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Census school finance file not found: {path}; run `python -m app.etl fetch census-finance`")
    with open(path) as f:
        return json.load(f)


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the given years (default: every configured year), adding the places and revenue items."""
    config = load_config(CONFIG)
    years = configured_years(config["file_settings"], years)
    directory = config_path(config["file_settings"]["directory"])

    places = [(state["code"], state["name"], "state") for state in config["states"].values()]
    places.append((config["nation"]["code"], config["nation"]["name"], "nation"))
    counts = {
        "jurisdiction": upsert_rows(conn, "jurisdiction", ("code", "name", "kind"), ("code",), places),
        "census_revenue_item": upsert_rows(
            conn, "census_revenue_item", ("code", "name", "source", "category", "display_order"), ("code",),
            [(code, item["name"], item["source"], item["category"], order)
             for order, (code, item) in enumerate(config["items"].items(), start=1)]),
    }
    place_ids = lookup_ids(conn, "jurisdiction", "code")
    item_ids = lookup_ids(conn, "census_revenue_item", "code")

    revenue_rows, enrollment_rows = [], []
    for year in years:
        saved = read_file(os.path.join(directory, file_name(year)))
        for place, items in saved["revenue"].items():
            revenue_rows.extend((year, place_ids[place], item_ids[code], amount) for code, amount in items.items())
        enrollment_rows.extend((year, place_ids[place], students) for place, students in saved["enrollment"].items())
    revenue_rows.sort()
    enrollment_rows.sort()
    counts[REVENUE_TABLE] = upsert_rows(conn, REVENUE_TABLE, ("year", "jurisdiction_id_fk", "census_revenue_item_id_fk", "amount_thousands"),
                                        ("year", "jurisdiction_id_fk", "census_revenue_item_id_fk"), revenue_rows)
    counts[ENROLLMENT_TABLE] = upsert_rows(conn, ENROLLMENT_TABLE, ("year", "jurisdiction_id_fk", "enrollment"),
                                           ("year", "jurisdiction_id_fk"), enrollment_rows)
    return counts
