"""
Licensed child care programs, from NH DHHS's Child Care Search (see child_care_config.yaml):

- child_care_program_type, child_care_quality_rating, child_care_region, county,
  child_care_license_status, child_care_availability: the config's fixed lists
- child_care_feature_category: the lists programs have, from the config
- child_care_review_type, child_care_feature: the licensing visits' types and the values of the
  programs' lists, added as they appear
- child_care_program: one row per program with its latest details (license, ages, contact, town);
  is_current marks the programs in the latest download
- child_care_program_snapshot: each download's license status, capacity, availability and vacancies for
  each program, for trends
- child_care_program_hours, child_care_program_rate: the hours and rates on each program's latest page
- child_care_program_feature_xref: each program's license types and its latest page's lists
- child_care_inspection: the licensing visits on its pages (each page shows three years; every saved
  download's visits are kept)

`fetch` saves the search's two statewide lists, the provider download and its unfiltered results, then
each program's own page, trimmed; `load` reads every saved download in the config.
"""
import gzip
import html
import json
import logging
import os
import re
import time
from datetime import date, datetime, timezone
from decimal import Decimal
from typing import Iterable, List, Optional
from urllib.error import URLError
from urllib.parse import urljoin
from urllib.request import Request, urlopen

from sqlalchemy import text
from sqlalchemy.engine import Connection

from app.etl.core import config_path, load_config, lookup_ids, replace_rows, upsert_rows, whole_number
from app.etl.location import TownMatcher

logger = logging.getLogger("app.etl")

CONFIG = "child_care_config.yaml"
PROVIDERS_METHOD = "fetchProviderList"
SEARCH_METHOD = "retrieveAccountRecords"
# The search's arguments for a search with no filters, in the order the page's script sends them
SEARCH_ARGUMENTS = [
    "", "", "",          # program name, zip, city
    "", "", "", "",      # type of care, region, language, (unused)
    "", "", "",          # latitude, longitude, radius in miles
    "", "", "",          # age group, quality rating, street address
    False, False,        # reopened programs only, residential programs only
    "", "",              # Head Start, Early Head Start
    "", "", "", "", "",  # financial assistance, transportation, schedule options, meals, environment
    False,               # accepts NH Child Care Scholarship
    False, False, False, False,  # infant, toddler, preschool, school-age openings
    False, False,        # accredited, Granite Steps for Quality
]

AGE_GROUPS = ("Infant", "Toddler", "Preschool", "School Age")
FLAG_COLUMNS = {"Infant": "infant", "Toddler": "toddler", "Preschool": "preschool", "School Age": "school_age"}
# The age groups each of a license's program types covers
LICENSE_AGE_GROUPS = {
    "Infant/Toddler Program": ("Infant", "Toddler"),
    "Preschool Program": ("Preschool",),
    "School Age Program": ("School Age",),
}
LICENSE_TYPE = "license_type"  # the feature category of a license's program types
# Each age group's months, by the portal's definitions, for a program known only by its age range.
# School age means attending full-day school, which a range can't tell, so it's a range reaching 6.
AGE_GROUP_MONTHS = {"Infant": (0, 13), "Toddler": (13, 36), "Preschool": (36, 60), "School Age": (72, None)}

# The config's fixed lists, by the table each fills
LISTS = {
    "quality_ratings": "child_care_quality_rating",
    "regions": "child_care_region",
    "counties": "county",
    "license_statuses": "child_care_license_status",
    "availabilities": "child_care_availability",
}
# The provider list's Child Care Scholarship enrollment status
SCHOLARSHIP_STATUSES = {"Active": True, "Inactive": False}

# A program page's sections, by their headings' ids, in order
PAGE_SECTIONS = ("ProgramInformation", "Schedules", "InspectionMonitoring", "AgesServed", "CCRR", "QRISRating", "OtherInformation")
DAYS = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 7}
RATE_PERIODS = {"Hourly": "hourly", "Daily": "daily", "Weekly": "weekly", "Monthly": "monthly"}
EMAIL_HIDDEN = "The provider has chosen not to display the email address."

PROGRAM_COLUMNS = (
    "source_id", "provider_number", "name", "program_type_id_fk", "license_issue_date", "license_expiration_date",
    "min_age_months", "max_age_months", "infant", "toddler", "preschool", "school_age", "age_groups_source",
    "head_start", "early_head_start", "accepts_scholarship", "preventive_protective_care", "quality_rating_id_fk",
    "gsq_step", "issued_to", "main_contact", "phone", "email", "email_hidden", "street", "city", "zip", "town_id_fk",
    "county_id_fk", "region_id_fk", "mailing_street", "mailing_city", "mailing_zip", "latitude", "longitude",
    "details_updated", "is_current",
)
# A program's page's columns, blank when no saved download has its page
PAGE_COLUMNS = ("head_start", "early_head_start", "main_contact", "email_hidden", "details_updated")
SNAPSHOT_COLUMNS = ("program_id_fk", "as_of", "license_status_id_fk", "capacity", "infant_capacity", "toddler_capacity",
                    "availability_id_fk", "infant_vacancies", "toddler_vacancies", "preschool_vacancies",
                    "school_age_vacancies", "vacancies_updated")


