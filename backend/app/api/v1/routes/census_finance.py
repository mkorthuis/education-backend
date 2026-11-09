from typing import List, Optional

from fastapi import APIRouter, Query

from app.api.v1.deps import SessionDep
from app.core.cache import cache_response
from app.schema.census_finance_schema import (
    CensusRevenueGet, CensusRevenueItemGet, CensusRevenueSummaryGet, CensusStateEnrollmentGet,
)
from app.service.public.census_finance_service import census_finance_service

router = APIRouter()

YEAR = "Filter by fiscal year (2024 is July 2023 to June 2024 in most states)"
PLACE = "Filter by place code: a state (NH, MA, DC) or US for the nation"
DOLLARS = "Also give amounts in this year's dollars, adjusted by the consumer price index (the site's inflation table)"
CALCULATED = ("Shares and per-pupil amounts are calculated here, not published by Census: per-pupil revenue is revenue "
              "divided by the fall enrollment Census uses for its own per-pupil spending.")


@router.get("/revenue-item",
    response_model=List[CensusRevenueItemGet],
    summary="Get the Census revenue items",
    description="Each revenue item in the Census Bureau's school finance survey (Title I, property taxes, ...), with its source (federal, state or local) and the category Census's summary tables put it in")
@cache_response("census_finance_items")
def get_items(session: SessionDep):
    return census_finance_service.get_items(session=session)


@router.get("/enrollment",
    response_model=List[CensusStateEnrollmentGet],
    summary="Get the enrollment behind Census's per-pupil amounts",
    description="Each state's fall enrollment (NCES's count of students in its public school systems) as the Census Bureau uses it for per-pupil amounts, FY2010 on")
@cache_response("census_finance_enrollment")
def get_enrollment(
    session: SessionDep,
    year: Optional[int] = Query(default=None, description=YEAR),
    jurisdiction: Optional[str] = Query(default=None, description=PLACE),
):
    return census_finance_service.get_enrollment(session=session, year=year, jurisdiction=jurisdiction)


@router.get("/revenue",
    response_model=List[CensusRevenueGet],
    summary="Get school system revenue by state, source and item",
    description=(
        "Public elementary-secondary school system revenue by state, FY2010 on, from the Census Bureau's Annual Survey "
        "of School System Finances: grouped by source (federal, state, local), by category (Census's summary-table "
        "columns, such as Title I or property taxes) or by item. Each row has its share of its source and of all "
        f"revenue, and its amount per pupil. {CALCULATED} Shares are of the full totals, whatever is filtered."
    ),
    response_description="Rows by year, then place, then source, category and item")
@cache_response("census_finance_revenue")
def get_revenue(
    session: SessionDep,
    year: Optional[int] = Query(default=None, description=YEAR),
    jurisdiction: Optional[str] = Query(default=None, description=PLACE),
    source: Optional[str] = Query(default=None, pattern="^(federal|state|local)$", description="Filter by source: federal, state or local"),
    category: Optional[str] = Query(default=None, description="Filter by category, e.g. Title I or Property taxes"),
    level: str = Query(default="item", pattern="^(source|category|item)$", description="Group by source, category or item"),
    in_dollars_of: Optional[int] = Query(default=None, ge=2000, le=2100, description=DOLLARS),
):
    return census_finance_service.get_revenue(
        session=session, year=year, jurisdiction=jurisdiction, source=source, category=category, level=level,
        in_dollars_of=in_dollars_of,
    )


@router.get("/revenue/summary",
    response_model=List[CensusRevenueSummaryGet],
    summary="Get each state's revenue by source",
    description=f"For each place and fiscal year: total revenue and its federal, state and local parts, each with its share and amount per pupil. {CALCULATED}",
    response_description="One row per place and year, by year then place")
@cache_response("census_finance_summary")
def get_summary(
    session: SessionDep,
    year: Optional[int] = Query(default=None, description=YEAR),
    jurisdiction: Optional[str] = Query(default=None, description=PLACE),
    in_dollars_of: Optional[int] = Query(default=None, ge=2000, le=2100, description=DOLLARS),
):
    return census_finance_service.get_summary(session=session, year=year, jurisdiction=jurisdiction, in_dollars_of=in_dollars_of)
