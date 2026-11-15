"""
NCES's state mapping study: each state's standard for proficient performance on its own test, placed on the NAEP
scale (its "NAEP equivalent score"), reading and math in grades 4 and 8, 2005 to 2022 (see
naep_state_standard_config.yaml).

- naep_state_standard: one row per NCES table, state, subject and grade, as published. 2009 has two: the per-year
  table (2009a/b) and the 2005–2009 comparison study's (1a/b).

NCES's Excel files have a stylesheet openpyxl refuses, so they're read from the sheet XML.
"""
import logging
import os
import re
import zipfile
from html.parser import HTMLParser
from typing import Iterable, List, Optional
from xml.etree import ElementTree

from sqlalchemy.engine import Connection

from app.etl import naep
from app.etl.core import config_path, load_config, lookup_ids, upsert_rows

logger = logging.getLogger("app.etl")

CONFIG = "naep_state_standard_config.yaml"
TABLE = "naep_state_standard"
COLUMNS = ("year", "jurisdiction_id_fk", "assessment_subject_id_fk", "grade_id_fk", "nces_table", "naep_equivalent",
           "standard_error", "relative_error", "caution", "testing_program", "note")
KEY = COLUMNS[:5]

SHEET = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
MISSING = {"—", "–", "-", "†", ""}  # not available, not applicable
CAUTION = {"▲", "!"}  # relative error greater than 0.5
SUBJECTS = {"Reading": "rea", "Mathematics": "mat"}
SUBJECT_WORDS = {"Reading": r"\breading\b", "Mathematics": r"\bmath"}
GRADES = {"a": 4, "b": 8}


def xlsx_rows(path: str) -> List[List[str]]:
    """The first sheet's rows, as text, with empty cells as ""."""
    with zipfile.ZipFile(path) as z:
        shared = [
            "".join(t.text or "" for t in si.iter(f"{SHEET}t"))
            for si in ElementTree.fromstring(z.read("xl/sharedStrings.xml")).iter(f"{SHEET}si")
        ] if "xl/sharedStrings.xml" in z.namelist() else []
        rows = []
        for row in ElementTree.fromstring(z.read("xl/worksheets/sheet1.xml")).iter(f"{SHEET}row"):
            cells = {}
            for c in row.iter(f"{SHEET}c"):
                letters = re.match(r"[A-Z]+", c.get("r")).group()
                column = sum((ord(ch) - 64) * 26 ** i for i, ch in enumerate(reversed(letters))) - 1
                v = c.find(f"{SHEET}v")
                if c.get("t") == "s":
                    value = shared[int(v.text)]
                elif c.get("t") == "inlineStr":
                    value = "".join(t.text or "" for t in c.iter(f"{SHEET}t"))
                else:
                    value = v.text if v is not None else ""
                cells[column] = (value or "").strip()
            rows.append([cells.get(i, "") for i in range(max(cells, default=-1) + 1)])
        return rows


class _Tables(HTMLParser):
    """Each <table>'s caption and rows of cell text"""

    def __init__(self):
        super().__init__()
        self.tables, self.text, self.row = [], None, None

    def handle_starttag(self, tag, attrs):
        if tag == "table":
            self.tables.append({"caption": "", "rows": []})
        elif tag in ("caption", "td", "th") and self.tables:
            self.text = []
        elif tag == "tr" and self.tables:
            self.row = []
        elif tag == "br" and self.text is not None:
            self.text.append(" ")

    def handle_endtag(self, tag):
        if tag == "caption" and self.text is not None:
            self.tables[-1]["caption"] = " ".join("".join(self.text).split())
            self.text = None
        elif tag in ("td", "th") and self.text is not None and self.row is not None:
            self.row.append(" ".join("".join(self.text).split()))
            self.text = None
        elif tag == "tr" and self.row is not None:
            if any(self.row):
                self.tables[-1]["rows"].append(self.row)
            self.row = None

    def handle_data(self, data):
        if self.text is not None:
            self.text.append(data)


def html_tables(path: str) -> List[dict]:
    parser = _Tables()
    with open(path, encoding="utf-8") as f:
        parser.feed(f.read())
    return [t for t in parser.tables if t["caption"].startswith("Table")]


def _number(cell: str) -> Optional[float]:
    return None if cell in MISSING else float(cell)


