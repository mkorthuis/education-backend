"""
Assessment results by state, district and school, from the state's yearly assessment files.

The files (app/alembic/assets/assessments/assessments-YYYY.csv) come in two layouts:
- 2009-2018, "replevel" layout: rows carry the district and school ids (discode, schcode).
  The 2009-2017 files have school rows for all students only; 2018 adds subgroups and
  district and state rows.
- 2019 onward, "Level of Data" layout: state, district and school rows, districts and
  schools matched by name. There was no test in 2020.

Loading a year replaces that year's rows in assessment_state, assessment_district and
assessment_school. For the school-only years (assessment_historical_data_config.yaml) the
district and state rows are then generated from the school rows. Newer files have their
own district and state rows, so a new year needs only its file.

The tables' unique keys include grade_id_fk, which is NULL for "all grades" rows, so rows
can't be upserted on them; whole years are replaced instead and reloaded rows get new ids.
"""
import logging
import re
from collections import Counter, defaultdict
from typing import Iterable, Optional

import pandas as pd
from sqlalchemy import text
from sqlalchemy.engine import Connection

from app.etl.core import (
    configured_years, existing_ids, known_school_ids, load_config, lookup_ids, refresh_dependent_views,
    replace_rows, year_file
)

logger = logging.getLogger("app.etl")

CONFIG = "assessment_data_config.yaml"                        # 2019 onward
HISTORICAL_CONFIG = "assessment_historical_data_config.yaml"  # school-only years
YEAR_2018 = 2018  # replevel layout with subgroups; its file is found through CONFIG's file pattern

TABLES = ("assessment_state", "assessment_district", "assessment_school")
VALUE_COLUMNS = (
    "assessment_subject_id_fk", "year", "grade_id_fk", "assessment_subgroup_id_fk",
    "total_fay_students_low", "total_fay_students_high",
    "level_1_percentage", "level_1_percentage_exception",
    "level_2_percentage", "level_2_percentage_exception",
    "level_3_percentage", "level_3_percentage_exception",
    "level_4_percentage", "level_4_percentage_exception",
    "above_proficient_percentage", "above_proficient_percentage_exception",
    "participate_percentage", "mean_sgp", "average_score",
)
COLUMNS = {
    "assessment_state": VALUE_COLUMNS,
    "assessment_district": ("district_id_fk",) + VALUE_COLUMNS,
    "assessment_school": ("school_id_fk",) + VALUE_COLUMNS,
}

SUBJECT_IDS = {"mat": 1, "rea": 2, "sci": 3, "Math": 1, "Reading": 2, "Science": 3, "MAT": 1, "REA": 2, "SCI": 3}
ALL_GRADES = {"0", "all", "all grades"}  # stored as grade_id_fk NULL
ALL_STUDENTS = "All students"

# Values of the assessment_exception enum (AssessmentException names)
TOO_FEW_SAMPLES, SCORE_UNDER_10, SCORE_OVER_90 = "TOO_FEW_SAMPLES", "SCORE_UNDER_10", "SCORE_OVER_90"

# Column names per layout; subgroup, participation and mean SGP are missing from some years
LEVEL_OF_DATA = {
    "level": "Level of Data", "levels": {"State Level": "state", "District Level": "district", "School Level": "school"},
    "subject": "Subject", "grade": "Grade", "subgroup": "Subgroup", "students": "Total FAY Students",
    "percentages": ("level1%", "level2%", "level3%", "level4%", "Above prof% (lvl 3&4)"),
    "participate": "Participate%", "mean_sgp": "Mean SGP", "average_score": "Avg Score",
    "optional": ("Mean SGP",),
}
REPLEVEL = {
    "level": "replevel", "levels": {"sta": "state", "dis": "district", "sch": "school"},
    "subject": "subject", "grade": "grade", "subgroup": "subgroup", "students": "NumberStudents",
    "percentages": ("plevel1", "plevel2", "plevel3", "plevel4", "pAboveprof"),
    "participate": "pParticipate", "mean_sgp": "MeanSGP", "average_score": "AvgScore",
    "optional": ("subgroup", "pParticipate", "MeanSGP"),
}