def file_name(as_of: date) -> str:
    return f"child-care-{as_of.isoformat()}.json"


def pages_file_name(as_of: date) -> str:
    return f"child-care-{as_of.isoformat()}-pages.json.gz"


def dereference(value, refs: Optional[dict] = None):
    """A Visualforce remoting answer with its shared values put back: {"s": n, "v": value} gives a
    value the number n, and {"r": n} later stands for it."""
    refs = {} if refs is None else refs
    if isinstance(value, list):
        return [dereference(item, refs) for item in value]
    if not isinstance(value, dict):
        return value
    if set(value) == {"r"}:
        return refs[value["r"]]
    if set(value) == {"s", "v"}:
        refs[value["s"]] = dereference(value["v"], refs)
        return refs[value["s"]]
    return {key: dereference(item, refs) for key, item in value.items()}


# -------------------- fetch --------------------

def remoting_methods(page: str, controller: str) -> dict:
    """{method: (its argument count, the context a call sends)} from the search page's remoting settings."""
    start = page.find("Visualforce.remoting.Manager.add(")
    match = re.search(r"RemotingProviderImpl\((\{.*?\})\)\);", page[start:], re.S) if start >= 0 else None
    if not match:
        raise ValueError("The search page has no remoting settings; has it changed?")
    settings = json.loads(match.group(1))
    methods = {}
    for method in settings["actions"][controller]["ms"]:
        context = {"csrf": method["csrf"], "vid": settings["vf"]["vid"], "ns": method["ns"], "ver": method["ver"]}
        if "authorization" in method:
            context["authorization"] = method["authorization"]
        methods[method["name"]] = (method["len"], context)
    return methods


def _call(config: dict, methods: dict, method: str, arguments: list) -> list:
    """Every record one of the search's methods returns."""
    if method not in methods:
        raise ValueError(f"The search page no longer offers {method}")
    length, context = methods[method]
    if len(arguments) != length:
        raise ValueError(f"The search page's {method} takes {length} arguments, not {len(arguments)}; has it changed?")
    body = json.dumps({"action": config["controller"], "method": method, "data": arguments, "type": "rpc", "tid": 1, "ctx": context})
    request = Request(config["remote_url"], data=body.encode(), headers={
        "Content-Type": "application/json", "Referer": config["search_page"], "X-User-Agent": "Visualforce-Remoting"})
    with urlopen(request, timeout=300) as response:
        answer = json.load(response)[0]
    if answer.get("statusCode") != 200 or "result" not in answer:
        raise ValueError(f"The search's {method} failed: {answer.get('message') or answer}")
    records = dereference(answer["result"])
    if not isinstance(records, list) or not records:
        raise ValueError(f"The search's {method} returned no programs")
    return sorted(records, key=lambda record: record["Id"])


def _write(path: str, fetched: date, config: dict, providers: list, search: list) -> None:
    """A saved download: where it came from, then each list's records, one per line."""
    controller = config["controller"]
    header = json.dumps({"source": "NH DHHS Child Care Search", "page": config["search_page"], "fetched": fetched.isoformat(),
                         "calls": {"providers": f"{controller}.{PROVIDERS_METHOD}(false), the provider download",
                                   "search": f"{controller}.{SEARCH_METHOD}, a search with no filters"}})

    def lines(records):
        return ",\n".join(json.dumps(record, ensure_ascii=False, separators=(",", ":")) for record in records)

    with open(path, "w", encoding="utf-8") as f:
        f.write(f'{header[:-1]}, "providers": [\n{lines(providers)}\n],\n"search": [\n{lines(search)}\n]}}\n')


def trim_page(page: str) -> str:
    """A program page's content, from its name to its hidden dialogs, without scripts, styles and
    hidden placeholders, its spaces collapsed."""
    page = re.sub(r"(?s)<script.*?</script>|<style.*?</style>|<svg.*?</svg>|<!--.*?-->", "", page)
    page = re.sub(r'<span id="[^"]*" style="display: none;"></span>', "", page)
    page = " ".join(page.split())
    name, end = page.find("fontStyleName"), page.find("Your feedback has been successfully submitted")
    if name < 0 or end < 0:
        raise ValueError("not a program page")
    return page[page.rfind("<", 0, name):end]


def read_pages(path: str) -> dict:
    """{record id: trimmed page} saved for a download, or nothing when its pages weren't fetched."""
    if not os.path.exists(path):
        return {}
    with gzip.open(path, "rt", encoding="utf-8") as f:
        return json.load(f)


