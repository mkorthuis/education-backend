"""
Private schools' Form 990 finances, in four tables:

- private_org: each organization that files (or needn't file) a private school's 990, by EIN, with
  its name, founding year and mission
- school_990_link: who files each school's 990. The school itself, an operator that runs several
  programs (one return for all of them, which can't be split by school), or no one: church schools
  needn't file, some schools have no IRS record, two file only the 990-N postcard
- private_org_990: the figures from each of the organizations' 990 and 990-EZ returns, a row per tax year
- private_org_990_revenue_line: each return's program service revenue lines as filed, sorted into
  categories (tuition, summer programs, transportation...) by the rules in the config

assets/private-990/school-990-link.csv gives each private school's case, from the 2026-11 research
(see private_990_config.yaml). `python -m app.etl fetch private-990` finds the filers' returns in the
IRS e-file indexes, reads each return's XML and saves the figures to assets/private-990/returns.json.
`load private-990` loads the four tables. Officers' names and pay, also on the 990, aren't kept.
"""
import csv
import json
import logging
import os
import re
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from typing import Iterable, Optional
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

from sqlalchemy import text
from sqlalchemy.engine import Connection

from app.etl.core import config_path, existing_ids, load_config, upsert_rows

logger = logging.getLogger("app.etl")

CONFIG = "private_990_config.yaml"
STATUSES = ("own_return", "operator_return", "postcard_only", "not_required_religious", "no_irs_record", "placeholder")
# The statuses whose filer's returns have figures
FILES_990 = ("own_return", "operator_return")
FORMS = ("990", "990EZ")
# Program service revenue categories; the config's rules sort each line into one, "other" when none match
CATEGORIES = ("tuition", "school_program", "room_and_board", "summer_auxiliary", "extended_care", "student_activities",
              "transportation", "therapy_tutoring", "human_services", "unspecified_program", "rental", "other")

# A return's figures, by the main form's element paths ("Group/Child"); the 990-EZ has fewer
FORM_FIELDS = {
    "990": {
        "total_revenue": "CYTotalRevenueAmt",
        "prior_total_revenue": "PYTotalRevenueAmt",
        "program_service_revenue": "CYProgramServiceRevenueAmt",
        "contributions": "CYContributionsGrantsAmt",
        "government_grants": "GovernmentGrantsAmt",
        "investment_income": "CYInvestmentIncomeAmt",
        "investment_gains": "NetGainOrLossInvestmentsGrp/TotalRevenueColumnAmt",
        "fundraising_event_income": "NetIncmFromFundraisingEvtGrp/TotalRevenueColumnAmt",
        "total_expenses": "CYTotalExpensesAmt",
        "prior_total_expenses": "PYTotalExpensesAmt",
        "program_expenses": "TotalFunctionalExpensesGrp/ProgramServicesAmt",
        "management_expenses": "TotalFunctionalExpensesGrp/ManagementAndGeneralAmt",
        "fundraising_expenses": "TotalFunctionalExpensesGrp/FundraisingAmt",
        "salaries_benefits": "CYSalariesCompEmpBnftPaidAmt",
        "total_assets_eoy": "TotalAssetsEOYAmt",
        "total_liabilities_eoy": "TotalLiabilitiesEOYAmt",
        "net_assets_eoy": "NetAssetsOrFundBalancesEOYAmt",
        "land_buildings_equipment_eoy": "LandBldgEquipBasisNetGrp/EOYAmt",
        "public_investments_eoy": "InvestmentsPubTradedSecGrp/EOYAmt",
        "tax_exempt_bonds_eoy": "TaxExemptBondLiabilitiesGrp/EOYAmt",
        "employees": "TotalEmployeeCnt",
        "volunteers": "TotalVolunteersCnt",
        "paid_over_100k": "IndivRcvdGreaterThan100KCnt",
    },
    "990EZ": {
        "total_revenue": "TotalRevenueAmt",
        "program_service_revenue": "ProgramServiceRevenueAmt",
        "contributions": "ContributionsGiftsGrantsEtcAmt",
        "investment_income": "InvestmentIncomeAmt",
        "total_expenses": "TotalExpensesAmt",
        "salaries_benefits": "SalariesOtherCompEmplBnftAmt",
        "total_assets_eoy": "Form990TotalAssetsGrp/EOYAmt",
        "total_liabilities_eoy": "SumOfTotalLiabilitiesGrp/EOYAmt",
        "net_assets_eoy": "NetAssetsOrFundBalancesGrp/EOYAmt",
    },
}
# Schedule D's endowment, and the shares of it that are board-designated, permanent and for a term
ENDOWMENT_FIELDS = {
    "endowment_eoy": "CYEndwmtFundGrp/EndYearBalanceAmt",
    "endowment_board_designated_share": "BoardDesignatedBalanceEOYPct",
    "endowment_permanent_share": "PrmnntEndowmentBalanceEOYPct",
    "endowment_term_share": "TermEndowmentBalanceEOYPct",
}
FIGURES = tuple(dict.fromkeys([*FORM_FIELDS["990"], *FORM_FIELDS["990EZ"], *ENDOWMENT_FIELDS]))
RETURN_COLUMNS = ("ein", "tax_period_end", "form", *FIGURES, "object_id")
LINE_COLUMNS = ("return_id", "line_no", "description", "business_code", "amount", "category")


