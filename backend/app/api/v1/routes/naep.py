from typing import List, Optional

from fastapi import APIRouter, Query

from app.api.v1.deps import SessionDep
from app.core.cache import cache_response
from app.schema.naep_schema import JurisdictionGet, NaepComparisonGet, NaepMeasureGet, NaepResultGet, NaepStudentGroupGet
from app.service.public.naep_service import naep_service

router = APIRouter()

SUBJECT = "Filter by assessment subject ID (1 math, 2 reading)"
GRADE = "Filter by grade ID (6 is Grade 4, 10 is Grade 8)"
PLACE = "Filter by NAEP place code, e.g. NH, MA, DC, NP (national public) or DS (DoDEA)"


@router.get("/jurisdiction",
    response_model=List[JurisdictionGet],
    summary="Get the places NAEP reports on",
    description="The national public average, the states and DC, and the Department of Defense schools (DoDEA), by NAEP's codes")
@cache_response("naep_jurisdictions")
def get_jurisdictions(session: SessionDep):
    return naep_service.get_jurisdictions(session=session)


@router.get("/measure",
    response_model=List[NaepMeasureGet],
    summary="Get the NAEP measures",
    description="Average scale score, and the shares of students at or above NAEP Basic and NAEP Proficient and at NAEP Advanced")
@cache_response("naep_measures")
def get_measures(session: SessionDep):
    return naep_service.get_measures(session=session)


@router.get("/student-group",
    response_model=List[NaepStudentGroupGet],
    summary="Get the NAEP student groups",
    description="NAEP's own student groups, which are defined differently from the state assessment's")
@cache_response("naep_student_groups")
def get_student_groups(session: SessionDep):
    return naep_service.get_student_groups(session=session)


@router.get("/result",
    response_model=List[NaepResultGet],
    summary="Get NAEP results",
    description="NAEP reading and math results in grades 4 and 8 for every state, DC, DoDEA and the national public average, 2003 on, with optional filters. Values are unrounded; NAEP publishes whole numbers.",
    response_description="Results, oldest year first, then by subject, grade, measure and place")
@cache_response("naep_result")
def get_results(
    session: SessionDep,
    year: Optional[int] = Query(default=None, description="Filter by year (2024 = tested January to March 2024)"),
    assessment_subject_id: Optional[int] = Query(default=None, description=SUBJECT),
    grade_id: Optional[int] = Query(default=None, description=GRADE),
    naep_measure_id: Optional[int] = Query(default=None, description="Filter by NAEP measure ID"),
    naep_student_group_id: Optional[int] = Query(default=None, description="Filter by NAEP student group ID"),
    jurisdiction: Optional[str] = Query(default=None, description=PLACE),
):
    return naep_service.get_results(
        session=session, year=year, assessment_subject_id=assessment_subject_id, grade_id=grade_id,
        naep_measure_id=naep_measure_id, naep_student_group_id=naep_student_group_id, jurisdiction=jurisdiction,
    )


@router.get("/comparison",
    response_model=List[NaepComparisonGet],
    summary="Get NAEP significance tests",
    description=(
        "NAEP's own tests of whether one place and year differ from another: New Hampshire against every other "
        "state, DC and DoDEA in the same year (basis all_jurisdictions, adjusted for comparing every state at once, "
        "as in NAEP's state reports); New Hampshire against the national public average (basis pair); and each "
        "place's latest year against each earlier year (basis pair). result is the first place or year against the "
        "other: higher, lower or not_significant."
    ),
    response_description="Tests, oldest year first, then by subject, grade, measure and the places compared")
@cache_response("naep_comparison")
def get_comparisons(
    session: SessionDep,
    year: Optional[int] = Query(default=None, description="Filter by the first year compared"),
    other_year: Optional[int] = Query(default=None, description="Filter by the year it's compared with"),
    assessment_subject_id: Optional[int] = Query(default=None, description=SUBJECT),
    grade_id: Optional[int] = Query(default=None, description=GRADE),
    naep_measure_id: Optional[int] = Query(default=None, description="Filter by NAEP measure ID"),
    naep_student_group_id: Optional[int] = Query(default=None, description="Filter by NAEP student group ID"),
    jurisdiction: Optional[str] = Query(default=None, description=f"{PLACE}: the first place compared"),
    other_jurisdiction: Optional[str] = Query(default=None, description="Filter by the place it's compared with"),
    basis: Optional[str] = Query(default=None, pattern="^(all_jurisdictions|pair)$",
                                 description="Filter by how the test was made: all_jurisdictions or pair"),
):
    return naep_service.get_comparisons(
        session=session, year=year, other_year=other_year, assessment_subject_id=assessment_subject_id,
        grade_id=grade_id, naep_measure_id=naep_measure_id, naep_student_group_id=naep_student_group_id,
        jurisdiction=jurisdiction, other_jurisdiction=other_jurisdiction, basis=basis,
    )
