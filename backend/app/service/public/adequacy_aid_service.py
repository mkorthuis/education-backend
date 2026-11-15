import logging
from collections import defaultdict
from typing import List, Optional

from fastapi import HTTPException
from sqlalchemy import text
from sqlmodel import Session

from app.etl.formula import names
from app.schema.adequacy_aid_schema import (
    AdequacyAidFormulaGet, AdequacyAidYearGet, DistrictAdequacyAidCalculationGet, DistrictAdequacyAidGet,
    StateAdequacyAidGet, TownAdequacyAidCalculationGet, TownAdequacyAidGet,
)

logger = logging.getLogger(__name__)

SUMMARY_COLUMNS = ("resident_adm", "base_aid", "frl_adm", "frl_aid", "sped_adm", "sped_aid", "ell_adm", "ell_aid",
                   "home_education_adm", "home_education_aid", "grade3_reading_adm", "grade3_reading_aid", "total_cost", "swept",
                   "equalized_valuation", "extraordinary_need_grant", "fiscal_capacity_disparity_aid", "other_added_aid",
                   "preliminary_grant", "hold_harmless", "adequacy_grant", "total_state_aid", "swept_above_cost")


def _number(value) -> Optional[float]:
    return None if value is None else float(value)


def _years(session: Session) -> dict:
    return {row["fiscal_year"]: dict(row) for row in session.execute(text(
        "SELECT fiscal_year, school_year, status, as_of, summary_url, split_url, explained_url FROM adequacy_aid_year "
        "ORDER BY fiscal_year")).mappings().all()}


def _year_fields(years: dict, year: int) -> dict:
    y = years[year]
    return {"fiscal_year": year, "school_year": y["school_year"], "status": y["status"], "as_of": y["as_of"]}


def _year_filter(year: Optional[int]) -> tuple:
    return ("", {}) if year is None else (" AND {}.fiscal_year = :year", {"year": year})


def _parameters(session: Session, years: List[int]) -> dict:
    found = defaultdict(dict)
    for year, code, value in session.execute(text(
            "SELECT fiscal_year, code, value FROM adequacy_aid_parameter WHERE fiscal_year = ANY(:years)"), {"years": years}).all():
        found[year][code] = float(value)
    return found


def _steps(session: Session, years: List[int]) -> dict:
    found = defaultdict(list)
    for row in session.execute(text("""
            SELECT s.fiscal_year, s.step, c.code, c.name, c.description, c.unit, c.role, s.formula, s.tolerance, s.explanation, s.citation
            FROM adequacy_aid_step s JOIN adequacy_aid_component c ON c.id = s.component_id_fk
            WHERE s.fiscal_year = ANY(:years) ORDER BY s.fiscal_year, s.step
        """), {"years": years}).mappings().all():
        found[row["fiscal_year"]].append(dict(row))
    return found


def _town_values(session: Session, towns: List[int], years: List[int]) -> dict:
    found = defaultdict(dict)
    for town, year, code, value in session.execute(text("""
            SELECT a.town_id_fk, a.fiscal_year, c.code, a.value
            FROM town_adequacy_aid a JOIN adequacy_aid_component c ON c.id = a.component_id_fk
            WHERE a.town_id_fk = ANY(:towns) AND a.fiscal_year = ANY(:years)
        """), {"towns": towns, "years": years}).all():
        found[(town, year)][code] = float(value)
    return found


def _lines(steps: List[dict], values: dict, parameters: dict) -> List[dict]:
    """A town's steps with its values: each step's published figure and, for a formula, what goes into it. A part the
    DOE left blank for the town counts as 0, as the load's checks count it."""
    lines = []
    for s in steps:
        inputs = {}
        if s["formula"]:
            for name in sorted(names(s["formula"])):
                inputs[name] = parameters[name] if name in parameters else values.get(name, 0.0)
        lines.append({"step": s["step"], "code": s["code"], "name": s["name"], "unit": s["unit"], "role": s["role"],
                      "value": values.get(s["code"], 0.0), "formula": s["formula"], "inputs": inputs,
                      "explanation": s["explanation"], "citation": s["citation"]})
    return lines


def _share_of_town(grant, swept, town_grant, town_swept) -> Optional[float]:
    total = float(town_grant or 0) + float(town_swept or 0)
    return None if total == 0 else round((float(grant) + float(swept)) / total, 4)


