from fastapi import APIRouter, Query
from typing import List, Optional

from app.api.v1.deps import SessionDep
from app.schema.enrollment_schema import (
    StateEnrollmentTypeGet,
    DistrictEnglishLearnerGet, DistrictReducedLunchGet, SchoolEnrollmentGet, SchoolReducedLunchGet,
    StateEnglishLearnerGet, StateEnrollmentGet, StateReducedLunchGet, StateSchoolCountGet, TownEnrollmentGet,
    TownEnrollmentStateGet,
)
from app.service.public.enrollment_service import enrollment_service
from app.core.cache import cache_response

router = APIRouter()

@router.get("/school/{school_id}", 
    response_model=List[SchoolEnrollmentGet],
    summary="Get school enrollments",
    description="Retrieves enrollment data for a specific school, with optional filtering by year",
    response_description="List of school enrollments")
@cache_response("enrollment_school")
def get_school_enrollments(
    school_id: int, 
    session: SessionDep,
    year: Optional[int] = Query(None, description="Filter enrollments by year")
):
    """
    Get enrollment data for a specific school, optionally filtered by year.
    
    Parameters:
    - **school_id**: The ID of the school to get enrollments for
    - **year**: Optional year to filter enrollments by
    
    Returns a list of enrollment records with grade information.
    """
    return enrollment_service.get_school_enrollments(
        session=session, 
        school_id=school_id, 
        year=year
    )

@router.get("/school/{school_id}/latest", 
    response_model=List[SchoolEnrollmentGet],
    summary="Get latest school enrollments",
    description="Retrieves the most recent enrollment data available for a specific school",
    response_description="List of latest school enrollments")
@cache_response("enrollment_school_latest")
def get_latest_school_enrollments(
    school_id: int, 
    session: SessionDep
):
    """
    Get the most recent enrollment data available for a specific school.
    
    This endpoint automatically finds the latest year for which enrollment data
    is available and returns all enrollment records for that year.
    
    Parameters:
    - **school_id**: The ID of the school to get enrollments for
    
    Returns a list of the most recent enrollment records with grade information.
    """
    return enrollment_service.get_latest_school_enrollments(
        session=session, 
        school_id=school_id
    )

@router.get("/town", 
    response_model=List[TownEnrollmentGet],
    summary="Get town enrollments",
    description="Retrieves enrollment data for towns, with optional filtering by town ID, district ID, and year",
    response_description="List of town enrollments")
@cache_response("enrollment_town")
def get_town_enrollments(
    session: SessionDep,
    town_id: Optional[int] = Query(None, description="Optional town ID to filter by"),
    district_id: Optional[int] = Query(None, description="Optional district ID to filter by. If both district_id and town_id are provided, district_id takes precedence"),
    year: Optional[int] = Query(None, description="Optional year to filter by")
):
    """
    Get enrollment data for towns, optionally filtered by town ID, district ID, and year.
    
    If town_id is provided, returns data for that specific town.
    If district_id is provided, returns data for all towns in that district.
    If year is provided, returns data for that specific year.
    
    If both town_id and district_id are provided, district_id takes precedence, 
    and the system will verify that the town belongs to the district.
    
    Parameters:
    - **town_id**: Optional town ID to filter enrollments by
    - **district_id**: Optional district ID to filter enrollments by
    - **year**: Optional year to filter enrollments by
    
    Returns a list of town enrollment records with grade information.
    """
    return enrollment_service.get_town_enrollments(
        session=session, 
        town_id=town_id,
        district_id=district_id,
        year=year
    )

@router.get("/town/state", 
    response_model=List[TownEnrollmentStateGet],
    summary="Get state-level town enrollments",
    description="Retrieves state-level town enrollment data aggregated by year and grade, with optional filtering",
    response_description="List of state-level town enrollment records")
@cache_response("enrollment_town_state")
def get_town_enrollment_state(
    session: SessionDep,
    year: Optional[int] = Query(None, description="Optional year to filter by"),
    grade_id: Optional[int] = Query(None, description="Optional grade ID to filter by")
):
    """
    Get state-level town enrollment data aggregated by year and grade, optionally filtered.
    
    This endpoint returns data from the town_enrollment_state materialized view, which
    contains pre-aggregated sums of town enrollments by year and grade.
    
    If year is provided, returns data for that specific year.
    If grade_id is provided, returns data for that specific grade.
    If both are provided, returns data for that specific combination.
    If neither is provided, returns all state-level town enrollment data.
    
    Parameters:
    - **year**: Optional year to filter by
    - **grade_id**: Optional grade ID to filter by
    
    Returns a list of state-level town enrollment records with grade information.
    """
    return enrollment_service.get_town_enrollment_state(
        session=session, 
        year=year, 
        grade_id=grade_id
    )