def _write_pages(path: str, pages: dict) -> None:
    """The pages, one per line, compressed without a timestamp so the same pages save the same file."""
    lines = ",\n".join(f"{json.dumps(key)}:{json.dumps(page, ensure_ascii=False)}" for key, page in sorted(pages.items()))
    with open(path, "wb") as raw, gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as f:
        f.write(f"{{\n{lines}\n}}\n".encode("utf-8"))


def _get(url: str, attempts: int = 3) -> str:
    for attempt in range(1, attempts + 1):
        try:
            with urlopen(url, timeout=120) as response:
                return response.read().decode("utf-8", errors="replace")
        except (URLError, TimeoutError):
            if attempt == attempts:
                raise
            time.sleep(30 * attempt)


def fetch_pages(config: dict, ids: List[str], path: str) -> tuple:
    """Each program's page, trimmed, one every delay_seconds, saved to path as it goes. Pages saved
    there earlier (the same day's interrupted fetch) are kept. Returns the pages and the ids not read."""
    pages = read_pages(path)
    todo = [program_id for program_id in ids if program_id not in pages]
    delay, failed = config["pages"]["delay_seconds"], []
    logger.info(f"Program pages: {len(pages)} saved already, {len(todo)} to read, one every {delay} seconds")
    for number, program_id in enumerate(todo, start=1):
        try:
            pages[program_id] = trim_page(_get(config["detail_url"].format(id=program_id)))
        except (URLError, TimeoutError, ValueError) as error:
            failed.append(program_id)
            logger.warning(f"Page for {program_id} not read: {error}")
        if number % 50 == 0 or number == len(todo):
            _write_pages(path, pages)
            logger.info(f"Program pages: {number} of {len(todo)} read")
        time.sleep(delay)
    return pages, failed


def fetch() -> str:
    """Save today's provider list, unfiltered search results and program pages to the config's directory."""
    config = load_config(CONFIG)
    with urlopen(config["search_page"], timeout=120) as response:
        page = response.read().decode("utf-8", errors="replace")
    methods = remoting_methods(page, config["controller"])
    providers = _call(config, methods, PROVIDERS_METHOD, [False])
    search = _call(config, methods, SEARCH_METHOD, SEARCH_ARGUMENTS)
    programs = parse_download({"providers": providers, "search": search}, config)

    today = date.today()
    directory = config_path(config["directory"])
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, file_name(today))
    _write(path, today, config, providers, search)
    logger.info(f"Child care search, {today}: {len(programs)} programs, capacity {sum(p['capacity'] for p in programs)}")

    pages, failed = fetch_pages(config, [p["source_id"] for p in programs], os.path.join(directory, pages_file_name(today)))
    if failed:
        logger.warning(f"{len(failed)} program pages weren't read; fetch again today to read just those: {failed}")
    logger.info(f"Saved {len(pages)} program pages; add {today} to downloads in {CONFIG}, then load")
    return path


# -------------------- parse --------------------

def _text(value) -> Optional[str]:
    """A text field with its spaces tidied; its lines (a program at two buildings) joined with "; "."""
    if value is None:
        return None
    lines = [" ".join(line.split()) for line in str(value).splitlines()]
    return "; ".join(line for line in lines if line) or None


def _zip(value) -> Optional[str]:
    zip_code = _text(value)
    return zip_code.rstrip("-") if zip_code else None


def _yes_no(value, field: str, name: str) -> Optional[bool]:
    value = _text(value)
    if value is None:
        return None
    if value not in ("Yes", "No"):
        raise ValueError(f"{name}: {field} is {value!r}, not Yes or No")
    return value == "Yes"


def _date(milliseconds) -> Optional[date]:
    """A Salesforce date, which arrives as midnight UTC in milliseconds."""
    return None if milliseconds is None else datetime.fromtimestamp(milliseconds / 1000, timezone.utc).date()


def _list(value) -> List[str]:
    """A multi-select field's values ("a;b;a"), once each, in order."""
    items = []
    for item in (value or "").split(";"):
        item = _text(item)
        if item and item not in items:
            items.append(item)
    return items


def min_age_months(record: dict) -> Optional[float]:
    """The youngest age a program takes, in months. The source gives it in weeks, or in years and months
    (2 years 8 months is age_yrs_lo__c 2, age_mos_lo__c 8)."""
    weeks, months, years = (record.get(key) for key in ("age_wks_lo__c", "age_mos_lo__c", "age_yrs_lo__c"))
    if weeks is not None:
        if months is not None or years is not None:
            raise ValueError(f"{record.get('Name')}: youngest age given in weeks and in months or years")
        return round(weeks * 12 / 52, 1)
    if months is None and years is None:
        return None
    return round((years or 0) * 12 + (months or 0), 1)


