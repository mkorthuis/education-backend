"""
Census Bureau American Community Survey 5-year estimates for New Hampshire's towns, school districts and
the state (see acs_config.yaml):

- acs_topic, acs_annotation, acs_release: the config's lists
- acs_table, acs_variable: the tables loaded and each of their values, from the config, acs_variables.csv
  and Census's labels; acs_variable_release: which releases have each value, and whether it means the
  same in each
- acs_measure: the summary's measures, with what the site shows for them and how each is worked out
- acs_town, acs_district: the Census area each town and district is, by Census's id
- town_acs_estimate, district_acs_estimate, state_acs_estimate: every value for every release, with its
  margin of error, and Census's annotation where it gives a code instead of a number

The API reads materialized views built from them (view_statements): for each level, one per topic with
a column per value and its margin of error ({level}_acs_{topic}), and a summary of the most-used
measures with margins of error and reliability ({level}_acs_summary). load refreshes them.
"""
import csv
import gzip
import json
import logging
import math
import os
import re
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from typing import Iterable, List, Optional
from urllib.error import URLError
from urllib.request import urlopen

from sqlalchemy import text
from sqlalchemy.engine import Connection

from app.etl.core import CONFIG_DIR, config_path, load_config, lookup_ids, refresh_dependent_views, upsert_rows

logger = logging.getLogger("app.etl")

CONFIG = "acs_config.yaml"
VARIABLES = "acs_variables.csv"
LEVELS = ("town", "district", "state")
KEYS = {"town": ("town_id_fk",), "district": ("district_id_fk",), "state": ()}
# Summary levels kept from the summary files: the state, county subdivisions and school districts
SUMMARY_LEVELS = {"040": "state", "060": "town", "950": "elementary", "960": "secondary", "970": "unified"}
DISTRICT_TYPES = ("elementary", "secondary", "unified")
UNITS = ("count", "dollars", "years", "year", "people", "index (0-1)", "percent")
WHOLE_UNITS = ("count", "dollars", "year")  # shown as whole numbers in the views
CONTROLLED = -555555555  # an estimate with no sampling error: its margin of error is 0
COMPARABILITY = ("same", "dollars", "years_move")
MEASURE_KINDS = ("value", "sum", "share")
ESTIMATE_COLUMNS = ("release_year", "variable_id_fk", "estimate", "moe", "estimate_annotation_id_fk", "moe_annotation_id_fk")


def file_name(year: int) -> str:
    return f"acs5-{year}.json.gz"


# -------------------- fetch --------------------

def _open(url: str, attempts: int = 3):
    for attempt in range(1, attempts + 1):
        try:
            return urlopen(url, timeout=120)
        except URLError as e:
            if attempt == attempts:
                raise
            logger.warning(f"{url}: {e}; trying again")


def _number(value: str):
    """A summary file value as a number: an int, a float, or None when it's blank."""
    value = value.strip()
    if not value:
        return None
    return int(value) if re.fullmatch(r"-?\d+", value) else float(value)


def parse_shells(lines: Iterable[str], tables: Iterable[str], pipe: bool) -> dict:
    """{table: {title, universe, five_year, lines: [[unique id or None, indent or None, label]]}} for the
    tables, from a release's table list: pipe-delimited with indents (2021 on), or the 2019 prototype's
    CSV, whose title rows say which releases (1- or 5-year) have the table."""
    wanted, found = set(tables), {}
    if pipe:
        for row in csv.DictReader(lines, delimiter="|"):
            table = row["Table ID"].strip()
            if table not in wanted:
                continue
            entry = found.setdefault(table, {"title": row["Title"], "universe": row["Universe"], "five_year": True, "lines": []})
            entry["lines"].append([row["Unique ID"] or None, int(row["Indent"] or 0), row["Label"].strip()])
        return found
    for row in csv.DictReader(lines):
        table = row["Table ID"].strip()
        if table not in wanted:
            continue
        entry = found.setdefault(table, {"title": None, "universe": None, "five_year": False, "lines": []})
        stub = row["Stub"].strip()
        if row["UniqueID"]:
            entry["lines"].append([row["UniqueID"], None, stub])
        elif stub.startswith("Universe:"):
            entry["universe"] = stub[len("Universe:"):].strip()
        elif entry["title"] is None:
            entry["title"] = stub
            entry["five_year"] = "5" in (row["Data Release"] or "")
    return found


