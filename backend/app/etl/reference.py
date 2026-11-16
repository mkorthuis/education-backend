"""
The reference library (see reference_config.yaml): cited facts about New Hampshire schools from the
Markdown files in assets/reference/, into reference_topic and reference_fact, with their number
tables in reference_table. The Ask answers rules, terms, research, help and district questions from
them, and links to each fact's source.

Topics are shared across files: a topic such as district-transportation appears once in each town's
research, and its facts from every file load under one reference_topic row, each with its place (a
district, a town, an SAU or a school outside New Hampshire). places.yaml lists those outside schools
and where each district's students go for the grades it doesn't run (district_service), which the
Ask's lookup follows.

Loading replaces the library with the files' contents, so a fact taken out of a file is taken out of
the database. A topic or fact missing something the format requires stops the load.
"""
import glob
import json
import logging
import os
import re
from collections import Counter
from datetime import date
from typing import Dict, Iterable, List, Optional, Tuple

import yaml
from sqlalchemy import text
from sqlalchemy.engine import Connection

from app.etl.core import config_path, has_column, load_config, lookup_ids, replace_rows, upsert_rows

logger = logging.getLogger("app.etl")

CONFIG = "reference_config.yaml"
TOPIC_TABLE = "reference_topic"
FACT_TABLE = "reference_fact"
NUMBER_TABLE = "reference_table"
TOPIC_HEADING = re.compile(r"^## ([a-z0-9]+(?:[-_][a-z0-9]+)*): (.+)$")
TOPIC_FIELD = re.compile(r"^- ([a-z_]+): (.*)$")
FACT_START = re.compile(r"^(\d+)\. (.+)$")
# Indented under the number: three spaces under "1. ", four under "10. "
FACT_FIELD = re.compile(r"^ {3,4}- ([a-z_]+): (.*)$")
# A bulleted line under a fact that isn't one of its fields
LIST_LINE = re.compile(r"^ {2,8}[-*] ")
WEB_ADDRESS = re.compile(r"https?://\S+")
ISO_DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
TOPIC_FIELDS = ("kind", "question_type", "description", "summary")
TABLE_FIELDS = ("unit", "period", "source", "as_of", "raw", "note", "topic", "place")
# A fact's place: "district Jackson", "town Jackson", "sau 9", or a school outside the state by its
# state's name: "maine Fryeburg Academy"
OUTSIDE_STATES = {"maine": "ME", "vermont": "VT", "massachusetts": "MA", "quebec": "QC"}
PLACE = re.compile(r"^(district|town|sau|" + "|".join(OUTSIDE_STATES) + r") (\S.*)$")
GRADES = {"K": 0, "PK": 0}
ARRANGEMENTS = ("tuition_contract", "area_agreement", "cooperative", "choice", "no_contract", "interstate_district", "joint_maintenance")


def _date(value: str) -> Optional[date]:
    """The first full date in a field ("2026-11-08", "Wayback snapshot 2026-10-30"), if any"""
    match = ISO_DATE.search(value or "")
    return date.fromisoformat(match.group(0)) if match else None