def age_group_flags(age_groups: List[str], license_types: List[str],
                    min_months: Optional[float], max_months: Optional[float]) -> dict:
    """
    Whether a program serves infants, toddlers, preschoolers and school-age children, and what says so
    (age_groups_source): the age groups it lists in the search ("listed"); without them, its license's
    program types ("license"); without those, its age range by AGE_GROUP_MONTHS ("age_range"). None
    when there's nothing to go by.
    """
    if age_groups:
        served, source = set(age_groups), "listed"
    elif any(license_type in LICENSE_AGE_GROUPS for license_type in license_types):
        served = {group for license_type in license_types for group in LICENSE_AGE_GROUPS.get(license_type, ())}
        source = "license"
    elif min_months is not None and max_months is not None:
        served = {group for group, (start, end) in AGE_GROUP_MONTHS.items()
                  if (end is None or min_months < end) and max_months >= start}
        source = "age_range"
    else:
        return {**{column: None for column in FLAG_COLUMNS.values()}, "age_groups_source": None}
    return {**{column: group in served for group, column in FLAG_COLUMNS.items()}, "age_groups_source": source}


def fixed_lists(config: dict) -> dict:
    """{list: {the source's value: its id}} for the config's fixed lists. The source names a region with
    its number ("Region 4 Greater Derry and Manchester")."""
    lists = {key: {name: list_id for list_id, name in config[key].items()} for key in LISTS}
    lists["regions"] = {f"Region {region_id} {name}": region_id for region_id, name in config["regions"].items()}
    return lists


def listed_id(lists: dict, key: str, value, name: str = "") -> Optional[int]:
    """A value's id in one of the config's fixed lists; a value it doesn't list stops the load."""
    value = _text(value)
    if value is None:
        return None
    if value not in lists[key]:
        raise ValueError(f"{name}: {value!r} isn't in {key} in {CONFIG}")
    return lists[key][value]


def page_lists(config: dict) -> dict:
    """{an Other Information list's heading, in capitals as the page has it: its feature category's code,
    or None for a list that isn't loaded (skipped_page_lists)}"""
    headings = {category["name"].upper(): category["code"] for category in config["feature_categories"].values()}
    headings.update({heading.upper(): None for heading in config.get("skipped_page_lists") or []})
    return headings


def gsq_step(value, name: str = "") -> Optional[int]:
    """A Granite Steps for Quality step as a number: Licensed is 0, then Step 1 to Step 4."""
    value = _text(value)
    if value is None:
        return None
    if value == "Licensed":
        return 0
    match = re.fullmatch(r"Step ([1-4])", value)
    if not match:
        raise ValueError(f"{name}: Granite Steps for Quality step {value!r} isn't Licensed or Step 1 to 4")
    return int(match.group(1))


def parse_download(saved: dict, config: dict) -> List[dict]:
    """
    One dict per program in a saved download: the provider list's record joined to the search's by
    record id, with the config's fixed lists' ids. Every program must have a known type of care, a
    provider number and a capacity, and appear once.
    """
    types = {program_type["name"] for program_type in config["program_types"].values()}
    lists = fixed_lists(config)
    excluded = set(config.get("excluded_program_types") or [])
    search = {record["Id"]: record for record in saved["search"]}
    programs, ids, numbers = [], set(), set()
    for record in saved["providers"]:
        name = _text(record.get("Name"))
        program_type = (record.get("RecordType") or {}).get("Name") or record.get("Record_Type__c")
        if program_type in excluded:
            continue
        if program_type not in types:
            raise ValueError(f"{name}: type of care {program_type!r} isn't in program_types in {CONFIG}")
        number = _text(record.get("License_Number__c"))
        if not number:
            raise ValueError(f"{name} has no provider number")
        if record["Id"] in ids or number in numbers:
            raise ValueError(f"{name} ({number}) is listed twice")
        ids.add(record["Id"])
        numbers.add(number)
        capacity = whole_number(record.get("Capacity__c"))
        if capacity is None or capacity < 0:
            raise ValueError(f"{name} ({number}) has no capacity: {record.get('Capacity__c')!r}")

        found = search.get(record["Id"], {})
        groups = _list(found.get("Age_Group__c"))
        unknown = [group for group in groups if group not in AGE_GROUPS]
        if unknown:
            raise ValueError(f"{name}: age groups {unknown} aren't {AGE_GROUPS}")
        groups = [group for group in AGE_GROUPS if group in groups]
        license_types = _list(record.get("License_Type_From_Application__c"))
        min_months = min_age_months(record)
        max_months = None if record.get("age_yrs_hi__c") is None else record["age_yrs_hi__c"] * 12
        # Active when it's a Child Care Scholarship provider. The provider list's "Enrolled in the NH Child
        # Care Scholarship" agrees except for a few enrolled programs that are Inactive.
        scholarship = _text(record.get("Provider_Enrollment_Status_Formula__c"))
        if scholarship is not None and scholarship not in SCHOLARSHIP_STATUSES:
            raise ValueError(f"{name}: scholarship enrollment status {scholarship!r} isn't {list(SCHOLARSHIP_STATUSES)}")
        programs.append({
            "source_id": record["Id"],
            "provider_number": number,
            "name": name,
            "program_type": program_type,
            "license_types": license_types,
            "license_issue_date": _date(record.get("Issue_Date__c")),
            "license_expiration_date": _date(record.get("Expiration_Date__c")),
            "min_age_months": min_months,
            "max_age_months": max_months,
            **age_group_flags(groups, license_types, min_months, max_months),
            "accepts_scholarship": SCHOLARSHIP_STATUSES.get(scholarship, False),
            "preventive_protective_care": _yes_no(found.get("Enrolled_as_a_Preventive_and_Protective__c"),
                                                  "Preventive and Protective Care", name),
            "quality_rating_id_fk": listed_id(lists, "quality_ratings", record.get("QRIS_Rating__c"), name),
            "gsq_step": gsq_step(record.get("Qris_GSQ_Approved_Step__c"), name),
            "issued_to": _text(record.get("Issued_To__c")),
            "phone": _text(record.get("Phone")),
            "email": _text(record.get("Email__c")),
            "street": _text(record.get("ShippingStreet")),
            "city": _text(record.get("ShippingCity")),
            "zip": _zip(record.get("ShippingPostalCode")),
            "county_id_fk": listed_id(lists, "counties", record.get("Shipping_County__c"), name),
            "region_id_fk": listed_id(lists, "regions", record.get("Shipping_Region__c"), name),
            "mailing_street": _text(record.get("BillingStreet")),
            "mailing_city": _text(record.get("BillingCity")),
            "mailing_zip": _zip(record.get("BillingPostalCode")),
            "latitude": found.get("ShippingLatitude"),
            "longitude": found.get("ShippingLongitude"),
            # This download's snapshot
            "license_status_id_fk": listed_id(lists, "license_statuses", found.get("License_Status__c"), name),
            "capacity": capacity,
            "infant_capacity": whole_number(found.get("Infant__c")),
            "toddler_capacity": whole_number(found.get("Toddler__c")),
        })

    missing = sorted(p["name"] for p in programs if p["source_id"] not in search)
    if missing:
        logger.warning(f"{len(missing)} programs aren't in the search's results, so they have no age groups, infant or "
                       f"toddler capacity, license status or map location: {missing}")
    unlisted = sorted(record.get("Name") or record["Id"] for record in saved["search"]
                      if record["Id"] not in ids and (record.get("RecordType") or {}).get("Name") not in excluded)
    if unlisted:
        logger.warning(f"{len(unlisted)} programs in the search's results aren't in the provider list and aren't loaded: {unlisted}")
    return programs


