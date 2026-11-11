"""
The data tools Claude uses to answer a visitor's question.

Each tool reads the same services the site's pages use, so an answer's figures match the pages.
Data comes back as small datasets: a title, a unit, a header row and value rows, plus the site
page that shows the same data. The answer's charts and tables are built from these datasets on
the server (Claude only names which dataset to show), so their numbers always come from the
database.
"""
from collections import defaultdict
from functools import lru_cache
from typing import Callable, Dict, List, Optional
from urllib.parse import urlparse

from fastapi import HTTPException
from sqlmodel import Session

from app.etl.core import load_config
from app.service.inflation import in_dollars_of
from app.service.public.assessment_service import assessment_service
from app.service.public.class_size_service import class_size_service
from app.service.public.education_freedom_account_service import education_freedom_account_service
from app.service.public.enrollment_service import enrollment_service
from app.service.public.finance_service import finance_service
from app.service.public.location_service import location_service
from app.service.public.measurement_service import measurement_service
from app.service.public.outcome_service import outcome_service
from app.service.public.question_two_service import question_two_service
from app.service.public.safety_service import safety_service
from app.service.public.staff_service import staff_service

TOPICS = ["enrollment", "test_scores", "graduation", "spending", "balance_sheet", "staff", "safety", "efa", "question_two"]
LEVELS = ["state", "district", "school"]

# Topics each level has, with the site page that shows them. Question 2 has no page yet, so its
# datasets name their source instead.
STATE_PAGES = {
    "enrollment": "/state/enrollment",
    "test_scores": "/state/academic",
    "graduation": "/state/outcomes",
    "spending": "/state/financials",
    "staff": "/state/staff",
    "safety": "/state/safety",
    "efa": "/state/efa",
}
DISTRICT_SECTIONS = {
    "enrollment": "enrollment",
    "test_scores": "academic",
    "graduation": "outcomes",
    "spending": "financials",
    "balance_sheet": "financials/balance-sheet",
    "staff": "staff",
    "safety": "safety",
    "efa": "efa",
}
SCHOOL_SECTIONS = {
    "enrollment": "enrollment",
    "test_scores": "academic",
    "graduation": "outcomes",
    "safety": "safety",
}

SUBJECTS = {1: "Math", 2: "Reading", 3: "Science"}
ALL_STUDENTS = 1

# Plain names for the state's student group and plan labels, as the site shows them
STUDENT_GROUPS = {
    "All students": "All Students",
    "IEP/SWD": "Students with Disabilities (IEP)",
    "Not IEP/SWD": "Students Without an IEP",
    "SES": "Low-Income (Free or Reduced-Price Meals)",
    "Not SES": "Not Low-Income",
    "EL - Current": "English Learners",
    "EL - Curr + Monitor Yr1-4": "English Learners, Current and Recently Exited",
    "Am. Indian": "American Indian or Alaska Native",
    "Asian+PI+Hawaiian": "Asian or Pacific Islander",
    "Black": "Black",
    "Hispanic": "Hispanic",
    "Two or More races": "Two or More Races",
    "White": "White",
    "Female": "Female",
    "Male": "Male",
    "Foster": "In Foster Care",
    "Homeless": "Experiencing Homelessness",
    "Migrant": "Migrant Families",
    "Military": "Military-Connected Families",
}
PLANS = {
    "4 Year College": "Four-Year College",
    "Less 4 Year College": "Two-Year College or Shorter Program",
    "Employed": "Working",
    "Armed Forces": "Military",
    "Unemployed": "Not Working",
    "Unknown": "Unknown",
    "Addl. High School": "Postgraduate Year at a High School",
}
EFA_STUDENTS_TYPE = 1  # "Base Aid": every EFA student gets it, so its count is the number of students
EFA_LOW_INCOME_TYPE = 2  # "Federal Free & Reduced (F&R) Price Meal Eligible"
EFA_SPECIAL_EDUCATION_TYPE = 3  # "Special Education Aid"
# EFA aid types as the statewide EFA page names them
EFA_AID = {
    "Base Aid": "Base amount (every EFA student)",
    "Federal Free & Reduced (F&R) Price Meal Eligible": "Extra: low-income (free or reduced-price meals)",
    "Special Education Aid": "Extra: special education",
    "English Language Learn Aid": "Extra: English learner",
    "3rd Grade Reading Aid": "Extra: grade 3 reading",
}
# October 1 enrollment types that are public schools, as on the statewide Enrollment page
PUBLIC_ENROLLMENT_TYPES = {
    "Public District Schools": "District schools",
    "Public Academies and Joint Maintenance Agreement Schools": "Academies",
    "Public Charter Schools": "Charter schools",
    "Interstate Schools": "Interstate schools",
}
PRIVATE_ENROLLMENT_TYPE = "Nonpublic Schools"
GRADE_YEARS = 11  # students by grade covers the latest year and the ten before it
# NH DOE's school profile measure for the share of students with disabilities (with an IEP)
DISABILITY_MEASURE = "Students with Disability (%)"

# Serious incidents from the School Safety Data Collection, as the Safety pages name them
INCIDENTS = {
    "Aggravated Felonious Sexual Assaults": "Aggravated sexual assault",
    "Arsons": "Arson",
    "Firearms Incidents Including More Than One Type of Weapon or Firearm": "Firearms: more than one type",
    "Firearms Possessions or Sales": "Firearm possession or sale",
    "First Degree Assaults": "First-degree assault",
    "Handgun Incidents": "Firearms: handgun",
    "Homicides": "Homicide",
    "Other Firearms Incidents": "Firearms: other",
    "Rifles/ Shotguns Incidents": "Firearms: rifle or shotgun",
    "Robberies": "Robbery",
}
DEGREES = {"Bachelor": "Bachelor's", "Masters": "Master's", "Beyond Masters": "Beyond master's", "None": "No degree reported"}
# Years whose degree counts add up to far more teachers than the staffing report can't be compared
# with (2011-12 statewide), so they're left out, as on the Staff page
MAX_DEGREE_COUNT_RATIO = 1.25


# Revenue sources as the site groups them, by the DOE-25 entry type's super category
REVENUE_SOURCES = ["Local", "State", "Federal", "Borrowing and transfers"]
# The state Financials page's spending lines and the group each is in (SPENDING_LINES in the
# frontend's stateMetrics.ts). Bond principal and transfers between funds are left out, as NH DOE's
# statewide total leaves them out.
SPENDING_LINES = {
    "Regular Instruction": "Instruction",
    "Vocational Education": "Instruction",
    "Other Instruction": "Instruction",
    "Special Education": "Special education",
    "Building Operations and Maintenance": "Support services",
    "Student Support": "Support services",
    "School Administration": "Support services",
    "Transportation": "Support services",
    "District Administration": "Support services",
    "Instructional Staff Support": "Support services",
    "Central Services": "Support services",
    "Business Services": "Support services",
    "Other Support Services": "Support services",
    "Debt Interest": "Everything else",
    "Food Service": "Everything else",
    "Construction and Facilities": "Everything else",
    "Other Programs": "Everything else",
}
SPENDING_GROUPS = ["Instruction", "Special education", "Support services", "Everything else"]
INSTRUCTION_LINES = {"Regular Programs": "Regular Instruction", "Special Programs": "Special Education", "Vocational Programs": "Vocational Education"}
SUPPORT_LINES = {
    "Operation/Maintenance of Plant": "Building Operations and Maintenance",
    "Student": "Student Support",
    "School Administration": "School Administration",
    "Student Transportation": "Transportation",
    "General Administration": "District Administration",
    "Instructional Staff": "Instructional Staff Support",
    "Central": "Central Services",
    "Business": "Business Services",
}
LINE_YEARS = 11  # spending by line covers the latest year and the ten before it
# The balance sheet's parts, by the DOE-25 entry type's super category
BALANCE_SECTIONS = {"Assets": "Assets", "Liabilities": "Liabilities", "Fund Equity": "Fund balance"}
UNASSIGNED = "Unassigned Fund Balance"
UNASSIGNED_RETAINED = "Unassigned Fund Balance Retained"


class DataToolError(Exception):
    """A tool input Claude can correct, such as an unknown place; sent back as an error tool result."""


def school_year(year: int) -> str:
    """2025 -> "2024-25", the site's school-year format."""
    return f"{year - 1}-{str(year)[-2:]}"


def _round(value: Optional[float], digits: int = 1) -> Optional[float]:
    return None if value is None else round(float(value), digits)


def _field(row, name):
    """A field from a service row, which is a dict or a response model."""
    return row.get(name) if isinstance(row, dict) else getattr(row, name, None)


def _grade_span(school) -> Optional[str]:
    """A school's grades as "Kindergarten to Grade 5", or None when it lists none."""
    grades = [g.name for g in sorted(school.grades or [], key=lambda g: g.id)]
    return f"{grades[0]} to {grades[-1]}" if grades else None


def _grade_order(name: str) -> int:
    """Sorts grade names by number ("Grade 3" before "Grade 10")."""
    return int("".join(c for c in name if c.isdigit()) or 0)


def dataset(title: str, unit: str, columns: List[str], rows: List[list], page: str, note: Optional[str] = None,
            column_units: Optional[Dict[str, str]] = None, key: Optional[str] = None) -> dict:
    """One dataset as the tools return it. `unit` (percent, dollars, count or number) applies to every
    value column except those named in `column_units`, such as a count beside percentages. `key`
    names the dataset for compare_places."""
    units = {name: (column_units or {}).get(name, unit) for name in columns[1:]}
    return {"title": title, "unit": unit, "columns": columns, "units": units, "rows": rows, "page": page, "note": note, "key": key}


def _per_thousand(count: Optional[float], students: Optional[float]) -> Optional[float]:
    return _round(1000 * count / students) if count is not None and students else None


