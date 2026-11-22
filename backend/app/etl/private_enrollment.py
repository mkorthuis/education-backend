"""
Private (nonpublic) schools' enrollment by grade on October 1, from NHED's iPlatform report "NonPublic
School Enrollments by Grade" (see private_enrollment_config.yaml), into:

- school_private_enrollment: a school's students in each grade it has students in, preschool to grade 12
  and postgraduate, shaped like the public schools' school_enrollment (which skips zeros too)
- school_private_enrollment_total: its ungraded elementary and secondary students, and its total, for
  every school the report lists, even one with none

Kept apart from school_enrollment, as the private schools' restraints and seclusions are kept apart from
the public schools': sums over the public schools' tables must never take in private schools.

Each export is checked before anything is written: it must be the report's Final data, each school's
grades and ungraded students must add up to its total, and every column must add up to the State Total
row. Schools not in the school table (closed, or not on the state's list) are skipped and logged.
"""
import logging
import re
from typing import Iterable, Optional

import pandas as pd
from sqlalchemy import text
from sqlalchemy.engine import Connection

from app.etl.core import configured_years, known_school_ids, load_config, upsert_rows, whole_number, year_file

logger = logging.getLogger("app.etl")

CONFIG = "private_enrollment_config.yaml"


def read_export(df: pd.DataFrame, year: int, config: dict, path: str) -> list:
    """
    The schools' rows of one year's export, as dicts of column header -> count, with "school_id";
    checked against each school's total and the State Total row.
    """
    cells = df.fillna("").astype(str).map(str.strip)
    rows = cells.values.tolist()
    flat = [" ".join(cell for cell in row if cell) for row in rows]
    if not any(re.search(r"Type of Data:\s*Final", line) for line in flat):
        raise ValueError(f"{path}: not the report's Final data")
    if not any(re.search(rf"{year - 1}\s*-\s*{year}\b", line) for line in flat):
        raise ValueError(f"{path}: not the {year - 1}-{year} report")
    header_index = next(i for i, row in enumerate(rows) if row and row[0] == "School #")
    header = rows[header_index]
    columns = [*config["grade_columns"], config["ungraded_elementary_column"], config["ungraded_secondary_column"], config["total_column"]]
    missing = [column for column in columns if column not in header]
    if missing:
        raise ValueError(f"{path}: no {missing} column")
    position = {column: header.index(column) for column in columns}

    def counts(row):
        values = {column: whole_number(row[position[column]].replace(",", "")) for column in columns}
        if any(value is None for value in values.values()):
            raise ValueError(f"{path}: a count that isn't a whole number in {row}")
        return values

    schools, state = [], None
    for row in rows[header_index + 1:]:
        if re.fullmatch(r"\d{4,6}", row[0]):
            schools.append({"school_id": int(row[0]), **counts(row)})
        elif "State Total" in row:
            state = counts(row)
    if state is None:
        raise ValueError(f"{path}: no State Total row")
    total = config["total_column"]
    wrong = [s["school_id"] for s in schools if sum(v for c, v in s.items() if c not in ("school_id", total)) != s[total]]
    if wrong:
        raise ValueError(f"{path}: schools whose grades don't add up to their total: {wrong}")
    off = {column: (sum(s[column] for s in schools), state[column]) for column in columns
           if sum(s[column] for s in schools) != state[column]}
    if off:
        raise ValueError(f"{path}: columns that don't add up to the State Total (schools, state): {off}")
    if len({s["school_id"] for s in schools}) != len(schools):
        raise ValueError(f"{path}: a school listed twice")
    return schools


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the given years (default: every configured year)."""
    config = load_config(CONFIG)
    known_schools = known_school_ids(conn)
    grade_ids = dict(conn.execute(text("SELECT name, id FROM grades")).fetchall())
    missing = sorted(set(config["grade_columns"].values()) - set(grade_ids))
    if missing:
        raise ValueError(f"{CONFIG}: grades not in the grades table: {missing}")

    grade_rows, total_rows, unknown = [], [], set()
    loaded_years = configured_years(config["file_settings"], years)
    for year in loaded_years:
        path = year_file(config["file_settings"], year)
        schools = read_export(pd.read_excel(path, header=None, dtype=str), year, config, path)
        seen = set()
        for school in schools:
            school_id = known_schools.get(school["school_id"])
            if school_id is None:
                unknown.add((year, school["school_id"]))
                continue
            if school_id in seen:
                raise ValueError(f"{path}: two rows for school {school_id} (a renumbered school and its new id)")
            seen.add(school_id)
            grade_rows += [(school_id, grade_ids[grade], year, school[column])
                           for column, grade in config["grade_columns"].items() if school[column] > 0]
            total_rows.append((school_id, year, school[config["ungraded_elementary_column"]],
                               school[config["ungraded_secondary_column"]], school[config["total_column"]]))
        logger.info(f"Private enrollment {year}: {len(seen)} schools, {sum(s[config['total_column']] for s in schools)} students in the report")

    if unknown:
        school_ids = sorted({school_id for _, school_id in unknown})
        logger.warning(f"Skipped {len(unknown)} school-years for {len(school_ids)} schools not in the school table: {school_ids}")
    # A reloaded year loses the rows it no longer has: schools dropped, grades gone to zero
    totals_kept = {(row[0], row[1]) for row in total_rows}
    grades_kept = {(row[0], row[1], row[2]) for row in grade_rows}
    deleted = 0
    for year in loaded_years:
        stale_totals = [row[0] for row in conn.execute(text(
            "SELECT id, school_id_fk FROM school_private_enrollment_total WHERE year = :year"), {"year": year})
            if (row[1], year) not in totals_kept]
        stale_grades = [row[0] for row in conn.execute(text(
            "SELECT id, school_id_fk, grade_id_fk FROM school_private_enrollment WHERE year = :year"), {"year": year})
            if (row[1], row[2], year) not in grades_kept]
        for table, ids in (("school_private_enrollment", stale_grades), ("school_private_enrollment_total", stale_totals)):
            if ids:
                deleted += conn.execute(text(f"DELETE FROM {table} WHERE id = ANY(:ids)"), {"ids": ids}).rowcount
    counts = {
        "school_private_enrollment_total": upsert_rows(conn, "school_private_enrollment_total",
                                                       ("school_id_fk", "year", "ungraded_elementary", "ungraded_secondary", "total"),
                                                       ("school_id_fk", "year"), total_rows),
        "school_private_enrollment": upsert_rows(conn, "school_private_enrollment",
                                                 ("school_id_fk", "grade_id_fk", "year", "enrollment"),
                                                 ("school_id_fk", "grade_id_fk", "year"), grade_rows),
    }
    counts["school_private_enrollment"]["deleted"] = deleted
    return counts