def parse_file(text_: str, name: str, config: dict) -> List[dict]:
    """The file's fact topics, each with its facts in order. Sections that aren't fact topics (a
    heading without a "- kind:" line, such as a number table) are skipped here, but a fact with a
    source in one stops the load, since it would never reach the Ask."""
    topics, topic, fact = [], None, None
    lines = text_.split("\n")

    def problem(line_number: int, message: str):
        return ValueError(f"{name}, line {line_number}: {message}")

    for number, line in enumerate(lines, start=1):
        heading = TOPIC_HEADING.match(line)
        if heading or line.startswith("## ") or line.startswith("# "):
            topic, fact = None, None
            if heading:
                topic = {"slug": heading.group(1), "title": heading.group(2).strip(), "file": name, "line": number, "facts": []}
                topics.append(topic)
            continue
        if topic is None:
            # A sourced fact under a heading that isn't a topic would otherwise be skipped silently
            field = FACT_FIELD.match(line)
            if field and field.group(1) == "source":
                raise problem(number, "a fact with a source is under a heading that isn't a topic (## slug: Title)")
            continue
        field = TOPIC_FIELD.match(line)
        if field and not topic["facts"] and field.group(1) in TOPIC_FIELDS:
            topic[field.group(1)] = field.group(2).strip()
            continue
        start = FACT_START.match(line)
        if start:
            fact = {"position": int(start.group(1)), "statement": start.group(2).strip(), "line": number}
            topic["facts"].append(fact)
            continue
        field = FACT_FIELD.match(line)
        if field and fact is not None:
            key, value = field.groups()
            if key not in config["fact_fields"]:
                raise problem(number, f"unknown fact field {key!r}")
            fact[key] = value.strip()
            continue
        if fact is not None and LIST_LINE.match(line):
            # The statement would keep only its first line and this list would be lost
            raise problem(number, f"fact {fact['position']} of {topic['slug']} runs onto a list line; write the statement as one line")
        if line.strip() and fact is not None:
            # Anything else after a fact ends it, so a stray line can't join a statement
            fact = None

    for t in topics:
        if "kind" not in t and any(f.get("source") for f in t["facts"]):
            raise problem(t["line"], f"topic {t['slug']} has facts with sources but no kind")
    facts_topics = [t for t in topics if "kind" in t]
    seen = set()
    for t in facts_topics:
        if t["slug"] in seen:
            raise problem(t["line"], f"topic {t['slug']} appears twice in the file")
        seen.add(t["slug"])
        if t["kind"] not in config["kinds"]:
            raise problem(t["line"], f"topic {t['slug']} has unknown kind {t['kind']!r}")
        for key in ("question_type", "description"):
            if not t.get(key):
                raise problem(t["line"], f"topic {t['slug']} has no {key}")
        if not t["facts"]:
            raise problem(t["line"], f"topic {t['slug']} has no facts")
        positions = Counter(f["position"] for f in t["facts"])
        repeated = [p for p, n in positions.items() if n > 1]
        if repeated:
            raise problem(t["line"], f"topic {t['slug']} numbers more than one fact {repeated[0]}")
        for f in t["facts"]:
            for key in ("source", "as_of", "review_by"):
                if not f.get(key):
                    raise problem(f["line"], f"fact {f['position']} of {t['slug']} has no {key}")
            # One link, shown as is: other links and remarks go in the note
            if not WEB_ADDRESS.fullmatch(f["source"]):
                raise problem(f["line"], f"fact {f['position']} of {t['slug']} has a source that isn't a single web address")
            if _date(f["review_by"]) is None:
                raise problem(f["line"], f"fact {f['position']} of {t['slug']} has no review_by date")
            if f.get("place") and not PLACE.match(f["place"]):
                raise problem(f["line"], f"fact {f['position']} of {t['slug']} has a place that isn't a district, town, SAU or "
                                         f"school outside the state")
    return facts_topics


def parse_tables(text_: str, name: str) -> List[dict]:
    """The file's number tables: a "## slug: Title" heading without "- kind:", its "- field:" lines,
    and the first Markdown table under it. Sections with no table are skipped."""
    tables, current = [], None
    for number, line in enumerate(text_.split("\n"), start=1):
        heading = TOPIC_HEADING.match(line)
        if heading or line.startswith("## ") or line.startswith("# "):
            if current is not None and current["columns"] and "kind" not in current["fields"]:
                tables.append(current)
            current = None
            if heading:
                current = {"slug": heading.group(1), "title": heading.group(2).strip(), "file": name, "line": number,
                           "fields": {}, "columns": [], "rows": [], "done": False}
            continue
        if current is None or current["done"]:
            continue
        field = TOPIC_FIELD.match(line)
        if field and not current["columns"]:
            current["fields"].setdefault(field.group(1), field.group(2).strip())
            continue
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not current["columns"]:
                current["columns"] = cells
            elif all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                continue
            else:
                current["rows"].append(cells)
        elif current["columns"] and line.strip():
            current["done"] = True  # only the first table
    if current is not None and current["columns"] and "kind" not in current["fields"]:
        tables.append(current)
    return tables


def library_files(config: dict) -> List[str]:
    """The files to load, in order, relative to the library's directory. An entry may be a pattern,
    such as town/*/*.md; files named in skip_files (README.md, brief.md) are left out."""
    directory = config_path(config["directory"])
    skip = set(config.get("skip_files", []))
    names = []
    for entry in config["files"]:
        if any(ch in entry for ch in "*?["):
            matched = sorted(os.path.relpath(p, directory) for p in glob.glob(os.path.join(directory, entry)))
            names.extend(n for n in matched if os.path.basename(n) not in skip and n not in names)
        elif entry not in names:
            names.append(entry)
    return names


