from typing import List, Optional

from fastapi import APIRouter, Query

from app.api.v1.deps import SessionDep
from app.core.cache import cache_response
from app.schema.property_tax_schema import PropertyTaxYearGet, TownPropertyTaxGet
from app.service.public.property_tax_service import property_tax_service

# Mounted at /finance/property-tax
router = APIRouter()

YEAR = Query(default=None, description="Only this tax year (set in the fall: 2025 pays for 2025-26); every year by default")
ABOUT = (
    " Two state publishers, each as published: NH DRA's tax rates per $1,000 of assessed value (municipal, county, local "
    "education, state education and total; tax years 2014-2025, with the full value rate and school tax dollars from 2018), "
    "and NH DOE's valuations report of each town's school tax dollars, valuations and rates (tax years 2011-2025)."
)


@router.get("/years", response_model=List[PropertyTaxYearGet], summary="Get the property tax years",
            description="Each tax year loaded: the school year it pays for and how many towns each publisher has." + ABOUT)
@cache_response("property_tax_years")
def get_property_tax_years(session: SessionDep, year: Optional[int] = YEAR):
    return property_tax_service.get_years(session=session, year=year)


@router.get("/town", response_model=List[TownPropertyTaxGet], summary="Get towns' property tax rates and school taxes",
            description="Each town's tax rates and school taxes per tax year, with the school share of its total rate and "
                        "the part of its local school tax that goes to a cooperative." + ABOUT)
@cache_response("property_tax_town")
def get_town_property_tax(
    session: SessionDep,
    town_id: Optional[int] = Query(default=None, description="Filter by town ID"),
    year: Optional[int] = YEAR,
):
    return property_tax_service.get_towns(session=session, town_id=town_id, year=year)


@router.get("/district", response_model=List[TownPropertyTaxGet], summary="Get a district's towns' property tax rates and school taxes",
            description="The property tax rates and school taxes of each town in a school district, per tax year." + ABOUT)
@cache_response("property_tax_district")
def get_district_property_tax(
    session: SessionDep,
    district_id: int = Query(description="The district's ID"),
    year: Optional[int] = YEAR,
):
    return property_tax_service.get_towns(session=session, district_id=district_id, year=year)
