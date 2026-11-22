"""
Turn tuition research into the CSVs app/etl/private_tuition.py loads:

    python backend/scripts/private_tuition_to_csv.py <out dir> <retrieved on, YYYY-MM-DD> <default school year end> research.json ...

Each research file is a JSON array, one object per school and school year, read from the school's own website:

    {"school_id": 20290, "status": "published" | "not_published" | "site_unavailable", "year": "2026-27" or null,
     "source_url": "...", "with_aid": "85% of students" or null, "note": "...", "pages_checked": ["..."],
     "rates": [{"band": "Grades 1-5", "lowest_grade": "Grade 1", "highest_grade": "Grade 5",
                "rate_type": "standard", "rate_label": null, "tuition": 12200, "required_fee": 800,
                "fee_note": "...", "rate_note": null}]}

Grades are the grades table's names (Preschool, Kindergarten, Grade 1 ... Grade 12, Post Graduate). A
school year is written "2026-27" and stored by its end (2027); a school with no year on its page, or one
without published tuition, gets the default year, and its note says so. A required_fee of null (a fee the
school names without an amount) stays empty, apart from 0 (none).
"""
import csv
import json
import os
import re
import sys


def year_end(year, default):
    if not year:
        return default, "The page gives no school year."
    m = re.fullmatch(r"(\d{4})-(\d{2}|\d{4})", year.strip())
    if not m:
        raise ValueError(f"A school year that isn't like 2026-27: {year!r}")
    return int(m.group(1)) + 1, None


def main(out_dir, retrieved_on, default_year, *paths):
    default_year = int(default_year)
    schools = []
    for school in (school for path in paths for school in json.load(open(path))):
        year, year_note = year_end(school.get("year"), default_year) if school["status"] == "published" else (default_year, None)
        schools.append((school["school_id"], year, year_note, school))
    keys = [(school_id, year) for school_id, year, _, _ in schools]
    if len(set(keys)) != len(keys):
        raise ValueError(f"School years researched twice: {sorted({k for k in keys if keys.count(k) > 1})}")
    sources, rates = [], []
    for school_id, year, year_note, school in sorted(schools, key=lambda s: s[:2]):
        if school["status"] != "published" and school.get("rates"):
            raise ValueError(f"School {school['school_id']} isn't published but has rates")
        pages = "; ".join(school.get("pages_checked") or [])
        note = " ".join(part for part in (year_note, school.get("note")) if part) or None
        if school["status"] != "published" and pages:
            note = " ".join(part for part in (note, f"Pages checked: {pages}") if part)
        sources.append([school["school_id"], year, school["status"], school.get("source_url") or "",
                        retrieved_on, school.get("with_aid") or "", note or ""])
        for rate_no, rate in enumerate(school.get("rates") or [], 1):
            rates.append([school["school_id"], year, rate_no, rate["band"], rate["lowest_grade"], rate["highest_grade"],
                          rate["rate_type"], rate.get("rate_label") or "", rate["tuition"],
                          "" if rate.get("required_fee") is None else rate["required_fee"],
                          rate.get("fee_note") or "", rate.get("rate_note") or ""])
    with open(os.path.join(out_dir, "school-tuition-sources.csv"), "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["school_id", "year", "status", "source_url", "retrieved_on", "with_aid", "note"])
        writer.writerows(sources)
    with open(os.path.join(out_dir, "school-tuition-rates.csv"), "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["school_id", "year", "rate_no", "band", "lowest_grade", "highest_grade", "rate_type", "rate_label",
                         "tuition", "required_fee", "fee_note", "rate_note"])
        writer.writerows(rates)
    published = sum(1 for row in sources if row[2] == "published")
    print(f"{len(sources)} school years ({published} published), {len(rates)} rates")


if __name__ == "__main__":
    main(*sys.argv[1:])