def _name(cell: str) -> tuple:
    """A row's place and the footnote numbers on it: "Connecticut1" is Connecticut, footnote 1"""
    name, markers = re.fullmatch(r"(.*?)([\d,]*)", cell.strip()).groups()
    return name.strip(), [m for m in markers.split(",") if m]


def _footnotes(cells: List[str]) -> dict:
    """{"–": the not-available note, "1": footnote 1, ...} from the one-cell rows below a table"""
    notes = {}
    for text in cells:
        text = " ".join(text.split())
        m = re.match(r"(\d+|[–—]) ?(.*)", text)
        if m:
            notes["–" if m.group(1) == "—" else m.group(1)] = m.group(2)
    return notes


def _sentences(text: str) -> List[str]:
    return [s for s in re.split(r"(?<=\.) +(?=[A-Z])", text) if s]


def _names_place(sentence: str, place: str, places: List[str]) -> bool:
    """Whether a sentence names the place, and not only a longer name ending in it (West Virginia, not Virginia)"""
    longer = [p for p in places if p != place and p.endswith(" " + place)]
    text = sentence
    for p in longer:
        text = text.replace(p, "")
    return re.search(rf"\b{re.escape(place)}\b", text) is not None


def _note(place: str, markers: List[str], subject: str, footnotes: dict, places: List[str], missing: bool) -> Optional[str]:
    """NCES's footnotes on a row: those its name carries, and every sentence of the table's notes that names the
    place (a sentence about one subject only goes on that subject's rows). A state NCES left out without naming it
    gets the not-available note."""
    other = "Mathematics" if subject == "Reading" else "Reading"
    notes = [sentence for m in markers if m in footnotes for sentence in _sentences(footnotes[m])]
    for text in footnotes.values():
        for sentence in _sentences(text):
            if sentence in notes or not _names_place(sentence, place, places):
                continue
            if {s for s, word in SUBJECT_WORDS.items() if re.search(word, sentence, re.I)} == {other}:
                continue
            notes.append(sentence)
    if missing and not notes and "–" in footnotes:
        notes.append(_sentences(footnotes["–"])[0])
    return " ".join(notes) or None


def _row(year, place, subject, grade, table, values, program, note) -> dict:
    equivalent, standard_error, relative_error, mark = values
    return {"year": year, "place": place, "subject": SUBJECTS[subject], "grade": grade, "nces_table": table,
            "naep_equivalent": _number(equivalent), "standard_error": _number(standard_error),
            "relative_error": _number(relative_error) if relative_error is not None else None,
            "caution": mark in CAUTION, "testing_program": program or None, "note": note}


def parse_excel(path: str, year: int, grade: int, table: str, places: List[str], config: dict) -> List[dict]:
    """One per-year table: each state's reading and math rows. Columns are found from the header row, since they
    move between years (a testing program column from 2015; the state in column A or B)."""
    rows = xlsx_rows(path)
    header = next(i for i, r in enumerate(rows) if "State" in r)
    state = rows[header].index("State")
    program = rows[header].index("Testing program") if "Testing program" in rows[header] else None
    starts = [i for i, cell in enumerate(rows[header]) if "equivalent" in cell]
    # The subject is in the row above, over the score or its standard error
    above = rows[header - 1] + [""] * 3
    subjects = [next((above[j] for j in range(i, i + 2) if above[j]), "") for i in starts]
    if subjects != ["Reading", "Mathematics"]:
        raise ValueError(f"{os.path.basename(path)}: expected reading then math columns, found {subjects}")

    body, notes = [], []
    for r in rows[header + 1:]:
        cells = r + [""] * (max(starts) + 4 - len(r))
        if any(cells[i] for i in starts):
            body.append(cells)
        elif any(cells):
            notes.append(next(c for c in cells if c))
    footnotes = _footnotes(notes)

    consortia = {}
    for cells in body:
        name, _ = _name(cells[state])
        if name in config["consortia"]:
            consortia[name] = [cells[i] for i in starts]

    parsed = []
    for cells in body:
        name, markers = _name(cells[state])
        if name in config["consortia"] or name in config["not_loaded"]:
            continue
        if name not in places:
            raise ValueError(f"{os.path.basename(path)}: unexpected place {cells[state]!r}")
        testing_program = cells[program] if program is not None and cells[program] not in MISSING else None
        for column, (subject, start) in enumerate(zip(SUBJECTS, starts)):
            values = cells[start:start + 4]
            note = _note(name, markers, subject, footnotes, places, values[0] in MISSING)
            same = [c for c, estimates in consortia.items() if values[0] not in MISSING and estimates[column] == values[0]]
            if same:
                note = " ".join(filter(None, [note, f"NCES's table gives the {same[0]} estimate for this state."]))
            parsed.append(_row(year, name, subject, grade, table, values, testing_program, note))
    return parsed