def shared_topics(config: dict) -> Dict[str, dict]:
    """The shared topics' own title, kind, question type and description, from the registry the town
    research keeps (shared-topics.md), if the config names one and it's there. Rows read
    "| `slug` | Title | kind | question_type | description |"; without a title column, the first
    file's heading is used."""
    name = config.get("shared_topics")
    if not name:
        return {}
    path = os.path.join(config_path(config["directory"]), name)
    if not os.path.exists(path):
        logger.info(f"Reference library: no shared topic list at {name}")
        return {}
    registry = {}
    with open(path) as f:
        for line in f:
            cells = [c.strip() for c in line.strip().strip("|").split("|")] if line.startswith("| `") else []
            if len(cells) == 5:
                slug, title, kind, question_type, description = cells
            elif len(cells) == 4:
                (slug, kind, question_type, description), title = cells, None
            else:
                continue
            registry[slug.strip("`")] = {"title": title, "kind": kind, "question_type": question_type, "description": description}
    return registry


def read_library(config: dict) -> List[dict]:
    """The library's topics, one per slug in the order they first appear, each with the facts of
    every file that has it. Each fact keeps its file and that file's heading for the topic. A topic
    whose kind or question type differs between files stops the load."""
    directory = config_path(config["directory"])
    registry = shared_topics(config)
    topics: Dict[str, dict] = {}
    for name in library_files(config):
        with open(os.path.join(directory, name)) as f:
            sections = parse_file(f.read(), name, config)
        for section in sections:
            for fact in section["facts"]:
                fact["file"], fact["section_title"] = name, section["title"]
            topic = topics.get(section["slug"])
            if topic is None:
                shared = registry.get(section["slug"], {})
                topic = {"slug": section["slug"], "file": name, "title": shared.get("title") or section["title"],
                         "kind": shared.get("kind") or section["kind"], "question_type": shared.get("question_type") or section["question_type"],
                         "description": shared.get("description") or section["description"], "summary": section.get("summary"),
                         "files": [], "facts": []}
                topics[section["slug"]] = topic
            for key in ("kind", "question_type"):
                if section[key] != topic[key]:
                    raise ValueError(f"Topic {section['slug']} is {key} {topic[key]!r} in {topic['files'][0] if topic['files'] else 'the shared list'} "
                                     f"but {section[key]!r} in {name}")
            topic["summary"] = topic["summary"] or section.get("summary")
            topic["files"].append(name)
            topic["facts"].extend(section["facts"])
    return list(topics.values())


def read_tables(config: dict) -> List[dict]:
    directory = config_path(config["directory"])
    tables, seen = [], {}
    for name in library_files(config):
        with open(os.path.join(directory, name)) as f:
            for table in parse_tables(f.read(), name):
                if table["slug"] in seen:
                    raise ValueError(f"Number table {table['slug']} is in both {seen[table['slug']]} and {name}")
                seen[table["slug"]] = name
                tables.append(table)
    return tables


def read_places(config: dict) -> dict:
    """places.yaml: the schools outside New Hampshire, and where each district's students go."""
    name = config.get("places")
    if not name:
        return {"outside_schools": [], "district_service": []}
    with open(os.path.join(config_path(config["directory"]), name)) as f:
        places = yaml.safe_load(f) or {}
    return {"outside_schools": places.get("outside_schools") or [], "district_service": places.get("district_service") or []}


def _grade(value) -> int:
    value = str(value).strip().upper()
    return GRADES[value] if value in GRADES else int(value)


class Places:
    """Turns a file's place ("district Jackson", "sau 9", "maine Fryeburg Academy") into the ids of
    reference_fact's place columns: (district, town, sau, outside school)."""

    def __init__(self, conn: Connection):
        self.districts = lookup_ids(conn, "district")
        self.towns = lookup_ids(conn, "town")
        self.saus = {str(i) for (i,) in conn.execute(text("SELECT id FROM sau"))}
        self.outside = {(row[0], row[1]): row[2] for row in conn.execute(text("SELECT name, state, id FROM outside_school"))}
        self.unmatched = set()

    def ids(self, place: Optional[str]) -> Tuple[Optional[int], Optional[int], Optional[int], Optional[int]]:
        if not place:
            return None, None, None, None
        kind, name = PLACE.match(place).groups()
        found = {"district": lambda: self.districts.get(name), "town": lambda: self.towns.get(name),
                 "sau": lambda: int(name) if name in self.saus else None}.get(kind, lambda: self.outside.get((name, OUTSIDE_STATES[kind])))()
        if found is None:
            self.unmatched.add(place)
            return None, None, None, None
        slot = {"district": 0, "town": 1, "sau": 2}.get(kind, 3)
        return tuple(found if i == slot else None for i in range(4))