def _strip(fragment: str) -> Optional[str]:
    """A piece of a page as text."""
    return _text(html.unescape(re.sub(r"<[^>]+>", " ", fragment)))


def _page_date(value: Optional[str]) -> Optional[date]:
    return datetime.strptime(value, "%m/%d/%Y").date() if value else None


def _time(value: Optional[str]):
    value = _strip(value or "")
    return datetime.strptime(value, "%I:%M %p").time() if value else None


def _labeled(section: str, label: str) -> Optional[str]:
    """The value after a label ("Main Contact: Robyn Andersen")."""
    match = re.search(rf'class="main-label[^"]*">\s*{re.escape(label)}:?\s*</(?:span|div)>(.*?)</(?:div|td)>', section)
    return _strip(match.group(1)) if match else None


def _last_updated(section: str) -> Optional[date]:
    match = re.search(r"Last Updated:\s*(\d{2}/\d{2}/\d{4})?", section)
    return _page_date(match.group(1)) if match else None


def _page_list(value: Optional[str]) -> List[str]:
    """One of Other Information's lists: some separate their values with ";", others with ",". A comma
    inside parentheses is part of a value: "CIVIL SERVICE DISCOUNT (POLICE, FIRE, EMERGENCY)"."""
    if not value:
        return []
    return _list(value if ";" in value else re.sub(r",(?![^()]*\))", ";", value))