# Generated district and state rows: all students, these grades (None: all grades)
GENERATED_GRADES = ("Grade 3", "Grade 4", "Grade 5", "Grade 6", "Grade 7", "Grade 8", "Grade 11", None)
PART_COLUMNS = (
    "total_fay_students_low", "total_fay_students_high",
    "level_1_percentage", "level_1_percentage_exception",
    "level_2_percentage", "level_2_percentage_exception",
    "level_3_percentage", "level_3_percentage_exception",
    "level_4_percentage", "level_4_percentage_exception",
    "above_proficient_percentage", "above_proficient_percentage_exception",
    "average_score",
)
LEVEL_FIELDS = ("level_1_percentage", "level_2_percentage", "level_3_percentage", "level_4_percentage",
                "above_proficient_percentage")
KEY_COLUMNS = ("assessment_subject_id_fk", "year", "grade_id_fk", "assessment_subgroup_id_fk")


def parse_percentage(value) -> tuple:
    """(percentage, exception) from a cell: "* n < 11" is too few students, "<10" and ">90" are bands."""
    if pd.isna(value) or value == "" or value == "-":
        return None, None
    if "*" in value:
        return None, TOO_FEW_SAMPLES
    if "<" in value and "10" in value:
        return None, SCORE_UNDER_10
    if ">" in value and "90" in value:
        return None, SCORE_OVER_90
    cleaned = re.sub(r"[^0-9.]", "", value)
    if cleaned == "":
        return None, None
    return float(cleaned), None


def parse_students(value) -> tuple:
    """(low, high) from a student count range like "35 - 40", or a single count."""
    if pd.isna(value) or value == "" or value == "-":
        return None, None
    value = value.replace(",", "")
    match = re.search(r"(\d+)\s*-\s*(\d+)", value)
    if match:
        return int(match.group(1)), int(match.group(2))
    try:
        count = int(float(re.sub(r"[^0-9.]", "", value)))
    except ValueError:
        return None, None
    if count == 43753:
        # A spreadsheet turned some 2019 ranges into this date
        return None, None
    return count, count


def parse_number(value) -> Optional[float]:
    """A plain number, or None for blanks and notes like "Not available" or "* n < 11"."""
    if pd.isna(value):
        return None
    try:
        return float(value)
    except ValueError:
        return None


class Subgroups:
    """Subgroup ids by name; new names get the next id in order of first appearance."""

    def __init__(self, conn: Connection):
        self.ids = lookup_ids(conn, "assessment_subgroup")
        self.new = []

    def id(self, name: str) -> int:
        if name not in self.ids:
            self.ids[name] = max(self.ids.values(), default=0) + 1
            self.new.append((self.ids[name], name))
        return self.ids[name]

    def save(self, conn: Connection) -> None:
        if self.new:
            logger.info(f"New assessment subgroups: {self.new}")
            replace_rows(conn, "assessment_subgroup", ("id", "name"), self.new)
            self.new = []


def _settings(config: str) -> dict:
    return load_config(config)["file_settings"]


def historical_years() -> list:
    """The school-only years (assessment_historical_data_config.yaml)."""
    return configured_years(_settings(HISTORICAL_CONFIG))


def current_years() -> list:
    """The years in assessment_data_config.yaml, less its missing_years (no test given)."""
    settings = _settings(CONFIG)
    return [y for y in configured_years(settings) if y not in settings["missing_years"]]


def loadable_years() -> list:
    """Every year with a file: the historical years, 2018, then the current years."""
    return historical_years() + [YEAR_2018] + current_years()


def _source(year: int) -> tuple:
    """(path, encoding, layout) of one year's file."""
    if year in historical_years():
        return year_file(_settings(HISTORICAL_CONFIG), year), "latin1", REPLEVEL
    if year == YEAR_2018:
        return year_file(_settings(CONFIG), year), None, REPLEVEL
    if year in current_years():
        return year_file(_settings(CONFIG), year), None, LEVEL_OF_DATA
    raise ValueError(f"No assessment file is configured for {year}; loadable years: {loadable_years()}")


def _name(value):
    """A district or school name for matching, with outer spaces removed and inner runs of spaces
    collapsed; the state's files and lists sometimes pad names (e.g. "Newfound Area ")."""
    if not isinstance(value, str):
        return value
    return " ".join(value.split())


def _check_alias_ids(conn: Connection, table: str, ids) -> None:
    """Fail if the config aliases a name to an id the table doesn't have."""
    missing = sorted(set(ids) - existing_ids(conn, table))
    if missing:
        raise ValueError(f"{CONFIG} aliases names to {table} ids that aren't in the database: {missing}")