def _share(part: Optional[float], whole: Optional[float]) -> Optional[float]:
    return _round(100 * part / whole) if part is not None and whole else None


def _once(session: Session, name: str, load: Callable[[], object]):
    """A lookup loaded once per request (entry types, say), however many places a request covers."""
    if name not in session.info:
        session.info[name] = load()
    return session.info[name]


# -------------------- Places --------------------

def find_places(session: Session, query: str) -> List[dict]:
    """Public districts, schools and towns whose name contains the query, best matches first."""
    words = [word for word in query.lower().replace(",", " ").split() if word not in {"school", "district", "nh", "the", "of"}]
    if not words:
        raise DataToolError("Give part of a district, school or town name to search for.")

    def matches(name: str) -> int:
        lowered = name.lower()
        return sum(1 for word in words if word in lowered)

    districts = list(location_service.get_districts(session, is_public=True))
    names = {d.id: d.name for d in districts}
    results = []
    for district in districts:
        score = matches(district.name)
        if score:
            results.append((score, 0, {"kind": "district", "id": district.id, "name": district.name, "page": f"/district/{district.id}"}))
    for town in location_service.get_towns(session):
        score = matches(town.name)
        district_ids = [i for i in (town.district_ids or []) if i in names]
        if score and district_ids:
            results.append((score, 1, {
                "kind": "town",
                "name": town.name,
                "districts": [{"id": i, "name": names[i], "page": f"/district/{i}"} for i in district_ids],
            }))
    for school in location_service.get_schools(session):
        district_id = _field(school, "district_id_fk")
        # A school matches on its name or its town, so "Hampton schools" finds Marston School
        score = max(matches(school.name), matches(school.city or ""))
        if score and district_id in names:
            results.append((score, 2, {
                "kind": "school",
                "id": school.id,
                "name": school.name,
                "town": (school.city or "").title(),
                "district_id": district_id,
                "grades": _grade_span(school),
                "page": f"/school/{school.id}",
            }))
    results.sort(key=lambda item: (-item[0], item[1], item[2]["name"]))
    return [item[2] for item in results[:20]]


def list_schools(session: Session, district_id: int) -> List[dict]:
    """A public district's current schools, with their grades and pages."""
    place = _place(session, "district", district_id)
    schools = []
    for school in location_service.get_schools(session, district_id=place["id"]):
        schools.append({
            "id": school.id,
            "name": school.name,
            "town": (school.city or "").title(),
            "grades": _grade_span(school),
            "page": f"/school/{school.id}",
        })
    return sorted(schools, key=lambda school: school["name"])


def _place(session: Session, level: str, place_id: Optional[int]) -> dict:
    """The place a data request is about, checked: a public district or a current school."""
    if level == "state":
        return {"level": "state", "id": None, "name": "New Hampshire (statewide)"}
    if place_id is None:
        raise DataToolError(f"A {level} id is required; use find_places to look it up.")
    if level == "district":
        districts = {d.id: d for d in location_service.get_districts(session, is_public=True)}
        if place_id not in districts:
            raise DataToolError(f"No public school district has id {place_id}; use find_places to look it up.")
        return {"level": "district", "id": place_id, "name": districts[place_id].name}
    schools = {s.id: s for s in location_service.get_schools(session)}
    if place_id not in schools:
        raise DataToolError(f"No current school has id {place_id}; use find_places to look it up.")
    return {"level": "school", "id": place_id, "name": schools[place_id].name, "district_id": _field(schools[place_id], "district_id_fk")}


def page_for(place: dict, topic: str) -> Optional[str]:
    """The site page showing a topic for a place, or None when no page shows it."""
    if place["level"] == "state":
        return STATE_PAGES.get(topic)
    section = (DISTRICT_SECTIONS if place["level"] == "district" else SCHOOL_SECTIONS).get(topic)
    return f"/{place['level']}/{place['id']}/{section}" if section else None


# -------------------- Topics --------------------

def _enrollment(session: Session, place: dict) -> List[dict]:
    page = page_for(place, "enrollment")
    by_grade: Dict[int, Dict[tuple, float]] = defaultdict(lambda: defaultdict(float))  # year -> (grade id, name) -> students
    if place["level"] == "state":
        by_year: Dict[int, dict] = defaultdict(lambda: defaultdict(int))
        private: Dict[int, int] = defaultdict(int)
        for row in enrollment_service.get_state_enrollment_by_type(session):
            kind = PUBLIC_ENROLLMENT_TYPES.get(row["enrollment_type"]["name"])
            if kind:
                by_year[row["year"]][kind] += row["enrollment"] or 0
                if row.get("grade"):
                    by_grade[row["year"]][(row["grade"]["id"], row["grade"]["name"])] += row["enrollment"] or 0
            elif row["enrollment_type"]["name"] == PRIVATE_ENROLLMENT_TYPE:
                private[row["year"]] += row["enrollment"] or 0
        kinds = list(PUBLIC_ENROLLMENT_TYPES.values())
        public = {year: sum(by_year[year].values()) for year in by_year}
        private_rows = [[school_year(year), public[year], private[year], _share(private[year], public[year] + private[year])]
                        for year in sorted(private) if year in public]
        return [*([dataset(
            "Public and private school students (October 1), statewide", "count",
            ["School year", "Public schools", "Private schools", "Share in private schools"], private_rows, page,
            "Private school counts are statewide only and come out a year after public ones. Education Freedom Account students aren't counted. There are no homeschool counts.",
            {"Share in private schools": "percent"},
        )] if private_rows else []), dataset(
            "Public school students (October 1), statewide", "count",
            ["School year", "All public schools", *kinds],
            [[school_year(year), sum(by_year[year].values()), *(by_year[year].get(kind, 0) for kind in kinds)] for year in sorted(by_year)],
            page,
            "Every public school student, preschool to grade 12, counted on October 1, as on the statewide Enrollment page.",
            key="students",
        ), *_student_needs(session, place),
            *_grades(by_grade, place, page, "Every public school student, counted on October 1, as in the statewide Enrollment page's grade table."),
            *_disabilities(session, place)]
    if place["level"] == "district":
        totals: Dict[int, float] = defaultdict(float)
        for row in enrollment_service.get_town_enrollments(session, district_id=place["id"]):
            totals[_field(row, "year")] += _field(row, "enrollment") or 0
            grade = _field(row, "grade")
            if grade:
                by_grade[_field(row, "year")][(_field(grade, "id"), _field(grade, "name"))] += _field(row, "enrollment") or 0
        return [dataset(
            f"Public school students living in the {place['name']} district's towns", "count",
            ["School year", "Students"],
            [[school_year(year), round(totals[year])] for year in sorted(totals)],
            page,
            "Students who live in the district's towns, wherever they attend public school, as on the district's Enrollment page.",
            key="students",
        ), *_student_needs(session, place),
            *_grades(by_grade, place, page, "Students who live in the district's towns, wherever they attend public school, counted on October 1."),
            *_disabilities(session, place)]
    totals = defaultdict(float)
    for row in enrollment_service.get_school_enrollments(session, school_id=place["id"]):
        totals[_field(row, "year")] += _field(row, "enrollment") or 0
        grade = _field(row, "grade")
        if grade:
            by_grade[_field(row, "year")][(_field(grade, "id"), _field(grade, "name"))] += _field(row, "enrollment") or 0
    return [dataset(
        f"Students at {place['name']} (October 1)", "count",
        ["School year", "Students"],
        [[school_year(year), round(totals[year])] for year in sorted(totals)],
        page, key="students",
    ), *_student_needs(session, place),
        *_grades(by_grade, place, page, "Students at the school, counted on October 1."),
        *_disabilities(session, place)]


def _grades(by_grade: Dict[int, Dict[tuple, float]], place: dict, page: str, note: str) -> List[dict]:
    """Students by grade: each grade over the latest years, and the latest year against ten years before."""
    years = sorted(year for year in by_grade if any(by_grade[year].values()))[-GRADE_YEARS:]
    if not years:
        return []
    grades = sorted({grade for year in years for grade, students in by_grade[year].items() if students})
    names = [name for _, name in grades]
    latest, earlier = years[-1], years[0]

    def count(year: int, grade: tuple) -> Optional[int]:
        return round(by_grade[year][grade]) if grade in by_grade[year] else None
    rows = [[name, count(latest, grade), count(earlier, grade)] for grade, name in zip(grades, names)]
    rows.append(["All grades", sum(row[1] or 0 for row in rows), sum(row[2] or 0 for row in rows)])
    return [
        dataset(
            f"Students by grade and year, {place['name']}", "count", ["School year", *names],
            [[school_year(year), *(count(year, grade) for grade in grades)] for year in years], page, note, key="grades",
        ),
        dataset(
            f"Students by grade, {school_year(latest)}, {place['name']}", "count",
            ["Grade", "Students", f"Students in {school_year(earlier)}"], rows, page, note,
        ),
    ]


def _disabilities(session: Session, place: dict) -> List[dict]:
    """The share of students with disabilities (with an IEP) by year, from NH DOE's school profiles."""
    types = _once(session, "measurement_types", lambda: {t.name: t.id for t in measurement_service.get_measurement_types(session)})
    if DISABILITY_MEASURE not in types:
        return []
    type_id = types[DISABILITY_MEASURE]
    if place["level"] == "state":
        rows = measurement_service.get_state_measurements(session, measurement_type_id=type_id)
        page = STATE_PAGES["efa"]
        note = ("Students with an IEP (an individualized education program for a disability) as a share of all students. "
                "The data has no statewide count, so this is the districts' shares averaged, weighted by enrollment, as on the statewide EFA page.")
    else:
        rows = measurement_service.get_measurements(session, measurement_type_id=type_id, **{f"{place['level']}_id": place["id"]})
        page = page_for(place, "enrollment")
        note = "Students with an IEP (an individualized education program for a disability) as a share of the students enrolled, from NH DOE's school profiles."
    values = {_field(row, "year"): _field(row, "field") for row in rows if _field(row, "field") is not None}
    if not values:
        return []
    return [dataset(
        f"Students with disabilities, {place['name']}", "percent", ["School year", "Share of students"],
        [[school_year(year), _round(values[year])] for year in sorted(values)], page, note, key="disabilities",
    )]


