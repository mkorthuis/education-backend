"""
New Hampshire special education aid (catastrophic aid until 2017): NH DOE's yearly table of each school district's
costs for high-cost special education students and the aid the state pays on them (see
special_education_aid_config.yaml):

- special_education_aid_year: each fiscal year of aid, its threshold, appropriation, proration and the DOE's
  statewide totals
- special_education_aid_band: each year's bands of a student's cost and the state's share of each
- district_special_education_aid: each district's total cost, entitlement and aid paid, as the DOE publishes them
- district_special_education_aid_band: each district's costs in each band

Values are the DOE's, never recomputed. The load checks them: each district's entitlement must be its band costs
times the year's state shares, its total cost the sum of its bands (but for districts the config lists), its aid
its entitlement times the year's proration (and at least the minimum share), and the districts must add up to the
DOE's state row. district_special_education_aid_summary is built on these tables.
"""
import csv
import logging
import os
import re
from collections import Counter
from typing import Iterable, List, Optional

from sqlalchemy import text
from sqlalchemy.engine import Connection

from app.etl.core import config_path, load_config, refresh_dependent_views, replace_rows, upsert_rows

logger = logging.getLogger("app.etl")

CONFIG = "special_education_aid_config.yaml"
STATUSES = ("final", "estimate")
# The DOE's columns by their headings, which vary a little from year to year (lower-cased, spaces collapsed); the
# first test a heading passes names it. The three bands are the files' through FY2028.
HEADINGS = [
    ("district_id", lambda h: h.startswith("district id")),
    ("name", lambda h: h == "district of liability"),
    ("students", lambda h: "students reported" in h),
    ("band_1", lambda h: "liability" in h),
    ("band_2", lambda h: "3.5 to 10" in h),
    ("band_3_students", lambda h: "students over" in h),
    ("band_3", lambda h: "over 10" in h),
    ("total_cost", lambda h: re.fullmatch(r"sum of district costs?", h) is not None),
    # Before entitlement: FY2023's is "Prorated Entitlement 98.2763"
    ("aid_paid", lambda h: "prorated" in h or "appropriation" in h),
    ("entitlement", lambda h: "entitlement" in h or "eligible" in h or "elligible" in h),
]
REQUIRED = ("name", "band_1", "band_2", "band_3", "total_cost", "entitlement")
FILE_BANDS = 3
STATE_ROW = re.compile(r"^(state|totals?$|grand total)", re.I)
# How far a district's figure may be from the formula (the DOE rounds to the cent), and the districts' sum from the
# DOE's state row (each district's rounding adds up)
CENTS = 0.02
STATE_TOLERANCE = 1.0


def _heading(value: str) -> str:
    return " ".join(value.split()).lower()


def _money(value: str) -> float:
    """A dollar amount as the DOE writes it ("$1,234.56 ", "$-", "-"), with a blank as $0."""
    value = value.strip().replace("$", "").replace(",", "").strip()
    return 0.0 if value in ("", "-") else float(value)


def _count(value: str) -> Optional[float]:
    value = value.strip().replace(",", "")
    return float(value) if value else None


def _check_repeat(year: int, number: int, row: List[str], state: Optional[dict]) -> None:
    """A row the config lists in repeat_rows (a second total, or a count below the table) may only repeat the state
    row's figures."""
    if state is None:
        raise ValueError(f"FY{year} row {number}: a repeat_rows row before the state row")
    published = {round(v, 2) for v in [*state["bands"].values(), *state["band_students"].values(), state["students"],
                                       state["total_cost"], state["entitlement"], state["aid_paid"]] if v is not None}
    for value in row:
        try:
            number_ = _money(value)
        except ValueError:
            continue  # its label
        if number_ and round(number_, 2) not in published:
            raise ValueError(f"FY{year} row {number} ({row[:2]}) has {number_:,.2f}, which isn't one of the state row's figures")


