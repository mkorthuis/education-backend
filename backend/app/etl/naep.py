"""
NAEP (the Nation's Report Card) results for every state, DC, DoDEA and the nation's public schools,
from NCES's NAEP Data Service (see naep_config.yaml).

- naep_result: each measure (average scale score; the shares at or above NAEP Basic and NAEP
  Proficient, and at NAEP Advanced) for every place and year
- naep_comparison: NAEP's own significance tests. New Hampshire against every other state, DC and
  DoDEA in the same year, adjusted for the many comparisons made at once (basis all_jurisdictions);
  New Hampshire against the national public average alone (basis pair); and each place's latest year
  against each earlier year (basis pair)
- the same for NAEP's student groups (sex, economic status and so on), for New Hampshire and the
  national public average, without the all-state tests

`fetch` saves the Data Service's answers under assets/naep/; `load` reads those files.
"""
import json
import logging
import os
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from typing import Iterable, List, Optional
from urllib.parse import urlencode
from urllib.request import urlopen

from sqlalchemy import text
from sqlalchemy.engine import Connection

from app.etl.core import config_path, configured_years, load_config, lookup_ids, upsert_rows

logger = logging.getLogger("app.etl")

CONFIG = "naep_config.yaml"
DATA_SERVICE = "https://www.nationsreportcard.gov/Dataservice/GetAdhocData.aspx"
RESULT_TABLE = "naep_result"
COMPARISON_TABLE = "naep_comparison"
RESULT_COLUMNS = ("year", "jurisdiction_id_fk", "assessment_subject_id_fk", "grade_id_fk", "naep_measure_id_fk",
                  "naep_student_group_id_fk", "value", "is_displayable")
RESULT_KEY = RESULT_COLUMNS[:6]
COMPARISON_COLUMNS = ("year", "jurisdiction_id_fk", "other_year", "other_jurisdiction_id_fk", "assessment_subject_id_fk",
                      "grade_id_fk", "naep_measure_id_fk", "naep_student_group_id_fk", "basis", "result", "difference")
COMPARISON_KEY = COMPARISON_COLUMNS[:9]

# The Data Service's verdict on the first place or year against the other
RESULTS = {"HIGHER": "higher", "LOWER": "lower", "EQUAL": "not_significant"}

# Fields kept from each Data Service record, by the kind of file
FIELDS = {
    "results": ("year", "sample", "stattype", "subject", "grade", "jurisdiction", "variable", "varValue", "value",
                "isStatDisplayable", "errorFlag"),
    "states": ("year", "sample", "statType", "subject", "grade", "focalJurisdiction", "targetJurisdiction", "variable",
               "valValue", "focalValue", "targetValue", "gap", "sig", "isSigDisplayable", "focalErrorFlag", "targetErrorFlag"),
    "years": ("focalYear", "targetYear", "focalSample", "targetSample", "statType", "subject", "grade", "jurisdiction",
              "variable", "valValue", "focalValue", "targetValue", "gap", "sig", "isSigDisplayable", "focalErrorFlag",
              "targetErrorFlag"),
}
FIELDS["nation"] = FIELDS["states"]
BASIS = {"states": "all_jurisdictions", "nation": "pair", "years": "pair"}
# Each kind of saved file, the kind of request it holds, and its file name's start
KINDS = {
    "results": ("results", "results"),
    "states": ("states", "compare-states"),
    "nation": ("nation", "compare-nation"),
    "years": ("years", "compare-years"),
    "group-results": ("results", "groups-results"),
    "group-nation": ("nation", "groups-compare-nation"),
    "group-years": ("years", "groups-compare-years"),
}

PARALLEL_REQUESTS = 4
TRIES = 3


def file_name(kind: str, subject: str, grade: int) -> str:
    """The saved file for one kind of request: results-mathematics-grade4.json, compare-states-..."""
    return f"{KINDS[kind][1]}-{subject}-grade{grade}.json"


def _url(subject: dict, subject_name: str, grade: int, variable: str = "TOTAL", **params) -> str:
    query = {"subject": subject_name, "grade": grade, "subscale": subject["scale"], "variable": variable, **params}
    return f"{DATA_SERVICE}?{urlencode(query, safe=':,')}"