def parse_study_page(path: str, year: int, places: List[str], config: dict) -> List[dict]:
    """One page of the 2005–2009 study: its reading (a) and math (b) tables, each with grades 4 and 8 (score,
    standard error and the relative error mark for each)."""
    parsed = []
    for t in html_tables(path):
        m = re.match(r"Table (\d+[ab])\. .*? (reading|mathematics) proficiency standards.*: (\d{4})$", t["caption"])
        if not m or int(m.group(3)) != year:
            raise ValueError(f"{os.path.basename(path)}: unexpected table {t['caption']!r}")
        table, subject = m.group(1), m.group(2).capitalize()
        footnotes = _footnotes([r[0] for r in t["rows"] if len(r) == 1])
        for cells in (r for r in t["rows"] if len(r) == 7):
            name, markers = _name(cells[0])
            if name in config["not_loaded"]:
                continue
            if name not in places:
                raise ValueError(f"{os.path.basename(path)}: unexpected place {cells[0]!r}")
            for grade, start in ((4, 1), (8, 4)):
                values = cells[start:start + 2] + [None, cells[start + 2]]
                note = _note(name, markers, subject, footnotes, places, values[0] in MISSING)
                parsed.append(_row(year, name, subject, grade, table, values, None, note))
    return parsed


def read(config: dict) -> List[dict]:
    """Every NCES table in the config, as rows by NAEP place name"""
    directory = config_path(config["directory"])
    places = [p["name"] for p in load_config(naep.CONFIG)["jurisdictions"].values()]
    rows = []
    for year in config["years"]:
        for letter, grade in GRADES.items():
            table = f"{year}{letter}"
            rows += parse_excel(os.path.join(directory, f"table_{table}.xlsx"), year, grade, table, places, config)
    for file, year in config["study_tables"].items():
        rows += parse_study_page(os.path.join(directory, file), year, places, config)
    return rows


def check(rows: List[dict]) -> None:
    """Stop on a row that doesn't hold together: a score without a standard error or the reverse, a score outside
    NAEP's 0-500 scale, a caution mark that doesn't match the relative error, or a place twice in one table."""
    seen = set()
    for r in rows:
        key = (r["nces_table"], r["place"], r["subject"], r["grade"])
        if key in seen:
            raise ValueError(f"{key}: twice")
        seen.add(key)
        if (r["naep_equivalent"] is None) != (r["standard_error"] is None):
            raise ValueError(f"{key}: a score without a standard error, or the reverse")
        if r["naep_equivalent"] is not None and not 0 <= r["naep_equivalent"] <= 500:
            raise ValueError(f"{key}: {r['naep_equivalent']} is off NAEP's scale")
        if r["relative_error"] is not None and r["caution"] != (r["relative_error"] > 0.5):
            raise ValueError(f"{key}: the caution mark doesn't match the relative error {r['relative_error']}")


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the given years (default: every table in the config) into naep_state_standard. The places are NAEP's
    jurisdictions, which the naep load adds."""
    config = load_config(CONFIG)
    rows = read(config)
    check(rows)
    if years is not None:
        years = set(years)
        unknown = sorted(years - {r["year"] for r in rows})
        if unknown:
            raise ValueError(f"No state mapping tables for {unknown}")
        rows = [r for r in rows if r["year"] in years]
    places = {p["name"]: code for code, p in load_config(naep.CONFIG)["jurisdictions"].items()}
    ids = lookup_ids(conn, "jurisdiction", "code")
    subjects = lookup_ids(conn, "assessment_subject")
    grades = lookup_ids(conn, "grades")
    missing = sorted({places[r["place"]] for r in rows} - set(ids))
    if missing:
        raise ValueError(f"Places {missing} aren't in jurisdiction; load naep first")
    values = sorted(
        (r["year"], ids[places[r["place"]]], subjects[r["subject"]], grades[f"Grade {r['grade']}"], r["nces_table"],
         r["naep_equivalent"], r["standard_error"], r["relative_error"], r["caution"], r["testing_program"], r["note"])
        for r in rows
    )
    return {TABLE: upsert_rows(conn, TABLE, COLUMNS, KEY, values)}