def _district_lookup(conn: Connection, aliases: dict) -> dict:
    """District ids by name (the first id wins), plus the config's older names of renamed districts."""
    ids = {}
    for district_id, name in conn.execute(text("SELECT id, name FROM district ORDER BY id")):
        ids.setdefault(_name(name), district_id)
    _check_alias_ids(conn, "district", aliases.values())
    ids.update({_name(name): district_id for name, district_id in aliases.items()})
    return ids


def _school_lookups(conn: Connection, aliases: dict) -> tuple:
    """
    School ids by (school name, district name) and by school name; the first id wins. The
    config's aliases add (school name, district name) pairs from the files for schools since
    renamed or moved to another district.
    """
    by_district, by_name = {}, {}
    for school_id, name, district in conn.execute(text(
        "SELECT s.id, s.name, d.name FROM school s LEFT JOIN district d ON s.district_id_fk = d.id ORDER BY s.id"
    )):
        by_name.setdefault(_name(name), school_id)
        if district is not None:
            by_district.setdefault((_name(name), _name(district)), school_id)
    _check_alias_ids(conn, "school", [i for schools in aliases.values() for i in schools.values()])
    by_district.update({(_name(name), _name(district)): school_id
                        for district, schools in aliases.items() for name, school_id in schools.items()})
    return by_district, by_name


def _school_id(lookups: tuple, name: str, district) -> Optional[int]:
    by_district, by_name = lookups
    if district and not pd.isna(district):
        return by_district.get((_name(name), _name(district)))
    return by_name.get(_name(name))


def _code(value) -> Optional[int]:
    """A district or school id from a replevel file; blank, NULL and 0 mean none."""
    if pd.isna(value) or value in ("", "NULL", "0"):
        return None
    return int(value)


def _add_to_merged(merged: dict, key: tuple, values: tuple, district) -> None:
    """Collect a merged school's numbers: counts, then the non-null percentages and scores."""
    low, high = values[4], values[5]
    numbers = values[6:16:2] + values[16:19]
    data = merged.setdefault(key, {"low": 0, "high": 0, "values": [[] for _ in numbers], "district": district})
    data["low"] += low or 0
    data["high"] += high or 0
    for collected, number in zip(data["values"], numbers):
        if number is not None:
            collected.append(number)
    if not data["district"] and district:
        data["district"] = district


def _merge_rows(merged: dict, lookups: tuple, skipped: Counter) -> list:
    """
    One school row per merged school (several file schools mapped to one school by the config).

    Counts are summed and percentages averaged over the rows that have a number; exceptions
    are dropped, as in the original migration.
    """
    rows = []
    for (name, year, subject_id, grade_id, subgroup_id), data in merged.items():
        school_id = _school_id(lookups, name, data["district"])
        if school_id is None:
            skipped[f"merged school not found: {name}"] += 1
            continue
        averages = [sum(v) / len(v) if v else None for v in data["values"]]
        low, high = data["low"], data["high"]
        levels = [x for average in averages[:5] for x in (average, None)]
        rows.append((school_id, subject_id, year, grade_id, subgroup_id,
                     low if low > 0 else None, high if high > 0 else None, *levels, *averages[5:]))
    return rows


def _check_not_found(config: dict, districts: set, schools: set) -> None:
    """
    Fail if a file names a district, or a (school, district) pair, that matches nothing and isn't
    in the config's skipped_districts or skipped_schools (a skipped district's schools are skipped too).
    """
    skipped_districts = {_name(d) for d in config.get("skipped_districts") or []}
    skipped_schools = {(_name(school), _name(district))
                       for district, schools in (config.get("skipped_schools") or {}).items() for school in schools}
    unknown = sorted(d for d in districts if _name(d) not in skipped_districts)
    unknown += sorted(f"{school} ({district})" for school, district in schools
                      if _name(district) not in skipped_districts
                      and (_name(school), _name(district)) not in skipped_schools)
    if unknown:
        raise ValueError(f"Assessment files name districts or schools that match nothing in the database; add each "
                         f"to the aliases or skipped lists in {CONFIG}: {unknown}")


