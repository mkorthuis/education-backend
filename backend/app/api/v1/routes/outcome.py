from fastapi import APIRouter, Query
from typing import List, Optional

from app.api.v1.deps import SessionDep
from app.schema.outcome_schema import (
    PostGraduationTypeGet,
    SchoolPostGraduationGet,
    StatePostGraduationGet,
    DistrictPostGraduationGet,
    SchoolEarlyExitGet,
    StateEarlyExitGet,
    DistrictEarlyExitGet,
    SchoolGraduationCohortGet,
    StateGraduationCohortGet,
    DistrictGraduationCohortGet,
)
from app.service.public.outcome_service import outcome_service

router = APIRouter(prefix="/outcome", tags=["Outcome"])

# -------------------- Post Graduation --------------------

@router.get(
    "/post-graduation-type",
    response_model=List[PostGraduationTypeGet],
    summary="Get post-graduation outcome types",
)
def get_post_graduation_types(session: SessionDep):
    return outcome_service.get_post_graduation_types(session=session)

@router.get(
    "/post-graduation/school",
    response_model=List[SchoolPostGraduationGet],
    summary="Get school post-graduation outcomes",
)
def get_school_post_graduation(
    session: SessionDep,
    year: Optional[int] = Query(default=None),
    school_id: Optional[int] = Query(default=None),
    district_id: Optional[int] = Query(default=None),
    post_graduation_type_id: Optional[int] = Query(default=None, description="Filter by post-graduation type id"),
):
    return outcome_service.get_school_post_graduation(
        session=session,
        year=year,
        school_id=school_id,
        district_id=district_id,
        pg_type_id=post_graduation_type_id,
    )

@router.get(
    "/post-graduation/district",
    response_model=List[DistrictPostGraduationGet],
    summary="Get district post-graduation outcomes",
)
def get_district_post_graduation(
    session: SessionDep,
    year: Optional[int] = Query(default=None),
    district_id: Optional[int] = Query(default=None),
    post_graduation_type_id: Optional[int] = Query(default=None, description="Filter by post-graduation type id"),
):
    return outcome_service.get_district_post_graduation(
        session=session,
        year=year,
        district_id=district_id,
        pg_type_id=post_graduation_type_id,
    )

@router.get(
    "/post-graduation/state",
    response_model=List[StatePostGraduationGet],
    summary="Get state post-graduation outcomes",
)
def get_state_post_graduation(
    session: SessionDep,
    year: Optional[int] = Query(default=None),
    post_graduation_type_id: Optional[int] = Query(default=None, description="Filter by post-graduation type id"),
):
    return outcome_service.get_state_post_graduation(
        session=session,
        year=year,
        pg_type_id=post_graduation_type_id,
    )

# -------------------- Early Exit --------------------

@router.get(
    "/early-exit/school",
    response_model=List[SchoolEarlyExitGet],
    summary="Get school early-exit data",
)
def get_school_early_exit(
    session: SessionDep,
    year: Optional[int] = Query(default=None),
    school_id: Optional[int] = Query(default=None),
    district_id: Optional[int] = Query(default=None),
):
    return outcome_service.get_school_early_exit(session=session, year=year, school_id=school_id, district_id=district_id)

@router.get(
    "/early-exit/district",
    response_model=List[DistrictEarlyExitGet],
    summary="Get district early-exit data",
)
def get_district_early_exit(
    session: SessionDep,
    year: Optional[int] = Query(default=None),
    district_id: Optional[int] = Query(default=None),
):
    return outcome_service.get_district_early_exit(session=session, year=year, district_id=district_id) 

@router.get(
    "/early-exit/state",
    response_model=List[StateEarlyExitGet],
    summary="Get state early-exit data",
)
def get_state_early_exit(
    session: SessionDep,
    year: Optional[int] = Query(default=None),
):
    return outcome_service.get_state_early_exit(session=session, year=year)

# -------------------- Cohort Graduation --------------------

@router.get(
    "/graduation-cohort/school",
    response_model=List[SchoolGraduationCohortGet],
    summary="Get school cohort graduation data",
)
def get_school_graduation_cohort(
    session: SessionDep,
    year: Optional[int] = Query(default=None),
    school_id: Optional[int] = Query(default=None),
    district_id: Optional[int] = Query(default=None),
):
    return outcome_service.get_school_graduation_cohort(
        session=session,
        year=year,
        school_id=school_id,
        district_id=district_id,
    )

@router.get(
    "/graduation-cohort/district",
    response_model=List[DistrictGraduationCohortGet],
    summary="Get district cohort graduation data",
)
def get_district_graduation_cohort(
    session: SessionDep,
    year: Optional[int] = Query(default=None),
    district_id: Optional[int] = Query(default=None),
):
    return outcome_service.get_district_graduation_cohort(
        session=session,
        year=year,
        district_id=district_id,
    )

@router.get(
    "/graduation-cohort/state",
    response_model=List[StateGraduationCohortGet],
    summary="Get state cohort graduation data",
)
def get_state_graduation_cohort(
    session: SessionDep,
    year: Optional[int] = Query(default=None),
):
    return outcome_service.get_state_graduation_cohort(
        session=session,
        year=year,
    )