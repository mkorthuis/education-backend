"""
Copy the Children's Scholarship Fund's EFA reports into CSVs for app/etl/education_freedom_account_provider.py:

- the Expenditure Reports (years 1-4, 2021-22 to 2024-25): every provider paid, by allowable category,
  to efa-expenditures-YYYY.csv (YYYY the school year's end)
- "Number Served Last Year" (calendar 2025): students served by each provider with 10 or more, to
  efa-served-2025.csv

    python backend/scripts/extract_education_freedom_account_expenditures.py <out dir> <year-1 report.pdf> <number served.pdf> \\
        2023:<reading 1>:<reading 2> 2024:... 2025:...

Year 1 has a text layer. Years 2-4 are scans, read twice by efa_ocr.swift (OCR_SCALE 3 and 4.5). Each
category's total is the sum of its provider lines, which is how categories are found in year 1 and how
every year is checked: nothing is written unless each category adds up and the categories add up to the
report's grand total. In the scans, categories are the sentence-case lines (providers are printed in
capitals); where the first reading's providers don't add up, a provider the two readings read
differently takes the second reading's amount when that closes the gap. CORRECTIONS holds the lines both
readings got wrong, each checked against the page. Needs pdfplumber, which the backend doesn't use.
"""
import csv
import difflib
import itertools
import os
import re
import sys
from decimal import Decimal

import pdfplumber

# Lines of the first reading the recognizer got wrong, as read -> as printed (checked against the page images)
CORRECTIONS = {
    2023: {
        # A category name's first line, half covered by the shaded bar it's printed on
        ".....Y\t....": "Computer hardware or other technological services and devices & Textbooks,",
    },
    2024: {
        "SCHOOLHOUSE DISCOVERIES LLC\t1,049,49\t0.01%": "SCHOOLHOUSE DISCOVERIES LLC\t1,049.49\t0.01%",
        "GRAND MONADNOCK YOUTH CHOIRS\t00:06\t0.00%": "GRAND MONADNOCK YOUTH CHOIRS\t90.00\t0.00%",
        "OLD STURBRIDGE VILLAGE\t00:69\t%00*0": "OLD STURBRIDGE VILLAGE\t69.00\t0.00%",
    },
    2025: {
        "WALKER FAMILY GOODS\t319.47.\t0.00%": "WALKER FAMILY GOODS\t319.47\t0.00%",
        "BREVARDZOO\t06Lt\t0.00%": "BREVARDZOO\t47.90\t0.00%",
        "CLICKBANK\t799\t0.00%": "CLICKBANK\t7.99\t0.00%",
        "Computer hardware or other technological services and devices\t1LLL'596\t4.78%":
            "Computer hardware or other technological services and devices\t965,717.41\t4.78%",
        # Half covered by the next category's shaded bar
        "MAIVISET SULUTIUNS\t44.55\tU.UV%": "RAMSEY SOLUTIONS\t44.99\t0.00%",
    },
}

# Page furniture, compared with spaces removed since the recognizer drops and adds them
FURNITURE = re.compile(r"^(===page|draft|datadec|\d\d-\d\defaexpenditure|category&?andprovider|allowablecategory|"
                       r"educationprovider/vendor|\d{4}-\d{4}efaexpenditurereport|page\d+of\d+|data.*page\d+of\d+$|.*summarypage\d+$)", re.I)
# A line's name, then its amount (cents always), then its share, which may have lost its "%"
LINE = re.compile(r"^(.*?)[\t ]+(-?\$?\d{1,3}(?:,\d{3})*\.\d\d)(?:[\t ]+-?\d{1,3}\.\d{1,2} ?%?)?[\t ]*$")


def spaceless(text):
    return re.sub(r"\s+", "", text).lower()


def key(name):
    return re.sub(r"[^A-Z0-9]", "", name.upper())


def amount_rows(lines):
    """(name, amount) for each line with an amount, from the first category on; a wrapped name's first part joined on."""
    start = next(i for i, l in enumerate(lines) if spaceless(l).startswith("tuitionandfeesataprivateschool") and LINE.match(l.strip()))
    pending = []
    for line in lines[start:]:
        line = line.strip()
        if not line or FURNITURE.search(spaceless(line)):
            continue
        m = LINE.match(line)
        if not m:
            pending.append(re.sub(r"\s+", " ", line))
            continue
        name = " ".join(pending + [re.sub(r"\s+", " ", m.group(1))]).strip()
        pending = []
        yield name, Decimal(m.group(2).replace(",", "").replace("$", ""))


