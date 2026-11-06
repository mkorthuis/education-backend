"""
Statewide October 1 enrollment by type of school and grade, from the state's "State Totals Ten Years
Public and Private Fall Enrollments" workbooks: public district schools, public academies and joint
maintenance agreement schools, public charter schools, interstate schools and nonpublic schools.
"""
import logging
from typing import Iterable, Optional

import pandas as pd
from sqlalchemy import text
from sqlalchemy.engine import Connection

from app.etl.core import config_path, configured_years, load_config, lookup_ids, upsert_rows, whole_number

logger = logging.getLogger("app.etl")

CONFIG = "state_enrollment_type_config.yaml"
TYPE_TABLE = "enrollment_type"
TABLE = "state_enrollment_type"
COLUMNS = ("year", "enrollment_type_id_fk", "grade_id_fk", "enrollment")
KEY = ("year", "enrollment_type_id_fk", "grade_id_fk")


def school_year_end(label: str) -> Optional[int]:
    """'17 - 18' as 2018 (the year the school year ends), or None for anything else."""
    parts = [part.strip() for part in str(label).split("-")]
    if len(parts) != 2 or not all(part.isdigit() and len(part) == 2 for part in parts):
        return None
    return 2000 + int(parts[1])


def parse_file(df: pd.DataFrame, config: dict) -> dict:
    """
    {(year, enrollment type, grade): students} from one workbook.

    A section starts with its title alone in the first column, followed by a row of school years
    ("17 - 18") and a row per grade. Each value is read from the column under its year, since a
    section can have fewer years than the others (nonpublic counts come in later). Sections not in
    the config (the total rows) are skipped, as are the sections' own total rows.
    """
    sections, grades = config["sections"], config["grades"]
    counts, section, year_columns = {}, None, {}
    for _, row in df.iterrows():
        first = str(row.iloc[0]).strip() if pd.notna(row.iloc[0]) else ""
        rest = [value for value in row.iloc[1:].tolist() if pd.notna(value)]
        if first and not rest:
            # A section title (or a heading, footnote or blank-valued total, which match no section)
            section = next((name for prefix, name in sections.items() if first.startswith(prefix)), None)
            year_columns = {}
            continue
        if section is None:
            continue
        years = {position: school_year_end(value) for position, value in enumerate(row.tolist()) if pd.notna(value)}
        if any(years.values()) and not first:
            year_columns = {position: year for position, year in years.items() if year}
            continue
        grade = grades.get(first)
        if grade is None:
            continue
        for position, year in year_columns.items():
            students = whole_number(row.iloc[position])
            if students is not None:
                key = (year, section, grade)
                counts[key] = counts.get(key, 0) + students
    return counts


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the given years (default: every configured year) into state_enrollment_type."""
    config = load_config(CONFIG)
    years = set(configured_years(config["file_settings"], years))

    counts = {}
    for file in config["file_settings"]["files"]:
        first, last = file["year_range"]
        if not years & set(range(first, last + 1)):
            continue
        file_counts = parse_file(pd.read_excel(config_path(file["path"]), header=None), config)
        # Each file supplies only its own years; later files win where they overlap
        counts.update({key: value for key, value in file_counts.items() if first <= key[0] <= last and key[0] in years})

    # New types are added in config order, so a fresh build numbers them the same way
    existing = lookup_ids(conn, TYPE_TABLE)
    for name in config["sections"].values():
        if name not in existing:
            conn.execute(text(f"INSERT INTO {TYPE_TABLE} (name) VALUES (:name)"), {"name": name})
    type_ids = lookup_ids(conn, TYPE_TABLE)
    grade_ids = lookup_ids(conn, "grades")
    missing = sorted({grade for (_, _, grade) in counts if grade not in grade_ids})
    if missing:
        raise ValueError(f"Grades not in the grades table: {missing}")

    rows = [(year, type_ids[section], grade_ids[grade], students)
            for (year, section, grade), students in sorted(counts.items(), key=lambda item: (item[0][0], type_ids[item[0][1]], grade_ids[item[0][2]]))]
    found_years = sorted({row[0] for row in rows})
    if set(found_years) != years:
        logger.warning(f"State enrollment by type: no counts for years {sorted(years - set(found_years))}")
    return {TABLE: upsert_rows(conn, TABLE, COLUMNS, KEY, rows)}