def parse_page(page: str, headings: dict, name: str = "") -> dict:
    """What a program's page adds to the provider list: availability, whether its email is hidden, its
    main contact, Head Start, hours, rates, inspections, vacancies and Other Information's lists, by their
    feature category's code (headings: page_lists)."""
    page = trim_page(page) if "<html" in page[:2000].lower() else page
    starts = {}
    for section in PAGE_SECTIONS:
        start = page.find(f'id="{section}"')
        if start < 0:
            raise ValueError(f"{name}: the page has no {section} section")
        starts[section] = page.rfind("<", 0, start)  # from its heading's tag
    header = page[:starts[PAGE_SECTIONS[0]]]
    sections = {section: page[start:(starts[PAGE_SECTIONS[i + 1]] if i + 1 < len(PAGE_SECTIONS) else len(page))]
                for i, (section, start) in enumerate(starts.items())}
    program, schedules = sections["ProgramInformation"], sections["Schedules"]

    availability = re.search(r"Availability</span>\s*<p[^>]*>(.*?)</p>", header)

    # Each schedule panel has days and hours, then rates: a table of age groups by period, or a note ("Please
    # contact the child care provider for the rates."), which having no rates says already. The panels have
    # no names, and some repeat another; each different one is numbered.
    panels = []
    for panel in re.split(r'<div class="panel panel-default schedulePanel"[^>]*>', schedules)[1:]:
        hours = list(dict.fromkeys((DAYS[day], _time(opens), _time(closes)) for day, opens, closes in re.findall(
            rf"<tr>\s*<td>({'|'.join(DAYS)})</td>\s*<td>([^<]*)</td>\s*<td>([^<]*)</td>\s*</tr>", panel)))
        rates = {}
        fees_start = panel.find(">Fees</h4>")
        table = panel[fees_start:] if fees_start >= 0 else ""
        headers = [_strip(header) for header in re.findall(r"<th>(.*?)</th>", table)]
        if headers and headers[0] == "Age Group":
            unknown = [header for header in headers[1:] if header not in RATE_PERIODS]
            if unknown:
                raise ValueError(f"{name}: rate periods {unknown} aren't {list(RATE_PERIODS)}")
            for age_group, cells in re.findall(r"<tr>\s*<td><b>(.*?)</b></td>(.*?)</tr>", table):
                if _strip(age_group) not in AGE_GROUPS:
                    raise ValueError(f"{name}: rates for {_strip(age_group)!r}, which isn't one of {AGE_GROUPS}")
                for period, cell in zip(headers[1:], re.findall(r"<td>(.*?)</td>", cells)):
                    amount = _strip(cell)
                    if amount:
                        rates[(_strip(age_group), RATE_PERIODS[period])] = Decimal(amount.replace("$", "").replace(",", ""))
        found = (tuple(hours), tuple((*key, amount) for key, amount in rates.items()))
        if (hours or rates) and found not in panels:
            panels.append(found)
    hours = [(schedule, *day) for schedule, (days, _) in enumerate(panels, start=1) for day in days]
    rates = [(schedule, *rate) for schedule, (_, panel_rates) in enumerate(panels, start=1) for rate in panel_rates]

    inspections = []
    for review_date, review_type, compliance, details, documents in re.findall(
            r'<td data-label="Visit Date">(.*?)</td>\s*<td data-label="Type of Visit">(.*?)</td>\s*'
            r'<td data-label="Level of Compliance">(.*?)</td>\s*<td data-label="Details">(.*?)</td>\s*'
            r'<td data-label="Visit Documents">(.*?)</td>', sections["InspectionMonitoring"]):
        counts = re.fullmatch(r"(\d+) / (\d+)", _strip(compliance) or "")
        if not _page_date(_strip(review_date)):
            raise ValueError(f"{name}: a licensing visit has no date")
        visit = re.search(r"getNonComplianceItem\('([^']+)'\)", details)
        links = [urljoin("https://new-hampshire.my.site.com/", html.unescape(href))
                 for href in re.findall(r'href="([^"]+)"', documents)]
        inspections.append({"review_date": _page_date(_strip(review_date)), "review_type": _strip(review_type),
                            "items_compliant": int(counts.group(1)) if counts else None,
                            "items_reviewed": int(counts.group(2)) if counts else None,
                            "visit_id": visit.group(1) if visit else None, "document_url": " ".join(links) or None})

    vacancies = {group: whole_number(_labeled(sections["AgesServed"], group)) for group in AGE_GROUPS}

    # The QRIS section's endorsement badges (a GSQ_Badge image) are left out: the provider list's quality
    # rating and Granite Steps for Quality step say more, and don't always agree with them
    features = {}
    other = sections["OtherInformation"]
    for label, value in re.findall(r'<span class="main-label">\s*([^<]+?):?\s*</span>\s*</td>\s*<td>(.*?)</td>', other):
        label = _text(label).upper()
        if label not in headings:
            raise ValueError(f"{name}: Other Information has a list {label!r} that isn't in feature_categories or "
                             f"skipped_page_lists in {CONFIG}")
        if headings[label]:
            features[headings[label]] = _page_list(_strip(value))

    updated = [day for day in (_last_updated(schedules), _last_updated(other)) if day]
    return {
        "availability": _strip(availability.group(1)) if availability else None,
        "email_hidden": EMAIL_HIDDEN in header,
        "main_contact": _labeled(program, "Main Contact"),
        "head_start": _yes_no(_labeled(program, "This is a Head Start Program"), "Head Start", name),
        "early_head_start": _yes_no(_labeled(program, "This is an Early Head Start Program"), "Early Head Start", name),
        "capacity": whole_number(_labeled(program, "Capacity")),
        "hours": hours,
        "rates": rates,
        "details_updated": max(updated) if updated else None,
        "inspections": inspections,
        "vacancies": vacancies,
        "vacancies_updated": _last_updated(sections["AgesServed"]),
        "features": {category: values for category, values in features.items() if values},
    }


# -------------------- load --------------------

