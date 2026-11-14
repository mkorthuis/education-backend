"""
New Hampshire adequacy aid: NH DOE's calculation for each town and how each town's grant divides among its school
districts (see adequacy_aid_config.yaml):

- adequacy_aid_year: each fiscal year loaded, its status and the DOE's files
- adequacy_aid_component: every part of the calculation in any year
- adequacy_aid_parameter, adequacy_aid_step: each year's rates and thresholds, and how its calculation works
- town_adequacy_aid, state_adequacy_aid: each town's value for each part, as the DOE publishes it, and the DOE's
  statewide totals
- district_adequacy_aid_share: each district's share of each member town's grant and SWEPT

Values are the DOE's, never recomputed. The load checks them: each step's formula must reproduce the DOE's figure
for every town, the towns must add up to the DOE's state totals, and each split town's shares must add up to its
grant and SWEPT. town_adequacy_aid_summary and district_adequacy_aid are built on these tables.
"""
import logging
import os
from datetime import date
from typing import Iterable, List, Optional

import openpyxl
from openpyxl.utils import column_index_from_string
from sqlalchemy import text
from sqlalchemy.engine import Connection

from app.etl.core import config_path, load_config, lookup_ids, refresh_dependent_views, replace_rows, upsert_rows
from app.etl.formula import evaluate, names

logger = logging.getLogger("app.etl")

CONFIG = "adequacy_aid_config.yaml"
ROLES = ("students", "cost", "cost_total", "swept", "added_aid", "hold_harmless", "result", "basis")
COMPONENT_UNITS = ("count", "dollars", "dollars_per_pupil", "fraction")
PARAMETER_UNITS = ("dollars_per_pupil", "dollars", "fraction", "dollars_per_thousand", "dollars_per_dollar")
STATUSES = ("final", "estimate")
SHARE_SOURCES = ("doe_split", "whole_town")
# The parts the towns' values should add up to in the DOE's state row
SUMMED_ROLES = ("students", "cost", "cost_total", "swept", "added_aid", "hold_harmless", "result")
# How far the places' sum may be from the DOE's state total: the state row's SWEPT isn't rounded as each town's is
# ($5.46 off on $363 million at most), so a ten-millionth of the total, at least $1
STATE_TOLERANCE = 1e-7


def _number(value):
    """A workbook cell as a number, or None when it's blank or an Excel error ("#DIV/0!")."""
    if isinstance(value, bool) or value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        value = value.strip().replace(",", "")
        if not value or value.startswith("#") or value == "-":
            return None
        try:
            return float(value)
        except ValueError:
            pass
    raise ValueError(f"Not a number: {value!r}")


def _column(letter: str) -> int:
    return column_index_from_string(letter) - 1


def read_summary(config: dict, year: int) -> tuple:
    """({town id: {component: value}}, {place name: {component: value}} for the lettered unincorporated places,
    {component: value} for the DOE's state row) from a year's workbook. A blank cell (or an Excel error) leaves the
    part out for that place."""
    settings = config["years"][year]["summary"]
    path = os.path.join(config_path(config["directory"]), settings["file"])
    workbook = openpyxl.load_workbook(path, read_only=True, data_only=True)
    last = max(settings["last_row"], *(settings.get("unincorporated_rows") or [0]))
    rows = list(workbook[settings["sheet"]].iter_rows(max_row=last, values_only=True))
    columns = {component: _column(letter) for component, letter in settings["columns"].items()}
    town_column = _column(settings["town_column"])

    def values(row, where):
        found = {}
        for component, index in columns.items():
            try:
                value = _number(row[index] if index < len(row) else None)
            except ValueError as e:
                raise ValueError(f"FY{year} {where}, {component}: {e}")
            if value is not None:
                found[component] = value
        return found

    towns = {}
    for number in range(settings["first_row"], settings["last_row"] + 1):
        row = rows[number - 1]
        town = row[town_column] if town_column < len(row) else None
        if not isinstance(town, (int, float)) or isinstance(town, bool) or int(town) != town:
            continue  # a blank or subtotal row
        if int(town) in towns:
            raise ValueError(f"FY{year}: town {int(town)} is in the workbook twice")
        towns[int(town)] = values(row, f"row {number}")
    others = {}
    if settings.get("unincorporated_rows"):
        first, last = settings["unincorporated_rows"]
        for number in range(first, last + 1):
            row = rows[number - 1]
            label, name = row[town_column], row[town_column + 1]
            if not (isinstance(label, str) and len(label.strip()) == 1 and isinstance(name, str)):
                raise ValueError(f"FY{year} row {number} isn't a lettered unincorporated place: {row[:6]}")
            others[name.strip()] = values(row, f"row {number}")
    state = values(rows[settings["state_row"] - 1], "the state row")
    return towns, others, state