def _student_needs(session: Session, place: dict) -> List[dict]:
    """English learners and low-income students (eligible for free or reduced-price meals), by year."""
    level, place_id = place["level"], place["id"]
    page = page_for(place, "enrollment")
    if level == "state":
        learners, meals = enrollment_service.get_state_english_learner(session), enrollment_service.get_state_reduced_lunch(session)
    elif level == "district":
        learners = enrollment_service.get_district_english_learner(session, district_id=place_id)
        meals = enrollment_service.get_district_reduced_lunch(session, district_id=place_id)
    else:
        learners, meals = [], enrollment_service.get_school_reduced_lunch(session, school_id=place_id)
    results = []
    learner_rows = [[school_year(r["year"]), r["eligible"], _round(100 * r["eligible"] / r["enrollment"]) if r["enrollment"] else None]
                    for r in sorted(learners, key=lambda r: r["year"]) if r.get("eligible") is not None]
    if learner_rows:
        results.append(dataset(
            f"English learners, {place['name']}", "count",
            ["School year", "English learners", "Share of students"], learner_rows, page,
            "Students eligible for English language services, as a count and a share of enrollment.",
            {"Share of students": "percent"}, key="english_learners",
        ))
    meal_rows = [[school_year(r["year"]), r["eligible"], _round(100 * r["eligible"] / r["enrollment"]) if r["enrollment"] else None]
                 for r in sorted(meals, key=lambda r: r["year"]) if r.get("eligible") is not None]
    if meal_rows:
        results.append(dataset(
            f"Low-income students (free or reduced-price meals), {place['name']}", "count",
            ["School year", "Low-income students", "Share of students"], meal_rows, page,
            "Students eligible for free or reduced-price school meals, the usual measure of low family income.",
            {"Share of students": "percent"}, key="low_income",
        ))
    return results


def _assessment_rows(session: Session, place: dict) -> list:
    if place["level"] == "state":
        return assessment_service.get_state_assessments(session)
    if place["level"] == "district":
        return assessment_service.get_district_assessments(session, district_id=place["id"])
    return assessment_service.get_school_assessments(session, school_id=place["id"])


def _proficiency(row) -> Optional[object]:
    """A share proficient, or "<10%" / ">90%" where the state reports only that."""
    value = _field(row, "above_proficient_percentage")
    if value is not None:
        return _round(value, 0)
    exception = _field(row, "above_proficient_percentage_exception")
    return {"SCORE_UNDER_10": "<10%", "SCORE_OVER_90": ">90%"}.get(exception)


def _test_scores(session: Session, place: dict) -> List[dict]:
    page = page_for(place, "test_scores")
    rows = _assessment_rows(session, place)
    subgroups = {g["id"]: STUDENT_GROUPS.get(g["name"], g["name"]) for g in assessment_service.get_assessment_subgroups(session)}
    grades = {g.id: g.name for g in location_service.get_grades(session)}
    by_year: Dict[int, dict] = defaultdict(dict)
    top: Dict[int, dict] = defaultdict(dict)
    for row in rows:
        if _field(row, "grade_id") is None and _field(row, "assessment_subgroup_id") == ALL_STUDENTS:
            subject = SUBJECTS.get(_field(row, "assessment_subject_id"))
            by_year[_field(row, "year")][subject] = _proficiency(row)
            if _field(row, "level_4_percentage") is not None:
                top[_field(row, "year")][subject] = _round(_field(row, "level_4_percentage"), 0)
    if not by_year:
        return []
    latest = max(by_year)
    results = [dataset(
        f"Percent proficient by year, all students, {place['name']}", "percent",
        ["School year", *SUBJECTS.values()],
        [[school_year(year), *(by_year[year].get(subject) for subject in SUBJECTS.values())] for year in sorted(by_year)],
        page,
        "Proficient means level 3 or 4 of 4. The state changed tests in 2014-15 and 2017-18, so scores before and after aren't directly comparable. No tests were given in spring 2020.",
        key="proficiency",
    )]
    if top:
        results.append(dataset(
            f"Percent at the highest level (4 of 4) by year, all students, {place['name']}", "percent",
            ["School year", *SUBJECTS.values()],
            [[school_year(year), *(top[year].get(subject) for subject in SUBJECTS.values())] for year in sorted(top)],
            page, "The share of students above the grade-level standard, the top of the four levels.",
        ))
    by_group: Dict[str, dict] = defaultdict(dict)
    by_grade: Dict[str, dict] = defaultdict(dict)
    for row in rows:
        if _field(row, "year") != latest:
            continue
        subject = SUBJECTS.get(_field(row, "assessment_subject_id"))
        if _field(row, "grade_id") is None:
            by_group[subgroups.get(_field(row, "assessment_subgroup_id"), "Unknown")][subject] = _proficiency(row)
        elif _field(row, "assessment_subgroup_id") == ALL_STUDENTS:
            by_grade[grades.get(_field(row, "grade_id"), str(_field(row, "grade_id")))][subject] = _proficiency(row)
    group_order = list(STUDENT_GROUPS.values())
    group_rows = [[name, *(by_group[name].get(s) for s in SUBJECTS.values())]
                  for name in sorted(by_group, key=lambda n: group_order.index(n) if n in group_order else 99)
                  if any(by_group[name].get(s) is not None for s in SUBJECTS.values())]
    if len(group_rows) > 1:
        results.append(dataset(
            f"Percent proficient by student group, {school_year(latest)}, {place['name']}", "percent",
            ["Student group", *SUBJECTS.values()], group_rows, page,
            "Groups with too few students to report are left out.",
        ))
    grade_rows = [[name, *(by_grade[name].get(s) for s in SUBJECTS.values())]
                  for name in sorted(by_grade, key=_grade_order)]
    if grade_rows:
        results.append(dataset(
            f"Percent proficient by grade, {school_year(latest)}, all students, {place['name']}", "percent",
            ["Grade", *SUBJECTS.values()], grade_rows, page,
        ))
    # Each grade over the years, one dataset per subject, for questions about a single grade
    for subject_id, subject in SUBJECTS.items():
        by_grade_year: Dict[int, dict] = defaultdict(dict)
        for row in rows:
            if _field(row, "assessment_subject_id") == subject_id and _field(row, "grade_id") is not None and _field(row, "assessment_subgroup_id") == ALL_STUDENTS:
                by_grade_year[_field(row, "year")][grades.get(_field(row, "grade_id"), str(_field(row, "grade_id")))] = _proficiency(row)
        names = sorted({name for values in by_grade_year.values() for name in values}, key=_grade_order)
        if names and len(by_grade_year) > 1:
            results.append(dataset(
                f"Percent proficient in {subject.lower()} by grade and year, all students, {place['name']}", "percent",
                ["School year", *names],
                [[school_year(year), *(by_grade_year[year].get(name) for name in names)] for year in sorted(by_grade_year)],
                page,
            ))
    return results


def _graduation(session: Session, place: dict) -> List[dict]:
    page = page_for(place, "graduation")
    level, place_id = place["level"], place["id"]
    if level == "state":
        cohorts = outcome_service.get_state_graduation_cohort(session)
        plans = outcome_service.get_state_post_graduation(session)
        exits = outcome_service.get_state_early_exit(session)
    elif level == "district":
        cohorts = outcome_service.get_district_graduation_cohort(session, district_id=place_id)
        plans = outcome_service.get_district_post_graduation(session, district_id=place_id)
        exits = outcome_service.get_district_early_exit(session, district_id=place_id)
    else:
        cohorts = outcome_service.get_school_graduation_cohort(session, school_id=place_id)
        plans = outcome_service.get_school_post_graduation(session, school_id=place_id)
        exits = outcome_service.get_school_early_exit(session, school_id=place_id)
    results = []
    cohort_rows = []
    for cohort in sorted(cohorts, key=lambda c: c["year"]):
        size = cohort["cohort_size"]
        if not size:
            continue
        other = size - cohort["graduate"] - cohort["earned_hiset"] - cohort["dropped_out"]
        cohort_rows.append([
            f"Class of {cohort['year']}",
            _round(100 * cohort["graduate"] / size), _round(100 * cohort["dropped_out"] / size),
            _round(100 * cohort["earned_hiset"] / size), _round(100 * other / size), size,
        ])
    if cohort_rows:
        results.append(dataset(
            f"Four-year graduation rate and outcomes by class, {place['name']}", "percent",
            ["Class", "Graduated", "Dropped out", "Earned a HiSET", "Still in high school or other", "Students in class"],
            cohort_rows, page,
            "Each class is the students who started grade 9 together, adjusted for transfers. Graduated means a regular or adult diploma within four years; HiSET is a high school equivalency test; still in high school or other includes students who left with a non-standard diploma.",
            {"Students in class": "count"}, key="cohorts",
        ))
    plan_counts: Dict[int, dict] = defaultdict(dict)
    for row in plans:
        plan_counts[row["year"]][PLANS.get(row["post_graduation_type"]["name"], row["post_graduation_type"]["name"])] = row["value"]
    if plan_counts:
        plan_names = [name for name in PLANS.values() if any(name in counts for counts in plan_counts.values())]
        plan_rows = []
        for year in sorted(plan_counts):
            total = sum(v or 0 for v in plan_counts[year].values())
            if total:
                plan_rows.append([f"Class of {year}", *(_round(100 * (plan_counts[year].get(name) or 0) / total) for name in plan_names), total])
        results.append(dataset(
            f"Graduates' plans after high school, {place['name']}", "percent",
            ["Class", *plan_names, "Graduates reported"], plan_rows, page,
            "Plans graduates report at the end of senior year, not confirmed enrollment or jobs. Shares of all graduates reported that year.",
            {"Graduates reported": "count"}, key="plans",
        ))
    exit_rows = [[school_year(row["year"]), _round(100 * row["annual_dropout_percentage"], 2)]
                 for row in sorted(exits, key=lambda r: r["year"]) if row.get("annual_dropout_percentage") is not None]
    if exit_rows:
        results.append(dataset(
            f"Annual dropout rate, grades 9-12, {place['name']}", "percent",
            ["School year", "Dropped out that year"], exit_rows, page,
            "Share of all high school students who dropped out during the school year; lower than the share of a class that drops out over four years.",
        ))
    return results


