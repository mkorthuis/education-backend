"""
The Ask's tools for how New Hampshire compares with other states and the nation: NAEP results (the
Nation's Report Card) and Census Bureau school system revenue by state.

Their datasets have no site page: the site doesn't show these figures yet, so an answer names the
source instead of linking to a page.
"""
from typing import Dict, List, Optional

from sqlmodel import Session, select

from app.etl.core import load_config
from app.model.assessment import AssessmentSubject
from app.model.location import Grade
from app.model.naep import Jurisdiction
from app.service.internal.ask.data_tools import DataToolError, _once, dataset, school_year
from app.service.public.census_finance_service import census_finance_service
from app.service.public.naep_service import naep_service

NATION = "US"  # the tools' code for the nation; NAEP's own is NP (the national public average)
NAEP_NATION = "NP"
FOCAL = "NH"
MAX_PLACES = 6

NAEP_SUBJECTS = {"math": "mat", "reading": "rea"}  # → assessment_subject names
NAEP_GRADES = {4: "Grade 4", 8: "Grade 8"}
NAEP_MEASURES = {
    "average_score": ("MN:MN", "Average score", "number"),
    "at_or_above_basic": ("ALC:AB", "At or above NAEP Basic", "percent"),
    "at_or_above_proficient": ("ALC:AP", "At or above NAEP Proficient", "percent"),
    "at_advanced": ("ALC:AD", "At NAEP Advanced", "percent"),
}
# NAEP's student groups as loaded (naep_config.yaml); groups other than all students are for New
# Hampshire and the nation only
NAEP_GROUPS = [name for group in load_config("naep_config.yaml")["student_groups"].values() for name in group["values"].values()]
VERDICTS = {"higher": "higher", "lower": "lower", "not_significant": "not significantly different"}
NAEP_NOTE = (
    "NAEP, the Nation's Report Card, is run by NCES (the National Center for Education Statistics, part of the U.S. "
    "Department of Education); public schools, tested January to March of the year shown. Scores are on NAEP's 0-500 scale. "
    "NCES says NAEP Proficient does not represent grade-level proficiency; it is a higher bar than proficient on New "
    "Hampshire's state test, so the two percentages aren't comparable. A difference counts only where NAEP's significance "
    "test finds one: New Hampshire is tested against every state at once, as in NAEP's state reports, and against the "
    "national public average on its own; a place's latest year is tested against each earlier year. A blank means NAEP "
    "doesn't report it (too few students)."
)

# The outside page each kind of dataset comes from, shown as a source when an answer uses it
NAEP_SOURCE = {"label": "NAEP Data Explorer (National Center for Education Statistics)",
               "url": "https://www.nationsreportcard.gov/ndecore/xplore/NDE", "site": "nationsreportcard.gov", "as_of": None}
CENSUS_SOURCE = {"label": "U.S. Census Bureau, Annual Survey of School System Finances",
                 "url": "https://www2.census.gov/programs-surveys/school-finances/tables/", "site": "census.gov", "as_of": None}


def _sourced(datasets: List[dict], source: dict) -> dict:
    for item in datasets:
        item["source"] = source
    return {"datasets": datasets}


REVENUE_MEASURES = {"per_pupil": "dollars", "share_of_total": "percent", "amount": "dollars"}
REVENUE_SOURCES = ("total", "federal", "state", "local")
REVENUE_NOTE = (
    "U.S. Census Bureau, Annual Survey of School System Finances: all revenue of each state's public school systems, "
    "including money for buildings and debt, in current dollars (not adjusted for inflation), by fiscal year (2023-24 is "
    "FY2024, mostly July to June). Shares and revenue per pupil are calculated from Census's figures, using the fall "
    "enrollment Census uses for its own per-pupil amounts; Census publishes per-pupil spending, not revenue. These "
    "differ from NH DOE's cost per pupil on the site's Financials pages, which counts operating spending only. The District "
    "of Columbia has no state government, so none of its revenue is from a state; rankings of the states should set it aside."
)


def _places(session: Session, codes: List[str]) -> Dict[str, Jurisdiction]:
    """The places asked for, by the tools' codes (US for the nation), checked."""
    known = _once(session, "jurisdictions", lambda: {p.code: p for p in session.exec(select(Jurisdiction)).all()})
    places = {}
    for code in dict.fromkeys(c.strip().upper() for c in codes):
        if code not in known:
            raise DataToolError(f"Unknown place {code}; use two-letter state codes (NH, MA, DC) or US for the nation.")
        places[code] = known[code]
    if len(places) > MAX_PLACES:
        raise DataToolError(f"Compare up to {MAX_PLACES} places at once, or leave places empty to rank every state.")
    return places


