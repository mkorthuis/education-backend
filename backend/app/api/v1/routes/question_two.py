from typing import List, Optional

from fastapi import APIRouter, Query

from app.api.v1.deps import SessionDep
from app.core.cache import cache_response
from app.schema.question_two_schema import DistrictQuestionTwoGet, SauQuestionTwoGet, TownQuestionTwoGet
from app.service.public.question_two_service import question_two_service

router = APIRouter()


@router.get(
    "/district",
    response_model=List[DistrictQuestionTwoGet],
    summary="Get each district's Question 2 result",
    description=(
        "Ballot Question 2 (HB 1300, 2026 chapter 324) by school district: the yes and no votes, the yes "
        "percentage, and whether the district adopted the school tax cap (60% yes or more). The SAU "
        "central-office cap is decided by the vote across the SAU's towns (see /sau). is_official is false until the "
        "results are certified."
    ),
    response_description="Question 2 results by district",
)
@cache_response("question_two_district")
def get_district_question_two(
    session: SessionDep,
    year: Optional[int] = Query(default=None, description="Filter by election year (2026, 2028)"),
    district_id: Optional[int] = Query(default=None, description="Filter by district ID"),
    passed: Optional[bool] = Query(default=None, description="Only districts that adopted (true) or didn't adopt (false) the school tax cap"),
):
    return question_two_service.get_district_results(
        session=session,
        year=year,
        district_id=district_id,
        passed=passed,
    )


@router.get(
    "/sau",
    response_model=List[SauQuestionTwoGet],
    summary="Get each SAU's Question 2 result",
    description=(
        "Ballot Question 2 by SAU: the yes and no votes across the SAU's towns, the yes percentage, and "
        "whether the SAU adopted the 6% cap on central-office spending (60% yes or more), with the SAU's "
        "school districts that voted. note says where the source's listing leaves a town out or puts one "
        "in the wrong SAU. is_official is false until the results are certified."
    ),
    response_description="Question 2 results by SAU",
)
@cache_response("question_two_sau")
def get_sau_question_two(
    session: SessionDep,
    year: Optional[int] = Query(default=None, description="Filter by election year (2026, 2028)"),
    sau_id: Optional[int] = Query(default=None, description="Filter by SAU number"),
    passed: Optional[bool] = Query(default=None, description="Only SAUs that adopted (true) or didn't adopt (false) the spending cap"),
):
    return question_two_service.get_sau_results(session=session, year=year, sau_id=sau_id, passed=passed)


@router.get(
    "/town",
    response_model=List[TownQuestionTwoGet],
    summary="Get each town's Question 2 vote",
    description=(
        "Ballot Question 2 by town: each town's own yes and no votes and yes percentage. A town's vote "
        "decides neither cap on its own; its school districts' and SAU's totals do."
    ),
    response_description="Question 2 votes by town",
)
@cache_response("question_two_town")
def get_town_question_two(
    session: SessionDep,
    year: Optional[int] = Query(default=None, description="Filter by election year (2026, 2028)"),
    town_id: Optional[int] = Query(default=None, description="Filter by town ID"),
    district_id: Optional[int] = Query(default=None, description="Only the towns of this school district"),
):
    return question_two_service.get_town_results(session=session, year=year, town_id=town_id, district_id=district_id)
