"""
Where Education Freedom Account money and students go, by provider, from the Children's Scholarship
Fund's reports (see education_freedom_account_provider_config.yaml):

- education_freedom_account_category: the allowable categories, and the combinations a purchase charged to several was published under
- education_freedom_account_provider: each provider, by its name key (its name in capitals, letters and digits only, since the
  scanned reports lose and gain spaces), with the private school it is when it's one on the state's list.
  CSF lists some individuals by initials ("CL Tutor"), so one name key can stand for several people
- education_freedom_account_expenditure: each provider line of each year's Expenditure Report: year, category, provider, amount
- education_freedom_account_served: each line of the list of students served by providers with 10 or more, by calendar year

Every year's lines must add up to each category's printed total and to the report's grand total before
anything is written.
"""
import csv
import logging
import os
import re
from collections import defaultdict
from decimal import Decimal
from typing import Iterable, Optional

from sqlalchemy import text
from sqlalchemy.engine import Connection

from app.etl.core import config_path, existing_ids, load_config, upsert_rows

logger = logging.getLogger("app.etl")

CONFIG = "education_freedom_account_provider_config.yaml"


def name_key(name: str) -> str:
    return re.sub(r"[^A-Z0-9]", "", name.upper())


def classify(published: str, categories: list) -> tuple:
    """The codes of the allowable categories a category as published names, in the config's order."""
    spaceless = re.sub(r"\s+", "", published).lower()
    codes = tuple(c["code"] for c in categories if re.search(c["pattern"], spaceless, re.I))
    if not codes:
        raise ValueError(f"No allowable category in {published!r}")
    return codes


def read_year(path: str, year: int, grand_total: Decimal) -> list:
    """A year's lines, checked: each category's lines add up to its printed total, and the totals to the grand total."""
    with open(path, newline="") as f:
        lines = [dict(row, year=int(row["year"]), line_no=int(row["line_no"]), amount=Decimal(row["amount"]),
                      category_total=Decimal(row["category_total"])) for row in csv.DictReader(f)]
    if any(line["year"] != year for line in lines):
        raise ValueError(f"{path}: a line for another year")
    if [line["line_no"] for line in lines] != list(range(1, len(lines) + 1)):
        raise ValueError(f"{path}: line numbers aren't 1 to {len(lines)}")
    # A category is a run of lines under the same name and total (one name can come twice in a year)
    runs = []
    for line in lines:
        if not runs or (runs[-1][0], runs[-1][1]) != (line["category"], line["category_total"]):
            runs.append([line["category"], line["category_total"], Decimal(0)])
        runs[-1][2] += line["amount"]
    wrong = [(name[:60], total, sum_) for name, total, sum_ in runs if sum_ != total]
    if wrong:
        raise ValueError(f"{path}: categories whose lines don't add up to their totals: {wrong}")
    if sum(total for _, total, _ in runs) != grand_total:
        raise ValueError(f"{path}: categories add up to {sum(total for _, total, _ in runs)}, not the grand total {grand_total}")
    return lines


def read_served(path: str, year: int) -> list:
    with open(path, newline="") as f:
        return [{"line_no": line_no, "provider": row["provider"], "students": int(row["students"])}
                for line_no, row in enumerate((row for row in csv.DictReader(f) if int(row["calendar_year"]) == year), 1)]


def read_matches(path: str) -> dict:
    """Name key -> school id, for the providers that are private schools on the state's list."""
    with open(path, newline="") as f:
        matches = {row["name_key"]: int(row["school_id"]) for row in csv.DictReader(f)}
    if any(key != name_key(key) for key in matches):
        raise ValueError(f"{path}: a name key that isn't capitals, letters and digits")
    return matches


