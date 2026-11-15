"""
Property tax rates and school taxes by town, from NH DRA's tax rates and NH DOE's valuations report (see
property_tax_config.yaml). A tax year is its starting year: rates set in the fall of 2025 are 2025, paying for 2025-26.

- town_property_tax: DRA's rates per $1,000 for each town and tax year, its equalization ratio, full value rate,
  valuations and (from 2018) school tax dollars
- town_school_tax: the DOE report's row for each town: its district and, for a member town, its cooperative (the
  report's numbers and names, as site district ids), school tax dollars, valuations, and rates per $1,000 of assessed
  and of equalized value
- town_school_tax_coop_share: the part of a town's local school tax that goes to a cooperative, from the report's
  "reference only" rows

Values are the publishers', never recomputed. The load checks them: DRA's four rates must add up to its total rate,
the DOE's rates must match DRA's within a cent and its school tax dollars DRA's within a dollar, and the DOE's state
education tax must equal the town's SWEPT in the adequacy aid tables for the next fiscal year; each known difference
is listed in the config. town_property_tax_summary is built on these tables.
"""
import csv
import logging
import os
import re
from collections import Counter
from typing import Dict, Iterable, List, Optional, Tuple

from sqlalchemy import text
from sqlalchemy.engine import Connection

from app.etl.core import config_path, load_config, refresh_dependent_views, replace_rows

logger = logging.getLogger("app.etl")

CONFIG = "property_tax_config.yaml"
# The report's two kinds of town row kept: a single-town district's, and a cooperative member town's
ROW_TYPES = ("single-town school district", "member town of cooperative/regional district")
# Rates are published to the cent; dollars to the dollar
CENT, DOLLAR = 0.005, 1.0
RATES = {"local": ("rate_local_educ", "local_education_rate"), "state": ("rate_state_educ", "state_education_rate"),
         "total": ("rate_total", "total_rate")}
DRA_PARTS = ("municipal_rate", "county_rate", "local_education_rate", "state_education_rate")
# "SOUHEGAN COOP  C: local_educ_tax 10690235": a cooperative's share of the town's local school tax, and its footnote
COOP_SHARE = re.compile(r"^(?P<name>.*?)\s+(?P<footnote>[A-Z]):\s*local_educ_tax\s+(?P<amount>-?[\d.]+)$")
# The DRA file's columns naming the files each figure was read from (in assets/property-tax/dra)
DRA_SOURCE_COLUMNS = ("rate_source_file", "ratio_source_file", "full_value_source_file", "calc_source_file")


def _number(value: str) -> Optional[float]:
    value = value.strip()
    return float(value) if value else None


def _read(config: dict, key: str) -> List[dict]:
    path = os.path.join(config_path(config["directory"]), config[key])
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def _years(settings: dict) -> range:
    return range(settings["start"], settings["end"] + 1)


def _file(cited: str) -> str:
    """The file a row cites, without the sheet named after it: "dra/x.xlsx (Ratio History 2025-2016)" is dra/x.xlsx"""
    return cited.split(" (")[0].strip()


def read(config: dict, years: Iterable[int]) -> Tuple[List[dict], List[dict]]:
    """(DRA's rows, the DOE's rows) for the years asked that each publisher's range covers, with their figures as
    numbers. Each DOE row's cooperative shares are parsed from its reference-only column."""
    years = set(years)
    dra_years, doe_years = years & set(_years(config["dra_years"])), years & set(_years(config["doe_years"]))
    dra = []
    for row in _read(config, "dra_file"):
        if int(row["tax_year"]) in dra_years:
            dra.append({**row, "town_id": int(row["town_id"]), "tax_year": int(row["tax_year"]),
                        **{c: _number(row[c]) for c in (*DRA_PARTS, "total_rate", "equalization_ratio", "full_value_tax_rate",
                                                         "assessed_valuation", "assessed_valuation_with_utilities",
                                                         "total_tax_commitment", "local_school_tax_effort", "state_education_tax_effort")}})
    doe = []
    for row in _read(config, "doe_file"):
        if int(row["tax_year"]) not in doe_years:
            continue
        shares = []
        if row["reference_only_coop_rows"].strip():
            match = COOP_SHARE.match(row["reference_only_coop_rows"].strip())
            if not match:
                raise ValueError(f"{row['town']} {row['tax_year']}: can't read the cooperative share {row['reference_only_coop_rows']!r}")
            shares.append({"name": " ".join(match["name"].split()), "footnote": match["footnote"], "amount": float(match["amount"])})
        doe.append({**row, "town_id": int(row["town_id"]), "tax_year": int(row["tax_year"]),
                    "district_number": int(row["doe_district_number"]) if row["doe_district_number"].strip() else None,
                    "cooperative": " ".join(row["cooperative_district"].split()) or None,
                    "coop_shares": shares,
                    **{c: _number(row[c]) for c in ("assessed_val_with_util", "assessed_val_wo_util", "equalized_val_with_util",
                                                     "equalized_val_wo_util", "local_educ_tax", "other_local_tax", "state_educ_tax",
                                                     "rate_local_educ", "rate_other_local", "rate_state_educ", "rate_total",
                                                     "eq_rate_local_educ", "eq_rate_other_local", "eq_rate_state_educ", "eq_rate_total")}})
    return dra, doe