def requests_for(config: dict) -> dict:
    """{(kind, subject, grade): [url, ...]}: the Data Service requests behind each saved file."""
    places = list(config["jurisdictions"])
    states = [code for code, place in config["jurisdictions"].items() if place["kind"] != "nation"]
    nation = next(code for code, place in config["jurisdictions"].items() if place["kind"] == "nation")
    focal = config["focal_jurisdiction"]
    years = sorted(config["years"])
    all_years = ",".join(map(str, years))
    compared = ",".join(config["compared_measures"])
    variables = [variable for variable in config["student_groups"] if variable != "TOTAL"]
    group_places = ",".join(config["group_jurisdictions"])
    plan = {}
    for subject_name, subject in config["subjects"].items():
        for grade in config["grades"]:
            common = dict(subject=subject, subject_name=subject_name, grade=grade)
            plan[("results", subject_name, grade)] = [_url(**common, type="data", jurisdiction=",".join(places),
                                                           stattype=",".join(config["measures"]), Year=",".join(map(str, years)))]
            plan[("states", subject_name, grade)] = [_url(**common, type="sigacrossjuris", jurisdiction=",".join(states),
                                                          stattype=compared, Year=",".join(map(str, years)))]
            plan[("nation", subject_name, grade)] = [_url(**common, type="sigacrossjuris", jurisdiction=f"{focal},{nation}",
                                                          stattype=compared, Year=",".join(map(str, years)))]
            # One pair of years per request, so each test is of those two years alone
            plan[("years", subject_name, grade)] = [_url(**common, type="sigacrossyear", jurisdiction=",".join(places),
                                                         stattype=compared, Year=f"{earlier},{years[-1]}")
                                                    for earlier in years[:-1]]
            # Student groups, one variable per request
            plan[("group-results", subject_name, grade)] = [
                _url(**common, variable=v, type="data", jurisdiction=group_places, stattype=",".join(config["measures"]),
                     Year=all_years) for v in variables]
            plan[("group-nation", subject_name, grade)] = [
                _url(**common, variable=v, type="sigacrossjuris", jurisdiction=f"{focal},{nation}", stattype=compared,
                     Year=all_years) for v in variables]
            plan[("group-years", subject_name, grade)] = [
                _url(**common, variable=v, type="sigacrossyear", jurisdiction=group_places, stattype=compared,
                     Year=f"{earlier},{years[-1]}") for v in variables for earlier in years[:-1]]
    return plan


def _get(url: str) -> List[dict]:
    """One Data Service answer's records, tried again after a failure."""
    for attempt in range(1, TRIES + 1):
        try:
            with urlopen(url, timeout=300) as response:
                body = json.load(response)
            if body.get("status") != 200 or not isinstance(body.get("result"), list):
                raise ValueError(f"Unexpected answer: status {body.get('status')}")
            return body["result"]
        except Exception as error:
            if attempt == TRIES:
                raise RuntimeError(f"NAEP Data Service request failed: {url}") from error
            logger.warning(f"NAEP request failed ({error}); trying again")
            time.sleep(10 * attempt)


def keep(kind: str, records: List[dict], config: dict) -> List[dict]:
    """The records worth saving, with only the fields the loader reads: the configured student groups,
    New Hampshire's comparisons, and each place's latest year against the others."""
    request = KINDS[kind][0]
    focal, latest = config["focal_jurisdiction"], max(config["years"])
    groups = config["student_groups"]
    records = [r for r in records
               if str(r.get("varValue", r.get("valValue"))) in groups.get(r["variable"], {}).get("values", {})]
    if request in ("states", "nation"):
        records = [r for r in records if r["focalJurisdiction"] == focal]
    elif request == "years":
        records = [r for r in records if r["focalYear"] == latest]
    return [{field: r.get(field) for field in FIELDS[request]} for r in records]


def _write(path: str, urls: List[str], records: List[dict]) -> None:
    """A saved file: where it came from, then one record per line."""
    header = json.dumps({"source": "NCES NAEP Data Service", "fetched": date.today().isoformat(), "queries": urls})
    lines = ",\n".join(json.dumps(record, separators=(",", ":")) for record in records)
    with open(path, "w") as f:
        f.write(f'{header[:-1]}, "records": [\n{lines}\n]}}\n')


def fetch(years: Optional[Iterable[int]] = None) -> dict:
    """Ask the Data Service for every configured year and save the answers under assets/naep/."""
    if years:
        raise ValueError("The NAEP fetch always asks for every configured year; add a year to the config first")
    config = load_config(CONFIG)
    directory = config_path(config["file_settings"]["directory"])
    os.makedirs(directory, exist_ok=True)
    plan = requests_for(config)
    urls = [url for file_urls in plan.values() for url in file_urls]
    logger.info(f"NAEP: {len(urls)} requests, {PARALLEL_REQUESTS} at a time")
    with ThreadPoolExecutor(PARALLEL_REQUESTS) as pool:
        answers = dict(zip(urls, pool.map(_get, urls)))
    saved = {}
    for (kind, subject, grade), file_urls in plan.items():
        records = keep(kind, [record for url in file_urls for record in answers[url]], config)
        name = file_name(kind, subject, grade)
        _write(os.path.join(directory, name), file_urls, records)
        saved[name] = len(records)
    return saved


def _subject_and_grade(record: dict, config: dict) -> tuple:
    subject = next((name for name, s in config["subjects"].items() if s["code"] == record["subject"]), None)
    grade = config["grades"].get(record["grade"])
    if subject is None or grade is None:
        raise ValueError(f"Unexpected subject or grade: {record['subject']}, {record['grade']}")
    return config["subjects"][subject]["assessment_subject"], grade


def _check(record: dict, config: dict, samples: tuple) -> None:
    if any(sample != config["sample"] for sample in samples):
        raise ValueError(f"Unexpected NAEP sample {samples}; only {config['sample']} is loaded")
    if record["stattype" if "stattype" in record else "statType"] not in config["measures"]:
        raise ValueError(f"Unexpected NAEP measure: {record}")


