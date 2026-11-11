from typing import List, Optional

from fastapi import APIRouter, Query

from app.api.v1.deps import SessionDep
from app.core.cache import cache_response
from app.schema.question_two_schema import DistrictQuestionTwoGet
from app.service.public.question_two_service import question_two_service

router = APIRouter()


@router.get(
    "/district",
    response_model=List[DistrictQuestionTwoGet],
    summary="Get each district's Question 2 result",
    description=(
        "Ballot Question 2 (HB 1300, 2026 chapter 324) by school district: the yes and no votes, the yes "
        "percentage, and whether the district adopted the school tax cap (60% yes or more). The SAU "
        "central-office cap is decided by the vote across the SAU's towns. is_official is false until the "
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