class AdequacyAidService:
    def get_years(self, session: Session) -> List[AdequacyAidYearGet]:
        return [AdequacyAidYearGet(**y) for y in _years(session).values()]

    def get_formula(self, session: Session, year: int) -> AdequacyAidFormulaGet:
        try:
            years = _years(session)
            if year not in years:
                raise HTTPException(status_code=404, detail=f"No adequacy aid for fiscal year {year}: {list(years)}")
            parameters = [dict(r) for r in session.execute(text(
                "SELECT code, name, value, unit, citation, source_url FROM adequacy_aid_parameter WHERE fiscal_year = :year ORDER BY id"),
                {"year": year}).mappings().all()]
            steps = [{**s, "uses": sorted(names(s["formula"])) if s["formula"] else [], "tolerance": float(s["tolerance"])}
                     for s in _steps(session, [year])[year]]
            # The parts a page needs to name each figure and formula input: what the DOE published for the year's towns,
            # each step's part, and the parts the formulas use
            uses = sorted({name for s in steps for name in s["uses"]} - {p["code"] for p in parameters})
            components = [dict(r) for r in session.execute(text("""
                    SELECT code, name, description, unit, role FROM adequacy_aid_component
                    WHERE id IN (SELECT DISTINCT component_id_fk FROM town_adequacy_aid WHERE fiscal_year = :year)
                       OR id IN (SELECT component_id_fk FROM adequacy_aid_step WHERE fiscal_year = :year)
                       OR code = ANY(:uses)
                    ORDER BY sort, code
                """), {"year": year, "uses": uses}).mappings().all()]
            return AdequacyAidFormulaGet(year=years[year], parameters=[{**p, "value": float(p["value"])} for p in parameters],
                                         steps=steps, components=components)
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Error fetching the FY{year} adequacy aid formula: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch the adequacy aid formula")

    def _districts(self, session: Session, district_id: Optional[int], year: Optional[int]) -> list:
        years = _years(session)
        where, params = _year_filter(year)
        if district_id is not None:
            where += " AND a.district_id_fk = :district_id"
            params["district_id"] = district_id
        rows = session.execute(text(f"""
            SELECT a.*, d.name AS district_name FROM district_adequacy_aid a JOIN district d ON d.id = a.district_id_fk
            WHERE TRUE{where.format('a')} ORDER BY a.fiscal_year, d.name
        """), params).mappings().all()
        return [{"district_id": r["district_id_fk"], "district_name": r["district_name"], **_year_fields(years, r["fiscal_year"]),
                 "adequacy_grant": float(r["adequacy_grant"]), "swept_retained": float(r["swept_retained"]),
                 "total_state_aid": float(r["total_state_aid"]), "member_towns": r["member_towns"],
                 "reported_adequacy_grant": _number(r["reported_adequacy_grant"]), "reported_difference": _number(r["reported_difference"])}
                for r in rows]

    def get_districts(self, session: Session, *, district_id: Optional[int] = None, year: Optional[int] = None) -> List[DistrictAdequacyAidGet]:
        """Each district's totals per year, by year and then name"""
        try:
            return [DistrictAdequacyAidGet(**d) for d in self._districts(session, district_id, year)]
        except Exception as e:
            logger.error(f"Error fetching district adequacy aid: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch district adequacy aid")

    def get_district_calculation(self, session: Session, district_id: int, year: Optional[int] = None) -> List[DistrictAdequacyAidCalculationGet]:
        """A district's totals per year, with each member town's share and calculation"""
        try:
            districts = self._districts(session, district_id, year)
            if not districts:
                raise HTTPException(status_code=404, detail=f"No adequacy aid for district {district_id}" + (f" in FY{year}" if year else ""))
            years = sorted({d["fiscal_year"] for d in districts})
            shares = session.execute(text("""
                SELECT s.fiscal_year, s.town_id_fk, t.name AS town_name, s.adequacy_grant, s.swept_retained, s.source,
                       m.adequacy_grant AS town_grant, m.swept AS town_swept, m.total_state_aid AS town_total
                FROM district_adequacy_aid_share s
                JOIN town t ON t.id = s.town_id_fk
                JOIN town_adequacy_aid_summary m ON m.town_id_fk = s.town_id_fk AND m.fiscal_year = s.fiscal_year
                WHERE s.district_id_fk = :district_id AND s.fiscal_year = ANY(:years)
                ORDER BY s.fiscal_year, t.name
            """), {"district_id": district_id, "years": years}).mappings().all()
            values = _town_values(session, sorted({s["town_id_fk"] for s in shares}), years)
            steps, parameters = _steps(session, years), _parameters(session, years)
            towns = defaultdict(list)
            for s in shares:
                key = (s["town_id_fk"], s["fiscal_year"])
                towns[s["fiscal_year"]].append({
                    "town_id": s["town_id_fk"], "town_name": s["town_name"],
                    "share": {"adequacy_grant": float(s["adequacy_grant"]), "swept_retained": float(s["swept_retained"]), "source": s["source"],
                              "share_of_town": _share_of_town(s["adequacy_grant"], s["swept_retained"], s["town_grant"], s["town_swept"])},
                    "town_totals": {"adequacy_grant": float(s["town_grant"] or 0), "swept": float(s["town_swept"] or 0),
                                    "total_state_aid": float(s["town_total"] or 0)},
                    "steps": _lines(steps[s["fiscal_year"]], values[key], parameters[s["fiscal_year"]]),
                    "values": values[key],
                })
            return [DistrictAdequacyAidCalculationGet(**d, towns=towns[d["fiscal_year"]]) for d in districts]
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Error fetching district {district_id}'s adequacy aid calculation: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch the district's adequacy aid calculation")

    def get_towns(self, session: Session, *, town_id: Optional[int] = None, district_id: Optional[int] = None,
                  year: Optional[int] = None) -> List[TownAdequacyAidGet]:
        """Each town's calculation as columns per year, by year and then name; district_id gives the towns whose aid
        goes to that district"""
        try:
            years = _years(session)
            where, params = _year_filter(year)
            where = where.format("m")
            if town_id is not None:
                where += " AND m.town_id_fk = :town_id"
                params["town_id"] = town_id
            if district_id is not None:
                where += (" AND EXISTS (SELECT 1 FROM district_adequacy_aid_share s WHERE s.town_id_fk = m.town_id_fk "
                          "AND s.fiscal_year = m.fiscal_year AND s.district_id_fk = :district_id)")
                params["district_id"] = district_id
            rows = session.execute(text(f"""
                SELECT m.*, t.name AS town_name FROM town_adequacy_aid_summary m JOIN town t ON t.id = m.town_id_fk
                WHERE TRUE{where} ORDER BY m.fiscal_year, t.name
            """), params).mappings().all()
            return [TownAdequacyAidGet(town_id=r["town_id_fk"], town_name=r["town_name"], **_year_fields(years, r["fiscal_year"]),
                                       **{c: _number(r[c]) for c in SUMMARY_COLUMNS}) for r in rows]
        except Exception as e:
            logger.error(f"Error fetching town adequacy aid: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch town adequacy aid")

    def get_town_calculation(self, session: Session, town_id: int, year: Optional[int] = None) -> List[TownAdequacyAidCalculationGet]:
        """A town's calculation per year, with the districts its grant and SWEPT go to"""
        try:
            years = _years(session)
            where, params = _year_filter(year)
            totals = session.execute(text(f"""
                SELECT m.fiscal_year, m.adequacy_grant, m.swept, m.total_state_aid, t.name AS town_name
                FROM town_adequacy_aid_summary m JOIN town t ON t.id = m.town_id_fk
                WHERE m.town_id_fk = :town_id{where.format('m')} ORDER BY m.fiscal_year
            """), {"town_id": town_id, **params}).mappings().all()
            if not totals:
                raise HTTPException(status_code=404, detail=f"No adequacy aid for town {town_id}" + (f" in FY{year}" if year else ""))
            loaded = [t["fiscal_year"] for t in totals]
            shares = defaultdict(list)
            for s in session.execute(text("""
                    SELECT s.fiscal_year, s.district_id_fk, d.name AS district_name, s.adequacy_grant, s.swept_retained, s.source
                    FROM district_adequacy_aid_share s JOIN district d ON d.id = s.district_id_fk
                    WHERE s.town_id_fk = :town_id AND s.fiscal_year = ANY(:years) ORDER BY s.fiscal_year, d.name
                """), {"town_id": town_id, "years": loaded}).mappings().all():
                shares[s["fiscal_year"]].append(s)
            values = _town_values(session, [town_id], loaded)
            steps, parameters = _steps(session, loaded), _parameters(session, loaded)
            out = []
            for t in totals:
                y = t["fiscal_year"]
                out.append(TownAdequacyAidCalculationGet(
                    town_id=town_id, town_name=t["town_name"], **_year_fields(years, y),
                    totals={"adequacy_grant": float(t["adequacy_grant"] or 0), "swept": float(t["swept"] or 0),
                            "total_state_aid": float(t["total_state_aid"] or 0)},
                    districts=[{"district_id": s["district_id_fk"], "district_name": s["district_name"],
                                "adequacy_grant": float(s["adequacy_grant"]), "swept_retained": float(s["swept_retained"]), "source": s["source"],
                                "share_of_town": _share_of_town(s["adequacy_grant"], s["swept_retained"], t["adequacy_grant"], t["swept"])}
                               for s in shares[y]],
                    steps=_lines(steps[y], values[(town_id, y)], parameters[y]),
                    values=values[(town_id, y)]))
            return out
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Error fetching town {town_id}'s adequacy aid calculation: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch the town's adequacy aid calculation")

    def get_state(self, session: Session, *, year: Optional[int] = None) -> List[StateAdequacyAidGet]:
        """The DOE's statewide totals per year"""
        try:
            years = _years(session)
            where, params = _year_filter(year)
            found = defaultdict(dict)
            for y, code, value in session.execute(text(f"""
                    SELECT s.fiscal_year, c.code, s.value FROM state_adequacy_aid s JOIN adequacy_aid_component c ON c.id = s.component_id_fk
                    WHERE TRUE{where.format('s')}
                """), params).all():
                found[y][code] = float(value)
            out = []
            for y in sorted(found):
                v = found[y]
                total = v.get("final_total_state_grant")
                if total is None and "adequacy_grant" in v and "swept" in v:
                    total = v["adequacy_grant"] + v["swept"]
                out.append(StateAdequacyAidGet(**_year_fields(years, y), adequacy_grant=v.get("adequacy_grant"), swept=v.get("swept"),
                                               total_state_aid=total, values=v))
            return out
        except Exception as e:
            logger.error(f"Error fetching state adequacy aid: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch state adequacy aid")


adequacy_aid_service = AdequacyAidService()