def _spending(session: Session, place: dict) -> List[dict]:
    if place["level"] == "school":
        raise DataToolError("Spending is reported for districts and the state, not individual schools; ask for the school's district.")
    page = page_for(place, "spending")
    if place["level"] == "state":
        rows = finance_service.get_state_per_pupil_costs(session)
    else:
        rows = finance_service.get_district_per_pupil_costs(session, district_id=place["id"])
    rows = sorted(rows, key=lambda r: _field(r, "year"))
    results = []
    if rows:
        latest = _field(rows[-1], "year")
        adjusted = f"All grades in {school_year(latest)} dollars"
        results.append(dataset(
            f"Cost per student, {place['name']}", "dollars",
            ["School year", "All grades", "Elementary", "Middle", "High", adjusted],
            [[school_year(_field(r, "year")), _field(r, "total"), _field(r, "elementary"), _field(r, "middle"), _field(r, "high"),
              in_dollars_of(_field(r, "total"), _field(r, "year"), latest)] for r in rows],
            page,
            f"The state's cost per pupil: operating spending less tuition and transportation, per student. The last column adjusts all grades for inflation into {school_year(latest)} dollars (consumer price index), as the page's inflation switch does.",
            key="cost",
        ))
    return results + _money(session, place, page)


def _revenue_source(entry_type) -> str:
    category = getattr(entry_type, "category", None)
    name = category.super_category.name if category and category.super_category else ""
    return next((source for source in ("Local", "State", "Federal") if source in name), "Borrowing and transfers")


def _spending_line(entry_type) -> Optional[str]:
    """The spending line a DOE-25 expenditure entry type is part of, or None when it's left out."""
    category = getattr(entry_type, "category", None)
    category_name = category.name if category else None
    super_name = category.super_category.name if category and category.super_category else ""
    name = entry_type.name or ""
    if category_name == "Fund Transfers" or name in ("Transfer to Other Funds", "Principal"):
        return None
    if category_name == "Instruction":
        return INSTRUCTION_LINES.get(name, "Other Instruction")
    if category_name == "Support Services":
        return SUPPORT_LINES.get(name, "Other Support Services")
    if category_name == "Debt Service":
        return "Debt Interest"
    if "Food Service" in super_name:
        return "Food Service"
    if name == "Facilities Acquisition & Construction":
        return "Construction and Facilities"
    # Adult education, community service, programs for private schools, and payments to charter schools
    return "Other Programs"


def _money(session: Session, place: dict, page: str) -> List[dict]:
    """Revenue by source and spending by category from the DOE-25 reports, by year."""
    revenue_types = _once(session, "revenue_types", lambda: {t.id: _revenue_source(t) for t in finance_service.get_revenue_entry_types(session)})
    spending_types = _once(session, "spending_types", lambda: {t.id: _spending_line(t) for t in finance_service.get_expenditure_entry_types(session)})
    revenue: Dict[int, Dict[str, float]] = defaultdict(lambda: defaultdict(float))
    spending: Dict[int, Dict[str, float]] = defaultdict(lambda: defaultdict(float))
    if place["level"] == "state":
        for row in finance_service.get_state_revenue(session):
            revenue[row.year][revenue_types.get(row.revenue_entry_type_id_fk, "Borrowing and transfers")] += row.value or 0
        for row in finance_service.get_state_expenditure(session):
            line = spending_types.get(row.expenditure_entry_type_id_fk)
            if line:
                spending[row.year][line] += row.value or 0
    else:
        try:
            reports = finance_service.get_financial_report(session, district_id=place["id"])
        except HTTPException:
            reports = []
        for report in reports:
            year = report.doe_form.year
            for row in report.revenues or []:
                revenue[year][revenue_types.get(row.revenue_entry_type_id_fk, "Borrowing and transfers")] += row.value or 0
            for row in report.expenditures or []:
                line = spending_types.get(row.expenditure_entry_type_id_fk)
                if line:
                    spending[year][line] += row.value or 0
    results = []
    if revenue:
        share_columns = [f"{source} share" for source in REVENUE_SOURCES[:3]]
        rows = []
        for year in sorted(revenue):
            total = sum(revenue[year].values())
            rows.append([school_year(year), *(round(revenue[year][source]) for source in REVENUE_SOURCES), round(total),
                         *(_share(revenue[year][source], total) for source in REVENUE_SOURCES[:3])])
        results.append(dataset(
            f"Revenue by source, {place['name']}", "dollars",
            ["School year", *REVENUE_SOURCES, "Total revenue", *share_columns], rows, page,
            "All revenue reported to the state on the DOE-25, every fund. Local is mostly property taxes; borrowing and transfers are bond sales and transfers between funds. Not adjusted for inflation.",
            {column: "percent" for column in share_columns}, key="revenue",
        ))
    if spending:
        share_columns = [f"{group} share" for group in SPENDING_GROUPS]
        rows = []
        for year in sorted(spending):
            groups = {group: sum(v for line, v in spending[year].items() if SPENDING_LINES[line] == group) for group in SPENDING_GROUPS}
            total = sum(groups.values())
            rows.append([school_year(year), *(round(groups[group]) for group in SPENDING_GROUPS), round(total),
                         *(_share(groups[group], total) for group in SPENDING_GROUPS)])
        results.append(dataset(
            f"Spending by category, {place['name']}", "dollars",
            ["School year", *SPENDING_GROUPS, "Total spending", *share_columns], rows, page,
            "All spending reported on the DOE-25 except bond principal and transfers between funds; this is total spending, not cost per student. Special education is the special programs instruction line. Not adjusted for inflation.",
            {column: "percent" for column in share_columns}, key="categories",
        ))
        years = sorted(spending)[-LINE_YEARS:]
        lines = [line for line in SPENDING_LINES if any(spending[year].get(line) for year in years)]
        results.append(dataset(
            f"Spending by line, {place['name']}", "dollars",
            ["School year", *lines],
            [[school_year(year), *(round(spending[year].get(line, 0)) for line in lines)] for year in years], page,
            "Each spending line summed over school levels and funds, as in the spending tables on the site. Vocational education is career and technical education. Not adjusted for inflation.",
        ))
    return results


def _balance_sheet(session: Session, place: dict) -> List[dict]:
    """A district's DOE-25 balance sheet: fund balance by year, and every line in the latest two years."""
    if place["level"] != "district":
        raise DataToolError("Balance sheets are reported for districts, not the state or individual schools; ask for a district.")
    page = page_for(place, "balance_sheet")
    types = _once(session, "balance_types", lambda: {t.id: t for t in finance_service.get_balance_entry_types(session)})
    try:
        reports = finance_service.get_financial_report(session, district_id=place["id"])
    except HTTPException:
        reports = []
    lines: Dict[int, Dict[tuple, float]] = defaultdict(lambda: defaultdict(float))  # year -> (section, category, line) -> dollars
    for report in reports:
        for row in report.balance_sheets or []:
            entry = types.get(row.balance_entry_type_id_fk)
            if entry is None or not row.value:
                continue
            category = entry.category
            section = BALANCE_SECTIONS.get(category.super_category.name if category and category.super_category else None, "Other")
            # The DOE-25 types file the unassigned fund balance under assigned
            part = "Unassigned" if entry.name == UNASSIGNED else category.name if category else ""
            lines[report.doe_form.year][(section, part, entry.name)] += row.value
    if not lines:
        return []
    years = sorted(lines)

    def total(year: int, section: str) -> int:
        return round(sum(value for (part, _, _), value in lines[year].items() if part == section))

    def line(year: int, name: str) -> int:
        return round(sum(value for (_, _, entry), value in lines[year].items() if entry == name))
    note = ("From the district's DOE-25 balance sheet at the end of the school year (June 30), all funds added together as on the "
            "site's Balance Sheet tab. Fund balance is what's left after liabilities, much of it set aside for a purpose; the unassigned "
            "fund balance is the part not set aside for anything. Assets and liabilities include what the district's funds owe each other "
            "(interfund), which can be large in some years. Not adjusted for inflation.")
    results = [dataset(
        f"Fund balance by year, {place['name']}", "dollars",
        ["School year", "Unassigned fund balance", "Unassigned fund balance retained", "Total fund balance", "Total assets", "Total liabilities"],
        [[school_year(year), line(year, UNASSIGNED), line(year, UNASSIGNED_RETAINED), total(year, "Fund balance"), total(year, "Assets"),
          total(year, "Liabilities")] for year in years],
        page, note + ' "Unassigned fund balance retained" is the DOE-25 line of that name, under committed fund balance.', key="fund_balance",
    )]
    latest, previous = years[-1], (years[-2] if len(years) > 1 else None)
    order = list(BALANCE_SECTIONS.values())
    keys = sorted(set(lines[latest]) | set(lines[previous] if previous else ()),
                  key=lambda key: (order.index(key[0]) if key[0] in order else len(order), key[1], key[2]))
    results.append(dataset(
        f"Balance sheet, end of {school_year(latest)}, {place['name']}", "dollars",
        ["Line", "Section", f"End of {school_year(latest)}", *([f"End of {school_year(previous)}"] if previous else [])],
        [[name, f"{section}: {category}" if category else section, round(lines[latest].get((section, category, name), 0)),
          *([round(lines[previous].get((section, category, name), 0))] if previous else [])] for section, category, name in keys],
        page, note,
    ))
    return results


