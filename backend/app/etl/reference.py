"""
The reference library (see reference_config.yaml): cited facts about New Hampshire schools from the
Markdown files in assets/reference/, into reference_topic and reference_fact. The Ask answers rules,
terms, research and help questions from them, and links to each fact's source.

Loading replaces the library with the files' contents, so a fact taken out of a file is taken out of
the database. A topic or fact missing something the format requires stops the load.
"""
import logging
import os
import re
from datetime import date
from typing import Iterable, List, Optional

from sqlalchemy import text
from sqlalchemy.engine import Connection

from app.etl.core import config_path, load_config, lookup_ids, replace_rows, upsert_rows

logger = logging.getLogger("app.etl")

CONFIG = "reference_config.yaml"
TOPIC_TABLE = "reference_topic"
FACT_TABLE = "reference_fact"
TOPIC_HEADING = re.compile(r"^## ([a-z0-9]+(?:[-_][a-z0-9]+)*): (.+)$")
TOPIC_FIELD = re.compile(r"^- ([a-z_]+): (.*)$")
FACT_START = re.compile(r"^(\d+)\. (.+)$")
# Indented under the number: three spaces under "1. ", four under "10. "
FACT_FIELD = re.compile(r"^ {3,4}- ([a-z_]+): (.*)$")
WEB_ADDRESS = re.compile(r"https?://\S+")
ISO_DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
TOPIC_FIELDS = ("kind", "question_type", "description", "summary")


def _date(value: str) -> Optional[date]:
    """The first full date in a field ("2026-11-08", "Wayback snapshot 2026-10-30"), if any"""
    match = ISO_DATE.search(value)
    return date.fromisoformat(match.group(0)) if match else None


def parse_file(text_: str, name: str, config: dict) -> List[dict]:
    """The file's fact topics, each with its facts in order. Sections that aren't fact topics (a
    heading without a "- kind:" line, such as a number table) are skipped."""
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
        if line.strip() and fact is not None and not line.startswith("   - "):
            # Anything else after a fact ends it, so a stray line can't join a statement
            fact = None

    facts_topics = [t for t in topics if "kind" in t]
    for t in facts_topics:
        if t["kind"] not in config["kinds"]:
            raise problem(t["line"], f"topic {t['slug']} has unknown kind {t['kind']!r}")
        for key in ("question_type", "description"):
            if not t.get(key):
                raise problem(t["line"], f"topic {t['slug']} has no {key}")
        if not t["facts"]:
            raise problem(t["line"], f"topic {t['slug']} has no facts")
        for f in t["facts"]:
            for key in ("source", "as_of", "review_by"):
                if not f.get(key):
                    raise problem(f["line"], f"fact {f['position']} of {t['slug']} has no {key}")
            # One link, shown as is: other links and remarks go in the note
            if not WEB_ADDRESS.fullmatch(f["source"]):
                raise problem(f["line"], f"fact {f['position']} of {t['slug']} has a source that isn't a single web address")
            if _date(f["review_by"]) is None:
                raise problem(f["line"], f"fact {f['position']} of {t['slug']} has no review_by date")
            if f.get("place") and not re.match(r"^(district|town) \S", f["place"]):
                raise problem(f["line"], f"fact {f['position']} of {t['slug']} has a place that isn't a district or town")
    return facts_topics


def read_library(config: dict) -> List[dict]:
    directory = config_path(config["directory"])
    topics = []
    for name in config["files"]:
        with open(os.path.join(directory, name)) as f:
            topics.extend(parse_file(f.read(), name, config))
    seen = {}
    for t in topics:
        if t["slug"] in seen:
            raise ValueError(f"Topic {t['slug']} is in both {seen[t['slug']]} and {t['file']}")
        seen[t["slug"]] = t["file"]
    return topics


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Replace the library with the files' contents. (The library has no years; `years` is ignored.)"""
    config = load_config(CONFIG)
    topics = read_library(config)
    districts = lookup_ids(conn, "district")
    towns = lookup_ids(conn, "town")

    unmatched = sorted({f["place"] for t in topics for f in t["facts"] if f.get("place")
                        and (districts if f["place"].startswith("district ") else towns).get(f["place"].split(" ", 1)[1]) is None})
    if unmatched:
        raise ValueError(f"Places not in the district or town table: {unmatched}")

    counts = {"facts_removed": conn.execute(text(f"DELETE FROM {FACT_TABLE}")).rowcount}
    counts[TOPIC_TABLE] = upsert_rows(
        conn, TOPIC_TABLE, ("slug", "title", "kind", "question_type", "description", "summary", "source_file", "display_order"),
        ("slug",), [(t["slug"], t["title"], t["kind"], t["question_type"], t["description"], t.get("summary"), t["file"], order)
                    for order, t in enumerate(topics, start=1)])
    counts["topics_removed"] = conn.execute(text(f"DELETE FROM {TOPIC_TABLE} WHERE slug <> ALL(:slugs)"),
                                            {"slugs": [t["slug"] for t in topics]}).rowcount
    topic_ids = lookup_ids(conn, TOPIC_TABLE, "slug")

    rows = []
    for t in topics:
        for f in t["facts"]:
            place = f.get("place", "")
            rows.append((
                topic_ids[t["slug"]], f["position"], f["statement"], f.get("citation"), f["source"], _date(f["as_of"]), f["as_of"],
                _date(f["review_by"]), f.get("note"),
                districts[place.split(" ", 1)[1]] if place.startswith("district ") else None,
                towns[place.split(" ", 1)[1]] if place.startswith("town ") else None,
            ))
    counts[FACT_TABLE] = replace_rows(conn, FACT_TABLE, (
        "reference_topic_id_fk", "position", "statement", "citation", "source_url", "as_of", "as_of_text", "review_by", "note",
        "district_id_fk", "town_id_fk"), rows)
    overdue = sum(1 for row in rows if row[7] < date.today())
    if overdue:
        logger.warning(f"Reference library: {overdue} facts are past their review date and won't be used until checked again")
    return counts
