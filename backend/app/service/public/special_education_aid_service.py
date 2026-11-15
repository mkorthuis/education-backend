import logging
from collections import defaultdict
from typing import List, Optional

from fastapi import HTTPException
from sqlalchemy import text
from sqlmodel import Session

from app.schema.special_education_aid_schema import DistrictSpecialEducationAidGet, SpecialEducationAidYearGet

logger = logging.getLogger(__name__)


def _number(value) -> Optional[float]:
    return None if value is None else float(value)


def _bands(session: Session, years: List[int]) -> dict:
    """{fiscal year: [its bands, lowest first]}"""
    found = defaultdict(list)
    for row in session.execute(text("""
            SELECT fiscal_year, band, label, from_multiple, to_multiple, state_share, citation, source_url
            FROM special_education_aid_band WHERE fiscal_year = ANY(:years) ORDER BY fiscal_year, band
        """), {"years": years}).mappings().all():
        found[row["fiscal_year"]].append({**row, "from_multiple": float(row["from_multiple"]),
                                          "to_multiple": _number(row["to_multiple"]), "state_share": float(row["state_share"])})
    return found


class SpecialEducationAidService:
    def get_years(self, session: Session, *, year: Optional[int] = None) -> List[SpecialEducationAidYearGet]:
        """Each fiscal year of aid, oldest first: its threshold, appropriation and proration, the DOE's statewide totals
        and its formula's bands"""
        try:
            rows = session.execute(text("""
                SELECT y.*, (SELECT COUNT(*) FROM district_special_education_aid a WHERE a.fiscal_year = y.fiscal_year) AS districts
                FROM special_education_aid_year y
                WHERE CAST(:year AS INTEGER) IS NULL OR y.fiscal_year = :year ORDER BY y.fiscal_year
            """), {"year": year}).mappings().all()
            bands = _bands(session, [r["fiscal_year"] for r in rows])
            return [SpecialEducationAidYearGet(
                fiscal_year=r["fiscal_year"], cost_school_year=r["cost_school_year"], status=r["status"], as_of=r["as_of"],
                state_average_cost=float(r["state_average_cost"]), threshold_cost=float(r["threshold_cost"]),
                appropriation=_number(r["appropriation"]), proration_rate=float(r["proration_rate"]),
                minimum_share=_number(r["minimum_share"]), students_reported=_number(r["state_students_reported"]),
                students_highest_band=_number(r["state_students_highest_band"]), total_cost=float(r["state_total_cost"]),
                entitlement=float(r["state_entitlement"]), aid_paid=float(r["state_aid_paid"]), districts=r["districts"],
                note=r["note"], source_url=r["source_url"], page_url=r["page_url"], bands=bands[r["fiscal_year"]],
            ) for r in rows]
        except Exception as e:
            logger.error(f"Error fetching special education aid years: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch special education aid years")

    def get_districts(self, session: Session, *, district_id: Optional[int] = None,
                      year: Optional[int] = None) -> List[DistrictSpecialEducationAidGet]:
        """Each district's costs, entitlement and aid per year, beside what it reported, by year and then name"""
        try:
            params = {"district_id": district_id, "year": year}
            rows = session.execute(text("""
                SELECT s.*, d.name AS district_name, a.id AS aid_id, a.source_name
                FROM district_special_education_aid_summary s
                JOIN district d ON d.id = s.district_id_fk
                JOIN district_special_education_aid a ON a.district_id_fk = s.district_id_fk AND a.fiscal_year = s.fiscal_year
                WHERE (CAST(:district_id AS INTEGER) IS NULL OR s.district_id_fk = :district_id)
                  AND (CAST(:year AS INTEGER) IS NULL OR s.fiscal_year = :year)
                ORDER BY s.fiscal_year, d.name
            """), params).mappings().all()
            bands = defaultdict(list)
            if rows:
                for row in session.execute(text("""
                        SELECT b.district_special_education_aid_id_fk AS aid_id, b.band, y.label, y.state_share, b.cost, b.students
                        FROM district_special_education_aid_band b
                        JOIN district_special_education_aid a ON a.id = b.district_special_education_aid_id_fk
                        JOIN special_education_aid_band y ON y.fiscal_year = a.fiscal_year AND y.band = b.band
                        WHERE b.district_special_education_aid_id_fk = ANY(:ids) ORDER BY b.band
                    """), {"ids": [r["aid_id"] for r in rows]}).mappings().all():
                    bands[row["aid_id"]].append({"band": row["band"], "label": row["label"], "state_share": float(row["state_share"]),
                                                 "cost": float(row["cost"]), "students": _number(row["students"])})
            return [DistrictSpecialEducationAidGet(
                district_id=r["district_id_fk"], district_name=r["district_name"], fiscal_year=r["fiscal_year"],
                cost_school_year=r["cost_school_year"], total_cost=float(r["total_cost"]),
                cost_below_threshold=float(r["cost_below_threshold"] or 0), cost_above_threshold=float(r["cost_above_threshold"] or 0),
                cost_over_10_times=float(r["cost_over_10_times"] or 0), entitlement=float(r["entitlement"]),
                aid_paid=float(r["aid_paid"]), share_of_cost_paid=_number(r["share_of_cost_paid"]),
                reported_aid=_number(r["reported_aid"]), reported_difference=_number(r["reported_difference"]),
                source_name=r["source_name"], bands=bands[r["aid_id"]],
            ) for r in rows]
        except Exception as e:
            logger.error(f"Error fetching district special education aid: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch district special education aid")


special_education_aid_service = SpecialEducationAidService()
