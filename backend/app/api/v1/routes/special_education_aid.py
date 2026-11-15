from typing import List, Optional

from fastapi import APIRouter, Query

from app.api.v1.deps import SessionDep
from app.core.cache import cache_response
from app.schema.special_education_aid_schema import DistrictSpecialEducationAidGet, SpecialEducationAidYearGet
from app.service.public.special_education_aid_service import special_education_aid_service

# Mounted at /finance/special-education-aid
router = APIRouter()

YEAR = Query(default=None, description="Only this fiscal year (2026: paid in 2025-26 on 2024-25 costs, as the financial "
                                       "report's year); every year by default")
ABOUT = (
    " NH DOE's special education aid (catastrophic aid until 2017; RSA 186-C:18, III): a district pays each high-cost "
    "student's costs up to a threshold, a multiple of the state average cost per pupil, and the state pays a share of the "
    "costs in each band above it, prorated when the appropriation falls short. The DOE gives no student counts by district."
)


@router.get("/years", response_model=List[SpecialEducationAidYearGet], summary="Get the special education aid years",
            description="Each fiscal year loaded: the costs it reimburses, the state average cost per pupil and the threshold, "
                        "the appropriation and proration, the DOE's statewide totals, and the formula's bands with the state's "
                        "share of each." + ABOUT)
@cache_response("special_education_aid_years")
def get_special_education_aid_years(session: SessionDep, year: Optional[int] = YEAR):
    return special_education_aid_service.get_years(session=session, year=year)


@router.get("/district", response_model=List[DistrictSpecialEducationAidGet], summary="Get districts' special education aid",
            description="Each school district's costs for its high-cost special education students per year: its total cost, "
                        "what it pays in full and what the state shares, by band; its entitlement and the aid paid; and the "
                        "special education aid it reported in its financial report, with the difference." + ABOUT)
@cache_response("special_education_aid_district")
def get_district_special_education_aid(
    session: SessionDep,
    district_id: Optional[int] = Query(default=None, description="Filter by district ID"),
    year: Optional[int] = YEAR,
):
    return special_education_aid_service.get_districts(session=session, district_id=district_id, year=year)
