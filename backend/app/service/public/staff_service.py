from typing import List, Optional
from sqlmodel import Session

from app.model.staff import (
    SchoolStaffType,
    TeacherEducationType,
    TeacherSalaryBandType,
    DistrictStaff,
    StateStaff,
    DistrictTeacherEducation,
    StateTeacherEducation,
    DistrictTeacherAverageSalary,
    StateTeacherAverageSalary,
    DistrictTeacherSalaryBand,
    StateTeacherSalaryBand
)
from app.service.dataset_query import Dataset, fetch_dataset, list_types

STAFF = Dataset(
    {"district": DistrictStaff, "state": StateStaff}, ("value",), "staff data",
    type_model=SchoolStaffType, type_fk="school_staff_type_id_fk", type_key="staff_type")
TEACHER_EDUCATION = Dataset(
    {"district": DistrictTeacherEducation, "state": StateTeacherEducation}, ("value",), "teacher education data",
    type_model=TeacherEducationType, type_fk="teacher_type_id_fk", type_key="teacher_type")
TEACHER_AVERAGE_SALARY = Dataset(
    {"district": DistrictTeacherAverageSalary, "state": StateTeacherAverageSalary}, ("salary",),
    "teacher average salary data")
TEACHER_SALARY_BAND = Dataset(
    {"district": DistrictTeacherSalaryBand}, ("min_salary", "max_salary", "steps"), "teacher salary band data",
    type_model=TeacherSalaryBandType, type_fk="teacher_salary_band_type_id_fk", type_key="salary_band_type",
    type_fields=("id", "name", "description"))
# The state salary band view has no id; it returns the band type id instead
STATE_TEACHER_SALARY_BAND = Dataset(
    {"state": StateTeacherSalaryBand},
    (("teacher_salary_band_type_id", "teacher_salary_band_type_id_fk"), "min_salary", "max_salary", "steps"),
    "teacher salary band data",
    type_model=TeacherSalaryBandType, type_fk="teacher_salary_band_type_id_fk", type_key="salary_band_type",
    type_fields=("id", "name", "description"))


class StaffService:
    def get_staff_types(self, session: Session) -> List[dict]:
        """Get all staff types"""
        return list_types(session, SchoolStaffType, "staff types")

    def get_teacher_education_types(self, session: Session) -> List[dict]:
        """Get all teacher education types"""
        return list_types(session, TeacherEducationType, "teacher education types")

    def get_teacher_salary_band_types(self, session: Session) -> List[dict]:
        """Get all teacher salary band types"""
        return list_types(session, TeacherSalaryBandType, "teacher salary band types", ("id", "name", "description"))

    def get_district_staff(self, session: Session, year: Optional[int] = None, district_id: Optional[int] = None,
                           staff_type_id: Optional[int] = None) -> List[dict]:
        """Get district staff data with optional filters"""
        return fetch_dataset(session, STAFF, "district", year, district_id=district_id, type_id=staff_type_id)

    def get_district_teacher_education(self, session: Session, year: Optional[int] = None,
                                       district_id: Optional[int] = None,
                                       teacher_type_id: Optional[int] = None) -> List[dict]:
        """Get district teacher education data with optional filters"""
        return fetch_dataset(session, TEACHER_EDUCATION, "district", year, district_id=district_id,
                             type_id=teacher_type_id)

    def get_district_teacher_average_salary(self, session: Session, year: Optional[int] = None,
                                            district_id: Optional[int] = None) -> List[dict]:
        """Get district teacher average salary data with optional filters"""
        return fetch_dataset(session, TEACHER_AVERAGE_SALARY, "district", year, district_id=district_id)

    def get_district_teacher_salary_band(self, session: Session, year: Optional[int] = None,
                                         district_id: Optional[int] = None,
                                         salary_band_type_id: Optional[int] = None) -> List[dict]:
        """Get district teacher salary band data with optional filters"""
        return fetch_dataset(session, TEACHER_SALARY_BAND, "district", year, district_id=district_id,
                             type_id=salary_band_type_id)

    def get_state_staff(self, session: Session, year: Optional[int] = None,
                        staff_type_id: Optional[int] = None) -> List[dict]:
        """Get state staff data with optional filters"""
        return fetch_dataset(session, STAFF, "state", year, type_id=staff_type_id)

    def get_state_teacher_education(self, session: Session, year: Optional[int] = None,
                                    teacher_type_id: Optional[int] = None) -> List[dict]:
        """Get state teacher education data with optional filters"""
        return fetch_dataset(session, TEACHER_EDUCATION, "state", year, type_id=teacher_type_id)

    def get_state_teacher_average_salary(self, session: Session, year: Optional[int] = None) -> List[dict]:
        """Get state teacher average salary data with optional filters"""
        return fetch_dataset(session, TEACHER_AVERAGE_SALARY, "state", year)

    def get_state_teacher_salary_band(self, session: Session, year: Optional[int] = None,
                                      salary_band_type_id: Optional[int] = None) -> List[dict]:
        """Get state teacher salary band data with optional filters"""
        return fetch_dataset(session, STATE_TEACHER_SALARY_BAND, "state", year, type_id=salary_band_type_id)


staff_service = StaffService()