def takes_every_arrangement(conn: Connection) -> bool:
    """Whether district_service's check allows every arrangement yet. The migrations that load the library
    call today's loader, and interstate_district and joint_maintenance came in a later one (b7d9f1a3c5e8)."""
    check = conn.execute(text("SELECT pg_get_constraintdef(oid) FROM pg_constraint WHERE conname = 'check_district_service_arrangement'")).scalar()
    return check is None or all(f"'{a}'" in check for a in ARRANGEMENTS)


def load_places(conn: Connection, config: dict) -> dict:
    """Outside schools (upserted by name and state) and district_service (replaced)."""
    places = read_places(config)
    counts = {"outside_school": upsert_rows(
        conn, "outside_school", ("name", "state", "kind", "url"), ("name", "state"),
        [(s["name"], s["state"], s["kind"], s.get("url")) for s in places["outside_schools"]])}
    if not takes_every_arrangement(conn):
        logger.info("district_service doesn't take every arrangement yet; a later migration loads it")
        return counts
    districts = lookup_ids(conn, "district")
    outside = {f"{row[0]} ({row[1]})": row[2] for row in conn.execute(text("SELECT name, state, id FROM outside_school"))}
    rows, problems = [], []
    for entry in places["district_service"]:
        sending = districts.get(entry["district"])
        receiving = districts.get(entry["receiving_district"]) if entry.get("receiving_district") else None
        school = outside.get(entry["outside_school"]) if entry.get("outside_school") else None
        if sending is None or (receiving is None) == (school is None):
            problems.append(f"{entry.get('district')} → {entry.get('receiving_district') or entry.get('outside_school')}")
            continue
        if entry["arrangement"] not in ARRANGEMENTS:
            problems.append(f"{entry['district']}: arrangement {entry['arrangement']!r}")
            continue
        low, high = (_grade(g) for g in entry["grades"])
        rows.append((sending, receiving, school, low, high, entry["arrangement"], entry.get("starts"), entry.get("ends"),
                     entry["source"], entry.get("note")))
    if problems:
        raise ValueError(f"places.yaml: districts or schools not found, or a bad arrangement: {problems}")
    counts["district_service"] = replace_rows(
        conn, "district_service", ("district_id_fk", "receiving_district_id_fk", "outside_school_id_fk", "grade_low", "grade_high",
                                   "arrangement", "starts", "ends", "source_url", "note"), rows, where="TRUE")
    return counts


