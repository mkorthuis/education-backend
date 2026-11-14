from typing import List, Optional

from fastapi import APIRouter, Query

from app.api.v1.deps import SessionDep
from app.core.cache import cache_response
from app.schema.adequacy_aid_schema import (
    AdequacyAidFormulaGet, AdequacyAidYearGet, DistrictAdequacyAidCalculationGet, DistrictAdequacyAidGet,
    StateAdequacyAidGet, TownAdequacyAidCalculationGet, TownAdequacyAidGet,
)
from app.service.public.adequacy_aid_service import adequacy_aid_service

# Mounted at /finance/adequacy-aid
router = APIRouter()

YEAR = Query(default=None, description="Only this fiscal year (2027: 2026-27, as the financial report's year); every year by default")
ABOUT = (
    " NH DOE's adequate education grants (RSA 198:40-a to 198:42). Every year is returned by default, each with its "
    "status: final, or estimate before the DOE's April final calculation."
)
CALCULATION = (
    " Each step has the DOE's published figure; a step with a formula also lists its inputs, the town's values and the "
    "year's rates, so the arithmetic can be shown (resident students x base rate = base aid). A step without a "
    "formula is explained only. values has every part the DOE published for the town and year."
)


@router.get("/years", response_model=List[AdequacyAidYearGet], summary="Get the adequacy aid years",
            description="Each fiscal year loaded, its status, and links to the DOE's workbook, split and explanation." + ABOUT)
@cache_response("adequacy_aid_years")
def get_adequacy_aid_years(session: SessionDep):
    return adequacy_aid_service.get_years(session=session)


@router.get("/formula", response_model=AdequacyAidFormulaGet, summary="Get how a year's adequacy aid is calculated",
            description="A year's rates, thresholds and shares, with their citations, and the steps of its calculation in "
                        "order: the part each produces, its formula and a plain-English explanation.")
@cache_response("adequacy_aid_formula")
def get_adequacy_aid_formula(session: SessionDep, year: int = Query(..., description="Fiscal year")):
    return adequacy_aid_service.get_formula(session=session, year=year)


@router.get("/district", response_model=List[DistrictAdequacyAidGet], summary="Get districts' adequacy aid",
            description="Each school district's adequacy grant, SWEPT kept and total state aid per year, from all its member "
                        "towns, beside the adequacy aid it reported in its financial report and the difference." + ABOUT)
@cache_response("adequacy_aid_district")
def get_district_adequacy_aid(
    session: SessionDep,
    district_id: Optional[int] = Query(default=None, description="Filter by district ID"),
    year: Optional[int] = YEAR,
):
    return adequacy_aid_service.get_districts(session=session, district_id=district_id, year=year)


@router.get("/district/{district_id}/calculation", response_model=List[DistrictAdequacyAidCalculationGet],
            summary="Get a district's adequacy aid calculation",
            description="A district's adequacy aid per year, with each member town's share (the DOE's split for towns in more "
                        "than one district; the whole town otherwise) and that town's calculation." + CALCULATION + ABOUT)
@cache_response("adequacy_aid_district_calculation")
def get_district_adequacy_aid_calculation(district_id: int, session: SessionDep, year: Optional[int] = YEAR):
    return adequacy_aid_service.get_district_calculation(session=session, district_id=district_id, year=year)


@router.get("/town", response_model=List[TownAdequacyAidGet], summary="Get towns' adequacy aid",
            description="Each town's calculation as columns per year: students and aid by group, cost, SWEPT, added aid, "
                        "hold-harmless, the grant, total state aid and SWEPT above cost." + ABOUT)
@cache_response("adequacy_aid_town")
def get_town_adequacy_aid(
    session: SessionDep,
    town_id: Optional[int] = Query(default=None, description="Filter by town ID"),
    district_id: Optional[int] = Query(default=None, description="Only the towns whose aid goes to this district"),
    year: Optional[int] = YEAR,
):
    return adequacy_aid_service.get_towns(session=session, town_id=town_id, district_id=district_id, year=year)


@router.get("/town/{town_id}/calculation", response_model=List[TownAdequacyAidCalculationGet],
            summary="Get a town's adequacy aid calculation",
            description="A town's adequacy aid per year, with the districts its grant and SWEPT go to." + CALCULATION + ABOUT)
@cache_response("adequacy_aid_town_calculation")
def get_town_adequacy_aid_calculation(town_id: int, session: SessionDep, year: Optional[int] = YEAR):
    return adequacy_aid_service.get_town_calculation(session=session, town_id=town_id, year=year)


@router.get("/state", response_model=List[StateAdequacyAidGet], summary="Get statewide adequacy aid",
            description="The DOE's statewide totals per year, for every part of the calculation." + ABOUT)
@cache_response("adequacy_aid_state")
def get_state_adequacy_aid(session: SessionDep, year: Optional[int] = YEAR):
    return adequacy_aid_service.get_state(session=session, year=year)
