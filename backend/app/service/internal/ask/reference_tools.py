"""
The Ask's reference tool: cited facts from the reference library (reference_topic and
reference_fact) on rules, terms, how schools work, research, programs and each district's own
practices, with the library's number tables.

A district's facts come with those of the places its students depend on: its towns, its SAU, and
the districts and outside schools that take its students for grades it doesn't run (district_service),
so a Jackson question also sees Kennett High's and Fryeburg Academy's facts. district_service is read
both ways, so a Conway question also sees the facts of the districts that send it students, and a
cooperative's those of its member districts, after the places its own students go. A topic can hold
hundreds of facts across towns, so each topic gives at most MAX_FACTS, ranked by an optional query
of a few words, then by how close the place is to the district asked about.

Claude sees each fact's id, statement, citation, date and place, not its link; the server keeps the
links and shows those of the facts the answer cites, so an answer can only link to a stored source.
"""
from datetime import date
from functools import lru_cache
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlparse

from sqlalchemy import text
from sqlmodel import Session, select

from app.core.db import engine
from app.model.location import District
from app.model.reference import ReferenceTopic
from app.service.internal.ask.data_tools import DataToolError

MAX_TOPICS = 4
MAX_FACTS = 25  # per topic
MAX_TABLES = 3  # per topic
MAX_TABLE_ROWS = 40
MAX_QUERY = 200
FACT_PREFIX = "r"
TABLE_PREFIX = "rt"
MAX_LABEL = 160
# Facts about this site's own methods: the Ask may use them, but they aren't outside sources
OWN_SITE = "nhfacts.com"

# How close a fact's place is to the district asked about; lower comes first
OWN, OWN_SAU, NO_PLACE, SERVES, SERVES_SAU, SENDS, SENDS_SAU, ELSEWHERE = 0, 1, 2, 3, 4, 5, 6, 7


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
            "district's own practices (local; give the district's id from find_places). A district's facts come with those of "
            "its towns, its SAU and the schools its students attend for grades it doesn't run, including schools in other "
            "states, then those of the districts that send it students, such as a cooperative's member districts; each fact "
            "says which place it's about. A topic gives at most "
            f"{MAX_FACTS} facts: for a long one, add a query of a few words (\"late bus\", \"AP courses\") to rank them. "
            f"Pick up to {MAX_TOPICS} topics:\n{lines}"
        ),
        # Not strict: strict tools are compiled into one grammar with the answer's schema, and an enum of
        # every topic grows with the library past the API's limit. The enum still guides Claude, and
        # look_up_reference checks the input itself.
        "input_schema": {
            "type": "object",
            "properties": {
                "topics": {"type": "array", "items": {"type": "string", "enum": [slug for slug, _, _ in topics]}},
                "district_id": {"type": ["integer", "null"], "description": "For local topics: the district's id from find_places; otherwise null"},
                "query": {"type": ["string", "null"], "description": "Optional: a few words to rank a topic's facts by, such as \"late bus\""},
            },
            "required": ["topics", "district_id"],
            "additionalProperties": False,
        },
    }


def _label(citation: Optional[str], title: str) -> str:
    label = citation or title
    return label if len(label) <= MAX_LABEL else label[: MAX_LABEL - 1].rstrip() + "…"


def related_places(session: Session, district: District) -> Dict[Tuple[str, int], int]:
    """The places whose facts a question about this district gets, each with how close it is:
    {("district", 271): OWN, ("town", 271): OWN, ("sau", 9): OWN_SAU, ("district", 113): SERVES, ...}.
    The districts that send it students come after those that take its own (Conway: Jackson, SENDS)."""
    places = {("district", district.id): OWN}
    for (town_id,) in session.execute(text("SELECT town_id_fk FROM town_district_xref WHERE district_id_fk = :d"), {"d": district.id}):
        places[("town", town_id)] = OWN
    if district.sau_id_fk:
        places[("sau", district.sau_id_fk)] = OWN_SAU
    for kind, ident, sau in session.execute(text("""
            SELECT 'district', d.id, d.sau_id_fk FROM district_service s JOIN district d ON d.id = s.receiving_district_id_fk
            WHERE s.district_id_fk = :d
            UNION
            SELECT 'outside', s.outside_school_id_fk, NULL FROM district_service s
            WHERE s.district_id_fk = :d AND s.outside_school_id_fk IS NOT NULL"""), {"d": district.id}):
        places.setdefault((kind, ident), SERVES)
        if sau:
            places.setdefault(("sau", sau), SERVES_SAU)
    for ident, sau in session.execute(text("""
            SELECT DISTINCT d.id, d.sau_id_fk FROM district_service s JOIN district d ON d.id = s.district_id_fk
            WHERE s.receiving_district_id_fk = :d"""), {"d": district.id}):
        places.setdefault(("district", ident), SENDS)
        if sau:
            places.setdefault(("sau", sau), SENDS_SAU)
    return places


