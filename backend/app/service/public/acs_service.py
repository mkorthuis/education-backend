import logging
import math
import re
from decimal import Decimal
from typing import List, Optional

from fastapi import HTTPException
from sqlalchemy import text
from sqlmodel import Session

from app.schema.acs_schema import (
    AcsMeasureGet, AcsReleaseGet, AcsTopicGet, AcsVariableGet, DistrictAcsSummaryGet, DistrictAcsTopicGet,
    StateAcsSummaryGet, StateAcsTopicGet, TownAcsSummaryGet, TownAcsTopicGet,
)

logger = logging.getLogger(__name__)

# Each level's place: its column in the views, its table, and its fields in the responses
LEVELS = {
    "town": {"key": "town_id_fk", "table": "town", "id": "town_id", "name": "town_name"},
    "district": {"key": "district_id_fk", "table": "district", "id": "district_id", "name": "district_name"},
    "state": None,
}
SUMMARY_SCHEMAS = {"town": TownAcsSummaryGet, "district": DistrictAcsSummaryGet, "state": StateAcsSummaryGet}
TOPIC_SCHEMAS = {"town": TownAcsTopicGet, "district": DistrictAcsTopicGet, "state": StateAcsTopicGet}
NAME = re.compile(r"^[a-z][a-z0-9_]*$")
OVERLAP = 5  # a 5-year release overlaps any other less than five years away

# The releases, topics, values and measures, read once per process: they change only when data is loaded
# (restart the web dynos after a load, as for the API cache)
_metadata = None


def _number(value):
    """A database number as an int when it's whole, else a float."""
    if value is None:
        return None
    value = float(value) if isinstance(value, Decimal) else value
    return int(value) if isinstance(value, float) and value.is_integer() else value


def _metadata_for(session: Session) -> dict:
    global _metadata
    if _metadata is not None:
        return _metadata
    releases = {year: {"year": year, "period": period, "dollars_year": dollars_year} for year, period, dollars_year in
                session.execute(text("SELECT year, period, dollars_year FROM acs_release ORDER BY year")).all()}
    topics = {code: {"code": code, "name": name, "tables": []} for code, name in
              session.execute(text("SELECT code, name FROM acs_topic ORDER BY id")).all()}
    for code, title, universe, tier, why, topic in session.execute(text(
            "SELECT t.code, t.title, t.universe, t.tier, t.why, tp.code FROM acs_table t "
            "JOIN acs_topic tp ON tp.id = t.topic_id_fk ORDER BY t.id")).all():
        topics[topic]["tables"].append({"code": code, "title": title, "universe": universe, "tier": tier, "why": why})
    available = {}
    for code, year, comparability in session.execute(text(
            "SELECT v.code, r.release_year, r.comparability FROM acs_variable_release r "
            "JOIN acs_variable v ON v.id = r.variable_id_fk ORDER BY r.release_year DESC")).all():
        available.setdefault(code, []).append({"year": year, "comparability": comparability})
    variables = [
        {"code": code, "column_name": column, "table": table, "table_title": title, "topic": topic, "tier": tier,
         "label": label, "description": description, "unit": unit, "releases": available.get(code, [])}
        for code, column, table, title, topic, tier, label, description, unit in session.execute(text(
            "SELECT v.code, v.column_name, t.code, t.title, tp.code, t.tier, v.label, v.description, v.unit "
            "FROM acs_variable v JOIN acs_table t ON t.id = v.table_id_fk JOIN acs_topic tp ON tp.id = t.topic_id_fk "
            "ORDER BY t.id, v.line")).all()]
    measures = [{"name": name, "label": label, "description": description, "unit": unit, "kind": kind, "formula": formula}
                for name, label, description, unit, kind, formula in session.execute(text(
                    "SELECT name, label, description, unit, kind, formula FROM acs_measure ORDER BY sort")).all()]
    if not all(NAME.match(v["column_name"]) for v in variables) or not all(NAME.match(m["name"]) for m in measures) \
            or not all(NAME.match(t) for t in topics):
        raise ValueError("An ACS column, measure or topic name isn't a plain lower-case name")
    _metadata = {"releases": releases, "topics": topics, "variables": variables, "measures": measures}
    return _metadata