def check(config: dict, dra: List[dict], doe: List[dict], swept: Optional[Dict[Tuple[int, int], float]] = None) -> Dict[Tuple[int, int], str]:
    """Check the figures (see the module's docstring); raise on any difference the config doesn't list. Returns the
    DOE rows' notes from the config, by (town id, tax year). `swept` is {(town id, fiscal year): SWEPT} from the
    adequacy aid tables, when they're loaded."""
    problems = []
    for name, rows in (("DRA", dra), ("DOE", doe)):
        repeated = [key for key, n in Counter((r["town_id"], r["tax_year"]) for r in rows).items() if n > 1]
        if repeated:
            problems.append(f"{name} has towns more than once in a year: {repeated[:5]}")

    # DRA: final years only, and its four rates add up to its total
    for r in dra:
        if r["status"] != "final":
            problems.append(f"DRA {r['town']} {r['tax_year']}: status {r['status']!r}; load only final years")
    dra_years = {r["tax_year"] for r in dra}
    differs = {(d["town_id"], d["tax_year"]) for d in config.get("dra_total_differs") or [] if d["tax_year"] in dra_years}
    found = set()
    for r in dra:
        if r["total_rate"] is None:
            continue  # nothing to add up to (Penacook 2015, whose PDF line has no total)
        parts = [r[c] for c in DRA_PARTS]
        if None in parts or abs(sum(parts) - r["total_rate"]) > 0.01 + CENT:
            found.add((r["town_id"], r["tax_year"]))
    problems += [f"DRA town {t} {y}: its rates don't add up to its total; list it in dra_total_differs if DRA's file says so"
                 for t, y in sorted(found - differs)]
    problems += [f"DRA town {t} {y}: its rates add up to its total, but dra_total_differs lists it" for t, y in sorted(differs - found)]

    # The DOE's rates against DRA's, by the cent
    by_dra = {(r["town_id"], r["tax_year"]): r for r in dra}
    doe_years = {r["tax_year"] for r in doe}
    listed = {(d["town_id"], d["tax_year"], rate) for d in config.get("rate_differences") or [] for rate in d["rates"]
              if d["tax_year"] in doe_years & dra_years}
    found = set()
    for r in doe:
        other = by_dra.get((r["town_id"], r["tax_year"]))
        if other is None:
            continue
        for rate, (doe_column, dra_column) in RATES.items():
            a, b = r[doe_column], other[dra_column]
            if (a is None) != (b is None) or (a is not None and abs(a - b) > 0.01 + CENT):
                found.add((r["town_id"], r["tax_year"], rate))
    problems += [f"DOE town {t} {y}: its {rate} rate differs from DRA's; list it in rate_differences if the files say so"
                 for t, y, rate in sorted(found - listed)]
    problems += [f"DOE town {t} {y}: its {rate} rate matches DRA's, but rate_differences lists it" for t, y, rate in sorted(listed - found)]

    # The DOE's school tax dollars against DRA's (from 2018), counting the towns DRA reports together as one
    combined = {int(town): towns for town, towns in (config.get("combined_towns") or {}).items()}
    parts_of = {part for towns in combined.values() for part in towns}
    by_doe = {(r["town_id"], r["tax_year"]): r for r in doe}
    for r in dra:
        if r["local_school_tax_effort"] is None or r["tax_year"] not in doe_years:
            continue
        towns = combined.get(r["town_id"], [r["town_id"]])
        if r["town_id"] in parts_of and r["town_id"] not in combined:
            continue  # counted in its whole town's figure
        rows = [by_doe.get((town, r["tax_year"])) for town in towns]
        if None in rows:
            problems.append(f"DRA town {r['town_id']} {r['tax_year']} has school tax dollars, but the DOE has no row for {towns}")
            continue
        for doe_column, dra_column in (("local_educ_tax", "local_school_tax_effort"), ("state_educ_tax", "state_education_tax_effort")):
            total = sum(row[doe_column] for row in rows)
            if abs(total - r[dra_column]) > DOLLAR:
                problems.append(f"town {r['town_id']} {r['tax_year']}: the DOE's {doe_column} is {total:,.2f}, DRA's {r[dra_column]:,.2f}")

    # The DOE's state education tax is the town's SWEPT for the fiscal year it pays for
    for r in doe:
        fiscal = swept.get((r["town_id"], r["tax_year"] + 1)) if swept else None
        if fiscal is not None and abs(fiscal - r["state_educ_tax"]) > DOLLAR:
            problems.append(f"town {r['town_id']} {r['tax_year']}: state education tax {r['state_educ_tax']:,.2f}, "
                            f"FY{r['tax_year'] + 1} SWEPT {fiscal:,.2f}")

    # Each DOE row is a single-town district's or a member town's, which names its cooperative; every cooperative it
    # names is in the config, and a member row's district number, where it has one, is its cooperative's (but for the
    # config's member_own_district)
    cooperatives = config.get("cooperatives") or {}
    aliases = config.get("district_aliases") or {}
    own = {(town, year) for town, years in (config.get("member_own_district") or {}).items() for year in years}
    differs = set()
    for r in doe:
        if r["doe_row_type"] not in ROW_TYPES:
            problems.append(f"DOE {r['town']} {r['tax_year']}: row type {r['doe_row_type']!r}")
        if (r["doe_row_type"] == ROW_TYPES[1]) != (r["cooperative"] is not None):
            problems.append(f"DOE {r['town']} {r['tax_year']}: a {r['doe_row_type']} row, with cooperative {r['cooperative']!r}")
        for name in [r["cooperative"], *(share["name"] for share in r["coop_shares"])]:
            if name is not None and name not in cooperatives:
                problems.append(f"DOE {r['town']} {r['tax_year']}: cooperative {name!r} isn't in the config's cooperatives")
        if r["cooperative"] in cooperatives and r["district_number"] is not None \
                and aliases.get(r["district_number"], r["district_number"]) != cooperatives[r["cooperative"]]:
            differs.add((r["town_id"], r["tax_year"]))
    doe_keys = {(r["town_id"], r["tax_year"]) for r in doe}
    problems += [f"DOE town {t} {y}: a member row with a district number not its cooperative's; list it in member_own_district"
                 for t, y in sorted(differs - own)]
    problems += [f"DOE town {t} {y}: member_own_district lists it, but its number is its cooperative's"
                 for t, y in sorted((own & doe_keys) - differs)]
    if problems:
        raise ValueError(f"Property tax: {len(problems)} figures don't check: {problems[:5]}")
    notes = {}
    for d in config.get("rate_differences") or []:
        if d.get("note"):
            notes[(d["town_id"], d["tax_year"])] = d["note"]
    return notes


