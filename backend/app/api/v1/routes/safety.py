from fastapi import APIRouter, Query
from typing import List, Optional

from app.api.v1.deps import SessionDep
from app.schema.safety_schema import (
    SchoolSafetyTypeGet, SchoolSafetyGet, TruancyGet,
    DisciplineIncidentTypeGet, DisciplineIncidentGet,
    DisciplineCountTypeGet, DisciplineCountGet,
    BullyingTypeGet, BullyingGet,
    BullyingClassificationTypeGet, BullyingClassificationGet,
    BullyingImpactTypeGet, BullyingImpactGet,
    HarassmentClassificationGet, HarassmentGet,
    RestraintGet, SeclusionGet
)
from app.service.public.safety_service import safety_service

router = APIRouter()

@router.get("/school-safety-type",
    response_model=List[SchoolSafetyTypeGet],
    summary="Get all school safety types",
    description="Retrieves a list of all school safety types",
    response_description="List of school safety types")
def get_school_safety_types(session: SessionDep):
    return safety_service.get_safety_types(session=session)

@router.get("/discipline-incident-type",
    response_model=List[DisciplineIncidentTypeGet],
    summary="Get all discipline incident types",
    description="Retrieves a list of all discipline incident types",
    response_description="List of discipline incident types")
def get_discipline_incident_types(session: SessionDep):
    return safety_service.get_discipline_incident_types(session=session)

@router.get("/discipline-count-type",
    response_model=List[DisciplineCountTypeGet],
    summary="Get all discipline count types",
    description="Retrieves a list of all discipline count types",
    response_description="List of discipline count types")
def get_discipline_count_types(session: SessionDep):
    return safety_service.get_discipline_count_types(session=session)

@router.get("/bullying-type",
    response_model=List[BullyingTypeGet],
    summary="Get all bullying types",
    description="Retrieves a list of all bullying types",
    response_description="List of bullying types")
def get_bullying_types(session: SessionDep):
    return safety_service.get_bullying_types(session=session)

@router.get("/bullying-classification-type",
    response_model=List[BullyingClassificationTypeGet],
    summary="Get all bullying classification types",
    description="Retrieves a list of all bullying classification types",
    response_description="List of bullying classification types")
def get_bullying_classification_types(session: SessionDep):
    return safety_service.get_bullying_classification_types(session=session)

@router.get("/bullying-impact-type",
    response_model=List[BullyingImpactTypeGet],
    summary="Get all bullying impact types",
    description="Retrieves a list of all bullying impact types",
    response_description="List of bullying impact types")
def get_bullying_impact_types(session: SessionDep):
    return safety_service.get_bullying_impact_types(session=session)

@router.get("/harassment-classification",
    response_model=List[HarassmentClassificationGet],
    summary="Get all harassment classifications",
    description="Retrieves a list of all harassment classifications",
    response_description="List of harassment classifications")
def get_harassment_classifications(session: SessionDep):
    return safety_service.get_harassment_classifications(session=session)

@router.get("/school-safety",
    response_model=List[SchoolSafetyGet],
    summary="Get school safety data",
    description="Retrieves school safety data with optional filters",
    response_description="List of school safety data")
def get_school_safety(
    session: SessionDep,
    year: Optional[int] = Query(default=None, description="Filter by year"),
    school_id: Optional[int] = Query(default=None, description="Filter by school ID"),
    district_id: Optional[int] = Query(default=None, description="Filter by district ID"),
    safety_type_id: Optional[int] = Query(default=None, description="Filter by safety type ID")
):
    return safety_service.get_school_safety(
        session=session,
        year=year,
        school_id=school_id,
        district_id=district_id,
        safety_type_id=safety_type_id
    )

@router.get("/truancy",
    response_model=List[TruancyGet],
    summary="Get truancy data",
    description="Retrieves truancy data with optional filters",
    response_description="List of truancy data")
def get_truancy(
    session: SessionDep,
    year: Optional[int] = Query(default=None, description="Filter by year"),
    school_id: Optional[int] = Query(default=None, description="Filter by school ID"),
    district_id: Optional[int] = Query(default=None, description="Filter by district ID")
):
    return safety_service.get_truancy(
        session=session,
        year=year,
        school_id=school_id,
        district_id=district_id
    )

@router.get("/discipline/incident",
    response_model=List[DisciplineIncidentGet],
    summary="Get discipline incident data",
    description="Retrieves discipline incident data with optional filters",
    response_description="List of discipline incident data")
def get_discipline_incidents(
    session: SessionDep,
    year: Optional[int] = Query(default=None, description="Filter by year"),
    school_id: Optional[int] = Query(default=None, description="Filter by school ID"),
    district_id: Optional[int] = Query(default=None, description="Filter by district ID"),
    discipline_incident_type_id: Optional[int] = Query(default=None, description="Filter by discipline incident type ID")
):
    return safety_service.get_discipline_incidents(
        session=session,
        year=year,
        school_id=school_id,
        district_id=district_id,
        discipline_incident_type_id=discipline_incident_type_id
    )