def load_files(conn: Connection, years: Iterable[int]) -> dict:
    """
    Replace the given years' state, district and school rows with the rows in their files.

    Rows are inserted in file order, years in the order given, then the rows of merged
    schools, so a fresh build assigns the ids the original migrations did. Rows for
    districts and schools that aren't in the database are skipped and reported.
    """
    years = list(years)
    config = load_config(CONFIG)
    translations = {_name(k): _name(v) for k, v in config["school_name_translations"].items()}
    merged_names = {t for t in translations.values() if list(translations.values()).count(t) > 1}

    subgroups = Subgroups(conn)
    grade_ids = lookup_ids(conn, "grades")
    district_ids = _district_lookup(conn, config.get("district_id_aliases") or {})
    known_districts, known_schools = existing_ids(conn, "district"), known_school_ids(conn)
    schools = _school_lookups(conn, config.get("school_id_aliases") or {})

    rows = {table: [] for table in TABLES}
    merged, skipped, not_found = {}, Counter(), defaultdict(set)
    unmatched_districts, unmatched_schools = set(), set()
    for year in years:
        path, encoding, layout = _source(year)
        df = pd.read_csv(path, dtype=str, encoding=encoding)
        required = [layout[k] for k in ("level", "subject", "grade", "subgroup", "students", "participate",
                                        "mean_sgp", "average_score")] + list(layout["percentages"])
        missing = [c for c in required if c not in df.columns and c not in layout["optional"]]
        if missing:
            raise ValueError(f"{path} is missing columns {missing}")
        logger.info(f"Assessments {year}: {len(df)} rows in {path}")

        for row in df.to_dict("records"):
            if pd.isna(row[layout["subject"]]) or pd.isna(row[layout["level"]]):
                skipped["blank subject or level"] += 1
                continue
            subject_id = SUBJECT_IDS.get(row[layout["subject"]])
            if subject_id is None:
                skipped[f"unknown subject {row[layout['subject']]!r}"] += 1
                continue

            subgroup = row.get(layout["subgroup"], ALL_STUDENTS)
            if pd.isna(subgroup) or not subgroup.strip():
                raise ValueError(f"Blank subgroup in {path}: {row}")
            subgroup_id = subgroups.id(subgroup.strip())

            file_year = row.get("yearid")
            if not pd.isna(file_year) and re.fullmatch(r"\d+(\.0*)?", file_year) and int(float(file_year)) != year:
                raise ValueError(f"Row for year {file_year} in the {year} file {path}")

            grade = row[layout["grade"]]
            grade = "0" if pd.isna(grade) else grade.strip().lower()
            if grade in ALL_GRADES:
                grade_id = None
            else:
                grade_id = grade_ids[f"Grade {grade[1:] if grade.startswith('0') and grade[1:].isdigit() else grade}"]

            percentages = [parse_percentage(row[c]) for c in layout["percentages"]]
            values = (subject_id, year, grade_id, subgroup_id, *parse_students(row[layout["students"]]),
                      *[x for pair in percentages for x in pair],
                      parse_percentage(row.get(layout["participate"]))[0],
                      parse_number(row.get(layout["mean_sgp"])), parse_number(row[layout["average_score"]]))

            level = layout["levels"].get(row[layout["level"]].strip())
            if level == "state":
                rows["assessment_state"].append(values)
            elif level is None:
                skipped[f"unknown level {row[layout['level']]!r}"] += 1
            elif layout is REPLEVEL:
                unit_id = _code(row["discode"] if level == "district" else row["schcode"])
                if unit_id in (known_districts if level == "district" else known_schools):
                    unit_id = unit_id if level == "district" else known_schools[unit_id]
                    rows[f"assessment_{level}"].append((unit_id, *values))
                else:
                    skipped[f"{level} not in the database"] += 1
                    not_found[level].add(unit_id)
            elif level == "district":
                district_id = district_ids.get(_name(row["District"]))
                if district_id is None:
                    skipped["district not in the database"] += 1
                    not_found["district"].add(row["District"])
                    unmatched_districts.add(row["District"])
                else:
                    rows["assessment_district"].append((district_id, *values))
            else:
                name = row["School"]
                if pd.isna(name) or not name:
                    skipped["school row without a school name"] += 1
                    continue
                name = _name(name)
                name = translations.get(name, name)
                if name in merged_names:
                    _add_to_merged(merged, (name, year, subject_id, grade_id, subgroup_id), values, row["District"])
                    continue
                school_id = _school_id(schools, name, row["District"])
                if school_id is None:
                    skipped["school not in the database"] += 1
                    not_found["school"].add(f"{name} ({row['District']})")
                    unmatched_schools.add((name, row["District"]))
                else:
                    rows["assessment_school"].append((school_id, *values))

    rows["assessment_school"].extend(_merge_rows(merged, schools, skipped))
    _check_not_found(config, unmatched_districts, unmatched_schools)
    if skipped:
        # Rows for districts and schools missing from the database are skipped, as the original migrations did
        logger.warning(f"Assessments {years}: skipped rows: {dict(skipped)}; not found: "
                       f"{ {level: sorted(names, key=str) for level, names in not_found.items()} }")

    subgroups.save(conn)
    counts = {}
    for table in TABLES:
        counts[table] = replace_rows(conn, table, COLUMNS[table], rows[table],
                                     where="year = ANY(:years)", params={"years": years})
    return counts


