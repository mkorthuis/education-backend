from fastapi import APIRouter, Query
from typing import List, Optional

from app.api.v1.deps import SessionDep
from app.schema.staff_schema import (
    SchoolStaffTypeGet, 
    TeacherEducationTypeGet, 
    TeacherSalaryBandTypeGet,
    DistrictStaffGet,
    StateStaffGet,
    DistrictTeacherEducationGet,
    StateTeacherEducationGet,
    DistrictTeacherAverageSalaryGet,
    StateTeacherAverageSalaryGet,
    DistrictTeacherSalaryBandGet,
    StateTeacherSalaryBandGet
)
from app.service.public.staff_service import staff_service

router = APIRouter()

@router.get("/staff-type",
    response_model=List[SchoolStaffTypeGet],
    summary="Get all staff types",
    description="Retrieves a list of all school staff types",
    response_description="List of staff types")
def get_staff_types(session: SessionDep):
    return staff_service.get_staff_types(session=session)

@router.get("/teacher-education-type",
    response_model=List[TeacherEducationTypeGet],
    summary="Get all teacher education types",
    description="Retrieves a list of all teacher education types",
    response_description="List of teacher education types")
def get_teacher_education_types(session: SessionDep):
    return staff_service.get_teacher_education_types(session=session)

@router.get("/teacher-salary-band-type",
    response_model=List[TeacherSalaryBandTypeGet],
    summary="Get all teacher salary band types",
    description="Retrieves a list of all teacher salary band types",
    response_description="List of teacher salary band types")
def get_teacher_salary_band_types(session: SessionDep):
    return staff_service.get_teacher_salary_band_types(session=session)

@router.get("/district/staff",
    response_model=List[DistrictStaffGet],
    summary="Get district staff data",
    description="Retrieves district staff data with optional filters",
    response_description="List of district staff data")
def get_district_staff(
    session: SessionDep,
    year: Optional[int] = Query(default=None, description="Filter by year"),
    district_id: Optional[int] = Query(default=None, description="Filter by district ID"),
    staff_type_id: Optional[int] = Query(default=None, description="Filter by staff type ID")
):
    return staff_service.get_district_staff(
        session=session,
        year=year,
        district_id=district_id,
        staff_type_id=staff_type_id
    )

@router.get("/state/staff",
    response_model=List[StateStaffGet],
    summary="Get state staff data",
    description="Retrieves state-level staff data with optional filters",
    response_description="List of state staff data")
def get_state_staff(
    session: SessionDep,
    year: Optional[int] = Query(default=None, description="Filter by year"),
    staff_type_id: Optional[int] = Query(default=None, description="Filter by staff type ID")
):
    return staff_service.get_state_staff(
        session=session,
        year=year,
        staff_type_id=staff_type_id
    )

@router.get("/district/teacher-education",
    response_model=List[DistrictTeacherEducationGet],
    summary="Get district teacher education data",
    description="Retrieves district teacher education data with optional filters",
    response_description="List of district teacher education data")
def get_district_teacher_education(
    session: SessionDep,
    year: Optional[int] = Query(default=None, description="Filter by year"),
    district_id: Optional[int] = Query(default=None, description="Filter by district ID"),
    teacher_type_id: Optional[int] = Query(default=None, description="Filter by teacher education type ID")
):
    return staff_service.get_district_teacher_education(
        session=session,
        year=year,
        district_id=district_id,
        teacher_type_id=teacher_type_id
    )

@router.get("/state/teacher-education",
    response_model=List[StateTeacherEducationGet],
    summary="Get state teacher education data",
    description="Retrieves state-level teacher education data with optional filters",
    response_description="List of state teacher education data")
def get_state_teacher_education(
    session: SessionDep,
    year: Optional[int] = Query(default=None, description="Filter by year"),
    teacher_type_id: Optional[int] = Query(default=None, description="Filter by teacher education type ID")
):
    return staff_service.get_state_teacher_education(
        session=session,
        year=year,
        teacher_type_id=teacher_type_id
    )

@router.get("/district/teacher-average-salary",
    response_model=List[DistrictTeacherAverageSalaryGet],
    summary="Get district teacher average salary data",
    description="Retrieves district teacher average salary data with optional filters",
    response_description="List of district teacher average salary data")
def get_district_teacher_average_salary(
    session: SessionDep,
    year: Optional[int] = Query(default=None, description="Filter by year"),
    district_id: Optional[int] = Query(default=None, description="Filter by district ID")
):
    return staff_service.get_district_teacher_average_salary(
        session=session,
        year=year,
        district_id=district_id
    )

@router.get("/state/teacher-average-salary",
    response_model=List[StateTeacherAverageSalaryGet],
    summary="Get state teacher average salary data",
    description="Retrieves state-level teacher average salary data with optional filters",
    response_description="List of state teacher average salary data")
def get_state_teacher_average_salary(
    session: SessionDep,
    year: Optional[int] = Query(default=None, description="Filter by year")
):
    return staff_service.get_state_teacher_average_salary(
        session=session,
        year=year
    )

@router.get("/district/teacher-salary-band",
    response_model=List[DistrictTeacherSalaryBandGet],
    summary="Get district teacher salary band data",
    description="Retrieves district teacher salary band data with optional filters",
    response_description="List of district teacher salary band data")
def get_district_teacher_salary_band(
    session: SessionDep,
    year: Optional[int] = Query(default=None, description="Filter by year"),
    district_id: Optional[int] = Query(default=None, description="Filter by district ID"),
    salary_band_type_id: Optional[int] = Query(default=None, description="Filter by salary band type ID")
):
    return staff_service.get_district_teacher_salary_band(
        session=session,
        year=year,
        district_id=district_id,
        salary_band_type_id=salary_band_type_id
    )

@router.get("/state/teacher-salary-band",
    response_model=List[StateTeacherSalaryBandGet],
    summary="Get state teacher salary band data",
    description="Retrieves state-level teacher salary band data with optional filters",
    response_description="List of state teacher salary band data")
def get_state_teacher_salary_band(
    session: SessionDep,
    year: Optional[int] = Query(default=None, description="Filter by year"),
    salary_band_type_id: Optional[int] = Query(default=None, description="Filter by salary band type ID")
):
    return staff_service.get_state_teacher_salary_band(
        session=session,
        year=year,
        salary_band_type_id=salary_band_type_id
    ) 