def _state_rows(lines: Iterable[str], state: str) -> tuple:
    """The header and New Hampshire's rows of a table's summary file."""
    prefixes = tuple(f"{level}0000US{state}" for level in SUMMARY_LEVELS)
    header, rows = None, {}
    for line in lines:
        if header is None:
            header = line.rstrip("\r\n").split("|")
            if header[0] != "GEO_ID":
                raise ValueError(f"Not a summary file: it starts {line[:80]!r}")
            continue
        if line.startswith(prefixes):
            values = line.rstrip("\r\n").split("|")
            rows[values[0]] = [_number(v) for v in values[1:]]
    return header[1:], rows


def fetch_release(config: dict, year: int) -> str:
    """Save a release's New Hampshire rows for every table in the config, with its labels."""
    release, state = config["releases"][year], config["state_fips"]
    base = release["base_url"].rstrip("/")
    tables = sorted(config["tables"])
    pipe = release["shells"].endswith(".txt")
    with _open(f"{base}/{release['shells']}") as response:
        shells = parse_shells((line.decode("utf-8" if pipe else "cp1252") for line in response), tables, pipe)
    missing = [table for table in tables if table not in shells]
    if missing:
        raise ValueError(f"{year}: the table list has no {missing}")

    geographies = None
    if release.get("geographies"):
        with _open(f"{base}/{release['geographies']}") as response:
            # The whole of each area (component 00), as the data files have them
            prefixes = tuple(f"{level}0000US{state}" for level in SUMMARY_LEVELS)
            geographies = {row["GEO_ID"]: row["NAME"] for row in csv.DictReader((line.decode("utf-8") for line in response), delimiter="|")
                           if row["GEO_ID"].startswith(prefixes)}

    def fetch_table(table):
        if not shells[table]["five_year"]:
            return table, None, None
        with _open(f"{base}/{release['data'].format(table=table.lower())}") as response:
            columns, rows = _state_rows((line.decode("utf-8") for line in response), state)
        logger.info(f"{year} {table}: {len(rows)} rows")
        return table, columns, rows

    saved = {"release": year, "period": release["period"], "source": base, "fetched": date.today().isoformat(),
             "geographies": geographies, "tables": {}}
    with ThreadPoolExecutor(max_workers=4) as pool:
        for table, columns, rows in pool.map(fetch_table, tables):
            saved["tables"][table] = {**shells[table], "columns": columns, "rows": rows}
    path = os.path.join(config_path(config["directory"]), file_name(year))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with gzip.GzipFile(path, "wb", mtime=0) as f:
        f.write(json.dumps(saved, separators=(",", ":"), sort_keys=True).encode("utf-8"))
    return path


def fetch() -> str:
    """Save every release in the config."""
    config = load_config(CONFIG)
    return ", ".join(fetch_release(config, year) for year in sorted(config["releases"]))


# -------------------- parse --------------------

def read_release(config: dict, year: int) -> dict:
    path = os.path.join(config_path(config["directory"]), file_name(year))
    if not os.path.exists(path):
        raise FileNotFoundError(f"ACS release not found: {path}; run `python -m app.etl fetch acs`")
    with gzip.open(path, "rt", encoding="utf-8") as f:
        return json.load(f)


def read_variables() -> List[dict]:
    """acs_variables.csv: every value loaded, with its column name in the views, unit and description."""
    with open(os.path.join(CONFIG_DIR, VARIABLES), encoding="utf-8") as f:
        variables = list(csv.DictReader(f))
    names = [v["column_name"] for v in variables]
    repeated = sorted({n for n in names if names.count(n) > 1})
    if repeated:
        raise ValueError(f"{VARIABLES}: column names used twice: {repeated}")
    too_long = [n for n in names if len(n) > 59]  # 63, less "_moe"
    if too_long:
        raise ValueError(f"{VARIABLES}: column names over 59 characters: {too_long}")
    units = sorted({v["unit"] for v in variables} - set(UNITS))
    if units:
        raise ValueError(f"{VARIABLES}: units {units} aren't {UNITS}")
    return variables


def label_paths(shell: dict) -> dict:
    """{unique id: its label with the labels it's nested under ("Total > Male > Under 5 years")}."""
    paths, stack = {}, []
    for uid, indent, label in shell["lines"]:
        stack = stack[:indent] + [re.sub(r"\s*(--|:)\s*$", "", label)]
        if uid:
            paths[uid] = " > ".join(stack)
    return paths