def read_year(config: dict, year: int) -> dict:
    """{"state": the DOE's state row, "districts": [each district's row]} from a year's file. Each row has the name
    (and the DOE's district ID, if the file has one), students, its band costs {1: ..., 2: ..., 3: ...}, band 3's
    students, total cost, entitlement and aid paid (None when the file has no prorated column)."""
    path = os.path.join(config_path(config["directory"]), config["years"][year]["file"])
    with open(path, encoding="utf-8-sig", errors="replace", newline="") as f:
        rows = list(csv.reader(f))
    header = next((i for i, row in enumerate(rows) if any(_heading(c) == "district of liability" for c in row)), None)
    if header is None:
        raise ValueError(f"FY{year}: no 'District of Liability' heading in {path}")
    columns = {}
    for index, cell in enumerate(rows[header]):
        heading = _heading(cell)
        field = next((name for name, test in HEADINGS if heading and test(heading)), None)
        if field and field not in columns:
            columns[field] = index
    name_index = columns.get("name")
    # FY2021's IDs sit in a column with no heading, before the names
    if "district_id" not in columns and name_index and not _heading(rows[header][name_index - 1]):
        columns["district_id"] = name_index - 1
    missing = [field for field in REQUIRED if field not in columns]
    if missing:
        raise ValueError(f"FY{year}: no column for {missing} in {path}; its headings are {rows[header]}")

    def cell(row, field):
        index = columns.get(field)
        return row[index] if index is not None and index < len(row) else ""

    state, districts, repeats = None, [], {name.lower() for name in config["years"][year].get("repeat_rows") or []}
    for number, row in enumerate(rows[header + 1:], start=header + 2):
        name = " ".join(cell(row, "name").split())
        if not re.search(r"[A-Za-z]", name):
            continue  # a blank row
        if name.lower() in repeats:
            _check_repeat(year, number, row, state)
            continue
        try:
            values = {
                "name": name, "students": _count(cell(row, "students")),
                "bands": {1: _money(cell(row, "band_1")), 2: _money(cell(row, "band_2")), 3: _money(cell(row, "band_3"))},
                "band_students": {3: _count(cell(row, "band_3_students"))},
                "total_cost": _money(cell(row, "total_cost")), "entitlement": _money(cell(row, "entitlement")),
                "aid_paid": _money(cell(row, "aid_paid")) if "aid_paid" in columns else None,
            }
        except ValueError as e:
            raise ValueError(f"FY{year} row {number} ({name}): {e}")
        if STATE_ROW.match(name):
            if state is not None:
                raise ValueError(f"FY{year}: a second state row, row {number} ({name})")
            state = values
            continue
        ident = cell(row, "district_id").strip()
        values["district_id"] = int(ident) if ident.isdigit() else None
        districts.append(values)
    if state is None:
        raise ValueError(f"FY{year}: no state totals row in {path}")
    return {"state": state, "districts": districts}


def bands_for(config: dict, year: int) -> List[dict]:
    """The year's bands, from the formula in effect: the one starting latest, but not after the year."""
    starts = [start for start in config["formulas"] if start <= year]
    if not starts:
        raise ValueError(f"FY{year}: no formula in {CONFIG} starts by then")
    formula = config["formulas"][max(starts)]
    return [{**band, "band": number, "citation": formula["citation"], "source_url": formula["source_url"]}
            for number, band in enumerate(formula["bands"], start=1)]