def _staff(session: Session, place: dict) -> List[dict]:
    if place["level"] == "school":
        raise DataToolError("Staff figures are reported for districts and the state, not individual schools; ask for the school's district.")
    page = page_for(place, "staff")
    if place["level"] == "state":
        salaries = staff_service.get_state_teacher_average_salary(session)
        staff = staff_service.get_state_staff(session)
        class_sizes = class_size_service.get_state_class_size(session)
        degrees = staff_service.get_state_teacher_education(session)
    else:
        salaries = staff_service.get_district_teacher_average_salary(session, district_id=place["id"])
        staff = staff_service.get_district_staff(session, district_id=place["id"])
        class_sizes = class_size_service.get_district_class_size(session, district_id=place["id"])
        degrees = staff_service.get_district_teacher_education(session, district_id=place["id"])
    results = []
    salaries = sorted((r for r in salaries if r.get("salary")), key=lambda r: r["year"])
    if salaries:
        latest = salaries[-1]["year"]
        adjusted = f"In {school_year(latest)} dollars"
        results.append(dataset(
            f"Average teacher salary, {place['name']}", "dollars",
            ["School year", "Average salary", adjusted],
            [[school_year(r["year"]), round(r["salary"]), in_dollars_of(r["salary"], r["year"], latest)] for r in salaries],
            page, f"The last column adjusts for inflation into {school_year(latest)} dollars (consumer price index), as the page's inflation switch does.",
            key="salary",
        ))
    if place["level"] == "district":
        results.extend(_salary_schedule(session, place, page))
    by_year: Dict[int, dict] = defaultdict(dict)
    for row in staff:
        by_year[row["year"]][row["staff_type"]["name"]] = row["value"]
    if by_year:
        types = ["Teacher", "Instruction Support", "Specialist", "Librarian", "Admin Support", "All Other Support"]
        results.append(dataset(
            f"Staff (full-time equivalents), {place['name']}", "count",
            ["School year", *types],
            [[school_year(year), *(_round(by_year[year].get(t)) for t in types)] for year in sorted(by_year)],
            page,
        ))
    results.extend(_degrees(degrees, {year: values.get("Teacher") for year, values in by_year.items()}, place, page))
    size_rows = [[school_year(_field(r, "year")), _field(r, "all_grades"), _field(r, "grades_1_2"), _field(r, "grades_3_4"), _field(r, "grades_5_8")]
                 for r in sorted(class_sizes, key=lambda r: _field(r, "year"))]
    if size_rows:
        results.append(dataset(
            f"Average class size, {place['name']}", "number",
            ["School year", "All grades", "Grades 1-2", "Grades 3-4", "Grades 5-8"], size_rows, page, key="class_size",
        ))
    return results


def _degrees(rows: list, teachers: Dict[int, Optional[float]], place: dict, page: str) -> List[dict]:
    """Teachers by highest degree, as full-time equivalents and shares, by year."""
    by_year: Dict[int, Dict[str, float]] = defaultdict(dict)
    for row in rows:
        name = DEGREES.get(row["teacher_type"]["name"], row["teacher_type"]["name"])
        by_year[row["year"]][name] = (by_year[row["year"]].get(name) or 0) + (row["value"] or 0)
    names = [name for name in DEGREES.values() if any(name in values for values in by_year.values())]
    out = []
    for year in sorted(by_year):
        total = sum(by_year[year].values())
        if not total or (teachers.get(year) and total > teachers[year] * MAX_DEGREE_COUNT_RATIO):
            continue
        graduate = sum(by_year[year].get(name) or 0 for name in ("Master's", "Beyond master's"))
        out.append([school_year(year), *(_round(by_year[year].get(name)) for name in names), _share(graduate, total)])
    if not out:
        return []
    return [dataset(
        f"Teachers by highest degree, {place['name']}", "count", ["School year", *names, "Share with a master's or more"], out, page,
        "Full-time-equivalent teachers by their highest degree. Years whose degree counts add up to far more teachers than the staffing report are left out.",
        {"Share with a master's or more": "percent"}, key="degrees",
    )]


def _salary_schedule(session: Session, place: dict, page: str) -> List[dict]:
    """A district's teacher salary schedule: starting (first step) and top salaries for each band."""
    bands: Dict[int, dict] = defaultdict(dict)
    for row in staff_service.get_district_teacher_salary_band(session, district_id=place["id"]):
        bands[row["year"]][row["salary_band_type"]["name"]] = row
    if not bands:
        return []
    latest = max(bands)

    def pay(year: int, band: str, end: str) -> Optional[float]:
        row = bands[year].get(band)
        return _round(row[end], 0) if row and row.get(end) else None
    results = [dataset(
        f"Teacher starting and top salaries by year, {place['name']}", "dollars",
        ["School year", "Starting, bachelor's", "Top, bachelor's", "Starting, master's", "Top, master's"],
        [[school_year(year), pay(year, "BA", "min_salary"), pay(year, "BA", "max_salary"), pay(year, "MA", "min_salary"), pay(year, "MA", "max_salary")]
         for year in sorted(bands)],
        page, "From the district's teacher salary schedule: starting is the first step, top is the last. Not adjusted for inflation.",
        key="schedule",
    )]
    results.append(dataset(
        f"Teacher salary schedule, {school_year(latest)}, {place['name']}", "dollars",
        ["Degree", "Starting salary", "Top salary", "Steps"],
        [[row["salary_band_type"]["description"], _round(row["min_salary"], 0), _round(row["max_salary"], 0), row.get("steps")]
         for _, row in sorted(bands[latest].items(), key=lambda item: item[1]["salary_band_type"]["id"])],
        page, "Each degree level's pay range on the schedule; steps are the yearly raises from starting to top.",
        {"Steps": "number"},
    ))
    return results


def _safety(session: Session, place: dict) -> List[dict]:
    page = page_for(place, "safety")
    level, place_id = place["level"], place["id"]
    # Each safety report for the place: the service's state_, district_ or school_ method of that name
    where = {} if level == "state" else {f"{level}_id": place_id}

    def report(name: str) -> List[dict]:
        return getattr(safety_service, f"get_{level}_{name}")(session, **where)
    truancy, enrollment, bullying, harassment = report("truancy"), report("safety_enrollment"), report("bullying"), report("harassment")
    discipline = report("discipline_counts")
    students = {row["year"]: row["total_enrollment"] for row in enrollment}
    results = []
    rows = []
    for row in sorted(truancy, key=lambda r: r["year"]):
        total = students.get(row["year"])
        rows.append([school_year(row["year"]), row["count"], _round(100 * row["count"] / total) if total else None])
    if rows:
        results.append(dataset(
            f"Students who were truant, {place['name']}", "count",
            ["School year", "Truant students", "Share of students"], rows, page,
            "Students with 10 or more half-days of unexcused absence.",
            {"Share of students": "percent"}, key="truancy",
        ))
    reports: Dict[int, List[float]] = defaultdict(lambda: [0, 0])
    for row in bullying:
        reports[row["year"]][0] += row.get("reported") or 0
        reports[row["year"]][1] += row.get("investigated_actual") or 0
    if reports:
        results.append(dataset(
            f"Bullying reports, {place['name']}", "count",
            ["School year", "Reported", "Confirmed after investigation", "Reports per 1,000 students"],
            [[school_year(year), reported, confirmed, _per_thousand(reported, students.get(year))] for year, (reported, confirmed) in sorted(reports.items())],
            page, "Bullying and cyber-bullying reports schools made to the state; per 1,000 students enrolled.",
            {"Reports per 1,000 students": "number"}, key="bullying",
        ))
    incidents: Dict[int, float] = defaultdict(float)
    by_kind: Dict[str, float] = defaultdict(float)
    latest = max((row["year"] for row in harassment), default=None)
    for row in harassment:
        incidents[row["year"]] += row.get("incident_count") or 0
        if row["year"] == latest:
            by_kind[row["classification"]["name"]] += row.get("incident_count") or 0
    if incidents:
        results.append(dataset(
            f"Harassment incidents, {place['name']}", "count",
            ["School year", "Incidents", "Incidents per 1,000 students"],
            [[school_year(year), count, _per_thousand(count, students.get(year))] for year, count in sorted(incidents.items())],
            page, "Harassment incidents schools reported, all kinds together.",
            {"Incidents per 1,000 students": "number"},
        ))
        results.append(dataset(
            f"Harassment incidents by kind, {school_year(latest)}, {place['name']}", "count",
            ["Kind", "Incidents"], [[kind, count] for kind, count in sorted(by_kind.items(), key=lambda item: -item[1])], page,
            "Kinds as the state classifies them (race, sex, disability, sexual orientation and others).",
        ))
    actions: Dict[int, dict] = defaultdict(dict)
    for row in discipline:
        actions[row["year"]][row["count_type"]["name"]] = row.get("count")
    if actions:
        names = {"Who Received In-School Suspensions": "In-school suspensions", "Who Received Out-of-School Suspensions": "Out-of-school suspensions", "Who Were Expelled": "Expelled"}
        results.append(dataset(
            f"Students suspended or expelled, {place['name']}", "count",
            ["School year", *names.values()],
            [[school_year(year), *(actions[year].get(name) for name in names)] for year in sorted(actions)],
            page, "Students who received at least one suspension, or were expelled, during the year.",
        ))
    results.extend(_by_kind(
        report("discipline_incidents"), "incident_type", students, None,
        f"Incidents that led to a suspension, by kind, {place['name']}", page,
        "Incidents schools reported that resulted in a suspension, by the state's kinds.",
    ))
    results.extend(_by_kind(
        report("bullying_classifications"), "classification_type", students, None,
        f"Confirmed bullying incidents by what they were based on, {place['name']}", page,
        "Confirmed bullying incidents by the basis schools reported; an incident can have more than one.",
    ))
    results.extend(_by_kind(
        report("bullying_impacts"), "impact_type", students, None,
        f"Confirmed bullying incidents by what they involved, {place['name']}", page,
        "Confirmed bullying incidents by what schools reported they involved; an incident can involve more than one.",
    ))
    return results + _serious_incidents(report("safety"), students, place, page) + _restraint(report("restraint"), report("seclusion"), students, place, page)


