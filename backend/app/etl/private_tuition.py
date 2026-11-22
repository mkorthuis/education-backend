"""
Private schools' tuition, as each school publishes it on its own website (see private_tuition_config.yaml),
into:

- school_tuition_source: a school's school year (by its end): whether it publishes its tuition, the page
  the figures are on and the day it was read, and who gets financial aid, as the school words it ("85% of
  students", "Nearly 35% of families", or "74%" where it doesn't say of whom)
- school_tuition: its rates, one per grade band and kind of rate (standard, day, boarding, parishioner...),
  each with its annual tuition and the fees every student pays each year (empty where the school names a
  required fee but not its amount; 0 where it charges none)

Every rate needs its school year's source row, a published one; every grade must be one of the grades
table's; a school without published tuition has no rates.
"""
import csv
import logging
import os
from datetime import date
from decimal import Decimal
from typing import Iterable, Optional

from sqlalchemy import text
from sqlalchemy.engine import Connection

from app.etl.core import config_path, existing_ids, load_config, upsert_rows

logger = logging.getLogger("app.etl")

CONFIG = "private_tuition_config.yaml"
STATUSES = ("published", "not_published", "site_unavailable")
RATE_TYPES = ("standard", "day", "boarding", "parishioner", "non_parishioner", "international", "half_day", "full_day", "other")
SOURCE_COLUMNS = ("school_id_fk", "year", "status", "source_url", "retrieved_on", "with_aid", "note")
RATE_COLUMNS = ("school_id_fk", "year", "rate_no", "band", "lowest_grade_id_fk", "highest_grade_id_fk", "rate_type",
                "rate_label", "tuition", "required_fee", "fee_note", "rate_note")


def blank(value: str) -> Optional[str]:
    value = (value or "").strip()
    return value or None


def read_sources(path: str) -> list:
    rows = []
    with open(path, newline="") as f:
        for record in csv.DictReader(f):
            row = {"school_id_fk": int(record["school_id"]), "year": int(record["year"]), "status": record["status"].strip(),
                   "source_url": blank(record["source_url"]), "retrieved_on": date.fromisoformat(record["retrieved_on"].strip()),
                   "with_aid": blank(record["with_aid"]), "note": blank(record["note"])}
            if row["status"] not in STATUSES:
                raise ValueError(f"{path}: school {row['school_id_fk']} has an unknown status {row['status']!r}")
            if row["status"] == "published" and not row["source_url"]:
                raise ValueError(f"{path}: school {row['school_id_fk']} publishes its tuition but has no source page")
            rows.append(row)
    if len({(row["school_id_fk"], row["year"]) for row in rows}) != len(rows):
        raise ValueError(f"{path}: a school year listed twice")
    return rows


def read_rates(path: str, sources: list, grade_ids: dict) -> list:
    published = {(row["school_id_fk"], row["year"]) for row in sources if row["status"] == "published"}
    rows = []
    with open(path, newline="") as f:
        for record in csv.DictReader(f):
            key = (int(record["school_id"]), int(record["year"]))
            if key not in published:
                raise ValueError(f"{path}: rates for school {key[0]}'s {key[1]} with no published source row")
            grades = [record["lowest_grade"].strip(), record["highest_grade"].strip()]
            unknown = [grade for grade in grades if grade not in grade_ids]
            if unknown:
                raise ValueError(f"{path}: school {key[0]}: grades not in the grades table: {unknown}")
            if grade_ids[grades[0]] > grade_ids[grades[1]]:
                raise ValueError(f"{path}: school {key[0]}: {grades[0]} is above {grades[1]}")
            rate_type = record["rate_type"].strip()
            if rate_type not in RATE_TYPES:
                raise ValueError(f"{path}: school {key[0]} has an unknown rate type {rate_type!r}")
            tuition, fee = Decimal(record["tuition"]), Decimal(record["required_fee"]) if blank(record["required_fee"]) else None
            if tuition <= 0 or (fee is not None and fee < 0):
                raise ValueError(f"{path}: school {key[0]} has a tuition of {tuition} or a fee of {fee}")
            rows.append({"school_id_fk": key[0], "year": key[1], "rate_no": int(record["rate_no"]), "band": record["band"].strip(),
                         "lowest_grade_id_fk": grade_ids[grades[0]], "highest_grade_id_fk": grade_ids[grades[1]],
                         "rate_type": rate_type, "rate_label": blank(record["rate_label"]), "tuition": tuition,
                         "required_fee": fee, "fee_note": blank(record["fee_note"]), "rate_note": blank(record["rate_note"])})
    if len({(row["school_id_fk"], row["year"], row["rate_no"]) for row in rows}) != len(rows):
        raise ValueError(f"{path}: a rate number used twice in a school year")
    missing = published - {(row["school_id_fk"], row["year"]) for row in rows}
    if missing:
        raise ValueError(f"{path}: published school years with no rates: {sorted(missing)}")
    return rows


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the sources and rates (default: every year in the files; given years, those school years)."""
    config = load_config(CONFIG)
    directory = config_path(config["directory"])
    grade_ids = dict(conn.execute(text("SELECT name, id FROM grades")).fetchall())
    sources = read_sources(os.path.join(directory, config["sources_file"]))
    rates = read_rates(os.path.join(directory, config["rates_file"]), sources, grade_ids)
    if years:
        wanted = set(years)
        sources = [row for row in sources if row["year"] in wanted]
        rates = [row for row in rates if row["year"] in wanted]
    unknown = sorted({row["school_id_fk"] for row in sources} - existing_ids(conn, "school"))
    if unknown:
        raise ValueError(f"{config['sources_file']}: school ids not in the school table: {unknown}")

    # A school year reloaded loses the rates it no longer has
    kept = {(row["school_id_fk"], row["year"], row["rate_no"]) for row in rates}
    loaded = {(row["school_id_fk"], row["year"]) for row in sources}
    stale = [row[0] for row in conn.execute(text("SELECT id, school_id_fk, year, rate_no FROM school_tuition"))
             if (row[1], row[2]) in loaded and (row[1], row[2], row[3]) not in kept]
    if stale:
        conn.execute(text("DELETE FROM school_tuition WHERE id = ANY(:ids)"), {"ids": stale})
    counts = {
        "school_tuition_source": upsert_rows(conn, "school_tuition_source", SOURCE_COLUMNS, ("school_id_fk", "year"),
                                             [tuple(row[c] for c in SOURCE_COLUMNS) for row in sources]),
        "school_tuition": upsert_rows(conn, "school_tuition", RATE_COLUMNS, ("school_id_fk", "year", "rate_no"),
                                      [tuple(row[c] for c in RATE_COLUMNS) for row in rates]),
    }
    counts["school_tuition"]["deleted"] = len(stale)
    return counts
