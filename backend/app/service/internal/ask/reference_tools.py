"""
The Ask's reference tool: cited facts from the reference library (reference_topic and
reference_fact) on rules, terms, how schools work, research, programs and each district's own
practices.

Claude sees each fact's id, statement, citation and date, not its link; the server keeps the links
and shows those of the facts the answer cites, so an answer can only link to a stored source.
"""
from datetime import date
from functools import lru_cache
from typing import List, Optional
from urllib.parse import urlparse

from sqlmodel import Session, select

from app.core.db import engine
from app.model.location import District
from app.model.reference import ReferenceFact, ReferenceTopic
from app.service.internal.ask.data_tools import DataToolError

MAX_TOPICS = 4
FACT_PREFIX = "r"
MAX_LABEL = 160
# Facts about this site's own methods: the Ask may use them, but they aren't outside sources
OWN_SITE = "nhfacts.com"


@lru_cache(maxsize=1)
def catalog() -> tuple:
    """(slug, kind, description) for every topic, in display order. Read once per process: reloading
    the library needs a restart, like the API cache."""
    with Session(engine) as session:
        topics = session.exec(select(ReferenceTopic).order_by(ReferenceTopic.display_order)).all()
        return tuple((t.slug, t.kind, t.description) for t in topics)


def site(url: str) -> str:
    """The website a link goes to, for showing beside it: gc.nh.gov, picnh.org"""
    host = urlparse(url).netloc.lower()
    return host[4:] if host.startswith("www.") else host


def tool_definition() -> dict:
    topics = catalog()
    lines = "\n".join(f"- {slug} ({kind}): {description}" for slug, kind, description in topics)
    return {
        "name": "look_up_reference",
        "description": (
            "Cited facts from this site's reference library on New Hampshire schools: what state and federal law require and "
            "what families can do (rule), what terms and the site's measures mean (term), how schools are run and paid for "
            "(how_it_works), what research says works (research), programs and where to get help (programs), and each "
            "district's own practices, such as kindergarten, preschool, budget votes and high school options (local; give "
            f"the district's id from find_places). Pick up to {MAX_TOPICS} topics:\n{lines}"
        ),
        # Not strict: strict tools are compiled into one grammar with the answer's schema, and an enum of
        # every topic grows with the library past the API's limit. The enum still guides Claude, and
        # look_up_reference checks the input itself.
        "input_schema": {
            "type": "object",
            "properties": {
                "topics": {"type": "array", "items": {"type": "string", "enum": [slug for slug, _, _ in topics]}},
                "district_id": {"type": ["integer", "null"], "description": "For local topics: the district's id from find_places; otherwise null"},
            },
            "required": ["topics", "district_id"],
            "additionalProperties": False,
        },
    }


def _label(fact: ReferenceFact, topic: ReferenceTopic) -> str:
    label = fact.citation or topic.title
    return label if len(label) <= MAX_LABEL else label[: MAX_LABEL - 1].rstrip() + "…"


def look_up_reference(session: Session, topics: List[str], district_id: Optional[int] = None) -> dict:
    """The facts of up to four topics that are within their review date. A fact about one district is
    given only when that district is asked for. Returns what Claude reads, and under "_sources" each
    fact's link, which isn't sent to Claude."""
    if not isinstance(topics, list) or not all(isinstance(slug, str) for slug in topics):
        raise DataToolError("topics must be a list of topic names.")
    if district_id is not None and (isinstance(district_id, bool) or not isinstance(district_id, int)):
        raise DataToolError("district_id must be a district's id number from find_places, or null.")
    slugs = list(dict.fromkeys(topics))
    if not slugs or len(slugs) > MAX_TOPICS:
        raise DataToolError(f"Pick 1 to {MAX_TOPICS} topics.")
    found = {t.slug: t for t in session.exec(select(ReferenceTopic).where(ReferenceTopic.slug.in_(slugs))).all()}
    unknown = [slug for slug in slugs if slug not in found]
    if unknown:
        raise DataToolError(f"Unknown topics: {', '.join(unknown)}.")
    district = None
    if district_id is not None:
        district = session.get(District, district_id)
        if district is None:
            raise DataToolError(f"No district has id {district_id}; use find_places to look it up.")

    today = date.today()
    facts = session.exec(
        select(ReferenceFact)
        .where(ReferenceFact.reference_topic_id_fk.in_([t.id for t in found.values()]))
        .order_by(ReferenceFact.reference_topic_id_fk, ReferenceFact.position)
    ).all()
    result, sources = {"topics": []}, {}
    for slug in slugs:
        topic = found[slug]
        entry = {"topic": slug, "title": topic.title, "kind": topic.kind, "facts": []}
        if topic.summary:
            entry["summary"] = topic.summary
        expired = 0
        for fact in (f for f in facts if f.reference_topic_id_fk == topic.id):
            if fact.district_id_fk is not None and fact.district_id_fk != district_id:
                continue
            if fact.review_by < today:
                expired += 1
                continue
            fact_id = f"{FACT_PREFIX}{fact.id}"
            entry["facts"].append({"id": fact_id, "statement": fact.statement, "citation": fact.citation, "as_of": fact.as_of_text,
                                   "site": site(fact.source_url)})
            if site(fact.source_url) != OWN_SITE:
                sources[fact_id] = {"label": _label(fact, topic), "url": fact.source_url, "site": site(fact.source_url),
                                    "as_of": fact.as_of.isoformat() if fact.as_of else None}
        if expired:
            # Shown in the server log so the facts get checked again
            entry["facts_withheld"] = f"{expired} facts are past their review date and aren't given"
        if topic.kind == "local" and district is None:
            entry["note"] = "This topic's facts are by district; call again with the district's id from find_places."
        elif topic.kind == "local" and not entry["facts"]:
            entry["note"] = f"The library has nothing on this for {district.name}; say so and suggest asking the district."
        result["topics"].append(entry)
    result["_sources"] = sources
    return result