def _by_kind(rows: List[dict], kind: str, students: Dict[int, int], labels: Optional[Dict[str, str]], title: str, page: str, note: str) -> List[dict]:
    """Counts of one safety report by kind and year: rows are kinds, columns the years the place
    reported to the state (zero where it reported none of a kind)."""
    counts: Dict[str, Dict[int, float]] = defaultdict(lambda: defaultdict(float))
    for row in rows:
        name = row[kind]["name"]
        counts[(labels or {}).get(name, name)][row["year"]] += row.get("count") or 0
    years = sorted(set(students) | {year for values in counts.values() for year in values})
    if not counts:
        return []
    order = sorted(counts, key=lambda name: (-sum(counts[name].values()), name))
    return [dataset(
        title, "count", ["Kind", *(school_year(year) for year in years)],
        [[name, *(round(counts[name].get(year, 0)) for year in years)] for name in order], page,
        note + " Zero means the place reported none that year.",
    )]


def _serious_incidents(rows: List[dict], students: Dict[int, int], place: dict, page: str) -> List[dict]:
    """Serious incidents (firearms, assaults, robberies and others) by year, and by kind."""
    firearms: Dict[int, float] = defaultdict(float)
    other: Dict[int, float] = defaultdict(float)
    for row in rows:
        label = INCIDENTS.get(row["safety_type"]["name"], row["safety_type"]["name"])
        (firearms if label.startswith("Firearm") else other)[row["year"]] += row.get("count") or 0
    if not rows:
        return []
    years = sorted(set(students) | set(firearms) | set(other))
    return [
        dataset(
            f"Serious safety incidents by year, {place['name']}", "count",
            ["School year", "Firearms incidents", "Other serious incidents", "All serious incidents"],
            [[school_year(year), round(firearms[year]), round(other[year]), round(firearms[year] + other[year])] for year in years], page,
            "Serious incidents schools reported to the state: firearms incidents, and assaults, robberies, arsons and homicides. "
            "Zero means the place reported none that year.", key="incidents",
        ),
        *_by_kind(rows, "safety_type", students, INCIDENTS, f"Serious safety incidents by kind, {place['name']}", page,
                  "Serious incidents schools reported to the state, by kind."),
    ]


def _restraint(restraints: List[dict], seclusions: List[dict], students: Dict[int, int], place: dict, page: str) -> List[dict]:
    """Restraints and seclusions by year, with rates per 1,000 students."""
    held = {row["year"]: row.get("generated") or 0 for row in restraints}
    isolated = {row["year"]: row.get("generated") or 0 for row in seclusions}
    years = sorted(set(held) | set(isolated))
    if not years:
        return []
    return [dataset(
        f"Restraints and seclusions, {place['name']}", "count",
        ["School year", "Restraints", "Seclusions", "Restraints per 1,000 students", "Seclusions per 1,000 students"],
        [[school_year(year), held.get(year), isolated.get(year), _per_thousand(held.get(year), students.get(year)),
          _per_thousand(isolated.get(year), students.get(year))] for year in years], page,
        "Times school staff physically held (restraint) or isolated (seclusion) a student, from the reports schools file with the state. "
        "One student can be counted many times. Per 1,000 students enrolled.",
        {"Restraints per 1,000 students": "number", "Seclusions per 1,000 students": "number"}, key="restraint",
    )]


def _efa(session: Session, place: dict) -> List[dict]:
    if place["level"] == "school":
        raise DataToolError("Education Freedom Account figures are by town and district, and statewide; ask for the district.")
    page = page_for(place, "efa")
    types = _once(session, "efa_types", lambda: education_freedom_account_service.get_entry_types_with_values(session))
    names = {t.id: t.name for t in types}
    amounts = {(t.id, t.year): t.value for t in types}
    counts: Dict[int, Dict[int, float]] = defaultdict(lambda: defaultdict(float))  # year -> aid type -> students
    by_town: Dict[int, Dict[int, float]] = defaultdict(lambda: defaultdict(float))  # year -> town -> students
    if place["level"] == "state":
        for row in education_freedom_account_service.get_state_entries(session):
            counts[_field(row, "year")][_field(row, "education_freedom_account_entry_type_id_fk")] += _field(row, "value") or 0
    else:
        try:
            entries = education_freedom_account_service.get_entries(session, district_id=place["id"])
        except HTTPException:
            entries = []
        for row in entries:
            counts[row.year][row.education_freedom_account_entry_type_id_fk] += row.value or 0
            if row.education_freedom_account_entry_type_id_fk == EFA_STUDENTS_TYPE:
                by_town[row.year][row.town_id_fk] += row.value or 0
    if not counts:
        return []
    latest = max(counts)

    def cost(year: int) -> Optional[float]:
        priced = [(students, amounts.get((type_id, year))) for type_id, students in counts[year].items()]
        return round(sum(students * amount for students, amount in priced if amount is not None)) if any(a is not None for _, a in priced) else None

    students = {year: counts[year].get(EFA_STUDENTS_TYPE) for year in counts}
    columns = ["School year", "EFA students", "Extra: low-income", "Extra: special education", "Estimated state cost"]
    column_units = {"Estimated state cost": "dollars"}
    public: Dict[int, float] = defaultdict(float)
    town_public: Dict[int, Dict[int, float]] = defaultdict(lambda: defaultdict(float))
    if place["level"] == "district":
        for row in enrollment_service.get_town_enrollments(session, district_id=place["id"]):
            public[_field(row, "year")] += _field(row, "enrollment") or 0
            town_public[_field(row, "year")][_field(row, "town_id_fk")] += _field(row, "enrollment") or 0
        columns.append("Share of public school students")
        column_units["Share of public school students"] = "percent"
    rows = []
    for year in sorted(counts):
        row = [school_year(year), _round(students[year], 0), _round(counts[year].get(EFA_LOW_INCOME_TYPE), 0), _round(counts[year].get(EFA_SPECIAL_EDUCATION_TYPE), 0), cost(year)]
        if place["level"] == "district":
            row.append(_share(students[year], public.get(year)))
        rows.append(row)
    where = "statewide" if place["level"] == "state" else f"in the {place['name']} district's towns"
    results = [dataset(
        f"Education Freedom Account (EFA) students, {place['name']}", "count", columns, rows, page,
        "EFAs are state-funded accounts families use for private school, homeschool and other approved costs. Every EFA student gets a base amount; extra columns count students who also get that extra aid. "
        f"The estimated state cost is each aid's students times that year's per-student amount, not actual payments. Counts are students living {where}; the latest year is the state's preliminary count."
        + (" The share compares EFA students with public school students living in the same towns, not with all children." if place["level"] == "district" else ""),
        column_units, key="efa_students",
    )]
    aid_rows = [[EFA_AID.get(names.get(type_id), names.get(type_id)), _round(n, 0), amounts.get((type_id, latest)),
                 round(n * amounts[(type_id, latest)]) if (type_id, latest) in amounts else None]
                for type_id, n in sorted(counts[latest].items())]
    results.append(dataset(
        f"EFA aid by type, {school_year(latest)}, {place['name']}", "dollars",
        ["Aid", "Students", "Per student", "Estimated total"], aid_rows, page,
        "Students can get more than one kind of extra aid; the base amount's students are the number of EFA students.",
        {"Students": "count"},
    ))
    if place["level"] == "district" and len({town for year in by_town for town in by_town[year]}) > 1:
        towns = {t.id: t.name for t in location_service.get_towns(session)}
        results.append(dataset(
            f"EFA students by town, {school_year(latest)}, {place['name']}", "count",
            ["Town", "EFA students", "Public school students", "Share of public school students"],
            [[towns.get(town, str(town)), _round(n, 0), town_public[latest].get(town) or None, _share(n, town_public[latest].get(town))]
             for town, n in sorted(by_town[latest].items(), key=lambda item: -item[1])],
            page, "Public school students are those living in the town, counted on October 1.",
            {"Share of public school students": "percent"},
        ))
    return results


# -------------------- Question 2 --------------------

QUESTION_TWO_NOTE = (
    "Ballot Question 2 (HB 1300, 2026 chapter 324): a school district adopts the school property tax cap when 60% or more of the "
    "votes in all its towns are yes. The same question's 6% cap on SAU central-office spending is decided by the vote across each "
    "SAU's towns, which isn't in this data."
)
UNOFFICIAL_NOTE = (
    " These results are unofficial: a district's result is final once its school board ratifies its towns' results and reports "
    "them to the Department of Revenue Administration."
)