def _normalized(label: str, years: bool = False) -> str:
    label = re.sub(r"\b(19|20)\d\d\b", "YEAR", label) if years else label
    return re.sub(r"[^a-z0-9]+", " ", label.lower()).strip()


def comparability(latest: dict, earlier: dict, unit: str, uid: str, table: str) -> Optional[str]:
    """Whether an earlier release's value is the latest's: "same"; "dollars" (the same, in its own year's
    dollars); "years_move" (the same line, its years moved with the release: "Built 2014 or later"); None
    when the earlier release doesn't have it or it means something else."""
    shell = earlier["tables"].get(table)
    if not shell or not shell["five_year"]:
        return None
    labels = {line[0]: line[2] for line in shell["lines"] if line[0]}
    latest_label = next(line[2] for line in latest["tables"][table]["lines"] if line[0] == uid)
    if uid not in labels:
        return None
    if _normalized(labels[uid]) == _normalized(latest_label):
        return "same"
    if _normalized(labels[uid], years=True) == _normalized(latest_label, years=True):
        return "dollars" if unit == "dollars" else "years_move"
    return None


def match_geographies(geographies: dict, towns: dict, districts: dict, config: dict) -> dict:
    """{Census id: (level, our id, district type)} for the state, towns and school districts. towns and
    districts: {name, lower case: id}. A Census area that matches nothing, and isn't in skip_towns or a
    district level's remainder, stops the load."""
    town_aliases = {k.lower(): v.lower() for k, v in (config.get("town_aliases") or {}).items()}
    district_aliases = {k.lower(): v.lower() for k, v in (config.get("district_aliases") or {}).items()}
    skip = {name.lower() for name in config.get("skip_towns") or []}
    matched, unmatched, used = {}, [], {}
    for geo_id, name in sorted(geographies.items()):
        level = SUMMARY_LEVELS[geo_id[:3]]
        if level == "state":
            matched[geo_id] = ("state", None, None)
            continue
        if level == "town":
            short = name.split(",")[0].strip().lower()
            if short in skip:
                continue
            candidate = town_aliases.get(short) or re.sub(r" (town|city)$", "", short)
            town_id = towns.get(candidate)
            if town_id is None:
                unmatched.append(name)
                continue
            matched[geo_id] = ("town", town_id, None)
            continue
        short = re.sub(r", New Hampshire$", "", name).strip()
        if short.startswith("Remainder of"):
            continue
        lower = short.lower()
        district_id = districts.get(district_aliases.get(lower, lower)) or districts.get(re.sub(r" school district$", "", lower))
        if district_id is None:
            unmatched.append(name)
            continue
        if district_id in used:
            raise ValueError(f"{name} and {used[district_id]} both match district {district_id}")
        used[district_id] = name
        matched[geo_id] = ("district", district_id, level)
    if unmatched:
        raise ValueError(f"Census areas that match no town or district: {unmatched}; add them to town_aliases, "
                         f"skip_towns or district_aliases in {CONFIG}")
    return matched


def value_pair(estimate, moe, annotation_ids: dict) -> tuple:
    """(estimate, margin of error, estimate's annotation id, margin's annotation id) from the summary
    file's values, where a code takes the place of a number."""
    estimate_annotation = annotation_ids.get(estimate)
    moe_annotation = annotation_ids.get(moe)
    if estimate_annotation:
        estimate = None
    if moe_annotation:
        moe = 0 if moe == CONTROLLED else None
    return estimate, moe, estimate_annotation, moe_annotation


# -------------------- load --------------------

