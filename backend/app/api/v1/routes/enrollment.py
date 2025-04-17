from fastapi import APIRouter, Query
from typing import List, Optional

from app.api.v1.deps import SessionDep
from app.schema.enrollment_schema import SchoolEnrollmentGet, StateEnrollmentGet, TownEnrollmentGet, TownEnrollmentStateGet
from app.service.public.enrollment_service import enrollment_service

router = APIRouter()

@router.get("/school/{school_id}", 
    response_model=List[SchoolEnrollmentGet],
    summary="Get school enrollments",
    description="Retrieves enrollment data for a specific school, with optional filtering by year",
    response_description="List of school enrollments")
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

@router.get("/state", 
    response_model=List[StateEnrollmentGet],
    summary="Get state-level enrollments",
    description="Retrieves state-level enrollment data, with optional filtering by year",
    response_description="List of state enrollment records")
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