@lru_cache(maxsize=1)
def _question_two_elections() -> dict:
    return load_config("question_two_config.yaml")["elections"]


def _question_two_source(year: int) -> Optional[dict]:
    """The page an election's results come from, shown as the answer's source."""
    election = _question_two_elections().get(year)
    if not election:
        return None
    host = urlparse(election["source_url"]).netloc.lower()
    return {"label": election["source_label"], "url": election["source_url"], "site": host[4:] if host.startswith("www.") else host,
            "as_of": str(election["as_of"])}


def _yes_no(value: bool) -> str:
    return "Yes" if value else "No"


def _question_two(session: Session, place: dict) -> List[dict]:
    """Question 2 results: every district's for the state, or one district's by election. There's no
    page for these on the site yet, so each dataset carries its source instead."""
    if place["level"] == "district":
        rows = question_two_service.get_district_results(session, district_id=place["id"])
        if not rows:
            raise DataToolError(f"{place['name']} isn't a school district that voted on Question 2; use find_places for the school districts of the towns it serves.")
        latest = max(row.year for row in rows)
        result = dataset(
            f"Question 2 results, {place['name']}", "count",
            ["Election", "Yes votes", "No votes", "Yes share", "Adopted the school tax cap", "Official results"],
            [[str(row.year), row.yes_votes, row.no_votes, row.yes_percentage, _yes_no(row.passed), _yes_no(row.is_official)] for row in rows],
            None, QUESTION_TWO_NOTE + ("" if all(row.is_official for row in rows) else UNOFFICIAL_NOTE) + " For a district of several towns, its towns' votes are added together.",
            {"Yes share": "percent"}, key="question_two",
        )
        result["source"] = _question_two_source(latest)
        return [result]
    rows = question_two_service.get_district_results(session)
    if not rows:
        return []
    by_year: Dict[int, list] = defaultdict(list)
    for row in rows:
        by_year[row.year].append(row)
    latest = max(by_year)
    official = all(row.is_official for row in by_year[latest])
    note = (QUESTION_TWO_NOTE + ("" if official else UNOFFICIAL_NOTE) +
            " Votes aren't added up statewide: voters in a town with both its own school district and a cooperative district voted in each.")
    results = [
        dataset(
            "Question 2 results, all school districts", "count",
            ["Election", "School districts", "Adopted the school tax cap", "Didn't adopt it", "Official results"],
            [[str(year), len(found), sum(row.passed for row in found), sum(not row.passed for row in found), _yes_no(all(row.is_official for row in found))]
             for year, found in sorted(by_year.items())],
            None, note,
        ),
        dataset(
            f"Question 2 results by school district, {latest}, highest yes share first", "count",
            ["District", "Yes votes", "No votes", "Yes share", "Adopted the school tax cap"],
            [[row.district_name, row.yes_votes, row.no_votes, row.yes_percentage, _yes_no(row.passed)]
             for row in sorted(by_year[latest], key=lambda row: (-row.yes_percentage, row.district_name))],
            None, note, {"Yes share": "percent"},
        ),
    ]
    for item in results:
        item["source"] = _question_two_source(latest)
    return results


# -------------------- Ranking districts --------------------

# Measures districts can be ranked on: label, unit, topic (for the page) and how to read them
RANK_MEASURES = {
    "cost_per_student": ("Cost per student", "dollars", "spending"),
    "teacher_salary": ("Average teacher salary", "dollars", "staff"),
    "graduation_rate": ("Four-year graduation rate", "percent", "graduation"),
    "math_proficiency": ("Percent proficient in math", "percent", "test_scores"),
    "reading_proficiency": ("Percent proficient in reading", "percent", "test_scores"),
    "science_proficiency": ("Percent proficient in science", "percent", "test_scores"),
    "students": ("Students enrolled", "count", "enrollment"),
    "question_two_yes_share": ("Question 2 yes share", "percent", "question_two"),
}
# Graduation rates for classes smaller than this swing too much from year to year to rank
MIN_CLASS_SIZE = 20


def rank_districts(session: Session, measure: str, order: str = "highest") -> dict:
    """Every public district's latest value of one measure, sorted, with each district's page."""
    if measure not in RANK_MEASURES:
        raise DataToolError(f"Unknown measure {measure}; use one of {', '.join(RANK_MEASURES)}.")
    label, unit, topic = RANK_MEASURES[measure]
    names = {d.id: d.name for d in location_service.get_districts(session, is_public=True)}
    values: Dict[int, Dict[int, float]] = defaultdict(dict)  # year -> district -> value
    note = None
    if measure == "cost_per_student":
        for row in finance_service.get_district_per_pupil_costs(session):
            district = _field(row, "district_id_fk") or _field(row, "district_id")
            if _field(row, "total") is not None:
                values[_field(row, "year")][district] = _field(row, "total")
        note = "The state's cost per pupil: operating spending less tuition and transportation, per student. Very small districts can have unusual figures."
    elif measure == "teacher_salary":
        for row in staff_service.get_district_teacher_average_salary(session):
            if row.get("salary"):
                values[row["year"]][row["district_id"]] = round(row["salary"])
    elif measure == "graduation_rate":
        for row in outcome_service.get_district_graduation_cohort(session):
            if row["cohort_size"] and row["cohort_size"] >= MIN_CLASS_SIZE:
                values[row["year"]][row["district_id"]] = _round(100 * row["graduate"] / row["cohort_size"])
        note = f"Districts with a high school whose class had at least {MIN_CLASS_SIZE} students. Years are graduating classes."
    elif measure.endswith("_proficiency"):
        subject = {"math": 1, "reading": 2, "science": 3}[measure.split("_")[0]]
        for row in assessment_service.get_district_assessments(session, assessment_subgroup_id=ALL_STUDENTS, assessment_subject_id=subject, grade_id=999):
            if row["above_proficient_percentage"] is not None:
                values[row["year"]][row["district_id"]] = _round(row["above_proficient_percentage"], 0)
        note = "All tested grades. Districts the state reports only as under 10% or over 90% are left out."
    elif measure == "question_two_yes_share":
        unofficial = set()
        for row in question_two_service.get_district_results(session):
            values[row.year][row.district_id] = row.yes_percentage
            if not row.is_official:
                unofficial.add(row.year)
        note = QUESTION_TWO_NOTE + (UNOFFICIAL_NOTE if unofficial and max(unofficial) == max(values) else "")
    else:
        for row in safety_service.get_district_safety_enrollment(session):
            if row["total_enrollment"]:
                values[row["year"]][row["district_id"]] = row["total_enrollment"]
        note = "Students enrolled in the district's schools, from the state's school safety reports."
    latest = max((year for year, by_district in values.items() if any(d in names for d in by_district)), default=None)
    if latest is None:
        return {"datasets": [], "districts": []}
    highest = order != "lowest"
    ranked = sorted(((names[d], v, d) for d, v in values[latest].items() if d in names), key=lambda item: item[1], reverse=highest)
    year_text = {"graduation_rate": f"class of {latest}", "question_two_yes_share": f"{latest} election"}.get(measure, school_year(latest))
    section = DISTRICT_SECTIONS.get(topic)
    ranking = dataset(
        f"{label} by district, {year_text}, {'highest' if highest else 'lowest'} first", unit,
        ["District", label], [[name, value] for name, value, _ in ranked],
        STATE_PAGES.get(topic), note,
    )
    if topic == "question_two":
        ranking["source"] = _question_two_source(latest)
    return {
        "datasets": [ranking],
        # Each district's page on this measure, for links; Question 2 has no page yet
        "districts": [{"name": name, "page": f"/district/{district}/{section}"} for name, _, district in ranked] if section else [],
    }


# -------------------- Ranking schools --------------------

SCHOOL_RANK_MEASURES = {
    "math_proficiency": ("Percent proficient in math", "percent", "test_scores"),
    "reading_proficiency": ("Percent proficient in reading", "percent", "test_scores"),
    "science_proficiency": ("Percent proficient in science", "percent", "test_scores"),
    "graduation_rate": ("Four-year graduation rate", "percent", "graduation"),
    "students": ("Students enrolled", "count", "enrollment"),
}
# Schools by the grades they teach (grade ids: 2 is kindergarten, 3 to 14 grades 1 to 12); K-8
# schools are elementary schools
SCHOOL_LEVELS = {
    "elementary": ("elementary schools", lambda low, high: low <= 4 and 5 <= high <= 10),
    "middle": ("middle schools", lambda low, high: 7 <= low <= 9 and 10 <= high <= 11),
    "high": ("high schools", lambda low, high: high >= 14),
    "all": ("all schools", lambda low, high: True),
}
SCHOOL_LEVEL_NOTE = ("Elementary schools start by grade 2 and end between grades 3 and 8 (so K-8 schools count); middle schools "
                     "start at grade 5, 6 or 7 and end at grade 8 or 9; high schools teach grade 12.")
# Schools with fewer students tested than this (the state's lower bound) swing too much to rank
MIN_TESTED = 20
# Where the state reports only a range, as the site shows it; ranked as just inside the range
BOUNDS = {"SCORE_UNDER_10": ("<10%", 9.5), "SCORE_OVER_90": (">90%", 90.5)}