def display_name(names: list) -> str:
    """A provider's name, from its latest listing; one not all in capitals (year 1's and the served list's) when there is one."""
    mixed = [name for name in names if name != name.upper()]
    return re.sub(r"\s+", " ", (mixed or names)[-1]).strip()


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the given years' expenditures (default: every configured year), the served lists, categories and providers."""
    config = load_config(CONFIG)
    directory = config_path(config["directory"])
    wanted = sorted(years) if years else list(range(config["year_start"], config["year_end"] + 1))
    lines = []
    for year in wanted:
        path = os.path.join(directory, config["expenditure_input"].replace("****", str(year)))
        lines += read_year(path, year, Decimal(str(config["grand_totals"][year])))
    served = {year: read_served(os.path.join(directory, name), year) for year, name in config["served_files"].items()}
    matches = read_matches(os.path.join(directory, config["school_match_file"]))

    # Categories, combined ones named after their parts
    names = {c["code"]: c["name"] for c in config["categories"]}
    codes = {line["category"]: classify(line["category"], config["categories"]) for line in lines}
    category_rows = sorted({("+".join(c), " & ".join(names[part] for part in c), len(c) > 1) for c in codes.values()})
    counts = {"education_freedom_account_category": upsert_rows(conn, "education_freedom_account_category", ("code", "name", "combined"), ("code",), category_rows)}

    # Providers, by name key, with every name they were listed under in order
    listed = defaultdict(list)
    for line in sorted(lines, key=lambda line: (line["year"], line["line_no"])):
        listed[name_key(line["provider"])].append(line["provider"])
    for year in sorted(served):
        for row in served[year]:
            listed[name_key(row["provider"])].append(row["provider"])
    schools = existing_ids(conn, "school")
    unknown = sorted({school_id for school_id in matches.values() if school_id not in schools})
    if unknown:
        raise ValueError(f"{config['school_match_file']}: school ids not in the school table: {unknown}")
    unmatched = sorted(key for key in matches if key not in listed)
    if unmatched:
        logger.warning(f"{config['school_match_file']}: name keys no report lists: {unmatched}")
    provider_rows = [(key, display_name(names_), matches.get(key)) for key, names_ in sorted(listed.items())]
    counts["education_freedom_account_provider"] = upsert_rows(conn, "education_freedom_account_provider", ("name_key", "name", "school_id_fk"), ("name_key",), provider_rows)

    providers = dict(conn.execute(text("SELECT name_key, id FROM education_freedom_account_provider")).fetchall())
    categories = dict(conn.execute(text("SELECT code, id FROM education_freedom_account_category")).fetchall())
    expenditure_rows = [(line["year"], line["line_no"], categories["+".join(codes[line["category"]])],
                         providers[name_key(line["provider"])], line["provider"], line["amount"]) for line in lines]
    # A year reloaded with fewer lines loses the extra old ones
    deleted = 0
    for year in wanted:
        last = max((line["line_no"] for line in lines if line["year"] == year), default=0)
        deleted += conn.execute(text("DELETE FROM education_freedom_account_expenditure WHERE year = :year AND line_no > :last"),
                                {"year": year, "last": last}).rowcount
    counts["education_freedom_account_expenditure"] = upsert_rows(conn, "education_freedom_account_expenditure", ("year", "line_no", "category_id", "provider_id",
                                            "provider_as_published", "amount"), ("year", "line_no"), expenditure_rows)
    counts["education_freedom_account_expenditure"]["deleted"] = deleted
    served_rows = [(year, row["line_no"], providers[name_key(row["provider"])], row["provider"], row["students"])
                   for year in sorted(served) for row in served[year]]
    served_deleted = sum(conn.execute(text("DELETE FROM education_freedom_account_served WHERE calendar_year = :year AND line_no > :last"),
                                      {"year": year, "last": len(rows)}).rowcount for year, rows in served.items())
    counts["education_freedom_account_served"] = upsert_rows(conn, "education_freedom_account_served", ("calendar_year", "line_no", "provider_id", "provider_as_published", "students"),
                                       ("calendar_year", "line_no"), served_rows)
    counts["education_freedom_account_served"]["deleted"] = served_deleted
    return counts