@router.get("/school-counts/state",
    response_model=List[StateSchoolCountGet],
    summary="Get the number of public schools and districts by year",
    description="Counts, for each year, the public schools with students in kindergarten to grade 12, and the public school districts they belong to",
    response_description="One row per year, oldest first")
@cache_response("enrollment_school_counts_state")
def get_state_school_counts(session: SessionDep):
    """
    Get the number of public schools and school districts with K-12 students, by year.

    Returns one row per year: the year, the number of schools and the number of districts.
    """
    return enrollment_service.get_state_school_counts(session=session)

# -------------------- October 1 enrollment by type of school --------------------

@router.get("/type/state",
    response_model=List[StateEnrollmentTypeGet],
    summary="Get statewide enrollment by type of school",
    description="October 1 enrollment by type of school (public district, public academy and joint maintenance agreement, public charter, interstate, nonpublic) and grade, statewide, by year")
@cache_response("enrollment_type_state")
def get_state_enrollment_by_type(
    session: SessionDep,
    year: Optional[int] = Query(default=None),
):
    return enrollment_service.get_state_enrollment_by_type(session=session, year=year)

# -------------------- Free and reduced-price lunch eligibility --------------------

@router.get("/reduced-lunch/school",
    response_model=List[SchoolReducedLunchGet],
    summary="Get free and reduced-price lunch eligibility by school",
    description="K-12 students and those eligible for free or reduced-price lunch, as of October 1, by school and year")
@cache_response("enrollment_reduced_lunch_school")
def get_school_reduced_lunch(
    session: SessionDep,
    year: Optional[int] = Query(default=None),
    school_id: Optional[int] = Query(default=None),
    district_id: Optional[int] = Query(default=None),
):
    return enrollment_service.get_school_reduced_lunch(session=session, year=year, school_id=school_id, district_id=district_id)

@router.get("/reduced-lunch/district",
    response_model=List[DistrictReducedLunchGet],
    summary="Get free and reduced-price lunch eligibility by district",
    description="K-12 students and those eligible for free or reduced-price lunch, as of October 1: each district's schools added up")
@cache_response("enrollment_reduced_lunch_district")
def get_district_reduced_lunch(
    session: SessionDep,
    year: Optional[int] = Query(default=None),
    district_id: Optional[int] = Query(default=None),
):
    return enrollment_service.get_district_reduced_lunch(session=session, year=year, district_id=district_id)

@router.get("/reduced-lunch/state",
    response_model=List[StateReducedLunchGet],
    summary="Get statewide free and reduced-price lunch eligibility",
    description="K-12 students in every public school (including academies, charter and interstate schools) and those eligible for free or reduced-price lunch, as of October 1")
@cache_response("enrollment_reduced_lunch_state")
def get_state_reduced_lunch(
    session: SessionDep,
    year: Optional[int] = Query(default=None),
):
    return enrollment_service.get_state_reduced_lunch(session=session, year=year)

# -------------------- English learners --------------------

@router.get("/english-learner/district",
    response_model=List[DistrictEnglishLearnerGet],
    summary="Get English learners by district",
    description="Students enrolled, English learners (eligible) and former English learners being monitored, as of October 1, by district and year")
@cache_response("enrollment_english_learner_district")
def get_district_english_learner(
    session: SessionDep,
    year: Optional[int] = Query(default=None),
    district_id: Optional[int] = Query(default=None),
):
    return enrollment_service.get_district_english_learner(session=session, year=year, district_id=district_id)

@router.get("/english-learner/state",
    response_model=List[StateEnglishLearnerGet],
    summary="Get statewide English learners",
    description="Students enrolled, English learners (eligible) and former English learners being monitored, as of October 1, for the state")
@cache_response("enrollment_english_learner_state")
def get_state_english_learner(
    session: SessionDep,
    year: Optional[int] = Query(default=None),
):
    return enrollment_service.get_state_english_learner(session=session, year=year)

@router.get("/state", 
    response_model=List[StateEnrollmentGet],
    summary="Get state-level enrollments",
    description="Retrieves state-level enrollment data, with optional filtering by year",
    response_description="List of state enrollment records")
@cache_response("enrollment_state")
def get_state_enrollments(
    session: SessionDep,
    year: Optional[int] = Query(None, description="Filter enrollments by year")
):
    """
    Get state-level enrollment data, optionally filtered by year.
    
    Parameters:
    - **year**: Optional year to filter enrollments by
    
    Returns a list of state enrollment records with elementary, middle, high, and total enrollment figures.
    """
    return enrollment_service.get_state_enrollments(
        session=session, 
        year=year
    )
