import logging
from collections import defaultdict
from typing import List, Optional

from fastapi import HTTPException
from sqlalchemy import text
from sqlmodel import Session

from app.schema.property_tax_schema import PropertyTaxYearGet, TownPropertyTaxGet

logger = logging.getLogger(__name__)

DRA_NUMBERS = ("municipal_rate", "county_rate", "local_education_rate", "state_education_rate", "total_rate",
               "equalization_ratio", "full_value_tax_rate", "assessed_valuation", "assessed_valuation_with_utilities",
               "total_tax_commitment", "local_school_tax_effort", "state_education_tax_effort")
DOE_NUMBERS = ("assessed_valuation", "assessed_valuation_with_utilities", "equalized_valuation",
               "equalized_valuation_with_utilities", "local_education_tax", "other_local_tax", "state_education_tax",
               "rate_local_education", "rate_other_local", "rate_state_education", "rate_total",
               "equalized_rate_local_education", "equalized_rate_other_local", "equalized_rate_state_education",
               "equalized_rate_total")


def _number(value) -> Optional[float]:
    return None if value is None else float(value)


class PropertyTaxService:
    def get_years(self, session: Session, *, year: Optional[int] = None) -> List[PropertyTaxYearGet]:
        """Each tax year loaded, oldest first, with how many towns each publisher has"""
        try:
            params = {"year": year}
            # Each publisher's towns: DRA's have its rates, the DOE's its school tax dollars
            rows = session.execute(text("""
                SELECT tax_year, school_year, COUNT(local_education_rate) AS dra_towns, COUNT(local_education_tax) AS doe_towns
                FROM town_property_tax_summary
                WHERE CAST(:year AS INTEGER) IS NULL OR tax_year = :year
                GROUP BY tax_year, school_year ORDER BY tax_year
            """), params).mappings().all()
            return [PropertyTaxYearGet(**r) for r in rows]
        except Exception as e:
            logger.error(f"Error fetching property tax years: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch property tax years")

    def get_towns(self, session: Session, *, town_id: Optional[int] = None, district_id: Optional[int] = None,
                  year: Optional[int] = None) -> List[TownPropertyTaxGet]:
        """Each town's tax rates and school taxes per tax year, by year and then town: one town, a district's towns, or
        every town"""
        try:
            params = {"town_id": town_id, "district_id": district_id, "year": year}
            # The towns asked for: one, a district's (as the site links them), or all
            towns = """
                (CAST(:town_id AS INTEGER) IS NULL OR {t} = :town_id)
                AND (CAST(:district_id AS INTEGER) IS NULL
                     OR {t} IN (SELECT town_id_fk FROM town_district_xref WHERE district_id_fk = :district_id))
                AND (CAST(:year AS INTEGER) IS NULL OR {y} = :year)
            """
            rows = session.execute(text(f"""
                SELECT v.town_id_fk, t.name AS town_name, v.tax_year, v.school_year, v.district_id_fk, d.name AS district_name,
                       v.school_share_of_total_rate
                FROM town_property_tax_summary v
                JOIN town t ON t.id = v.town_id_fk
                LEFT JOIN district d ON d.id = v.district_id_fk
                WHERE {towns.format(t="v.town_id_fk", y="v.tax_year")}
                ORDER BY v.tax_year, t.name
            """), params).mappings().all()
            dra = {(r["town_id_fk"], r["tax_year"]): r for r in session.execute(text(f"""
                SELECT * FROM town_property_tax WHERE {towns.format(t="town_id_fk", y="tax_year")}
            """), params).mappings().all()}
            doe = {(r["town_id_fk"], r["tax_year"]): r for r in session.execute(text(f"""
                SELECT s.*, c.name AS cooperative_district_name FROM town_school_tax s
                LEFT JOIN district c ON c.id = s.cooperative_district_id_fk
                WHERE {towns.format(t="s.town_id_fk", y="s.tax_year")}
            """), params).mappings().all()}
            shares = defaultdict(list)
            if doe:
                for row in session.execute(text("""
                        SELECT c.town_school_tax_id_fk, c.district_id_fk, d.name, c.footnote, c.local_education_tax
                        FROM town_school_tax_coop_share c JOIN district d ON d.id = c.district_id_fk
                        WHERE c.town_school_tax_id_fk = ANY(:ids) ORDER BY d.name
                    """), {"ids": [r["id"] for r in doe.values()]}).mappings().all():
                    shares[row["town_school_tax_id_fk"]].append({
                        "district_id": row["district_id_fk"], "district_name": row["name"],
                        "footnote": row["footnote"], "local_education_tax": float(row["local_education_tax"])})

            def dra_part(r):
                return None if r is None else {"name": r["dra_name"], "date_rate_set": r["date_rate_set"], "note": r["note"],
                              **{k: _number(r[k]) for k in DRA_NUMBERS}}

            def doe_part(r):
                return None if r is None else {"cooperative_district_id": r["cooperative_district_id_fk"],
                              "cooperative_district_name": r["cooperative_district_name"], "note": r["note"],
                              "cooperative_shares": shares[r["id"]], **{k: float(r[k]) for k in DOE_NUMBERS}}

            return [TownPropertyTaxGet(
                town_id=r["town_id_fk"], town_name=r["town_name"], tax_year=r["tax_year"], school_year=r["school_year"],
                district_id=r["district_id_fk"], district_name=r["district_name"],
                school_share_of_total_rate=_number(r["school_share_of_total_rate"]),
                dra=dra_part(dra.get((r["town_id_fk"], r["tax_year"]))), doe=doe_part(doe.get((r["town_id_fk"], r["tax_year"]))),
            ) for r in rows]
        except Exception as e:
            logger.error(f"Error fetching town property taxes: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch town property taxes")


property_tax_service = PropertyTaxService()