def rank_schools(session: Session, measure: str, order: str = "highest", level: str = "all", district_id: Optional[int] = None) -> dict:
    """Current public schools' latest value of one measure, sorted, with each school's page; all
    schools of one level, or a district's."""
    if measure not in SCHOOL_RANK_MEASURES:
        raise DataToolError(f"Unknown measure {measure}; use one of {', '.join(SCHOOL_RANK_MEASURES)}.")
    if level not in SCHOOL_LEVELS:
        raise DataToolError(f"Unknown level {level}; use one of {', '.join(SCHOOL_LEVELS)}.")
    label, unit, topic = SCHOOL_RANK_MEASURES[measure]
    level_name, in_level = SCHOOL_LEVELS[level]
    district = _place(session, "district", district_id) if district_id is not None else None
    districts = {d.id: d.name for d in location_service.get_districts(session, is_public=True)}
    schools = {}
    for school in location_service.get_schools(session, district_id=district["id"] if district else None):
        grades = sorted(g.id for g in (school.grades or []))
        if _field(school, "district_id_fk") in districts and grades and in_level(grades[0], grades[-1]):
            schools[school.id] = school
    values: Dict[int, Dict[int, tuple]] = defaultdict(dict)  # year -> school -> (shown, sort value)
    notes = [SCHOOL_LEVEL_NOTE]
    if measure.endswith("_proficiency"):
        subject = {"math": 1, "reading": 2, "science": 3}[measure.split("_")[0]]
        for row in assessment_service.get_school_assessments(session, district_id=district["id"] if district else None,
                                                             assessment_subgroup_id=ALL_STUDENTS, assessment_subject_id=subject, grade_id=999):
            if row["school_id"] not in schools or (row.get("total_fay_students_low") or 0) < MIN_TESTED:
                continue
            exception = getattr(row.get("above_proficient_percentage_exception"), "name", row.get("above_proficient_percentage_exception"))
            if row["above_proficient_percentage"] is not None:
                value = _round(row["above_proficient_percentage"], 0)
                values[row["year"]][row["school_id"]] = (value, value)
            elif exception in BOUNDS:
                values[row["year"]][row["school_id"]] = BOUNDS[exception]
        notes.append(f"All tested grades. Schools with fewer than {MIN_TESTED} students tested are left out; where the state reports only "
                     "under 10% or over 90%, that's shown and ranked just inside it.")
    elif measure == "graduation_rate":
        for row in outcome_service.get_school_graduation_cohort(session, district_id=district["id"] if district else None):
            if row["school_id"] in schools and row["cohort_size"] and row["cohort_size"] >= MIN_CLASS_SIZE:
                value = _round(100 * row["graduate"] / row["cohort_size"])
                values[row["year"]][row["school_id"]] = (value, value)
        notes.append(f"High schools whose class had at least {MIN_CLASS_SIZE} students. Years are graduating classes.")
    else:
        for row in enrollment_service.get_school_enrollment_totals(session):
            if row["school_id"] in schools and row["enrollment"]:
                values[row["year"]][row["school_id"]] = (row["enrollment"], row["enrollment"])
        notes.append("Students at each school on October 1, all grades.")
    latest = max((year for year, by_school in values.items() if by_school), default=None)
    if latest is None:
        return {"datasets": [], "schools": []}
    highest = order != "lowest"
    ranked = sorted(values[latest].items(), key=lambda item: (-item[1][1] if highest else item[1][1], schools[item[0]].name))
    year_text = f"class of {latest}" if measure == "graduation_rate" else school_year(latest)
    where = f" in {district['name']}" if district else ""
    section = SCHOOL_SECTIONS[topic]
    return {
        "datasets": [dataset(
            f"{label} by school, {level_name}{where}, {year_text}, {'highest' if highest else 'lowest'} first", unit,
            ["School", "District", "Grades", label],
            [[schools[i].name.strip(), districts[_field(schools[i], "district_id_fk")], _grade_span(schools[i]), shown] for i, (shown, _) in ranked],
            page_for(district, topic) if district else STATE_PAGES[topic], " ".join(notes),
        )],
        # Each school's page on this measure, for links
        "schools": [{"name": schools[i].name.strip(), "page": f"/school/{i}/{section}"} for i, _ in ranked],
    }


# -------------------- Comparing places --------------------

# What compare_places lines up for each topic: (dataset key, column, label)
COMPARE_MEASURES = {
    "enrollment": [("students", 1, "Students"), ("low_income", "Share of students", "Low-income share"), ("english_learners", "Share of students", "English learner share"),
                   ("disabilities", "Share of students", "Students with disabilities share")],
    "test_scores": [("proficiency", "Math", "Percent proficient in math"), ("proficiency", "Reading", "Percent proficient in reading"), ("proficiency", "Science", "Percent proficient in science")],
    "graduation": [("cohorts", "Graduated", "Four-year graduation rate"), ("cohorts", "Dropped out", "Dropped out"), ("plans", "Four-Year College", "Planning a four-year college")],
    "spending": [("cost", "All grades", "Cost per student"), ("revenue", "Local share", "Share of revenue from local sources"),
                 ("categories", "Special education share", "Special education share of spending")],
    "balance_sheet": [("fund_balance", "Unassigned fund balance", "Unassigned fund balance"), ("fund_balance", "Total fund balance", "Total fund balance")],
    "staff": [("salary", "Average salary", "Average teacher salary"), ("schedule", "Starting, bachelor's", "Starting teacher salary (bachelor's)"),
              ("class_size", "Grades 3-4", "Average class size, grades 3-4"), ("degrees", "Share with a master's or more", "Teachers with a master's or more")],
    "safety": [("truancy", "Share of students", "Share of students truant"), ("bullying", "Reports per 1,000 students", "Bullying reports per 1,000 students"),
               ("restraint", "Restraints per 1,000 students", "Restraints per 1,000 students"), ("incidents", "All serious incidents", "Serious safety incidents")],
    "efa": [("efa_students", "EFA students", "EFA students"), ("efa_students", "Share of public school students", "EFA students as a share of public school students")],
    "question_two": [("question_two", "Yes share", "Question 2 yes share"), ("question_two", "Adopted the school tax cap", "Adopted the school tax cap")],
}
MAX_COMPARE = 5


def compare_places(session: Session, topic: str, places: List[dict]) -> dict:
    """The same measures for several places side by side: each measure by year with a column per
    place, and the latest year shared by all as one table with a row per place."""
    if topic not in COMPARE_MEASURES:
        raise DataToolError(f"Comparisons cover {', '.join(COMPARE_MEASURES)}; for {topic}, call get_data for each place.")
    if not 2 <= len(places) <= MAX_COMPARE:
        raise DataToolError(f"Compare 2 to {MAX_COMPARE} places.")
    found = []
    for item in places:
        place = _place(session, item.get("level"), item.get("id"))
        if place["level"] == "school" and topic not in SCHOOL_SECTIONS:
            raise DataToolError(f"{topic} isn't reported for individual schools; compare their districts.")
        name = "New Hampshire" if place["level"] == "state" else place["name"]
        found.append((name, {d["key"]: d for d in TOPIC_FUNCTIONS[topic](session, place) if d.get("key")}))
    names = [name for name, _ in found]
    results = []
    latest_rows: Dict[str, dict] = defaultdict(dict)
    latest_units: Dict[str, str] = {}
    for key, column, label in COMPARE_MEASURES[topic]:
        by_label: Dict[str, dict] = defaultdict(dict)
        unit, first_column, source = None, None, None
        for name, datasets in found:
            data = datasets.get(key)
            if not data:
                continue
            index = column if isinstance(column, int) else data["columns"].index(column) if column in data["columns"] else None
            if index is None:
                continue
            unit = unit or data["units"][data["columns"][index]]
            first_column = first_column or data["columns"][0]
            # Data with no site page (Question 2) names its outside source instead
            source = source or data.get("source")
            for row in data["rows"]:
                by_label[row[0]][name] = row[index]
        if not by_label:
            continue
        labels = sorted(by_label)
        present = [name for name in names if any(name in values for values in by_label.values())]
        results.append(dataset(
            f"{label} by year: {', '.join(present)}", unit, [first_column, *present],
            [[x, *(by_label[x].get(name) for name in present)] for x in labels], STATE_PAGES.get(topic),
        ))
        if source:
            results[-1]["source"] = source
        shared = [x for x in labels if all(by_label[x].get(name) is not None for name in present)]
        if shared:
            heading = f"{label} ({shared[-1]})"
            latest_units[heading] = unit
            for name in present:
                latest_rows[name][heading] = by_label[shared[-1]][name]
    if latest_rows:
        columns = list(latest_units)
        results.append(dataset(
            f"Latest comparison: {', '.join(names)}", "number", ["Place", *columns],
            [[name, *(latest_rows[name].get(heading) for heading in columns)] for name in names if name in latest_rows],
            STATE_PAGES.get(topic), "Each measure's latest year that every place has, shown in its column heading.", latest_units,
        ))
        if any(item.get("source") for item in results):
            results[-1]["source"] = next(item["source"] for item in results if item.get("source"))
    return {"places": names, "datasets": results}


TOPIC_FUNCTIONS: Dict[str, Callable[[Session, dict], List[dict]]] = {
    "enrollment": _enrollment,
    "test_scores": _test_scores,
    "graduation": _graduation,
    "spending": _spending,
    "balance_sheet": _balance_sheet,
    "staff": _staff,
    "safety": _safety,
    "efa": _efa,
    "question_two": _question_two,
}


def get_data(session: Session, topic: str, level: str, place_id: Optional[int] = None) -> dict:
    """The datasets for one topic at one place, with the place's name."""
    if topic not in TOPIC_FUNCTIONS:
        raise DataToolError(f"Unknown topic {topic}; use one of {', '.join(TOPICS)}.")
    if level not in LEVELS:
        raise DataToolError(f"Unknown level {level}; use state, district or school.")
    place = _place(session, level, place_id)
    if level == "school" and topic not in SCHOOL_SECTIONS:
        raise DataToolError(f"{topic} isn't reported for individual schools; ask for the school's district (district id {place.get('district_id')}).")
    datasets = TOPIC_FUNCTIONS[topic](session, place)
    return {"place": place["name"], "datasets": datasets}