# -------------------- the link: who files for each school --------------------

def read_link(path: str) -> list:
    """The link file's rows, checked: a known status, an EIN of nine digits, and one for every school whose filer files a 990."""
    rows = []
    with open(path, newline="") as f:
        for record in csv.DictReader(f):
            school_id, status, ein = int(record["school_id"]), record["status"], record["ein"].strip() or None
            if status not in STATUSES:
                raise ValueError(f"{path}: school {school_id} has an unknown status {status!r}")
            if ein is not None and not re.fullmatch(r"\d{9}", ein):
                raise ValueError(f"{path}: school {school_id} has an EIN that isn't nine digits: {ein!r}")
            if status in FILES_990 and ein is None:
                raise ValueError(f"{path}: school {school_id} files a 990 ({status}) but has no EIN")
            rows.append({"school_id": school_id, "status": status, "ein": ein,
                         "filer_name": record["filer_name"].strip() or None, "note": record["note"].strip() or None})
    if len({row["school_id"] for row in rows}) != len(rows):
        raise ValueError(f"{path}: a school is listed twice")
    return rows


def organizations(link: list, returns: list) -> list:
    """
    Rows of (ein, name, founded, mission): each EIN in the link, named as the link names it (one name
    an EIN), with the founding year and mission from its latest return that gives them.
    """
    names = {}
    for row in link:
        if row["ein"] is None:
            continue
        if names.setdefault(row["ein"], row["filer_name"]) != row["filer_name"]:
            raise ValueError(f"EIN {row['ein']} has two names in the link: {names[row['ein']]!r} and {row['filer_name']!r}")
    latest = {}
    for r in sorted(returns, key=lambda r: r["tax_period_end"]):
        for key in ("founded", "mission"):
            if r.get(key):
                latest.setdefault(r["ein"], {})[key] = r[key]
    return [(ein, name, latest.get(ein, {}).get("founded"), latest.get(ein, {}).get("mission")) for ein, name in sorted(names.items())]


def categorize(description: str, rules: list) -> str:
    """A program service revenue line's category: the first rule whose pattern the description matches."""
    for rule in rules:
        if re.search(rule["pattern"], description, re.I):
            return rule["category"]
    return "other"


# -------------------- fetch: the filers' returns from the IRS e-file data --------------------

def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _find(element, path: str):
    """The first element at a path of local names ("Form990TotalAssetsGrp/EOYAmt"), at any depth for its first step."""
    first, *rest = path.split("/")
    for candidate in element.iter():
        if _local(candidate.tag) != first:
            continue
        found = candidate
        for name in rest:
            found = next((child for child in found if _local(child.tag) == name), None)
            if found is None:
                break
        if found is not None:
            return found
    return None