def _label(place: Jurisdiction) -> str:
    return {"US": "United States", "NP": "United States (public schools)", "DS": "Defense Department schools (DoDEA)"}.get(place.code, place.name)


# -------------------- NAEP --------------------

def _naep_ids(session: Session) -> dict:
    def load():
        return {
            "subjects": {s.name: s.id for s in session.exec(select(AssessmentSubject)).all()},
            "grades": {g.name: g.id for g in session.exec(select(Grade)).all()},
            "measures": {m.code: m.id for m in naep_service.get_measures(session)},
            "groups": {g.name: g for g in naep_service.get_student_groups(session)},
        }
    return _once(session, "naep_ids", load)


def naep_results(session: Session, subject: str, grade: int, measure: str, places: List[str],
                 student_group: str = "All students") -> dict:
    """NAEP results by year for up to six places, with NAEP's tests of New Hampshire against each in the
    latest year and against its own earlier years; with no places, every state ranked in the latest year."""
    if subject not in NAEP_SUBJECTS or grade not in NAEP_GRADES or measure not in NAEP_MEASURES:
        raise DataToolError("NAEP covers math and reading in grades 4 and 8, with average_score, at_or_above_basic, "
                            "at_or_above_proficient or at_advanced.")
    ids = _naep_ids(session)
    group = ids["groups"].get(student_group)
    if group is None:
        raise DataToolError(f"Unknown NAEP student group {student_group}; use one of: {', '.join(ids['groups'])}.")
    code, label, unit = NAEP_MEASURES[measure]
    chosen = _places(session, places)
    naep_codes = {NAEP_NATION if c == NATION else c: c for c in chosen}
    if group.variable != "TOTAL" and (not chosen or set(naep_codes) - {FOCAL, NAEP_NATION}):
        raise DataToolError("NAEP student groups are loaded for New Hampshire and the nation (US) only; ask for those places.")
    filters = dict(assessment_subject_id=ids["subjects"][NAEP_SUBJECTS[subject]], grade_id=ids["grades"][NAEP_GRADES[grade]],
                   naep_measure_id=ids["measures"][code], naep_student_group_id=group.id)
    what = f"{label}, grade {grade} {subject}" + ("" if group.variable == "TOTAL" else f", {group.name}")
    value = lambda r: (round(r["value"]) if unit == "number" else round(r["value"], 1)) if r["is_displayable"] else None

    if not chosen:
        rows = naep_service.get_results(session, **filters)
        latest = max(r["year"] for r in rows)
        latest_rows = [r for r in rows if r["year"] == latest and r["jurisdiction"]["kind"] != "other"]
        verdicts = {t["other_jurisdiction"]["code"]: VERDICTS[t["result"]] for t in naep_service.get_comparisons(
            session, year=latest, other_year=latest, jurisdiction=FOCAL, **filters)}
        ranked = sorted(latest_rows, key=lambda r: -(r["value"] or 0))
        return _sourced([dataset(
            f"NAEP {what}, {latest}, every state", unit, ["Place", label, "New Hampshire compared with it"],
            [[_label_from(r["jurisdiction"]), value(r), "-" if r["jurisdiction"]["code"] == FOCAL else verdicts.get(r["jurisdiction"]["code"])]
             for r in ranked],
            None, NAEP_NOTE, {"New Hampshire compared with it": "number"},
        )], NAEP_SOURCE)

    by_year: Dict[int, dict] = {}
    for naep_code, tool_code in naep_codes.items():
        for r in naep_service.get_results(session, jurisdiction=naep_code, **filters):
            by_year.setdefault(r["year"], {})[tool_code] = value(r)
    names = [_label(chosen[c]) for c in chosen]
    years = sorted(by_year)
    latest = years[-1]
    datasets = [dataset(f"NAEP {what} by year: {', '.join(names)}", unit, ["Year", *names],
                        [[str(year), *(by_year[year].get(c) for c in chosen)] for year in years], None, NAEP_NOTE)]

    # New Hampshire against each other place, in each year NAEP tested them
    others = [(n, c) for n, c in naep_codes.items() if n != FOCAL]
    if others:
        tests = {(t["year"], t["other_jurisdiction"]["code"]): VERDICTS[t["result"]]
                 for t in naep_service.get_comparisons(session, jurisdiction=FOCAL, **filters) if t["other_year"] == t["year"]}
        datasets.append(dataset(
            f"NAEP's test of New Hampshire against each place by year, {what}", "number",
            ["Year", *(f"New Hampshire compared with {_label(chosen[c])}" for _, c in others)],
            [[str(year), *(tests.get((year, n)) for n, _ in others)] for year in years], None, NAEP_NOTE,
        ))
    # Each place's latest year against its earlier years
    against_years = {}
    for n, c in naep_codes.items():
        for t in naep_service.get_comparisons(session, year=latest, jurisdiction=n, other_jurisdiction=n, **filters):
            against_years.setdefault(t["other_year"], {})[c] = VERDICTS[t["result"]]
    if against_years:
        datasets.append(dataset(
            f"NAEP's test of each place's {latest} result against earlier years, {what}", "number",
            ["Earlier year", *(f"{_label(chosen[c])} in {latest} is" for c in chosen)],
            [[str(year), *(against_years[year].get(c) for c in chosen)] for year in sorted(against_years)], None, NAEP_NOTE,
        ))
    return _sourced(datasets, NAEP_SOURCE)


