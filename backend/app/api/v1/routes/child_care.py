from typing import List, Optional

from fastapi import APIRouter, Query

from app.api.v1.deps import SessionDep
from app.core.cache import cache_response
from app.schema.child_care_schema import (
    ChildCareProgramDetailGet, ChildCareProgramGet, DistrictChildCareGet, StateChildCareGet, TownChildCareGet,
)
from app.service.public.child_care_service import child_care_service

router = APIRouter()

AS_OF = Query(default=None, pattern=r"^\d{4}-\d{2}-\d{2}$",
              description="Only this download (YYYY-MM-DD); each is a snapshot of the DHHS Child Care Search")
TOTALS = (
    " Each row is one download: programs and licensed capacity, the licensed ones, the infant and toddler "
    "capacity, the programs serving each age group, and the openings programs report on their pages (each as "
    "of its own date, some over a year old)."
)
HIDE_HIDDEN_EMAIL = Query(
    default=False,
    description="Leave the email blank for programs whose page says they chose not to show it (email_hidden). "
                "By default every email is returned.",
)


@router.get(
    "/state",
    response_model=List[StateChildCareGet],
    summary="Get statewide child care totals",
    description="Licensed and license-exempt child care programs added up statewide." + TOTALS,
    response_description="Statewide child care totals by download",
)
@cache_response("child_care_state")
def get_state_child_care(session: SessionDep, as_of: Optional[str] = AS_OF):
    return child_care_service.get_state_totals(session=session, as_of=as_of)


@router.get(
    "/town",
    response_model=List[TownChildCareGet],
    summary="Get child care totals by town",
    description="Child care programs added up by the town they're in." + TOTALS,
    response_description="Child care totals by town and download",
)
@cache_response("child_care_town")
def get_town_child_care(
    session: SessionDep,
    as_of: Optional[str] = AS_OF,
    town_id: Optional[int] = Query(default=None, description="Filter by town ID"),
    district_id: Optional[int] = Query(default=None, description="Only the towns of this school district"),
):
    return child_care_service.get_town_totals(session=session, as_of=as_of, town_id=town_id, district_id=district_id)


@router.get(
    "/district",
    response_model=List[DistrictChildCareGet],
    summary="Get child care totals by school district",
    description=(
        "Child care programs added up by school district. A town's programs count toward the district that "
        "teaches its kindergarten, so a town in an elementary and a cooperative district (Amherst and Souhegan) "
        "counts once, and the districts add up to the state." + TOTALS
    ),
    response_description="Child care totals by district and download",
)
@cache_response("child_care_district")
def get_district_child_care(
    session: SessionDep,
    as_of: Optional[str] = AS_OF,
    district_id: Optional[int] = Query(default=None, description="Filter by district ID"),
):
    return child_care_service.get_district_totals(session=session, as_of=as_of, district_id=district_id)


@router.get(
    "/program",
    response_model=List[ChildCareProgramGet],
    summary="Get child care programs",
    description=(
        "Child care programs with their contact details, ages served, quality ratings and their latest download's "
        "license status, capacity, availability and vacancies, by town and then name. Only programs in the latest "
        "download unless is_current is false. A program that chose not to show its email on its page has "
        "email_hidden true; hide_hidden_email leaves those emails blank."
    ),
    response_description="Child care programs",
)
@cache_response("child_care_program")
def get_child_care_programs(
    session: SessionDep,
    town_id: Optional[int] = Query(default=None, description="Filter by town ID"),
    district_id: Optional[int] = Query(default=None, description="Only programs in this school district's towns"),
    program_type_id: Optional[int] = Query(
        default=None, description="Filter by type of care: 1 Licensed Group, 2 Licensed Family, 3 License Exempt Family, "
                                  "4 License Exempt Facility"),
    age_group: Optional[str] = Query(default=None, pattern="^(infant|toddler|preschool|school_age)$",
                                     description="Only programs serving this age group"),
    availability_id: Optional[int] = Query(
        default=None, description="Filter by availability: 1 Accepting Children, 2 Accepting Children on Wait List, "
                                  "3 Not Accepting Children"),
    has_vacancies: Optional[bool] = Query(
        default=None, description="Only programs reporting openings (true) or none (false), in age_group if given"),
    accepts_scholarship: Optional[bool] = Query(default=None, description="Only NH Child Care Scholarship providers (true) or not"),
    is_current: Optional[bool] = Query(default=True, description="Programs in the latest download (true) or no longer listed (false)"),
    hide_hidden_email: bool = HIDE_HIDDEN_EMAIL,
):
    return child_care_service.get_programs(
        session=session,
        town_id=town_id,
        district_id=district_id,
        program_type_id=program_type_id,
        age_group=age_group,
        availability_id=availability_id,
        has_vacancies=has_vacancies,
        accepts_scholarship=accepts_scholarship,
        is_current=is_current,
        hide_hidden_email=hide_hidden_email,
    )


@router.get(
    "/program/{program_id}",
    response_model=ChildCareProgramDetailGet,
    summary="Get a child care program",
    description=(
        "One program's details with its mailing address, hours and rates by schedule (a page's schedules have no "
        "names, so each different one is numbered), its license types and page lists (features), its licensing "
        "visits, newest first, and every download's snapshot. A program that chose not to show its email has "
        "email_hidden true; hide_hidden_email leaves its email blank."
    ),
    response_description="Child care program details",
)
@cache_response("child_care_program_by_id")
def get_child_care_program(
    program_id: int,
    session: SessionDep,
    hide_hidden_email: bool = HIDE_HIDDEN_EMAIL,
):
    return child_care_service.get_program(session=session, program_id=program_id, hide_hidden_email=hide_hidden_email)