def check_year(config: dict, year: int, parsed: dict, bands: List[dict]) -> float:
    """Check a year's figures (see the module's docstring), filling in aid paid for a year paid in full. Returns the
    year's proration: aid paid as a share of entitlement, from the DOE's state row."""
    settings = config["years"][year]
    state, districts = parsed["state"], parsed["districts"]
    if len(bands) != FILE_BANDS:
        raise ValueError(f"FY{year}'s formula has {len(bands)} bands; the DOE's file layout read here has {FILE_BANDS}. "
                         f"Map the new file's columns in HEADINGS first")
    shares = {band["band"]: band["state_share"] for band in bands}
    problems = []

    # The threshold: each reported student counts at it in the first column, so it's the most common value there
    common = Counter(round(d["bands"][1], 2) for d in districts).most_common(1)[0][0]
    if abs(common - settings["threshold_cost"]) > 0.01:
        problems.append(f"the most common first-band cost is {common:,.2f}, not threshold_cost {settings['threshold_cost']:,.2f}")

    differs = {name.lower() for name in settings.get("total_cost_differs") or []}
    for d in districts:
        entitlement = sum(cost * shares[band] for band, cost in d["bands"].items())
        if abs(entitlement - d["entitlement"]) > CENTS:
            problems.append(f"{d['name']}: its bands give an entitlement of {entitlement:,.2f}, the DOE {d['entitlement']:,.2f}")
        total = sum(d["bands"].values())
        if (abs(total - d["total_cost"]) > CENTS) != (d["name"].lower() in differs):
            problems.append(f"{d['name']}: its bands add up to {total:,.2f}, its total cost is {d['total_cost']:,.2f}"
                            + (" (listed in total_cost_differs)" if d["name"].lower() in differs else ""))
    unlisted = differs - {d["name"].lower() for d in districts}
    if unlisted:
        problems.append(f"total_cost_differs names {sorted(unlisted)}, which aren't in the file")

    if settings.get("paid_in_full"):
        if state["aid_paid"] is not None:
            problems.append("paid_in_full, but the file has a prorated column")
        for d in [state, *districts]:
            d["aid_paid"] = d["entitlement"]
        rate = 1.0
    else:
        if state["aid_paid"] is None:
            raise ValueError(f"FY{year}: the file has no prorated column; set paid_in_full if the year was")
        rate = state["aid_paid"] / state["entitlement"]
        minimum = settings.get("minimum_share")
        for d in districts:
            expected = d["entitlement"] * max(rate, minimum or 0)
            if abs(expected - d["aid_paid"]) > STATE_TOLERANCE:
                problems.append(f"{d['name']}: aid of {d['aid_paid']:,.2f}, against {expected:,.2f} at the year's proration")
        appropriation = settings.get("appropriation")
        if appropriation is not None and abs(appropriation - state["aid_paid"]) > STATE_TOLERANCE:
            problems.append(f"the state row's aid of {state['aid_paid']:,.2f} isn't the appropriation of {appropriation:,.2f}")

    sums = {
        **{f"band {band}": (sum(d["bands"][band] for d in districts), state["bands"][band]) for band in shares},
        "total cost": (sum(d["total_cost"] for d in districts), state["total_cost"]),
        "entitlement": (sum(d["entitlement"] for d in districts), state["entitlement"]),
        "aid paid": (sum(d["aid_paid"] for d in districts), state["aid_paid"]),
    }
    for what, (found, published) in sums.items():
        if abs(found - published) > STATE_TOLERANCE:
            problems.append(f"the districts' {what} adds up to {found:,.2f}, the state row {published:,.2f}")
    if problems:
        raise ValueError(f"FY{year}: {len(problems)} figures don't check: {problems[:5]}")
    return rate