def _text(element, path: str) -> Optional[str]:
    found = _find(element, path) if element is not None else None
    return re.sub(r"\s+", " ", found.text).strip() if found is not None and found.text and found.text.strip() else None


def _amount(element, path: str) -> Optional[int]:
    value = _text(element, path)
    return int(float(value)) if value is not None else None


def parse_return(xml: bytes, object_id: str) -> dict:
    """One return's figures, program service revenue lines, founding year and mission."""
    root = ET.fromstring(xml)
    header = _find(root, "ReturnHeader")
    form = _text(header, "ReturnTypeCd")
    if form not in FORM_FIELDS:
        raise ValueError(f"{object_id}: a {form} return")
    main = _find(root, "IRS990" if form == "990" else "IRS990EZ")
    figures = {name: _amount(main, path) for name, path in FORM_FIELDS[form].items()}
    schedule_d = _find(root, "IRS990ScheduleD")
    if schedule_d is not None:
        figures["endowment_eoy"] = _amount(schedule_d, ENDOWMENT_FIELDS["endowment_eoy"])
        for name in ("endowment_board_designated_share", "endowment_permanent_share", "endowment_term_share"):
            value = _text(schedule_d, ENDOWMENT_FIELDS[name])
            figures[name] = float(value) if value is not None else None
    lines = [{"description": _text(group, "Desc"), "business_code": _text(group, "BusinessCd"),
              "amount": _amount(group, "TotalRevenueColumnAmt")}
             for group in main.iter() if _local(group.tag) == "ProgramServiceRevenueGrp"]
    return {
        "ein": _text(_find(header, "Filer"), "EIN"),
        "tax_period_end": _text(header, "TaxPeriodEndDt"),
        "form": form,
        "name_as_filed": _text(_find(header, "Filer"), "BusinessNameLine1Txt"),
        **{name: figures.get(name) for name in FIGURES},
        "lines": [line for line in lines if line["description"] and line["amount"] is not None],
        "founded": _amount(main, "FormationYr"),
        "mission": _text(main, "MissionDesc" if form == "990" else "PrimaryExemptPurposeTxt"),
        "object_id": object_id,
    }


def _open(url: str, attempts: int = 3):
    for attempt in range(1, attempts + 1):
        try:
            return urlopen(url, timeout=300)
        except HTTPError:
            raise
        except URLError as e:
            if attempt == attempts:
                raise
            logger.warning(f"{url}: {e}; trying again")


def find_returns(config: dict, eins: set) -> dict:
    """Each filer's 990 and 990-EZ returns in the configured index years: the last filed for each tax period (an amendment replaces its original)."""
    found = {}
    for year in config["index_years"]:
        with _open(config["index_url"].format(year=year)) as response:
            for row in csv.DictReader(line.decode("utf-8", "replace") for line in response):
                ein = (row.get("EIN") or "").strip().zfill(9)
                if ein in eins and row.get("RETURN_TYPE") in FORMS:
                    key = (ein, row["TAX_PERIOD"])
                    if key not in found or row["OBJECT_ID"] > found[key]:
                        found[key] = row["OBJECT_ID"]
        logger.info(f"index {year}: {len(found)} returns so far")
    return found


def save_returns(config: dict, object_ids: Iterable[str], eins: set) -> str:
    """Read each return's XML and save the figures to the config's returns file."""
    def read(object_id):
        try:
            with _open(config["xml_url"].format(object_id=object_id)) as response:
                return parse_return(response.read(), object_id), None
        except HTTPError as e:
            return None, f"{object_id}: HTTP {e.code}"

    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(read, sorted(object_ids)))
    returns = sorted((r for r, _ in results if r), key=lambda r: (r["ein"], r["tax_period_end"]))
    missing = [error for _, error in results if error]
    without = sorted(eins - {r["ein"] for r in returns})
    saved = {"fetched": date.today().isoformat(), "index_years": config["index_years"],
             "returns": returns, "not_in_the_e_file_data": missing, "filers_without_returns": without}
    path = os.path.join(config_path(config["directory"]), config["returns_file"])
    with open(path, "w") as f:
        json.dump(saved, f, indent=1)
    logger.info(f"{len(returns)} returns for {len({r['ein'] for r in returns})} of {len(eins)} filers; "
                f"{len(missing)} not in the e-file data; filers without returns: {without}")
    return path