def _years(meta: dict, release: Optional[int], compare_to: Optional[int] = None) -> tuple:
    """The releases to return, and the one to compare them with, or a 422 when they aren't releases or overlap."""
    known = list(meta["releases"])
    for value, name in ((release, "release"), (compare_to, "compare_to")):
        if value is not None and value not in meta["releases"]:
            raise HTTPException(status_code=422, detail=f"{name} {value} isn't a release: {known}")
    if compare_to is None:
        return ([release] if release else known), None
    release = release or known[-1]
    if abs(release - compare_to) < OVERLAP:
        raise HTTPException(status_code=422, detail=f"Releases {compare_to} and {release} cover overlapping years; "
                                                    f"Census advises against comparing them")
    return [release], compare_to


def _place_query(level: str, view: str, select: str, *, place_id=None, district_id=None, census_type=None) -> tuple:
    """SELECT ... FROM a level's view with its place's name, filtered, and its parameters."""
    place = LEVELS[level]
    if place is None:
        return f"SELECT {select} FROM {view} v WHERE v.release_year = ANY(:years) ORDER BY v.release_year", {}
    sql = f"SELECT {select}, p.name AS place_name"
    joins = f" FROM {view} v JOIN {place['table']} p ON p.id = v.{place['key']}"
    where, params = ["v.release_year = ANY(:years)"], {}
    if level == "district":
        sql += ", a.census_type"
        joins += " JOIN acs_district a ON a.district_id_fk = v.district_id_fk"
        if census_type:
            where.append("a.census_type = :census_type")
            params["census_type"] = census_type
    if place_id is not None:
        where.append(f"v.{place['key']} = :place_id")
        params["place_id"] = place_id
    if district_id is not None and level == "town":
        where.append("v.town_id_fk IN (SELECT town_id_fk FROM town_district_xref WHERE district_id_fk = :district_id)")
        params["district_id"] = district_id
    return f"{sql}{joins} WHERE {' AND '.join(where)} ORDER BY v.release_year, p.name", params


def _place_fields(level: str, row) -> tuple:
    """(the place's key, its fields in a response)."""
    place = LEVELS[level]
    if place is None:
        return None, {}
    fields = {place["id"]: row[place["key"]], place["name"]: row["place_name"]}
    if level == "district":
        fields["census_type"] = row["census_type"]
    return row[place["key"]], fields


def _comparison(value, moe, previous: dict, year: int) -> dict:
    change = None if value is None or previous["value"] is None else _number(round(value - previous["value"], 1))
    significant = None
    if change is not None and moe is not None and previous["moe"] is not None:
        significant = abs(change) > math.sqrt(moe ** 2 + previous["moe"] ** 2)
    return {"release_year": year, **previous, "change": change, "significant": significant}