class _Towns:
    """A program's town from its city: the config's town_aliases, then the villages and one-word
    matching the school list uses (location.TownMatcher)."""

    def __init__(self, conn: Connection, aliases: Optional[dict]):
        rows = conn.execute(text("SELECT id, name FROM town")).all()
        self.matcher = TownMatcher({town_id: {"name": name} for town_id, name in rows})
        by_name = {name.lower().strip(): town_id for town_id, name in rows}
        self.aliases = {}
        for city, town in (aliases or {}).items():
            if town.lower() not in by_name:
                raise ValueError(f"town_aliases in {CONFIG} gives {city} the town {town}, which isn't in the town table")
            self.aliases[city.lower()] = by_name[town.lower()]

    def find(self, city: Optional[str]) -> Optional[int]:
        if not city:
            return None
        return self.aliases.get(city.lower()) or self.matcher.find(city)


def read_file(config: dict, as_of: date) -> dict:
    path = os.path.join(config_path(config["directory"]), file_name(as_of))
    if not os.path.exists(path):
        raise FileNotFoundError(f"Child care download not found: {path}; run `python -m app.etl fetch child-care`")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _page_rows(pages: dict, program_ids: dict, numbers: dict, review_type_ids: dict) -> dict:
    """The hours, rate and inspection rows from each program's latest page, by table. Every saved
    download's visits are kept: a visit is the same one when its id, or (with no id, a visit from the
    state's older system) its date, type and document are."""
    rows = {table: [] for table in PAGE_TABLES}
    for key in sorted(pages, key=lambda key: numbers[key]):
        page, program_id = pages[key]["page"], program_ids[key]
        rows["child_care_program_hours"].extend((program_id, *hours) for hours in page["hours"])
        rows["child_care_program_rate"].extend((program_id, *rate) for rate in page["rates"])
        visits = {}
        for visit in pages[key]["inspections"]:
            same = visit["visit_id"] or (visit["review_date"], visit["review_type"], visit["document_url"])
            visits[same] = (program_id, visit["visit_id"], visit["review_date"], review_type_ids.get(visit["review_type"]),
                            visit["items_reviewed"], visit["items_compliant"], visit["document_url"])
        rows["child_care_inspection"].extend(sorted(visits.values(), key=lambda row: (row[2], row[3] or 0), reverse=True))
    return rows