def _parts(conn: Connection, table: str, unit_column: str, years: list, subgroup_id: int) -> list:
    """(unit id, subject, year, grade, values) of a table's all-students rows, in id order."""
    result = conn.execute(text(f"""
        SELECT {unit_column}, {", ".join(KEY_COLUMNS[:3])}, {", ".join(PART_COLUMNS)}
        FROM {table}
        WHERE year = ANY(:years) AND assessment_subgroup_id_fk = :subgroup_id
        ORDER BY id
    """), {"years": years, "subgroup_id": subgroup_id})
    return [(row[0], row[1], row[2], row[3], dict(zip(PART_COLUMNS, row[4:]))) for row in result]


def _has_too_few_samples(part: dict) -> bool:
    return any(part[f"{field}_exception"] == TOO_FEW_SAMPLES for field in LEVEL_FIELDS)


def _band_value(part: dict, field: str):
    """A level percentage, with the <10 and >90 bands counted as 9 and 91."""
    exception = part[f"{field}_exception"]
    if exception == SCORE_UNDER_10:
        return 9.0
    if exception == SCORE_OVER_90:
        return 91.0
    return part[field]


def _weighted_average(values: list, weights: list) -> Optional[float]:
    valid = [(v, w) for v, w in zip(values, weights) if v is not None]
    if not valid:
        return None
    total_weight = sum(w for _, w in valid)
    if total_weight == 0:
        return None
    return sum(float(v) * float(w) for v, w in valid) / float(total_weight)


def _weighted_exception(values: list, weights: list) -> Optional[str]:
    """The exception with the largest total weight; the first one seen wins a tie."""
    totals = {}
    for value, weight in zip(values, weights):
        if value is not None:
            totals[value] = totals.get(value, 0) + weight
    return max(totals.items(), key=lambda item: item[1])[0] if totals else None


def _combine(parts: list) -> Optional[dict]:
    """
    Combine rows (schools of a district, or districts) into one, weighted by student count.

    Rows with any too-few-students exception are left out. Counts are summed; the weight
    is the middle of the count range. Exceptions take the value with the most weight.
    """
    parts = [p for p in parts if not _has_too_few_samples(p)]
    if not parts:
        return None
    weights = []
    for p in parts:
        low, high = p["total_fay_students_low"] or 0, p["total_fay_students_high"] or 0
        weights.append((low + high) / 2 if low and high else low or high or 1)

    combined = {}
    for column in ("total_fay_students_low", "total_fay_students_high"):
        counts = [p[column] for p in parts if p[column] is not None]
        total = sum(counts) if counts else None
        combined[column] = total if total and total > 0 else None
    for field in LEVEL_FIELDS:
        combined[field] = _weighted_average([_band_value(p, field) for p in parts], weights)
        combined[f"{field}_exception"] = _weighted_exception([p[f"{field}_exception"] for p in parts], weights)
    combined["average_score"] = _weighted_average([p["average_score"] for p in parts], weights)
    return combined


def _single(part: dict) -> Optional[dict]:
    """A district with one school takes its row, with bands counted as 9 and 91, unless it is too small."""
    if _has_too_few_samples(part):
        return None
    return {**part, **{field: _band_value(part, field) for field in LEVEL_FIELDS}}


def _generated_grade_ids(conn: Connection) -> list:
    grade_ids = lookup_ids(conn, "grades")
    return [None if grade is None else grade_ids[grade] for grade in GENERATED_GRADES]


def _subject_ids(conn: Connection) -> list:
    return [row[0] for row in conn.execute(text("SELECT id FROM assessment_subject ORDER BY id"))]