def fetch() -> str:
    """Find every return of the link file's filers and save their figures to assets/private-990/returns.json."""
    config = load_config(CONFIG)
    link = read_link(os.path.join(config_path(config["directory"]), config["link_file"]))
    eins = {row["ein"] for row in link if row["status"] in FILES_990}
    return save_returns(config, find_returns(config, eins).values(), eins)


# -------------------- load --------------------

def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """
    Load the organizations, the link, and the returns with their revenue lines (default: every return;
    given years, those whose fiscal year ends in them). Schools not in the school table are skipped and logged.
    """
    config = load_config(CONFIG)
    rules = config["revenue_line_categories"]
    unknown_categories = sorted({rule["category"] for rule in rules} - set(CATEGORIES))
    if unknown_categories:
        raise ValueError(f"{CONFIG}: unknown revenue line categories {unknown_categories}")
    directory = config_path(config["directory"])
    link = read_link(os.path.join(directory, config["link_file"]))
    path = os.path.join(directory, config["returns_file"])
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} not found; run `python -m app.etl fetch private-990`")
    with open(path) as f:
        all_returns = json.load(f)["returns"]
    wanted = set(years) if years else None
    returns = [r for r in all_returns if wanted is None or int(r["tax_period_end"][:4]) in wanted]

    counts = {"private_org": upsert_rows(conn, "private_org", ("ein", "name", "founded", "mission"), ("ein",),
                                         organizations(link, all_returns))}
    known = existing_ids(conn, "school")
    unknown = sorted(row["school_id"] for row in link if row["school_id"] not in known)
    if unknown:
        logger.warning(f"Skipped {len(unknown)} schools not in the school table: {unknown}")
    counts["school_990_link"] = upsert_rows(
        conn, "school_990_link", ("school_id_fk", "status", "ein", "note"), ("school_id_fk",),
        [(row["school_id"], row["status"], row["ein"], row["note"]) for row in link if row["school_id"] in known])
    counts["private_org_990"] = upsert_rows(conn, "private_org_990", RETURN_COLUMNS, ("ein", "tax_period_end"),
                                            [tuple(r[column] for column in RETURN_COLUMNS) for r in returns])

    # Each return's lines, under the id its row has now; a reloaded return's extra old lines are removed
    ids = {(row[1], str(row[2])): row[0] for row in conn.execute(text("SELECT id, ein, tax_period_end FROM private_org_990"))}
    lines, uncategorized = [], set()
    for r in returns:
        return_id = ids[(r["ein"], r["tax_period_end"])]
        for line_no, line in enumerate(r["lines"], 1):
            category = categorize(line["description"], rules)
            if category == "other":
                uncategorized.add(line["description"])
            lines.append((return_id, line_no, line["description"], line["business_code"], line["amount"], category))
    loaded = [ids[(r["ein"], r["tax_period_end"])] for r in returns]
    kept = {(line[0], line[1]) for line in lines}
    stale = [row[0] for row in conn.execute(text(
        "SELECT id, return_id, line_no FROM private_org_990_revenue_line WHERE return_id = ANY(:ids)"), {"ids": loaded})
        if (row[1], row[2]) not in kept]
    if stale:
        conn.execute(text("DELETE FROM private_org_990_revenue_line WHERE id = ANY(:ids)"), {"ids": stale})
    counts["private_org_990_revenue_line"] = upsert_rows(conn, "private_org_990_revenue_line", LINE_COLUMNS,
                                                         ("return_id", "line_no"), lines)
    counts["private_org_990_revenue_line"]["deleted"] = len(stale)
    if uncategorized:
        logger.info(f"Revenue lines no rule matched (category other): {sorted(uncategorized)}")
    return counts