def _swept(conn: Connection) -> Dict[Tuple[int, int], float]:
    """{(town id, fiscal year): SWEPT} from the adequacy aid tables, or {} before they're built"""
    if not conn.execute(text("SELECT to_regclass('town_adequacy_aid')")).scalar():
        return {}
    return {(town, year): float(value) for town, year, value in conn.execute(text("""
        SELECT t.town_id_fk, t.fiscal_year, t.value FROM town_adequacy_aid t
        JOIN adequacy_aid_component c ON c.id = t.component_id_fk WHERE c.code = 'swept'
    """)).all()}


def check_files(config: dict, dra: List[dict], doe: List[dict]) -> None:
    """Every file a row cites is in the repo: DRA's in the config's dra_directory, the DOE's reports in its
    doe_report_directory. DATA_SOURCES.md says where each was first downloaded."""
    cited = {_file(part) for r in dra for column in DRA_SOURCE_COLUMNS for part in r[column].split("; ") if part.strip()}
    missing = sorted(f for f in cited if not os.path.exists(os.path.join(config_path(config["directory"]), f)))
    reports = {os.path.basename(r["source_file"]) for r in doe}
    missing += sorted(f for f in reports if not os.path.exists(os.path.join(config_path(config["doe_report_directory"]), f)))
    if missing:
        raise ValueError(f"Property tax: the files {missing} that rows cite aren't in the repo; save them (see DATA_SOURCES.md)")