def _all_students(conn: Connection) -> int:
    subgroups = Subgroups(conn)
    subgroup_id = subgroups.id(ALL_STUDENTS)
    subgroups.save(conn)
    return subgroup_id


def generate_district_rows(conn: Connection, years: Iterable[int]) -> dict:
    """
    Add all-students district rows aggregated from the district's school rows, for each
    district, year, subject and grade that has school rows but no district row yet.

    For the years whose files have school rows only (2009-2017).
    """
    years = list(years)
    subgroup_id = _all_students(conn)
    grade_ids, subject_ids = _generated_grade_ids(conn), _subject_ids(conn)

    district_schools = defaultdict(list)
    for school_id, district_id in conn.execute(text("SELECT id, district_id_fk FROM school ORDER BY id")):
        district_schools[district_id].append(school_id)
    school_parts = {}
    for school_id, subject_id, year, grade_id, part in _parts(conn, "assessment_school", "school_id_fk",
                                                               years, subgroup_id):
        school_parts.setdefault((school_id, year, subject_id, grade_id), part)
    existing = {key[:4] for key in _parts(conn, "assessment_district", "district_id_fk", years, subgroup_id)}

    rows = []
    for district_id in [row[0] for row in conn.execute(text("SELECT id FROM district ORDER BY id"))]:
        for year in years:
            for subject_id in subject_ids:
                for grade_id in grade_ids:
                    if (district_id, subject_id, year, grade_id) in existing:
                        continue
                    parts = [school_parts[key] for key in
                             ((s, year, subject_id, grade_id) for s in district_schools[district_id])
                             if key in school_parts]
                    if not parts:
                        continue
                    combined = _single(parts[0]) if len(parts) == 1 else _combine(parts)
                    if combined:
                        rows.append((district_id, subject_id, year, grade_id, subgroup_id,
                                     *[combined[c] for c in PART_COLUMNS]))

    columns = ("district_id_fk",) + KEY_COLUMNS + PART_COLUMNS
    return replace_rows(conn, "assessment_district", columns, rows)


def generate_state_rows(conn: Connection, years: Iterable[int]) -> dict:
    """
    Add all-students state rows aggregated from the district rows, for each year, subject
    and grade that has district rows but no state row yet.

    For the years whose files have school rows only (2009-2017), after generate_district_rows.
    """
    years = list(years)
    subgroup_id = _all_students(conn)
    grade_ids, subject_ids = _generated_grade_ids(conn), _subject_ids(conn)

    district_parts = defaultdict(list)
    for _, subject_id, year, grade_id, part in _parts(conn, "assessment_district", "district_id_fk",
                                                      years, subgroup_id):
        district_parts[(year, subject_id, grade_id)].append(part)
    existing = {(year, subject_id, grade_id) for subject_id, year, grade_id in conn.execute(text(
        "SELECT assessment_subject_id_fk, year, grade_id_fk FROM assessment_state "
        "WHERE year = ANY(:years) AND assessment_subgroup_id_fk = :subgroup_id"
    ), {"years": years, "subgroup_id": subgroup_id})}

    rows = []
    for year in years:
        for subject_id in subject_ids:
            for grade_id in grade_ids:
                if (year, subject_id, grade_id) in existing:
                    continue
                combined = _combine(district_parts[(year, subject_id, grade_id)])
                if combined:
                    rows.append((subject_id, year, grade_id, subgroup_id, *[combined[c] for c in PART_COLUMNS]))

    return replace_rows(conn, "assessment_state", KEY_COLUMNS + PART_COLUMNS, rows)


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """
    Load the given years (default: every year with a file): replace their file rows, then
    for school-only years generate the district and state rows.
    """
    loadable = loadable_years()
    years = loadable if years is None else sorted(set(int(y) for y in years))
    outside = [y for y in years if y not in loadable]
    if outside:
        raise ValueError(f"Years {outside} have no configured assessment file; loadable years: {loadable}. "
                         f"For a new year, add its file and raise year_end in {CONFIG}")

    counts = load_files(conn, years)
    school_only = [y for y in years if y in historical_years()]
    if school_only:
        counts["generated assessment_district"] = generate_district_rows(conn, school_only)
        counts["generated assessment_state"] = generate_state_rows(conn, school_only)
    counts["views_refreshed"] = [view for table in TABLES for view in refresh_dependent_views(conn, table)]
    return counts