def _label_from(place: dict) -> str:
    return {"NP": "United States (public schools)"}.get(place["code"], place["name"])


# -------------------- Census school revenue --------------------

def state_school_revenue(session: Session, places: List[str], measure: str = "per_pupil", source: str = "total") -> dict:
    """Census school system revenue for up to six places: the chosen source by year, every source in the
    latest year, and the categories within each source; with no places, every state ranked."""
    if measure not in REVENUE_MEASURES or source not in REVENUE_SOURCES:
        raise DataToolError("Measures: per_pupil, share_of_total or amount; sources: total, federal, state or local.")
    unit = REVENUE_MEASURES[measure]
    if measure == "share_of_total" and source == "total":
        raise DataToolError("The share of total revenue is for federal, state or local revenue; choose a source.")
    pick = lambda part: part[measure] if measure != "share_of_total" else part["share_of_total"]
    label = {"per_pupil": "revenue per pupil", "share_of_total": "share of all revenue", "amount": "revenue"}[measure]
    what = f"{source.capitalize() if source != 'total' else 'Total'} school {label}"
    chosen = _places(session, places)

    if not chosen:
        rows = census_finance_service.get_summary(session)
        latest = max(r["year"] for r in rows)
        ranked = sorted((r for r in rows if r["year"] == latest), key=lambda r: -(pick(r[source]) or 0))
        return _sourced([dataset(
            f"{what}, {school_year(latest)}, every state", unit, ["Place", what], [[_label_from(r["jurisdiction"]), pick(r[source])] for r in ranked],
            None, REVENUE_NOTE,
        )], CENSUS_SOURCE)

    summaries = {code: census_finance_service.get_summary(session, jurisdiction=code) for code in chosen}
    names = [_label(chosen[c]) for c in chosen]
    years = sorted({r["year"] for rows in summaries.values() for r in rows})
    latest = years[-1]
    by_year = {code: {r["year"]: r for r in rows} for code, rows in summaries.items()}
    datasets = [dataset(
        f"{what} by year: {', '.join(names)}", unit, ["School year", *names],
        [[school_year(y), *(pick(by_year[c][y][source]) if y in by_year[c] else None for c in chosen)] for y in years],
        None, REVENUE_NOTE,
    )]
    datasets.append(dataset(
        f"School revenue by source, {school_year(latest)}", "dollars",
        ["Place", "Revenue per pupil", "Federal per pupil", "State per pupil", "Local per pupil", "Federal share", "State share", "Local share",
         "Enrollment"],
        [[_label(chosen[c]), *(by_year[c][latest][s]["per_pupil"] for s in REVENUE_SOURCES),
          *(by_year[c][latest][s]["share_of_total"] for s in REVENUE_SOURCES[1:]), by_year[c][latest]["enrollment"]]
         for c in chosen if latest in by_year[c]],
        None, REVENUE_NOTE,
        {"Federal share": "percent", "State share": "percent", "Local share": "percent", "Enrollment": "count"},
    ))
    categories: Dict[tuple, dict] = {}
    for code in chosen:
        for r in census_finance_service.get_revenue(session, year=latest, jurisdiction=code, level="category",
                                                    source=None if source == "total" else source):
            categories.setdefault((r["source"], r["category"]), {})[code] = r
    datasets.append(dataset(
        f"School revenue per pupil by category, {school_year(latest)}" + ("" if source == "total" else f", {source} sources"), "dollars",
        ["Category", *names, *(f"{n}: share of its source" for n in names)],
        [[f"{src.capitalize()}: {category}", *(values[c]["per_pupil"] if c in values else None for c in chosen),
          *(values[c]["share_of_source"] if c in values else None for c in chosen)]
         for (src, category), values in categories.items()],
        None, REVENUE_NOTE + " Categories are the columns of Census's summary tables (Title I, property taxes and so on).",
        {f"{n}: share of its source": "percent" for n in names},
    ))
    return _sourced(datasets, CENSUS_SOURCE)
