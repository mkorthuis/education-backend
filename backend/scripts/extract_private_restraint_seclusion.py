"""
Copy the private (nonpublic) schools' rows out of NHED's restraint and seclusion report PDFs, one
CSV per school year, for app/etl/private_safety.py:

    python backend/scripts/extract_private_restraint_seclusion.py backend/app/alembic/assets/private-safety report.pdf ...

Needs pdfplumber (pip install pdfplumber), which the backend itself doesn't use, so run it outside
the app's environment. The rows start after the report's nonpublic summary table, whose printed
totals each year's rows are checked against; add those totals to
private_school_restraint_seclusion_config.yaml with the new year. A school listed twice with the
same figures is kept once; with different figures, the script stops.
"""
import csv, re, sys, pdfplumber

COLUMNS = ["year", "school_id", "school_name", "enrollment", "restraint_reports", "restraints_bodily_harm",
           "restraints_serious_injury_or_death", "restraint_investigations_active", "restraint_investigations_closed",
           "seclusion_reports", "seclusion_investigations_active", "seclusion_investigations_closed"]
# Summary line -> the column it totals
SUMMARY = {
    "students enrolled": "enrollment",
    "restraint reports generated": "restraint_reports",
    "active/on-going restraint": "restraint_investigations_active",
    "closed restraint": "restraint_investigations_closed",
    "bodily harm": "restraints_bodily_harm",
    "serious injury or death": "restraints_serious_injury_or_death",
    "seclusion reports generated": "seclusion_reports",
    "active/on-going seclusion": "seclusion_investigations_active",
    "closed seclusion": "seclusion_investigations_closed",
}

def number(cell):
    cell = (cell or "").replace(",", "").strip()
    return int(cell) if re.fullmatch(r"\d+", cell) else None

def extract(path):
    rows, summary, in_nonpublic = [], {}, False
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            for table in page.extract_tables():
                flat = " ".join(c for row in table for c in row if c)
                if not in_nonpublic and re.search(r"(?i)non-?public", flat) and re.search(r"(?i)restraint", flat):
                    in_nonpublic = True
                    for row in table:
                        label = re.sub(r"\s+", " ", row[0] or "").lower()
                        for key, column in SUMMARY.items():
                            if key in label:
                                summary[column] = number(row[1])
                    continue
                if not in_nonpublic:
                    continue
                for row in table:
                    cells = [re.sub(r"\s+", " ", c or "").strip() for c in row]
                    if len(cells) >= 12 and re.fullmatch(r"20\d\d", cells[0]) and re.fullmatch(r"\d+", cells[1]):
                        rows.append(dict(zip(COLUMNS, [int(cells[0]), int(cells[1]), cells[2]] + [number(c) for c in cells[3:12]])))
    return rows, summary

for path in sys.argv[2:]:
    rows, summary = extract(path)
    # Some reports list a school twice with the same figures (2020-21, 2021-22): keep one; differing repeats are an error
    unique = {}
    for row in rows:
        if row["school_id"] in unique and unique[row["school_id"]] != row:
            raise ValueError(f"{path}: school {row['school_id']} listed twice with different figures")
        unique[row["school_id"]] = row
    repeats = len(rows) - len(unique)
    rows = list(unique.values())
    years = {row["year"] for row in rows}
    year = years.pop() if len(years) == 1 else None
    ids = [row["school_id"] for row in rows]
    problems = []
    if year is None:
        problems.append(f"years in rows: {sorted({row['year'] for row in rows})}")
    if len(ids) != len(set(ids)):
        problems.append(f"duplicate school ids: {sorted({i for i in ids if ids.count(i) > 1})}")
    for column, expected in summary.items():
        total = sum(row[column] or 0 for row in rows)
        if total != expected:
            problems.append(f"{column}: rows sum to {total}, summary says {expected}")
    blank = [row["school_name"] for row in rows if all(row[c] is None for c in COLUMNS[3:])]
    out = f"{sys.argv[1]}/nonpublic-restraint-seclusion-{year}.csv"
    with open(out, "w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda row: row["school_id"]))
    print(f"{path.rsplit('/', 1)[1]}: year {year}, {len(rows)} schools, summary checked {len(summary)}/9 columns, "
          f"{'OK' if not problems else 'PROBLEMS: ' + '; '.join(problems)}; repeats dropped: {repeats}; all-blank rows: {blank}")