def _places(conn: Connection) -> tuple:
    towns = {name.lower(): town_id for town_id, name in conn.execute(text("SELECT id, name FROM town")).all()}
    districts = {}
    # A current district wins over a former one of the same name
    for district_id, name in conn.execute(text(
            "SELECT id, name FROM district WHERE kind = 'district' ORDER BY is_current, id")).all():
        districts[name.lower()] = district_id
    return towns, districts


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the config's releases (or those in years): the tables' and values' descriptions, the Census
    areas, and every value. Then refresh the views built on them."""
    config = load_config(CONFIG)
    configured = sorted(config["releases"])
    years = sorted(set(years or configured))
    unknown = [year for year in years if year not in configured]
    if unknown:
        raise ValueError(f"Releases {unknown} aren't in {CONFIG}: {configured}")
    latest_year = configured[-1]
    releases = {year: read_release(config, year) for year in sorted(set(years) | {latest_year})}
    latest = releases[latest_year]
    variables = read_variables()

    # Every line of every table is listed in acs_variables.csv, and every value listed is in the latest release
    listed = {v["variable"] for v in variables}
    lines = {uid for table in config["tables"] for uid, _, _ in latest["tables"][table]["lines"] if uid}
    if listed != lines:
        raise ValueError(f"{VARIABLES} and the tables' lines differ: not listed {sorted(lines - listed)[:10]}, "
                         f"not in the tables {sorted(listed - lines)[:10]}")

    topics = {topic["code"]: topic_id for topic_id, topic in config["topics"].items()}
    counts = {
        "acs_topic": upsert_rows(conn, "acs_topic", ("id", "code", "name"), ("id",),
                                 [(i, t["code"], t["name"]) for i, t in sorted(config["topics"].items())]),
        "acs_annotation": upsert_rows(conn, "acs_annotation", ("id", "code", "name"), ("id",),
                                      [(i, a["code"], a["name"]) for i, a in sorted(config["annotations"].items())]),
        "acs_release": upsert_rows(conn, "acs_release", ("year", "period", "dollars_year", "source_url"), ("year",),
                                   [(year, str(r["period"]), year, r["base_url"]) for year, r in sorted(config["releases"].items())]),
    }
    unknown = sorted({t["topic"] for t in config["tables"].values()} - set(topics))
    if unknown:
        raise ValueError(f"Tables' topics {unknown} aren't in topics in {CONFIG}")
    counts["acs_table"] = upsert_rows(
        conn, "acs_table", ("code", "title", "universe", "topic_id_fk", "tier", "why"), ("code",),
        [(code, latest["tables"][code]["title"], latest["tables"][code]["universe"], topics[t["topic"]], t["tier"], t["why"])
         for code, t in config["tables"].items()])
    table_ids = lookup_ids(conn, "acs_table", "code")
    paths = {uid: path for table in config["tables"] for uid, path in label_paths(latest["tables"][table]).items()}
    counts["acs_variable"] = upsert_rows(
        conn, "acs_variable", ("code", "table_id_fk", "line", "column_name", "label", "description", "unit"), ("code",),
        [(v["variable"], table_ids[v["variable"].split("_")[0]], int(v["variable"].split("_")[1]), v["column_name"],
          paths[v["variable"]], v["description"], v["unit"]) for v in variables])
    variable_ids = lookup_ids(conn, "acs_variable", "code")

    # The summary's measures: a share is a percent; a value or sum has its lines' unit
    units, measures = {v["variable"]: v["unit"] for v in variables}, []
    for sort, (name, measure) in enumerate(config["summary"].items(), start=1):
        if not measure.get("label") or not measure.get("description"):
            raise ValueError(f"Summary measure {name} in {CONFIG} needs a label and a description")
        kind = measure_kind(measure)
        unit = "percent" if kind == "share" else units[measure["value"] if kind == "value" else measure["sum"][0]]
        measures.append((name, sort, measure["label"], measure["description"], unit, kind, formula(measure)))
    counts["acs_measure"] = upsert_rows(conn, "acs_measure", ("name", "sort", "label", "description", "unit", "kind", "formula"),
                                        ("name",), measures)
    conn.execute(text("DELETE FROM acs_measure WHERE NOT (name = ANY(:names))"), {"names": list(config["summary"])})

    # Which releases have each value
    available = {}
    for year, release in releases.items():
        for v in variables:
            table = v["variable"].split("_")[0]
            kind = "same" if year == latest_year else comparability(latest, release, v["unit"], v["variable"], table)
            if kind:
                label = next(line[2] for line in release["tables"][table]["lines"] if line[0] == v["variable"])
                available[(v["variable"], year)] = (kind, label)
    counts["acs_variable_release"] = upsert_rows(
        conn, "acs_variable_release", ("variable_id_fk", "release_year", "label", "comparability"), ("variable_id_fk", "release_year"),
        [(variable_ids[code], year, label, kind) for (code, year), (kind, label) in sorted(available.items())])
    for year in releases:
        if year != latest_year:
            left_out = sorted(code for code in listed if (code, year) not in available)
            logger.info(f"ACS {year}: {len(left_out)} values aren't in it or mean something else: {left_out[:12]}")

    # Census areas, by the latest release's names; earlier releases have the same ids
    towns, districts = _places(conn)
    areas = match_geographies(latest["geographies"], towns, districts, config)
    counts["acs_town"] = upsert_rows(
        conn, "acs_town", ("town_id_fk", "census_geo_id", "census_name"), ("town_id_fk",),
        [(our_id, geo_id, latest["geographies"][geo_id]) for geo_id, (level, our_id, _) in sorted(areas.items()) if level == "town"])
    counts["acs_district"] = upsert_rows(
        conn, "acs_district", ("district_id_fk", "census_geo_id", "census_name", "census_type"), ("district_id_fk",),
        [(our_id, geo_id, latest["geographies"][geo_id], kind) for geo_id, (level, our_id, kind) in sorted(areas.items())
         if level == "district"])
    logger.info(f"ACS areas: {sum(1 for a in areas.values() if a[0] == 'town')} towns, "
                f"{sum(1 for a in areas.values() if a[0] == 'district')} school districts")

    # Every value for every place and release
    annotation_ids = {a["code"]: i for i, a in config["annotations"].items()}
    table_lines = {}
    for uid in sorted(paths):
        table_lines.setdefault(uid.split("_")[0], []).append(uid)
    rows = {level: [] for level in LEVELS}
    for year in years:
        release = releases[year]
        unknown = sorted(geo_id for table in release["tables"].values() for geo_id in (table["rows"] or {})
                         if geo_id not in areas and geo_id not in latest["geographies"])
        if unknown:
            raise ValueError(f"ACS {year} has Census areas the latest release doesn't: {unknown[:10]}")
        for table, data in sorted(release["tables"].items()):
            if table not in config["tables"] or not data["rows"]:
                continue
            columns = {column: i for i, column in enumerate(data["columns"])}
            for geo_id, values in sorted(data["rows"].items()):
                if geo_id not in areas:
                    continue
                level, our_id, _ = areas[geo_id]
                for uid in table_lines[table]:
                    if (uid, year) not in available:
                        continue
                    line = uid.split("_")[1]
                    estimate, moe = values[columns[f"{table}_E{line}"]], values[columns[f"{table}_M{line}"]]
                    key = () if level == "state" else (our_id,)
                    rows[level].append((*key, year, variable_ids[uid], *value_pair(estimate, moe, annotation_ids)))
    for level in LEVELS:
        table = f"{level}_acs_estimate"
        columns = (*KEYS[level], *ESTIMATE_COLUMNS)
        counts[table] = upsert_rows(conn, table, columns, (*KEYS[level], "release_year", "variable_id_fk"), rows[level])
        # Values and places no longer loaded
        kept = {row[:len(KEYS[level]) + 2] for row in rows[level]}  # (place, release, variable)
        stale = [row for row in conn.execute(text(
            f"SELECT {', '.join((*KEYS[level], 'release_year', 'variable_id_fk', 'id'))} FROM {table} WHERE release_year = ANY(:years)"),
            {"years": years}).all() if tuple(row[:-1]) not in kept]
        if stale:
            conn.execute(text(f"DELETE FROM {table} WHERE id = ANY(:ids)"), {"ids": [row[-1] for row in stale]})
            logger.info(f"{table}: deleted {len(stale)} values no longer loaded")
        refresh_dependent_views(conn, table)
    return counts


# -------------------- views --------------------

def _sum_sql(terms: List[str]) -> tuple:
    """The SQL for a sum of the summary's pivoted columns ("-B25070_011" subtracts) and its margin of error:
    the square root of the sum of the squared margins, counting only the largest margin among the parts
    that are zero, as Census advises."""
    columns = [(term.startswith("-"), term.lstrip("-").lower()) for term in terms]
    estimate = " ".join(f"{'-' if minus else '+'} {c}" for minus, c in columns).lstrip("+ ")
    nonzero = " + ".join(f"CASE WHEN {c} <> 0 THEN {c}_moe ^ 2 ELSE 0 END" for _, c in columns)
    zero = f"COALESCE(GREATEST({', '.join(f'CASE WHEN {c} = 0 THEN {c}_moe END' for _, c in columns)}), 0) ^ 2"
    return f"({estimate})", f"sqrt({nonzero} + {zero})"


def measure_kind(measure: dict) -> str:
    return next(kind for kind in ("share", "sum", "value") if kind in measure)


def formula(measure: dict) -> str:
    """How a measure is worked out, by Census's line ids: "(B25070_007 + ...) / (B25070_001 - B25070_011)"."""
    def terms(lines):
        return " ".join(f"{'-' if line.startswith('-') else '+'} {line.lstrip('-')}" for line in lines).lstrip("+ ")
    kind = measure_kind(measure)
    if kind == "value":
        return measure["value"]
    if kind == "sum":
        return terms(measure["sum"])
    return f"({terms(measure['share'])}) / ({terms(measure['of'])})"