def district_ids(conn: Connection, config: dict, year: int, districts: List[dict]) -> List[int]:
    """Each row's district: by the DOE's ID where the file has one (its name must match too), else by name or alias."""
    names = {}
    for ident, name in conn.execute(text("SELECT id, name FROM district WHERE kind = 'district'")).all():
        names.setdefault(name.lower(), []).append(ident)
    known = {i for ids in names.values() for i in ids}
    aliases = {k.lower(): v.lower() for k, v in (config.get("district_aliases") or {}).items()}
    unknown_aliases = sorted(v for v in aliases.values() if v not in names)
    if unknown_aliases:
        raise ValueError(f"district_aliases in {CONFIG} name {unknown_aliases}, which aren't districts")
    found, problems = [], []
    for d in districts:
        by_name = names.get(aliases.get(d["name"].lower(), d["name"].lower()), [])
        if len(by_name) > 1:
            problems.append(f"{d['name']} names {len(by_name)} districts")
        elif d["district_id"] is not None:
            if d["district_id"] not in known or by_name != [d["district_id"]]:
                problems.append(f"{d['name']} has ID {d['district_id']}, which isn't the district of that name ({by_name})")
        elif not by_name:
            problems.append(f"{d['name']} matches no district; add it to district_aliases")
        found.append(d["district_id"] if d["district_id"] is not None else (by_name[0] if by_name else None))
    repeated = [i for i, n in Counter(found).items() if n > 1 and i is not None]
    if repeated:
        problems.append(f"districts {repeated} are in the file twice")
    if problems:
        raise ValueError(f"FY{year}: {problems[:5]}")
    return found


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the config's years (or those given): each year, its bands and every district's figures, after checking
    them. Then refresh the view built on them."""
    config = load_config(CONFIG)
    configured = sorted(config["years"])
    years = sorted(set(years or configured))
    unknown = [y for y in years if y not in configured]
    if unknown:
        raise ValueError(f"Fiscal years {unknown} aren't in {CONFIG}: {configured}")

    year_rows, band_rows, district_rows, district_bands = [], [], [], {}
    for year in years:
        settings = config["years"][year]
        if settings["status"] not in STATUSES:
            raise ValueError(f"FY{year}: status {settings['status']!r} isn't one of {STATUSES}")
        parsed = read_year(config, year)
        bands = bands_for(config, year)
        rate = check_year(config, year, parsed, bands)
        ids = district_ids(conn, config, year, parsed["districts"])
        first_paid = next(b for b in bands if b["state_share"] > 0)
        state = parsed["state"]
        year_rows.append((
            year, settings["cost_school_year"], settings["status"], settings.get("as_of"),
            round(settings["threshold_cost"] / first_paid["from"], 2), settings["threshold_cost"], settings.get("appropriation"),
            round(rate, 7), settings.get("minimum_share"), state["students"], state["band_students"][3],
            state["total_cost"], state["entitlement"], state["aid_paid"], settings["url"], config["page_url"], settings.get("note"),
        ))
        band_rows.extend((year, b["band"], b["from"], b["to"], b["state_share"], b["label"], b["citation"], b["source_url"])
                         for b in bands)
        for district, d in zip(ids, parsed["districts"]):
            district_rows.append((district, year, d["name"], d["students"], d["total_cost"], d["entitlement"], d["aid_paid"]))
            district_bands[(district, year)] = [(band, cost, d["band_students"].get(band)) for band, cost in d["bands"].items()]
        logger.info(f"Special education aid FY{year}: {len(ids)} districts, entitlement {state['entitlement']:,.2f}, "
                    f"paid {state['aid_paid']:,.2f} ({rate:.4%})")

    where, params = "fiscal_year = ANY(:years)", {"years": years}
    counts = {"special_education_aid_year": upsert_rows(
        conn, "special_education_aid_year",
        ("fiscal_year", "cost_school_year", "status", "as_of", "state_average_cost", "threshold_cost", "appropriation",
         "proration_rate", "minimum_share", "state_students_reported", "state_students_highest_band", "state_total_cost",
         "state_entitlement", "state_aid_paid", "source_url", "page_url", "note"),
        ("fiscal_year",), year_rows)}
    counts["special_education_aid_band"] = replace_rows(
        conn, "special_education_aid_band",
        ("fiscal_year", "band", "from_multiple", "to_multiple", "state_share", "label", "citation", "source_url"), band_rows, where, params)
    # A district's bands go with it (ON DELETE CASCADE), and come back with its new id
    counts["district_special_education_aid"] = replace_rows(
        conn, "district_special_education_aid",
        ("district_id_fk", "fiscal_year", "source_name", "students_reported", "total_cost", "entitlement", "aid_paid"),
        district_rows, where, params)
    aid_ids = {(district, year): i for i, district, year in conn.execute(text(
        "SELECT id, district_id_fk, fiscal_year FROM district_special_education_aid WHERE fiscal_year = ANY(:years)"), params).all()}
    counts["district_special_education_aid_band"] = replace_rows(
        conn, "district_special_education_aid_band", ("district_special_education_aid_id_fk", "band", "cost", "students"),
        [(aid_ids[key], band, cost, students) for key, rows in district_bands.items() for band, cost, students in rows])
    # The summary is built on both district tables; refreshing it once covers both
    refresh_dependent_views(conn, "district_special_education_aid")
    return counts