def _districts(conn: Connection, config: dict, doe: List[dict]) -> Dict[int, int]:
    """{DOE district number: the site's district id}: the same number, but for the config's district_aliases. Every
    number, and every cooperative in the config, must be a site district."""
    sites = {i for (i,) in conn.execute(text("SELECT id FROM district WHERE kind = 'district'")).all()}
    aliases = config.get("district_aliases") or {}
    found = {n: aliases.get(n, n) for n in {r["district_number"] for r in doe if r["district_number"] is not None}}
    unknown = sorted(n for n, i in found.items() if i not in sites)
    if unknown:
        raise ValueError(f"DOE district numbers {unknown} aren't site districts; map them in district_aliases")
    unknown = [i for i in (config.get("cooperatives") or {}).values() if i not in sites]
    if unknown:
        raise ValueError(f"cooperatives in {CONFIG} name districts {unknown}, which aren't site districts")
    return found


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the config's tax years (or those given) from both publishers, after checking them. Then refresh the view
    built on them."""
    config = load_config(CONFIG)
    configured = sorted(set(_years(config["dra_years"])) | set(_years(config["doe_years"])))
    years = sorted(set(years or configured))
    unknown = [y for y in years if y not in configured]
    if unknown:
        raise ValueError(f"Tax years {unknown} aren't in {CONFIG}: {configured[0]}-{configured[-1]}")

    towns = {i for (i,) in conn.execute(text("SELECT id FROM town")).all()}
    dra, doe = read(config, years)
    missing = sorted({r["town_id"] for r in dra + doe} - towns)
    if missing:
        raise ValueError(f"Town ids {missing} aren't in the town table")
    notes = check(config, dra, doe, _swept(conn))
    check_files(config, dra, doe)
    districts = _districts(conn, config, doe)
    differs = {(d["town_id"], d["tax_year"]): d["note"] for d in config.get("dra_total_differs") or [] if d.get("note")}

    dra_rows = [(
        r["town_id"], r["tax_year"], r["dra_name"], *(r[c] for c in DRA_PARTS), r["total_rate"], r["equalization_ratio"],
        r["full_value_tax_rate"], r["assessed_valuation"], r["assessed_valuation_with_utilities"], r["total_tax_commitment"],
        r["local_school_tax_effort"], r["state_education_tax_effort"], r["date_rate_set"],
        "; ".join(n for n in (r["note"].strip(), differs.get((r["town_id"], r["tax_year"]))) if n) or None,
    ) for r in dra]
    cooperatives = config.get("cooperatives") or {}
    doe_rows = [(
        r["town_id"], r["tax_year"], districts.get(r["district_number"]), cooperatives.get(r["cooperative"]),
        r["assessed_val_wo_util"], r["assessed_val_with_util"], r["equalized_val_wo_util"], r["equalized_val_with_util"],
        r["local_educ_tax"], r["other_local_tax"], r["state_educ_tax"],
        r["rate_local_educ"], r["rate_other_local"], r["rate_state_educ"], r["rate_total"],
        r["eq_rate_local_educ"], r["eq_rate_other_local"], r["eq_rate_state_educ"], r["eq_rate_total"],
        notes.get((r["town_id"], r["tax_year"])),
    ) for r in doe]
    for year in years:
        logger.info(f"Property tax {year}: DRA {sum(r['tax_year'] == year for r in dra)} towns, "
                    f"DOE {sum(r['tax_year'] == year for r in doe)} towns")

    where, params = "tax_year = ANY(:years)", {"years": years}
    counts = {"town_property_tax": replace_rows(
        conn, "town_property_tax",
        ("town_id_fk", "tax_year", "dra_name", *DRA_PARTS, "total_rate", "equalization_ratio", "full_value_tax_rate",
         "assessed_valuation", "assessed_valuation_with_utilities", "total_tax_commitment", "local_school_tax_effort",
         "state_education_tax_effort", "date_rate_set", "note"), dra_rows, where, params)}
    # A town's cooperative shares go with its row (ON DELETE CASCADE), and come back with its new id
    counts["town_school_tax"] = replace_rows(
        conn, "town_school_tax",
        ("town_id_fk", "tax_year", "district_id_fk", "cooperative_district_id_fk",
         "assessed_valuation", "assessed_valuation_with_utilities", "equalized_valuation", "equalized_valuation_with_utilities",
         "local_education_tax", "other_local_tax", "state_education_tax",
         "rate_local_education", "rate_other_local", "rate_state_education", "rate_total",
         "equalized_rate_local_education", "equalized_rate_other_local", "equalized_rate_state_education", "equalized_rate_total",
         "note"), doe_rows, where, params)
    ids = {(town, year): i for i, town, year in conn.execute(text(
        "SELECT id, town_id_fk, tax_year FROM town_school_tax WHERE tax_year = ANY(:years)"), params).all()}
    counts["town_school_tax_coop_share"] = replace_rows(
        conn, "town_school_tax_coop_share", ("town_school_tax_id_fk", "district_id_fk", "footnote", "local_education_tax"),
        [(ids[(r["town_id"], r["tax_year"])], cooperatives[s["name"]], s["footnote"], s["amount"])
         for r in doe for s in r["coop_shares"]])
    # The summary is built on both town tables; refreshing it once covers both
    refresh_dependent_views(conn, "town_property_tax")
    return counts
