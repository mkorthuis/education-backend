"""
The NCES Private School Survey's answers for New Hampshire's private schools, every two years (see
private_school_survey_config.yaml), into:

- school_private_survey: a school's survey year: its type, affiliation and religious orientation,
  level and community; students (K-12 and ungraded, and with preschool), full-time-equivalent teachers
  and students per teacher, male students and the shares of each race; the school day's length; and
  for a high school, its seniors the year before and the share of those graduates who went on to a
  four-year college
- school_private_survey_grade: its students by grade

Schools are matched by NCES's PPIN (pss-school-match.csv); NCES has given a few schools a new one, so
a school can have several, but only one row a year. Coded answers are stored as the codebook's labels;
a code the config has no label for stops the load.
"""
import csv
import logging
import os
from decimal import Decimal, ROUND_HALF_UP
from typing import Iterable, Optional

from sqlalchemy import text
from sqlalchemy.engine import Connection

from app.etl.core import config_path, existing_ids, load_config, upsert_rows

logger = logging.getLogger("app.etl")

CONFIG = "private_school_survey_config.yaml"
# The survey's coded answers: column -> the config's list of labels
CODED = {"typology": "TYPOLOGY", "affiliation": "RELIG", "religious_orientation": "ORIENT", "level": "LEVEL", "community_type": "UCOMMTYP"}
COUNTS = {"students": "NUMSTUDS", "students_with_preschool": "P305", "male_students": "MALES",
          "seniors_prior_year": "P350", "to_four_year_college_pct": "P360"}
# Rounded to the hundredth, as the table keeps them
MEASURES = {"teachers_fte": "NUMTEACH", "students_per_teacher": "STTCH_RT", "school_day_hours": "TOTHRS",
            "pct_american_indian": "P_INDIAN", "pct_asian": "P_ASIAN", "pct_pacific_islander": "P_PACIFIC",
            "pct_hispanic": "P_HISP", "pct_white": "P_WHITE", "pct_black": "P_BLACK", "pct_two_or_more_races": "P_TR"}
COLUMNS = ("school_id_fk", "year", "ppin", *CODED, *COUNTS, *MEASURES)


def answer(record: dict, column: str) -> Optional[Decimal]:
    """A survey answer; blank, or negative (the survey's "valid skip"), is no answer."""
    value = (record.get(column) or "").strip()
    if not value:
        return None
    number = Decimal(value)
    return None if number < 0 else number


def labelled(record: dict, column: str, labels: dict, path: str) -> Optional[str]:
    code = answer(record, column)
    if code is None:
        return None
    if int(code) not in labels:
        raise ValueError(f"{path}: {column} code {int(code)} has no label in {CONFIG}")
    return labels[int(code)]


def read_matches(path: str) -> dict:
    """
    PPIN -> (school id, the survey years it's matched in, or None for every year). A school renumbered by
    NCES has a row for each of its PPINs.
    """
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    matches = {row["ppin"]: (int(row["school_id"]), {int(year) for year in row["years"].split()} or None) for row in rows}
    if len(matches) != len(rows):
        raise ValueError(f"{path}: a PPIN listed twice")
    return matches


def survey_rows(path: str, year: int, matches: dict, config: dict, grade_ids: dict) -> tuple:
    """A survey file's rows for the matched schools, their students by grade, and the PPINs no school matches."""
    rows, grades, unmatched = [], [], []
    # The 2017-18 file's first column name carries a mangled byte-order mark; it isn't read
    with open(path, newline="", encoding="utf-8", errors="replace") as f:
        for record in csv.DictReader(f):
            ppin = record["PPIN"].strip()
            school_id, match_years = matches.get(ppin, (None, None))
            if school_id is None or (match_years is not None and year not in match_years):
                unmatched.append(ppin)
                continue
            if any(row[0] == school_id for row in rows):
                raise ValueError(f"{path}: school {school_id} matches two of the year's PPINs")
            counts = {name: answer(record, column) for name, column in COUNTS.items()}
            measures = {name: answer(record, column) for name, column in MEASURES.items()}
            rows.append((
                school_id, year, ppin,
                *(labelled(record, column, config[name], path) for name, column in CODED.items()),
                *(int(value) if value is not None else None for value in counts.values()),
                *(value.quantize(Decimal("0.01"), ROUND_HALF_UP) if value is not None else None for value in measures.values()),
            ))
            by_grade = {}
            for column, grade in config["grade_columns"].items():
                students = answer(record, column)
                if students:
                    by_grade[grade_ids[grade]] = by_grade.get(grade_ids[grade], 0) + int(students)
            grades += [(school_id, year, grade_id, students) for grade_id, students in sorted(by_grade.items())]
    return rows, grades, unmatched


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the given survey years (default: every configured one)."""
    config = load_config(CONFIG)
    directory = config_path(config["directory"])
    matches = read_matches(os.path.join(directory, config["match_file"]))
    unknown = sorted({school_id for school_id, _ in matches.values()} - existing_ids(conn, "school"))
    if unknown:
        raise ValueError(f"{config['match_file']}: school ids not in the school table: {unknown}")
    grade_ids = dict(conn.execute(text("SELECT name, id FROM grades")).fetchall())
    missing = sorted(set(config["grade_columns"].values()) - set(grade_ids))
    if missing:
        raise ValueError(f"{CONFIG}: grades not in the grades table: {missing}")

    wanted = sorted(years) if years else sorted(config["files"])
    rows, grades = [], []
    for year in wanted:
        year_rows, year_grades, unmatched = survey_rows(os.path.join(directory, config["files"][year]), year, matches, config, grade_ids)
        rows += year_rows
        grades += year_grades
        logger.info(f"Private School Survey {year}: {len(year_rows)} schools; {len(unmatched)} schools not on the state's list or not matched")

    # A school year reloaded loses the grades its school no longer reports
    deleted = 0
    for school_id, year in {(row[0], row[1]) for row in rows}:
        kept = [grade_id for s, y, grade_id, _ in grades if (s, y) == (school_id, year)]
        deleted += conn.execute(text("""
            DELETE FROM school_private_survey_grade
            WHERE school_id_fk = :school AND year = :year AND NOT (grade_id_fk = ANY(:kept))
        """), {"school": school_id, "year": year, "kept": kept}).rowcount
    counts = {
        "school_private_survey": upsert_rows(conn, "school_private_survey", COLUMNS, ("school_id_fk", "year"), rows),
        "school_private_survey_grade": upsert_rows(conn, "school_private_survey_grade",
                                                   ("school_id_fk", "year", "grade_id_fk", "students"),
                                                   ("school_id_fk", "year", "grade_id_fk"), grades),
    }
    counts["school_private_survey_grade"]["deleted"] = deleted
    return counts