@router.get("/discipline/count",
    response_model=List[DisciplineCountGet],
    summary="Get discipline count data",
    description="Retrieves discipline count data with optional filters",
    response_description="List of discipline count data")
def get_discipline_counts(
    session: SessionDep,
    year: Optional[int] = Query(default=None, description="Filter by year"),
    school_id: Optional[int] = Query(default=None, description="Filter by school ID"),
    district_id: Optional[int] = Query(default=None, description="Filter by district ID"),
    discipline_count_type_id: Optional[int] = Query(default=None, description="Filter by discipline count type ID")
):
    return safety_service.get_discipline_counts(
        session=session,
        year=year,
        school_id=school_id,
        district_id=district_id,
        discipline_count_type_id=discipline_count_type_id
    )

@router.get("/bullying",
    response_model=List[BullyingGet],
    summary="Get bullying data",
    description="Retrieves bullying data with optional filters",
    response_description="List of bullying data")
def get_bullying(
    session: SessionDep,
    year: Optional[int] = Query(default=None, description="Filter by year"),
    school_id: Optional[int] = Query(default=None, description="Filter by school ID"),
    district_id: Optional[int] = Query(default=None, description="Filter by district ID"),
    bullying_type_id: Optional[int] = Query(default=None, description="Filter by bullying type ID")
):
    return safety_service.get_bullying(
        session=session,
        year=year,
        school_id=school_id,
        district_id=district_id,
        bullying_type_id=bullying_type_id
    )

@router.get("/bullying/classification",
    response_model=List[BullyingClassificationGet],
    summary="Get bullying classification data",
    description="Retrieves bullying classification data with optional filters",
    response_description="List of bullying classification data")
def get_bullying_classifications(
    session: SessionDep,
    year: Optional[int] = Query(default=None, description="Filter by year"),
    school_id: Optional[int] = Query(default=None, description="Filter by school ID"),
    district_id: Optional[int] = Query(default=None, description="Filter by district ID"),
    bullying_classification_type_id: Optional[int] = Query(default=None, description="Filter by bullying classification type ID")
):
    return safety_service.get_bullying_classifications(
        session=session,
        year=year,
        school_id=school_id,
        district_id=district_id,
        bullying_classification_type_id=bullying_classification_type_id
    )

@router.get("/bullying/impact",
    response_model=List[BullyingImpactGet],
    summary="Get bullying impact data",
    description="Retrieves bullying impact data with optional filters",
    response_description="List of bullying impact data")
def get_bullying_impacts(
    session: SessionDep,
    year: Optional[int] = Query(default=None, description="Filter by year"),
    school_id: Optional[int] = Query(default=None, description="Filter by school ID"),
    district_id: Optional[int] = Query(default=None, description="Filter by district ID"),
    bullying_impact_type_id: Optional[int] = Query(default=None, description="Filter by bullying impact type ID")
):
    return safety_service.get_bullying_impacts(
        session=session,
        year=year,
        school_id=school_id,
        district_id=district_id,
        bullying_impact_type_id=bullying_impact_type_id
    )

@router.get("/harassment",
    response_model=List[HarassmentGet],
    summary="Get harassment data",
    description="Retrieves harassment data with optional filters",
    response_description="List of harassment data")
def get_harassment(
    session: SessionDep,
    year: Optional[int] = Query(default=None, description="Filter by year"),
    school_id: Optional[int] = Query(default=None, description="Filter by school ID"),
    district_id: Optional[int] = Query(default=None, description="Filter by district ID"),
    harassment_classification_id: Optional[int] = Query(default=None, description="Filter by harassment classification ID")
):
    return safety_service.get_harassment(
        session=session,
        year=year,
        school_id=school_id,
        district_id=district_id,
        harassment_classification_id=harassment_classification_id
    )

@router.get("/restraint",
    response_model=List[RestraintGet],
    summary="Get restraint data",
    description="Retrieves restraint data with optional filters",
    response_description="List of restraint data")
def get_restraint(
    session: SessionDep,
    year: Optional[int] = Query(default=None, description="Filter by year"),
    school_id: Optional[int] = Query(default=None, description="Filter by school ID"),
    district_id: Optional[int] = Query(default=None, description="Filter by district ID")
):
    return safety_service.get_restraint(
        session=session,
        year=year,
        school_id=school_id,
        district_id=district_id
    )

@router.get("/seclusion",
    response_model=List[SeclusionGet],
    summary="Get seclusion data",
    description="Retrieves seclusion data with optional filters",
    response_description="List of seclusion data")
def get_seclusion(
    session: SessionDep,
    year: Optional[int] = Query(default=None, description="Filter by year"),
    school_id: Optional[int] = Query(default=None, description="Filter by school ID"),
    district_id: Optional[int] = Query(default=None, description="Filter by district ID")
):
    return safety_service.get_seclusion(
        session=session,
        year=year,
        school_id=school_id,
        district_id=district_id
    ) 