def summary_terms(measure: dict) -> List[str]:
    return [term.lstrip("-") for key in ("value", "sum", "share", "of") for term in
            ([measure[key]] if isinstance(measure.get(key), str) else measure.get(key) or [])]


def view_statements(config: dict, variables: List[dict]) -> List[str]:
    """CREATE statements for the materialized views and their unique indexes: each level's topic views
    and summary. They're built from the estimate tables directly, so a load refreshes them all."""
    statements = []
    by_table = {}
    for v in variables:
        by_table.setdefault(v["variable"].split("_")[0], []).append(v)
    for level in LEVELS:
        keys = [*KEYS[level], "release_year"]
        estimates = f"{level}_acs_estimate"
        for topic in config["topics"].values():
            columns = []
            for table, settings in config["tables"].items():
                if settings["topic"] != topic["code"]:
                    continue
                for v in by_table[table]:
                    cast = "::integer" if v["unit"] in WHOLE_UNITS else ""
                    for source, name in (("estimate", v["column_name"]), ("moe", f"{v['column_name']}_moe")):
                        columns.append(f"(MAX(e.{source}) FILTER (WHERE v.code = '{v['variable']}')){cast} AS {name}")
            if len(columns) + len(keys) > 1600:
                raise ValueError(f"{level}_acs_{topic['code']} would have {len(columns)} columns, more than Postgres allows")
            view = f"{level}_acs_{topic['code']}"
            statements.append(
                f"CREATE MATERIALIZED VIEW {view} AS\n"
                f"SELECT {', '.join('e.' + k for k in keys)},\n    " + ",\n    ".join(columns) + "\n"
                f"FROM {estimates} e\n"
                f"JOIN acs_variable v ON v.id = e.variable_id_fk\n"
                f"JOIN acs_table t ON t.id = v.table_id_fk\n"
                f"JOIN acs_topic tp ON tp.id = t.topic_id_fk AND tp.code = '{topic['code']}'\n"
                f"GROUP BY {', '.join('e.' + k for k in keys)}")
            statements.append(f"CREATE UNIQUE INDEX idx_{view} ON {view} ({', '.join(keys)})")

        codes = sorted({term for measure in config["summary"].values() for term in summary_terms(measure)})
        pivot = ",\n        ".join(
            f"MAX(e.{source}) FILTER (WHERE v.code = '{code}') AS {code.lower()}{suffix}"
            for code in codes for source, suffix in (("estimate", ""), ("moe", "_moe")))
        parts, measures = [], []
        for name, measure in config["summary"].items():
            if "share" in measure:
                x, mx = _sum_sql(measure["share"])
                y, my = _sum_sql(measure["of"])
                parts.append(f"{x} AS {name}_x, {mx} AS {name}_x_moe, {y} AS {name}_y, {my} AS {name}_y_moe")
                p = f"({name}_x / NULLIF({name}_y, 0))"
                under = f"{name}_x_moe ^ 2 - {p} ^ 2 * {name}_y_moe ^ 2"
                moe = (f"(CASE WHEN {under} >= 0 THEN sqrt({under}) "
                       f"ELSE sqrt({name}_x_moe ^ 2 + {p} ^ 2 * {name}_y_moe ^ 2) END / NULLIF({name}_y, 0))")
                measures.append(f"round(100 * {p}, 1) AS {name}, round(100 * {moe}, 1) AS {name}_moe, "
                                f"acs_reliability({p}, {moe}) AS {name}_reliability")
            else:
                x, mx = _sum_sql([measure["value"]] if "value" in measure else measure["sum"])
                parts.append(f"{x} AS {name}_x, {mx} AS {name}_x_moe")
                measures.append(f"{name}_x AS {name}, CASE WHEN {name}_x IS NOT NULL THEN round({name}_x_moe, 1) END AS {name}_moe, "
                                f"acs_reliability({name}_x, {name}_x_moe) AS {name}_reliability")
        view = f"{level}_acs_summary"
        statements.append(
            f"CREATE MATERIALIZED VIEW {view} AS\n"
            f"WITH pivot AS (\n    SELECT {', '.join('e.' + k for k in keys)},\n        {pivot}\n"
            f"    FROM {estimates} e JOIN acs_variable v ON v.id = e.variable_id_fk\n"
            f"    WHERE v.code IN ({', '.join(repr(c) for c in codes)})\n"
            f"    GROUP BY {', '.join('e.' + k for k in keys)}\n"
            f"), parts AS (\n    SELECT {', '.join(keys)},\n        " + ",\n        ".join(parts) + "\n    FROM pivot\n)\n"
            f"SELECT {', '.join(keys)},\n    " + ",\n    ".join(measures) + "\nFROM parts")
        statements.append(f"CREATE UNIQUE INDEX idx_{view} ON {view} ({', '.join(keys)})")
    return statements