def read_split(config: dict, year: int) -> List[tuple]:
    """[(district id, town id, name, adequacy grant, SWEPT kept)] from a year's split workbook."""
    settings = config["years"][year]["split"]
    path = os.path.join(config_path(config["directory"]), settings["file"])
    workbook = openpyxl.load_workbook(path, read_only=True, data_only=True)
    rows = list(workbook[settings["sheet"]].iter_rows(max_row=settings["last_row"], values_only=True))
    c = {key: _column(letter) for key, letter in settings["columns"].items()}
    fixes = settings.get("town_fixes") or {}
    shares = []
    for number in range(settings["first_row"], settings["last_row"] + 1):
        row = rows[number - 1]
        district, town, name = (row[c[k]] if c[k] < len(row) else None for k in ("district", "town", "name"))
        if not isinstance(district, (int, float)) or not isinstance(town, (int, float)) or not isinstance(name, str):
            continue  # a blank or total row
        name = name.strip()
        town = fixes.get(name, int(town))
        grant, swept, total = (_number(row[c[k]]) for k in ("adequacy_grant", "swept_retained", "total"))
        if (grant is None or swept is None) and total:
            raise ValueError(f"FY{year} split row {number} ({name}): a blank amount but a total of {total}")
        grant, swept = grant or 0.0, swept or 0.0
        if total is not None and abs(grant + swept - total) > 0.01:
            raise ValueError(f"FY{year} split row {number} ({name}): {grant} + {swept} isn't its total {total}")
        if town == 0:
            raise ValueError(f"FY{year} split row {number} ({name}) has no town number; add it to town_fixes")
        shares.append((int(district), int(town), name, grant, swept))
    return shares


def check_steps(config: dict, year: int, towns: dict) -> int:
    """Each step's formula against the DOE's published value for every town. Returns how many values it checked;
    a value off by more than the step's tolerance stops the load."""
    settings = config["years"][year]
    components = set(settings["summary"]["columns"])
    parameters = {code: p["value"] for code, p in settings["parameters"].items()}
    checked, problems = 0, []
    for step in settings["steps"]:
        if step["component"] not in components:
            raise ValueError(f"FY{year} step for {step['component']}, which isn't in the year's columns")
        if not step.get("formula"):
            continue
        unknown = names(step["formula"]) - components - set(parameters)
        if unknown:
            raise ValueError(f"FY{year} {step['component']}'s formula uses {sorted(unknown)}, which aren't the year's components or parameters")
        for town, values in towns.items():
            if step["component"] not in values:
                continue
            env = {**{c: 0.0 for c in components}, **values, **parameters}
            try:
                found = evaluate(step["formula"], env)
            except ZeroDivisionError:
                continue  # a town with none of the students a share divides by
            checked += 1
            if abs(found - values[step["component"]]) > step.get("tolerance", 0.02):
                problems.append(f"town {town} {step['component']}: the formula gives {found:,.2f}, the DOE {values[step['component']]:,.2f}")
    if problems:
        raise ValueError(f"FY{year}: {len(problems)} values don't match their step's formula: {problems[:5]}")
    return checked


def check_state(config: dict, year: int, towns: dict, state: dict, roles: dict) -> None:
    """The towns add up to the DOE's state row for every part that sums."""
    problems = []
    for component, total in state.items():
        if roles[component] not in SUMMED_ROLES:
            continue
        found = sum(values.get(component, 0.0) for values in towns.values())
        if abs(found - total) > max(1.0, STATE_TOLERANCE * abs(total)):
            problems.append(f"{component}: towns {found:,.2f}, state row {total:,.2f}")
    if problems:
        raise ValueError(f"FY{year}: the towns don't add up to the DOE's state totals: {problems[:5]}")