def by_totals(lines):
    """Categories [name, total, rows] found by their totals: once a category's providers add up to it, the next line starts the next."""
    categories, grand = [], None
    for name, amount in amount_rows(lines):
        if spaceless(name).startswith("grandtotal"):
            grand = amount
            break
        if not categories or sum(a for _, a in categories[-1][2]) == categories[-1][1]:
            categories.append([name, amount, []])
        else:
            categories[-1][2].append((name, amount))
    return categories, grand


def by_case(lines):
    """Categories [name, total, rows] in the scans: the sentence-case lines; providers are printed in capitals."""
    categories, grand = [], None
    for name, amount in amount_rows(lines):
        if spaceless(name).startswith("grandtotal"):
            grand = amount
            break
        if len(re.findall(r"[a-z]", name)) >= 5:
            categories.append([name, amount, []])
        else:
            categories[-1][2].append((name, amount))
    return categories, grand


def combine(first, second):
    """
    Where the first reading's providers don't add up: the second reading's providers, if they add up; or the
    second reading's amount for one or two providers the two read differently, if that closes the gap.
    """
    if len(first) != len(second):
        raise ValueError(f"{len(first)} categories in one reading, {len(second)} in the other")
    for category, other in zip(first, second):
        rows = category[2]
        if sum(a for _, a in rows) == category[1]:
            continue
        if sum(a for _, a in other[2]) == category[1]:
            category[2] = other[2]                     # the second reading adds up on its own: take it
            continue
        matcher = difflib.SequenceMatcher(None, [key(n) for n, _ in rows], [key(n) for n, _ in other[2]], autojunk=False)
        pairs = [(i, other[2][j][1]) for block in matcher.get_matching_blocks()
                 for i, j in zip(range(block.a, block.a + block.size), range(block.b, block.b + block.size)) if rows[i][1] != other[2][j][1]]
        gap = category[1] - sum(a for _, a in rows)
        fixed = next((combo for n in (1, 2) for combo in itertools.combinations(pairs, n)
                      if sum(new - rows[i][1] for i, new in combo) == gap), None)
        for i, new in fixed or ():
            rows[i] = (rows[i][0], new)
    return first


def check(year, categories, grand):
    problems = [f"{name[:60]!r}: providers add up to {sum(a for _, a in rows)}, total {total}"
                for name, total, rows in categories if sum(a for _, a in rows) != total]
    if grand is None or sum(total for _, total, _ in categories) != grand:
        problems.append(f"categories add up to {sum(total for _, total, _ in categories)}, grand total {grand}")
    if problems:
        raise ValueError(f"{year}: " + "; ".join(problems))


def text_lines(pdf_path):
    """A PDF's text layer, each line in the recognizer's shape: name, amount and share split by tabs."""
    lines = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            for line in (page.extract_text() or "").splitlines():
                m = re.match(r"^(.*?)\s+(-?[\d,]+\.\d\d)\s+(-?[\d.]+%)$", line)
                lines.append("\t".join(m.groups()) if m else line)
    return lines


def write_expenditures(out_dir, year, categories, grand):
    path = os.path.join(out_dir, f"efa-expenditures-{year}.csv")
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["year", "line_no", "category", "category_total", "provider", "amount"])
        line_no = 0
        for name, total, rows in categories:
            for provider, amount in rows:
                line_no += 1
                writer.writerow([year, line_no, name, total, provider, amount])
    print(f"{path}: {len(categories)} categories, {line_no} provider lines, {grand}")


def write_served(out_dir, pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        lines = [l for page in pdf.pages for l in (page.extract_text() or "").splitlines()]
    rows = [m.groups() for m in (re.match(r"^(.*\S)\s+(\d[\d,]*)$", l) for l in lines) if m]
    path = os.path.join(out_dir, "efa-served-2025.csv")
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["calendar_year", "provider", "students"])
        for provider, students in rows:
            writer.writerow([2025, provider, students.replace(",", "")])
    print(f"{path}: {len(rows)} providers")


def main(out_dir, year_one_pdf, served_pdf, *scans):
    categories, grand = by_totals(text_lines(year_one_pdf))
    check(2022, categories, grand)
    write_expenditures(out_dir, 2022, categories, grand)
    for scan in scans:
        year, first, second = scan.split(":")
        year = int(year)
        corrections = CORRECTIONS.get(year, {})
        lines = [corrections.get(l, l) for l in open(first, encoding="utf-8").read().splitlines()]
        unused = set(corrections) - set(open(first, encoding="utf-8").read().splitlines())
        if unused:
            raise ValueError(f"{year}: corrections for lines the reading doesn't have: {sorted(unused)}")
        categories, grand = by_case(lines)
        other, _ = by_case(open(second, encoding="utf-8").read().splitlines())
        categories = combine(categories, other)
        check(year, categories, grand)
        write_expenditures(out_dir, year, categories, grand)
    write_served(out_dir, served_pdf)


if __name__ == "__main__":
    main(*sys.argv[1:])