def _place_of(row) -> Optional[Tuple[str, int]]:
    for kind, value in (("district", row.district_id_fk), ("town", row.town_id_fk), ("sau", row.sau_id_fk), ("outside", row.outside_school_id_fk)):
        if value is not None:
            return kind, value
    return None


# Each fact's place, by name: a district, "Town of Jackson", "SAU 9" or "Fryeburg Academy (ME)"
PLACE_JOINS = """LEFT JOIN district pd ON pd.id = f.district_id_fk LEFT JOIN town pt ON pt.id = f.town_id_fk
    LEFT JOIN outside_school po ON po.id = f.outside_school_id_fk"""
PLACE_NAME = """COALESCE(pd.name, 'Town of ' || pt.name, 'SAU ' || f.sau_id_fk, po.name || ' (' || po.state || ')')"""
# A local topic's facts: those about no place, or about the district asked about and its related places
PLACE_FILTER = """(
    (f.district_id_fk IS NULL AND f.town_id_fk IS NULL AND f.sau_id_fk IS NULL AND f.outside_school_id_fk IS NULL)
    OR f.district_id_fk = ANY(CAST(:districts AS INTEGER[])) OR f.town_id_fk = ANY(CAST(:towns AS INTEGER[]))
    OR f.sau_id_fk = ANY(CAST(:saus AS INTEGER[])) OR f.outside_school_id_fk = ANY(CAST(:outside AS INTEGER[])))"""