def town_districts(conn: Connection, config: dict) -> dict:
    """{town id: [district ids]}: the current school districts each town belongs to, with the config's overrides."""
    found = {}
    for town, district in conn.execute(text(
            "SELECT x.town_id_fk, x.district_id_fk FROM town_district_xref x JOIN district d ON d.id = x.district_id_fk "
            "WHERE d.is_current AND d.kind = 'district' ORDER BY x.town_id_fk, x.district_id_fk")).all():
        found.setdefault(town, []).append(district)
    towns = {name.lower(): i for i, name in conn.execute(text("SELECT id, name FROM town")).all()}
    districts = {name.lower(): i for i, name in conn.execute(text(
        "SELECT id, name FROM district WHERE is_current AND kind = 'district'")).all()}
    for town, names_ in (config.get("town_districts") or {}).items():
        unknown = [n for n in [town] if n.lower() not in towns] + [n for n in names_ if n.lower() not in districts]
        if unknown:
            raise ValueError(f"town_districts in {CONFIG} names {unknown}, which aren't a town or current district")
        found[towns[town.lower()]] = [districts[n.lower()] for n in names_]
    return found


def district_shares(year: int, towns: dict, split: List[tuple], memberships: dict) -> List[tuple]:
    """[(district id, town id, adequacy grant, SWEPT kept, source)]: the split's shares for split towns, and the whole
    town to its one district for the rest. Split towns' shares must add up to the town's grant and SWEPT."""
    shares, split_towns = [], {}
    for district, town, name, grant, swept in split:
        split_towns.setdefault(town, []).append((district, grant, swept))
    for town, parts in split_towns.items():
        if town not in towns:
            raise ValueError(f"FY{year}: the split has town {town}, which the workbook doesn't")
        grant, swept = sum(p[1] for p in parts), sum(p[2] for p in parts)
        if abs(grant - towns[town].get("adequacy_grant", 0.0)) > 0.01 or abs(swept - towns[town].get("swept", 0.0)) > 0.5:
            raise ValueError(f"FY{year}: town {town}'s shares ({grant:,.2f}, {swept:,.2f}) don't add up to its grant and SWEPT")
        shares.extend((district, town, g, s, "doe_split") for district, g, s in parts)
    for town, values in towns.items():
        if town in split_towns:
            continue
        districts = memberships.get(town, [])
        if len(districts) != 1:
            raise ValueError(f"FY{year}: town {town} isn't in the split and belongs to {len(districts)} current districts "
                             f"({districts}); add it to town_districts in {CONFIG}")
        shares.append((districts[0], town, values.get("adequacy_grant", 0.0), values.get("swept", 0.0), "whole_town"))
    return sorted(shares, key=lambda s: (s[0], s[1]))


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the config's years (or those given): the components, each year's parameters and steps, every town's
    values, the state totals and the district shares, after checking them. Then refresh the views built on them."""
    config = load_config(CONFIG)
    configured = sorted(config["years"])
    years = sorted(set(years or configured))
    unknown = [y for y in years if y not in configured]
    if unknown:
        raise ValueError(f"Fiscal years {unknown} aren't in {CONFIG}: {configured}")

    components = config["components"]
    bad = [c["code"] for c in components if c["role"] not in ROLES or c["unit"] not in COMPONENT_UNITS]
    if bad:
        raise ValueError(f"Components with an unknown role or unit in {CONFIG}: {bad}")
    roles = {c["code"]: c["role"] for c in components}
    counts = {"adequacy_aid_component": upsert_rows(
        conn, "adequacy_aid_component", ("code", "name", "description", "unit", "role", "sort"), ("code",),
        [(c["code"], c["name"], c["description"], c["unit"], c["role"], sort) for sort, c in enumerate(components, start=1)])}
    component_ids = lookup_ids(conn, "adequacy_aid_component", "code")
    counts["adequacy_aid_year"] = upsert_rows(
        conn, "adequacy_aid_year", ("fiscal_year", "school_year", "status", "as_of", "summary_url", "split_url", "explained_url"),
        ("fiscal_year",),
        [(year, str(y["school_year"]), y["status"], date.fromisoformat(str(y["as_of"])), y["summary"]["url"], y["split"]["url"],
          y["explained_url"]) for year, y in sorted(config["years"].items())])

    known_towns = {i for (i,) in conn.execute(text("SELECT id FROM town")).all()}
    known_districts = {i for (i,) in conn.execute(text("SELECT id FROM district")).all()}
    memberships = town_districts(conn, config)
    town_rows, state_rows, parameter_rows, step_rows, share_rows = [], [], [], [], []
    for year in years:
        settings = config["years"][year]
        unknown = [c for c in settings["summary"]["columns"] if c not in component_ids]
        if unknown:
            raise ValueError(f"FY{year} columns {unknown} aren't in components in {CONFIG}")
        bad = [code for code, p in settings["parameters"].items() if p["unit"] not in PARAMETER_UNITS]
        if bad:
            raise ValueError(f"FY{year} parameters with an unknown unit: {bad}")
        places, lettered, state = read_summary(config, year)
        checked = check_steps(config, year, places)
        check_state(config, year, {**places, **lettered}, state, roles)
        # Unincorporated places count in the checks, but have no town row or district
        unincorporated = {int(k) for k in config.get("unincorporated") or {}}
        unknown = sorted(set(places) - known_towns - unincorporated)
        if unknown:
            raise ValueError(f"FY{year}: town numbers {unknown} aren't in the town table or unincorporated in {CONFIG}")
        others = {**{config["unincorporated"][p]: places[p] for p in unincorporated & set(places)}, **lettered}
        with_students = [n for n, v in others.items() if v.get("resident_adm_base")]
        if with_students:
            raise ValueError(f"FY{year}: unincorporated places {with_students} have students")
        granted = {n: v["adequacy_grant"] for n, v in others.items() if v.get("adequacy_grant")}
        logger.info(f"Adequacy aid FY{year}: {len(others)} unincorporated places left out, with SWEPT of "
                    f"{sum(v.get('swept', 0) for v in others.values()):,.0f}" + (f" and grants {granted}" if granted else ""))
        towns = {t: v for t, v in places.items() if t not in unincorporated}
        split = read_split(config, year)
        unknown = sorted({d for d, *_ in split} - known_districts)
        if unknown:
            raise ValueError(f"FY{year}: district numbers {unknown} in the split aren't in the district table")
        shares = district_shares(year, towns, split, memberships)
        logger.info(f"Adequacy aid FY{year}: {len(towns)} towns, {sum(len(v) for v in towns.values())} values, "
                    f"{checked} checked against {sum(1 for s in settings['steps'] if s.get('formula'))} formulas; "
                    f"{len(split)} split shares; {len(shares)} district shares")

        town_rows.extend((town, year, component_ids[c], v) for town, values in sorted(towns.items()) for c, v in values.items())
        state_rows.extend((year, component_ids[c], v) for c, v in state.items())
        parameter_rows.extend((year, code, p["name"], p["value"], p["unit"], p["citation"], p["source_url"])
                              for code, p in settings["parameters"].items())
        step_rows.extend((year, number, component_ids[s["component"]], s.get("formula"), s.get("tolerance", 0.02),
                          s["explanation"], s["citation"]) for number, s in enumerate(settings["steps"], start=1))
        share_rows.extend((d, t, year, g, s, source) for d, t, g, s, source in shares)

    where, params = "fiscal_year = ANY(:years)", {"years": years}
    counts["adequacy_aid_parameter"] = replace_rows(
        conn, "adequacy_aid_parameter", ("fiscal_year", "code", "name", "value", "unit", "citation", "source_url"), parameter_rows, where, params)
    counts["adequacy_aid_step"] = replace_rows(
        conn, "adequacy_aid_step", ("fiscal_year", "step", "component_id_fk", "formula", "tolerance", "explanation", "citation"),
        step_rows, where, params)
    counts["town_adequacy_aid"] = replace_rows(
        conn, "town_adequacy_aid", ("town_id_fk", "fiscal_year", "component_id_fk", "value"), town_rows, where, params)
    counts["state_adequacy_aid"] = replace_rows(
        conn, "state_adequacy_aid", ("fiscal_year", "component_id_fk", "value"), state_rows, where, params)
    counts["district_adequacy_aid_share"] = replace_rows(
        conn, "district_adequacy_aid_share", ("district_id_fk", "town_id_fk", "fiscal_year", "adequacy_grant", "swept_retained", "source"),
        share_rows, where, params)
    for table in ("town_adequacy_aid", "district_adequacy_aid_share"):
        refresh_dependent_views(conn, table)
    return counts