def reliability_function(config: dict) -> str:
    """acs_reliability(estimate, moe): high, caution or low, by the coefficient of variation (the
    standard error, the margin of error / 1.645, as a percent of the estimate)."""
    high, caution = config["reliability"]["high"], config["reliability"]["caution"]
    return f"""
        CREATE FUNCTION acs_reliability(estimate NUMERIC, moe NUMERIC) RETURNS VARCHAR(10)
        LANGUAGE sql IMMUTABLE AS $$
            SELECT CASE
                WHEN estimate IS NULL OR moe IS NULL THEN NULL
                WHEN moe = 0 THEN 'high'
                WHEN estimate = 0 THEN 'low'
                WHEN moe / 1.645 / abs(estimate) * 100 <= {high} THEN 'high'
                WHEN moe / 1.645 / abs(estimate) * 100 <= {caution} THEN 'caution'
                ELSE 'low'
            END
        $$
    """


def view_names(config: dict) -> List[str]:
    return [f"{level}_acs_{topic['code']}" for level in LEVELS for topic in config["topics"].values()] + \
           [f"{level}_acs_summary" for level in LEVELS]


# -------------------- the summary, in Python (for checking the views) --------------------

def reliability(estimate, moe, config: dict) -> Optional[str]:
    if estimate is None or moe is None:
        return None
    if moe == 0:
        return "high"
    if estimate == 0:
        return "low"
    cv = moe / 1.645 / abs(estimate) * 100
    return "high" if cv <= config["reliability"]["high"] else "caution" if cv <= config["reliability"]["caution"] else "low"