def _group(record: dict, config: dict) -> tuple:
    variable, value = record["variable"], str(record.get("varValue", record.get("valValue")))
    if value not in config["student_groups"].get(variable, {}).get("values", {}):
        raise ValueError(f"Unexpected NAEP student group {(variable, value)}")
    return variable, value


def parse_results(records: List[dict], config: dict) -> dict:
    """{(year, place, subject, grade, measure, group): (value, displayable)}. A figure that doesn't
    meet NAEP's reporting standards is kept as not displayable, with no value."""
    results = {}
    for r in records:
        _check(r, config, (r["sample"],))
        if r["jurisdiction"] not in config["jurisdictions"]:
            raise ValueError(f"Unexpected NAEP place {r['jurisdiction']}")
        subject, grade = _subject_and_grade(r, config)
        displayable = bool(r["isStatDisplayable"])
        key = (r["year"], r["jurisdiction"], subject, grade, r["stattype"], _group(r, config))
        results[key] = (r["value"] if displayable else None, displayable)
    return results


def parse_comparisons(kind: str, records: List[dict], config: dict) -> dict:
    """{(year, place, other year, other place, subject, grade, measure, group, basis): (result, difference)}.
    Tests NAEP couldn't report are left out."""
    comparisons = {}
    for r in records:
        if kind == "years":
            _check(r, config, (r["focalSample"], r["targetSample"]))
            places, years = (r["jurisdiction"], r["jurisdiction"]), (r["focalYear"], r["targetYear"])
        else:
            _check(r, config, (r["sample"],))
            places, years = (r["focalJurisdiction"], r["targetJurisdiction"]), (r["year"], r["year"])
        if not r["isSigDisplayable"]:
            continue
        if r["sig"] not in RESULTS:
            raise ValueError(f"Unexpected NAEP significance result {r['sig']}")
        subject, grade = _subject_and_grade(r, config)
        key = (years[0], places[0], years[1], places[1], subject, grade, r["statType"], _group(r, config), BASIS[kind])
        comparisons[key] = (RESULTS[r["sig"]], r["gap"])
    return comparisons


def read_file(path: str) -> List[dict]:
    if not os.path.exists(path):
        raise FileNotFoundError(f"NAEP file not found: {path}; run `python -m app.etl fetch naep`")
    with open(path) as f:
        return json.load(f)["records"]


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the given years (default: every configured year) into naep_result and naep_comparison,
    adding the places, measures and student groups in config order."""
    config = load_config(CONFIG)
    years = set(configured_years(config["file_settings"], years)) & set(config["years"])
    directory = config_path(config["file_settings"]["directory"])

    counts = {
        "jurisdiction": upsert_rows(conn, "jurisdiction", ("code", "name", "kind"), ("code",),
                                    [(code, place["name"], place["kind"]) for code, place in config["jurisdictions"].items()]),
        "naep_measure": upsert_rows(conn, "naep_measure", ("code", "name", "unit"), ("code",),
                                    [(code, m["name"], m["unit"]) for code, m in config["measures"].items()]),
        "naep_student_group": upsert_rows(conn, "naep_student_group", ("variable", "value", "variable_name", "name"),
                                          ("variable", "value"),
                                          [(variable, value, group["name"], name) for variable, group in config["student_groups"].items()
                                           for value, name in group["values"].items()]),
    }
    places = lookup_ids(conn, "jurisdiction", "code")
    measures = lookup_ids(conn, "naep_measure", "code")
    groups = {(variable, value): id for variable, value, id in conn.execute(text("SELECT variable, value, id FROM naep_student_group"))}
    subjects = lookup_ids(conn, "assessment_subject")
    grades = lookup_ids(conn, "grades")

    results, comparisons = {}, {}
    for subject_name in config["subjects"]:
        for grade in config["grades"]:
            for kind, (request, _) in KINDS.items():
                records = read_file(os.path.join(directory, file_name(kind, subject_name, grade)))
                if request == "results":
                    results.update(parse_results(records, config))
                else:
                    comparisons.update(parse_comparisons(request, records, config))

    result_rows = sorted(
        (year, places[place], subjects[subject], grades[grade], measures[measure], groups[group], value, displayable)
        for (year, place, subject, grade, measure, group), (value, displayable) in results.items() if year in years
    )
    comparison_rows = sorted(
        (year, places[place], other_year, places[other], subjects[subject], grades[grade], measures[measure], groups[group],
         basis, result, difference)
        for (year, place, other_year, other, subject, grade, measure, group, basis), (result, difference) in comparisons.items()
        if year in years
    )
    missing = sorted(years - {row[0] for row in result_rows})
    if missing:
        logger.warning(f"NAEP: no results for years {missing}")
    counts[RESULT_TABLE] = upsert_rows(conn, RESULT_TABLE, RESULT_COLUMNS, RESULT_KEY, result_rows)
    counts[COMPARISON_TABLE] = upsert_rows(conn, COMPARISON_TABLE, COMPARISON_COLUMNS, COMPARISON_KEY, comparison_rows)
    return counts
