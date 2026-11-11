"""
Ballot Question 2 (HB 1300, 2026 chapter 324) results, by school district, SAU and town (see
question_two_config.yaml):

- district_question_two: the vote in each school district's towns, which decides its school tax cap
- sau_question_two: the vote across each SAU's towns, which decides its 6% central-office spending cap
- town_question_two: each town's own vote, which decides neither on its own

Each file's rows are checked before anything is written: every place must be in its table, the share
must agree with the votes, and a district or SAU passes only with 60% yes or more.
"""
import logging
from typing import Iterable, List, Optional

import pandas as pd
from sqlalchemy.engine import Connection

from app.etl.core import config_path, load_config, lookup_ids, upsert_rows

logger = logging.getLogger("app.etl")

CONFIG = "question_two_config.yaml"
# Each level: its file's key in the config, its table, the file's column naming the place, the
# table's id column, and whether the vote decides a cap (and so has a result)
LEVELS = {
    "districts": ("district_question_two", "district", "district_id_fk", True),
    "saus": ("sau_question_two", "sau", "sau_id_fk", True),
    "towns": ("town_question_two", "town", "town_id_fk", False),
}
# The source rounds the share to a tenth of a percent (a few rows to a hundredth)
PERCENT_TOLERANCE = 0.06


def parse_file(df: pd.DataFrame, threshold: float, name: str, key: str = "district", decides: bool = True) -> List[dict]:
    """One dict per place, checked against itself: the place, yes, no, percent, note, and for a
    district or SAU whether it passed and the towns whose votes make up its total."""
    required = [key, "yes_votes", "no_votes", "yes_percent", *(["result"] if decides else [])]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"{name}: columns missing: {missing}")
    rows, seen = [], set()
    for number, row in enumerate(df.to_dict("records"), start=2):
        place = str(row[key]).strip()
        yes, no, percent = int(row["yes_votes"]), int(row["no_votes"]), float(row["yes_percent"])
        if place in seen:
            raise ValueError(f"{name}, line {number}: {place} is listed twice")
        seen.add(place)
        if yes < 0 or no < 0 or yes + no == 0:
            raise ValueError(f"{name}, line {number}: {place} has no votes")
        share = 100 * yes / (yes + no)
        if abs(share - percent) > PERCENT_TOLERANCE:
            raise ValueError(f"{name}, line {number}: {place}'s {percent}% doesn't match {yes} yes and {no} no ({share:.2f}%)")
        note = row.get("note")
        parsed = {key: place, "yes": yes, "no": no, "percent": round(percent, 2),
                  "note": None if pd.isna(note) or not str(note).strip() else str(note).strip()}
        if decides:
            result = str(row["result"]).strip().upper()
            if result not in ("PASS", "FAIL") or (result == "PASS") != (share >= threshold):
                raise ValueError(f"{name}, line {number}: {place} is marked {result} with {share:.2f}% yes")
            parsed["passed"] = result == "PASS"
            towns = row.get("towns")
            parsed["towns"] = None if pd.isna(towns) or not str(towns).strip() else str(towns).strip()
        rows.append(parsed)
    return rows


def _ids(conn: Connection, key: str) -> dict:
    """The file's names for a level's places (an SAU by its number, which is its id) -> ids."""
    if key == "sau":
        return {str(sau_id): sau_id for sau_id in lookup_ids(conn, "sau", "id")}
    return lookup_ids(conn, key)


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the given election years (default: every configured one) at every level."""
    config = load_config(CONFIG)
    elections = config["elections"]
    years = sorted(elections) if years is None else sorted(years)
    unknown = [y for y in years if y not in elections]
    if unknown:
        raise ValueError(f"Question 2 has no configured election for {unknown}; configured: {sorted(elections)}")

    counts = {table: {} for table, _, _, _ in LEVELS.values()}
    for year in years:
        election = elections[year]
        summary = []
        for level, (table, key, id_column, decides) in LEVELS.items():
            file = election[level]
            df = pd.read_csv(config_path(f"{config['directory']}/{file}"), dtype={key: str})
            rows = parse_file(df, config["threshold_percent"], file, key, decides)
            ids = _ids(conn, key)
            unmatched = sorted(r[key] for r in rows if r[key] not in ids)
            if unmatched:
                raise ValueError(f"{file}: places not in the {key} table: {unmatched}")
            columns = (id_column, "year", "yes_votes", "no_votes", "yes_percentage", *(["passed", "towns"] if decides else []), "is_official", "note")
            counts[table][year] = upsert_rows(conn, table, columns, (id_column, "year"), [
                (ids[r[key]], year, r["yes"], r["no"], r["percent"], *([r["passed"], r["towns"]] if decides else []),
                 bool(election["official"]), r["note"])
                for r in rows
            ])
            summary.append(f"{sum(r['passed'] for r in rows)} of {len(rows)} {level} passed" if decides else f"{len(rows)} {level}")
        logger.info(f"Question 2, {year}: {'; '.join(summary)}")
    return counts