def _sum(values: dict, terms: List[str]) -> tuple:
    """As _sum_sql: a part with no margin of error leaves the sum without one, unless the part is zero."""
    parts = [(-1 if t.startswith("-") else 1, *values.get(t.lstrip("-"), (None, None))) for t in terms]
    if any(e is None for _, e, _ in parts):
        return None, None
    if any(m is None for _, e, m in parts if e != 0):
        return sum(sign * e for sign, e, _ in parts), None
    zero = [m for _, e, m in parts if e == 0 and m is not None]
    squares = sum(m * m for _, e, m in parts if e != 0) + (max(zero) ** 2 if zero else 0)
    return sum(sign * e for sign, e, _ in parts), math.sqrt(squares)


def summary(values: dict, config: dict) -> dict:
    """{measure: (value, margin of error, reliability)} from {variable code: (estimate, moe)}."""
    out = {}
    for name, measure in config["summary"].items():
        if "share" not in measure:
            x, mx = _sum(values, [measure["value"]] if "value" in measure else measure["sum"])
            out[name] = (x, mx, reliability(x, mx, config))
            continue
        x, mx = _sum(values, measure["share"])
        y, my = _sum(values, measure["of"])
        if x is None or y is None or y == 0:
            out[name] = (None, None, None)
            continue
        p = x / y
        under = mx * mx - p * p * my * my
        mp = math.sqrt(under if under >= 0 else mx * mx + p * p * my * my) / y
        out[name] = (round(100 * p, 1), round(100 * mp, 1), reliability(p, mp, config))
    return out
