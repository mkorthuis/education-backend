"""
Ballot Question 2 (HB 1300, 2026 chapter 324) by school district, into district_question_two: the
yes and no votes, the yes share, and whether the district adopted the school tax cap (see
question_two_config.yaml; the SAU central-office cap is decided across the SAU's towns).

Each file's rows are checked before anything is written: every district must be in the district
table, the share must agree with the votes, and a district passes only with 60% yes or more.
"""
import logging
from typing import Iterable, List, Optional

import pandas as pd
from sqlalchemy.engine import Connection

from app.etl.core import config_path, load_config, lookup_ids, upsert_rows

logger = logging.getLogger("app.etl")

CONFIG = "question_two_config.yaml"
TABLE = "district_question_two"
COLUMNS = ("district", "yes_votes", "no_votes", "yes_percent", "result")
# The source rounds the share to a tenth of a percent (a few rows to a hundredth)
PERCENT_TOLERANCE = 0.06


def parse_file(df: pd.DataFrame, threshold: float, name: str) -> List[dict]:
    """One dict per district, checked against itself: district, yes, no, percent, passed."""
    missing = [c for c in COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"{name}: columns missing: {missing}")
    rows, seen = [], set()
    for number, row in enumerate(df.itertuples(index=False), start=2):
        district = str(row.district).strip()
        yes, no, percent = int(row.yes_votes), int(row.no_votes), float(row.yes_percent)
        result = str(row.result).strip().upper()
        if district in seen:
            raise ValueError(f"{name}, line {number}: {district} is listed twice")
        seen.add(district)
        if yes < 0 or no < 0 or yes + no == 0:
            raise ValueError(f"{name}, line {number}: {district} has no votes")
        share = 100 * yes / (yes + no)
        if abs(share - percent) > PERCENT_TOLERANCE:
            raise ValueError(f"{name}, line {number}: {district}'s {percent}% doesn't match {yes} yes and {no} no ({share:.2f}%)")
        if result not in ("PASS", "FAIL") or (result == "PASS") != (share >= threshold):
            raise ValueError(f"{name}, line {number}: {district} is marked {result} with {share:.2f}% yes")
        rows.append({"district": district, "yes": yes, "no": no, "percent": round(percent, 2), "passed": result == "PASS"})
    return rows


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the given election years (default: every configured one) into district_question_two."""
    config = load_config(CONFIG)
    elections = config["elections"]
    years = sorted(elections) if years is None else sorted(years)
    unknown = [y for y in years if y not in elections]
    if unknown:
        raise ValueError(f"Question 2 has no configured election for {unknown}; configured: {sorted(elections)}")

    districts = lookup_ids(conn, "district")
    counts = {}
    for year in years:
        election = elections[year]
        df = pd.read_csv(config_path(f"{config['directory']}/{election['file']}"), dtype={"district": str})
        rows = parse_file(df, config["threshold_percent"], election["file"])
        unmatched = sorted(r["district"] for r in rows if r["district"] not in districts)
        if unmatched:
            raise ValueError(f"{election['file']}: districts not in the district table: {unmatched}")
        counts[year] = upsert_rows(
            conn, TABLE, ("district_id_fk", "year", "yes_votes", "no_votes", "yes_percentage", "passed", "is_official"),
            ("district_id_fk", "year"),
            [(districts[r["district"]], year, r["yes"], r["no"], r["percent"], r["passed"], bool(election["official"])) for r in rows])
        logger.info(f"Question 2, {year}: {sum(r['passed'] for r in rows)} of {len(rows)} districts adopted the school tax cap")
    return {TABLE: counts}