def look_up_reference(session: Session, topics: List[str], district_id: Optional[int] = None, query: Optional[str] = None) -> dict:
    """The facts of up to four topics that are within their review date, ranked and capped, with their
    linked tables. A local topic gives the facts about no place and those about the district asked
    about and its related places (only those about no place, without a district); other topics give
    all their facts, the related places' first. Returns what Claude reads, and under "_sources" each
    fact's and table's link, which isn't sent to Claude."""
    if not isinstance(topics, list) or not all(isinstance(slug, str) for slug in topics):
        raise DataToolError("topics must be a list of topic names.")
    if district_id is not None and (isinstance(district_id, bool) or not isinstance(district_id, int)):
        raise DataToolError("district_id must be a district's id number from find_places, or null.")
    if query is not None and not isinstance(query, str):
        raise DataToolError("query must be a few words, or null.")
    query = (query or "").strip()[:MAX_QUERY] or None
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

    places = related_places(session, district) if district else {}
    params = {"topics": [t.id for t in found.values()], "q": query or ""}
    for kind, key in (("district", "districts"), ("town", "towns"), ("sau", "saus"), ("outside", "outside")):
        params[key] = [ident for (k, ident) in places if k == kind]
    rank = "ts_rank_cd(f.search, websearch_to_tsquery('english', :q))" if query else "0"
    facts = session.execute(text(f"""
        SELECT f.id, f.reference_topic_id_fk, f.statement, f.citation, f.source_url, f.as_of, f.as_of_text, f.review_by,
               f.district_id_fk, f.town_id_fk, f.sau_id_fk, f.outside_school_id_fk, {PLACE_NAME} AS place_name, {rank} AS rank
        FROM reference_fact f JOIN reference_topic t ON t.id = f.reference_topic_id_fk {PLACE_JOINS}
        WHERE f.reference_topic_id_fk = ANY(CAST(:topics AS INTEGER[])) AND (t.kind <> 'local' OR {PLACE_FILTER})
        ORDER BY f.id"""), params).all()
    tables = session.execute(text(f"""
        SELECT f.id, f.reference_topic_id_fk, f.title, f.unit, f.period, f.source_url, f.as_of, f.as_of_text, f.columns, f.rows,
               f.district_id_fk, f.town_id_fk, f.sau_id_fk, f.outside_school_id_fk, {PLACE_NAME} AS place_name
        FROM reference_table f JOIN reference_topic t ON t.id = f.reference_topic_id_fk {PLACE_JOINS}
        WHERE f.reference_topic_id_fk = ANY(CAST(:topics AS INTEGER[])) AND (t.kind <> 'local' OR {PLACE_FILTER})
        ORDER BY f.display_order"""), params).all()

    today = date.today()
    result, sources = {"topics": []}, {}
    for slug in slugs:
        topic = found[slug]
        entry = {"topic": slug, "title": topic.title, "kind": topic.kind, "facts": []}
        if topic.summary:
            entry["summary"] = topic.summary
        current, expired, seen = [], 0, set()
        for fact in (f for f in facts if f.reference_topic_id_fk == topic.id):
            if fact.review_by < today:
                expired += 1
                continue
            place = _place_of(fact)
            # Two towns' research may hold the same fact about a shared school
            same = (place, fact.source_url, " ".join(fact.statement.lower().split()))
            if same in seen:
                continue
            seen.add(same)
            closeness = places.get(place, ELSEWHERE) if place else NO_PLACE
            current.append((-(fact.rank > 0), -fact.rank, closeness, fact.id, fact, place))
        current.sort(key=lambda item: item[:4])
        for *_, fact, place in current[:MAX_FACTS]:
            fact_id = f"{FACT_PREFIX}{fact.id}"
            item = {"id": fact_id, "statement": fact.statement, "citation": fact.citation, "as_of": fact.as_of_text,
                    "site": site(fact.source_url)}
            if place:
                item["place"] = fact.place_name
            entry["facts"].append(item)
            if site(fact.source_url) != OWN_SITE:
                sources[fact_id] = {"label": _label(fact.citation, topic.title), "url": fact.source_url, "site": site(fact.source_url),
                                    "as_of": fact.as_of.isoformat() if fact.as_of else None}
        if len(current) > MAX_FACTS:
            entry["more_facts"] = (f"{len(current) - MAX_FACTS} more facts on this topic; call again with a query of a few words "
                                   f"to rank them by what the question asks")
        topic_tables = sorted((tb for tb in tables if tb.reference_topic_id_fk == topic.id),
                              key=lambda tb: places.get(_place_of(tb), ELSEWHERE) if _place_of(tb) else NO_PLACE)
        for tb in topic_tables[:MAX_TABLES]:
            table_id = f"{TABLE_PREFIX}{tb.id}"
            item = {"id": table_id, "title": tb.title, "unit": tb.unit, "period": tb.period, "columns": tb.columns,
                    "rows": tb.rows[:MAX_TABLE_ROWS]}
            if _place_of(tb):
                item["place"] = tb.place_name
            if len(tb.rows) > MAX_TABLE_ROWS:
                item["more_rows"] = len(tb.rows) - MAX_TABLE_ROWS
            entry.setdefault("tables", []).append(item)
            if tb.source_url and site(tb.source_url) != OWN_SITE:
                sources[table_id] = {"label": _label(None, tb.title), "url": tb.source_url, "site": site(tb.source_url),
                                     "as_of": tb.as_of.isoformat() if tb.as_of else None}
        if expired:
            # Shown in the server log so the facts get checked again
            entry["facts_withheld"] = f"{expired} facts are past their review date and aren't given"
        if topic.kind == "local" and district is None:
            entry["note"] = "This topic's facts are by district; call again with the district's id from find_places."
        elif topic.kind == "local" and not any(_place_of(fact) for *_, fact, _place in current):
            entry["note"] = f"The library has nothing on this for {district.name}; say so and suggest asking the district."
        result["topics"].append(entry)
    result["_sources"] = sources
    return result