PAGE_TABLES = {
    "child_care_program_hours": ("program_id_fk", "schedule", "day_of_week", "opens", "closes"),
    "child_care_program_rate": ("program_id_fk", "schedule", "age_group", "period", "amount"),
    "child_care_inspection": ("program_id_fk", "visit_id", "review_date", "review_type_id_fk", "items_reviewed",
                              "items_compliant", "document_url"),
}


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load every download in the config: each program's latest details and pages, and each download's snapshot."""
    if years:
        raise ValueError(f"child-care loads every download in {CONFIG}; it takes no --year")
    config = load_config(CONFIG)
    downloads = sorted(config["downloads"])
    if not downloads:
        raise ValueError(f"No downloads in {CONFIG}")

    counts = {"child_care_program_type": upsert_rows(
        conn, "child_care_program_type", ("id", "name", "is_licensed"), ("id",),
        [(type_id, program_type["name"], bool(program_type["is_licensed"]))
         for type_id, program_type in sorted(config["program_types"].items())])}
    for key, table in LISTS.items():
        counts[table] = upsert_rows(conn, table, ("id", "name"), ("id",), sorted(config[key].items()))
    counts["child_care_feature_category"] = upsert_rows(
        conn, "child_care_feature_category", ("id", "code", "name"), ("id",),
        [(category_id, category["code"], category["name"]) for category_id, category in sorted(config["feature_categories"].items())])
    type_ids = lookup_ids(conn, "child_care_program_type")
    category_ids = lookup_ids(conn, "child_care_feature_category", "code")
    if LICENSE_TYPE not in category_ids:
        raise ValueError(f"feature_categories in {CONFIG} has no {LICENSE_TYPE}, for the license's program types")
    lists, headings = fixed_lists(config), page_lists(config)

    # The latest download a program is in gives its details, and the latest with its page its page's
    # details; every download gives a snapshot
    latest, snapshots, pages = {}, [], {}
    for as_of in downloads:
        programs = parse_download(read_file(config, as_of), config)
        saved_pages = read_pages(os.path.join(config_path(config["directory"]), pages_file_name(as_of)))
        differ = []
        for program in programs:
            key = program["source_id"]
            page = parse_page(saved_pages[key], headings, program["name"]) if key in saved_pages else None
            latest[key] = program
            if page:
                visits = (pages.get(key) or {}).get("inspections", []) + page["inspections"]
                pages[key] = {"page": page, "inspections": visits}
                if page["capacity"] is not None and page["capacity"] != program["capacity"]:
                    differ.append(f"{program['name']} ({page['capacity']} on its page, {program['capacity']} listed)")
            vacancies = page["vacancies"] if page else {}
            availability = listed_id(lists, "availabilities", page and page["availability"], program["name"])
            snapshots.append((key, as_of, program["license_status_id_fk"], program["capacity"],
                              program["infant_capacity"], program["toddler_capacity"], availability,
                              *(vacancies.get(group) for group in AGE_GROUPS), page and page["vacancies_updated"]))
        read = sum(1 for program in programs if program["source_id"] in saved_pages)
        logger.info(f"Child care, {as_of}: {len(programs)} programs, capacity {sum(p['capacity'] for p in programs)}, "
                    f"{read} program pages")
        if saved_pages and read < len(programs):
            logger.warning(f"Child care, {as_of}: {len(programs) - read} programs' pages weren't saved: "
                           f"{sorted(p['name'] for p in programs if p['source_id'] not in saved_pages)}")
        if differ:
            logger.warning(f"Child care, {as_of}: {len(differ)} pages give a different capacity: {differ}")
    current = {program["source_id"] for program in programs}  # the latest download's

    towns = _Towns(conn, config.get("town_aliases"))
    town_ids = {key: towns.find(program["city"]) for key, program in latest.items()}
    unmatched = sorted({latest[key]["city"] or "(blank)" for key, town_id in town_ids.items() if town_id is None})
    if unmatched:
        raise ValueError(f"Program cities that match no town: {unmatched}; add them to town_aliases in {CONFIG}")
    guessed = sorted(towns.matcher.villages | towns.matcher.partial)
    if guessed:
        logger.info(f"Matched {len(guessed)} villages and city names to towns by name or one word: {guessed}")

    rows = []
    for key, program in sorted(latest.items(), key=lambda item: item[1]["provider_number"]):
        page = pages[key]["page"] if key in pages else {}
        values = {**program, **{column: page.get(column) for column in PAGE_COLUMNS},
                  "program_type_id_fk": type_ids[program["program_type"]], "town_id_fk": town_ids[key],
                  "is_current": key in current}
        rows.append(tuple(values[column] for column in PROGRAM_COLUMNS))
    counts["child_care_program"] = upsert_rows(conn, "child_care_program", PROGRAM_COLUMNS, ("source_id",), rows)
    # Programs loaded before whose downloads have since left the config
    conn.execute(text("UPDATE child_care_program SET is_current = FALSE WHERE is_current AND NOT (source_id = ANY(:ids))"),
                 {"ids": list(latest)})

    program_ids = lookup_ids(conn, "child_care_program", "source_id")
    counts["child_care_program_snapshot"] = upsert_rows(
        conn, "child_care_program_snapshot", SNAPSHOT_COLUMNS, ("program_id_fk", "as_of"),
        [(program_ids[key], *rest) for key, *rest in snapshots])
    numbers = {key: program["provider_number"] for key, program in latest.items()}

    # Each program's features, as (category id, value): its license's program types, and its latest page's
    # lists. Values new to child_care_feature are added, in order.
    features = {key: [(category_ids[LICENSE_TYPE], license_type) for license_type in latest[key]["license_types"]]
                     + [(category_ids[code], value) for code, values in (pages[key]["page"]["features"] if key in pages else {}).items()
                        for value in values]
                for key in sorted(latest, key=lambda key: numbers[key])}
    counts["child_care_feature"] = upsert_rows(
        conn, "child_care_feature", ("category_id_fk", "name"), ("category_id_fk", "name"),
        sorted({feature for found in features.values() for feature in found}))
    feature_ids = {(category_id, name): feature_id for category_id, name, feature_id in
                   conn.execute(text("SELECT category_id_fk, name, id FROM child_care_feature"))}
    counts["child_care_program_feature_xref"] = replace_rows(
        conn, "child_care_program_feature_xref", ("program_id_fk", "feature_id_fk"),
        [(program_ids[key], feature_ids[feature]) for key, found in features.items() for feature in found],
        "program_id_fk = ANY(:ids)", {"ids": [program_ids[key] for key in latest]})
    # Values no program lists any more (once read wrongly, say)
    counts["child_care_feature"]["deleted"] = conn.execute(text(
        "DELETE FROM child_care_feature f WHERE NOT EXISTS "
        "(SELECT 1 FROM child_care_program_feature_xref x WHERE x.feature_id_fk = f.id)")).rowcount

    # What the programs' latest pages list replaces what they listed before
    counts["child_care_review_type"] = upsert_rows(
        conn, "child_care_review_type", ("name",), ("name",),
        sorted({(visit["review_type"],) for page in pages.values() for visit in page["inspections"] if visit["review_type"]}))
    page_rows = _page_rows(pages, program_ids, numbers, lookup_ids(conn, "child_care_review_type"))
    params = {"ids": [program_ids[key] for key in pages]}
    for table, columns in PAGE_TABLES.items():
        counts[table] = replace_rows(conn, table, columns, page_rows[table], "program_id_fk = ANY(:ids)", params)
    return counts