class AcsService:
    def get_releases(self, session: Session) -> List[AcsReleaseGet]:
        return [AcsReleaseGet(**r) for r in _metadata_for(session)["releases"].values()]

    def get_topics(self, session: Session) -> List[AcsTopicGet]:
        return [AcsTopicGet(**t) for t in _metadata_for(session)["topics"].values()]

    def get_variables(self, session: Session, *, topic: Optional[str] = None, tier: Optional[str] = None,
                      table: Optional[str] = None) -> List[AcsVariableGet]:
        return [AcsVariableGet(**v) for v in _metadata_for(session)["variables"]
                if (topic is None or v["topic"] == topic) and (tier is None or v["tier"] == tier)
                and (table is None or v["table"] == table.upper())]

    def get_measures(self, session: Session) -> List[AcsMeasureGet]:
        return [AcsMeasureGet(**m) for m in _metadata_for(session)["measures"]]

    def get_summary(self, session: Session, level: str, *, release: Optional[int] = None, compare_to: Optional[int] = None,
                    place_id: Optional[int] = None, district_id: Optional[int] = None, census_type: Optional[str] = None) -> list:
        """Each place's summary measures for each release (or one, compared with an earlier one), by release and name"""
        try:
            meta = _metadata_for(session)
            years, compare_year = _years(meta, release, compare_to)
            sql, params = _place_query(level, f"{level}_acs_summary", "v.*", place_id=place_id, district_id=district_id,
                                       census_type=census_type)
            rows = session.execute(text(sql), {**params, "years": years}).mappings().all()
            previous = {}
            if compare_year:
                for row in session.execute(text(sql), {**params, "years": [compare_year]}).mappings().all():
                    previous[_place_fields(level, row)[0]] = row
            out = []
            for row in rows:
                key, fields = _place_fields(level, row)
                measures = {}
                for m in meta["measures"]:
                    value, moe = _number(row[m["name"]]), _number(row[f"{m['name']}_moe"])
                    measure = {"value": value, "moe": moe, "reliability": row[f"{m['name']}_reliability"]}
                    if compare_year and key in previous:
                        earlier = previous[key]
                        measure["compare"] = _comparison(value, moe, {
                            "value": _number(earlier[m["name"]]), "moe": _number(earlier[f"{m['name']}_moe"]),
                            "reliability": earlier[f"{m['name']}_reliability"]}, compare_year)
                    measures[m["name"]] = measure
                out.append(SUMMARY_SCHEMAS[level](**fields, release_year=row["release_year"],
                                                  period=meta["releases"][row["release_year"]]["period"], measures=measures))
            return out
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Error fetching {level} ACS summary: {e}")
            raise HTTPException(status_code=500, detail=f"Failed to fetch the {level} ACS summary")

    def get_topic(self, session: Session, level: str, topic: str, *, release: Optional[int] = None, tier: str = "core",
                  variables: Optional[str] = None, place_id: Optional[int] = None, district_id: Optional[int] = None,
                  census_type: Optional[str] = None) -> list:
        """Each place's values in a topic for each release: its core values, all of them, or those named"""
        try:
            meta = _metadata_for(session)
            if topic not in meta["topics"]:
                raise HTTPException(status_code=404, detail=f"No ACS topic {topic}: {list(meta['topics'])}")
            candidates = [v for v in meta["variables"] if v["topic"] == topic]
            if variables:
                names = [name.strip() for name in variables.split(",") if name.strip()]
                unknown = [name for name in names if name not in {v["column_name"] for v in candidates}]
                if unknown:
                    raise HTTPException(status_code=422, detail=f"{unknown} aren't values in topic {topic}; see /acs/variable")
            else:
                names = [v["column_name"] for v in candidates if tier == "all" or v["tier"] == "core"]
            years, _ = _years(meta, release)
            columns = ", ".join(f"v.{name}, v.{name}_moe" for name in names)
            key = [LEVELS[level]["key"]] if LEVELS[level] else []
            select = ", ".join([*(f"v.{k}" for k in key), "v.release_year", columns])
            sql, params = _place_query(level, f"{level}_acs_{topic}", select, place_id=place_id, district_id=district_id,
                                       census_type=census_type)
            out = []
            for row in session.execute(text(sql), {**params, "years": years}).mappings().all():
                _, fields = _place_fields(level, row)
                values = {name: {"estimate": _number(row[name]), "moe": _number(row[f"{name}_moe"])} for name in names}
                out.append(TOPIC_SCHEMAS[level](**fields, release_year=row["release_year"],
                                                period=meta["releases"][row["release_year"]]["period"], values=values))
            return out
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Error fetching {level} ACS {topic}: {e}")
            raise HTTPException(status_code=500, detail=f"Failed to fetch the {level} ACS {topic} values")


acs_service = AcsService()