def link_tables(topics: List[dict], tables: List[dict]) -> None:
    """A table without "- topic:" or "- place:" lines takes them from the facts that mention it by
    name ("See table jackson_transport_ride_minutes"): the topic most of them are under, and the
    place most of those have. Explicit lines win."""
    if not tables:
        return
    names = re.compile(r"(?<![\w-])(" + "|".join(sorted((re.escape(tb["slug"]) for tb in tables), key=len, reverse=True)) + r")(?![\w-])")
    mentions: Dict[str, Counter] = {}
    for t in topics:
        for f in t["facts"]:
            for name in set(names.findall(f"{f['statement']} {f.get('note', '')}")):
                mentions.setdefault(name, Counter())[(t["slug"], f.get("place"))] += 1
    for tb in tables:
        found = mentions.get(tb["slug"])
        if not found:
            continue
        fields = tb["fields"]
        if not fields.get("topic"):
            by_topic = Counter()
            for (slug, _), n in found.items():
                by_topic[slug] += n
            fields["topic"] = by_topic.most_common(1)[0][0]
        if not fields.get("place"):
            by_place = Counter({place: n for (slug, place), n in found.items() if slug == fields["topic"]})
            place = by_place.most_common(1)[0][0] if by_place else None
            if place:
                fields["place"] = place


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Replace the library with the files' contents. (The library has no years; `years` is ignored.)"""
    if not has_column(conn, FACT_TABLE, "fact_key"):
        # Built from an empty database, the first reference migration (d5f7b9c1e3a4) made only the topic and
        # fact tables; the one that adds outside schools, number tables and fact keys (a8c0e2f4b6d8) loads it
        logger.info("The reference library's later tables aren't made yet; a later migration loads it")
        return {}
    config = load_config(CONFIG)
    topics = read_library(config)
    tables = read_tables(config)
    counts = load_places(conn, config)
    places = Places(conn)

    fact_rows, keys = [], Counter()
    for t in topics:
        for f in t["facts"]:
            keys[f"{f['file']}#{t['slug']}#{f['position']}"] += 1
    repeated_keys = [k for k, n in keys.items() if n > 1]
    if repeated_keys:
        raise ValueError(f"Facts with the same file, topic and number: {repeated_keys[:5]}")
    for t in topics:
        for f in t["facts"]:
            places.ids(f.get("place"))
    for table in tables:
        places.ids(table["fields"].get("place"))
    if places.unmatched:
        raise ValueError(f"Places not in the district, town, sau or outside_school table: {sorted(places.unmatched)}")

    counts["facts_removed"] = conn.execute(text(f"DELETE FROM {FACT_TABLE}")).rowcount
    counts[TOPIC_TABLE] = upsert_rows(
        conn, TOPIC_TABLE, ("slug", "title", "kind", "question_type", "description", "summary", "source_file", "display_order"),
        ("slug",), [(t["slug"], t["title"], t["kind"], t["question_type"], t["description"], t.get("summary"), t["file"], order)
                    for order, t in enumerate(topics, start=1)])
    counts["topics_removed"] = conn.execute(text(f"DELETE FROM {TOPIC_TABLE} WHERE slug <> ALL(:slugs)"),
                                            {"slugs": [t["slug"] for t in topics]}).rowcount
    topic_ids = lookup_ids(conn, TOPIC_TABLE, "slug")

    # The same statement, source and place under one topic, as when two towns' research gathered
    # the same Kennett fact: loaded, but worth folding
    same = Counter()
    for t in topics:
        for f in t["facts"]:
            district, town, sau, outside = places.ids(f.get("place"))
            same[(t["slug"], f.get("place"), f["source"], f["statement"].strip().lower())] += 1
            fact_rows.append((
                topic_ids[t["slug"]], f["position"], f["statement"], f.get("citation"), f["source"], _date(f["as_of"]), f["as_of"],
                _date(f["review_by"]), f.get("note"), district, town, sau, outside,
                f"{f['file']}#{t['slug']}#{f['position']}", f["file"], f["section_title"],
            ))
    counts[FACT_TABLE] = replace_rows(conn, FACT_TABLE, (
        "reference_topic_id_fk", "position", "statement", "citation", "source_url", "as_of", "as_of_text", "review_by", "note",
        "district_id_fk", "town_id_fk", "sau_id_fk", "outside_school_id_fk", "fact_key", "source_file", "section_title"), fact_rows)
    repeats = sum(n - 1 for n in same.values() if n > 1)
    if repeats:
        logger.warning(f"Reference library: {repeats} facts repeat another fact's topic, place, source and statement")

    link_tables(topics, tables)
    unknown_topics = sorted({tb["fields"]["topic"] for tb in tables if tb["fields"].get("topic") and tb["fields"]["topic"] not in topic_ids})
    if unknown_topics:
        raise ValueError(f"Number tables name topics that don't exist: {unknown_topics}")
    table_rows = []
    for order, tb in enumerate(tables, start=1):
        fields = tb["fields"]
        link = WEB_ADDRESS.search(fields.get("source", ""))
        table_rows.append((
            tb["slug"], tb["title"], tb["file"], fields.get("unit"), fields.get("period"), fields.get("source"),
            link.group(0).rstrip(".,;)") if link else None, _date(fields.get("as_of")), fields.get("as_of"), fields.get("note"),
            topic_ids.get(fields.get("topic")), *places.ids(fields.get("place")),
            json.dumps(tb["columns"]), json.dumps(tb["rows"]), order,
        ))
    counts["tables_removed"] = conn.execute(text(f"DELETE FROM {NUMBER_TABLE}")).rowcount
    counts[NUMBER_TABLE] = replace_rows(conn, NUMBER_TABLE, (
        "slug", "title", "source_file", "unit", "period", "source", "source_url", "as_of", "as_of_text", "note",
        "reference_topic_id_fk", "district_id_fk", "town_id_fk", "sau_id_fk", "outside_school_id_fk", "columns", "rows",
        "display_order"), table_rows)

    overdue = sum(1 for row in fact_rows if row[7] < date.today())
    if overdue:
        logger.warning(f"Reference library: {overdue} facts are past their review date and won't be used until checked again")
    return counts
