from pydantic import BaseModel
from typing import Optional, List


class SchoolStaffTypeGet(BaseModel):
    id: int
    name: str


class TeacherEducationTypeGet(BaseModel):
    id: int
    name: str


class TeacherSalaryBandTypeGet(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


class DistrictStaffGet(BaseModel):
    id: int
    district_id: int
    year: int
    value: Optional[float] = None
    staff_type: Optional[SchoolStaffTypeGet] = None


class StateStaffGet(BaseModel):
    id: int
    year: int
    value: Optional[float] = None
    staff_type: Optional[SchoolStaffTypeGet] = None


class DistrictTeacherEducationGet(BaseModel):
    id: int
    district_id: int
    year: int
    value: Optional[float] = None
    teacher_type: Optional[TeacherEducationTypeGet] = None


class StateTeacherEducationGet(BaseModel):
    id: int
    year: int
    value: Optional[float] = None
    teacher_type: Optional[TeacherEducationTypeGet] = None


class DistrictTeacherAverageSalaryGet(BaseModel):
    id: int
    district_id: int
    year: int
    salary: Optional[float] = None


class StateTeacherAverageSalaryGet(BaseModel):
    id: int
    year: int
    salary: Optional[float] = None


class DistrictTeacherSalaryBandGet(BaseModel):
    id: int
    district_id: int
    year: int
    min_salary: Optional[float] = None
    max_salary: Optional[float] = None
    steps: Optional[int] = None
    salary_band_type: Optional[TeacherSalaryBandTypeGet] = None


class StateTeacherSalaryBandGet(BaseModel):
    teacher_salary_band_type_id: int
    year: int
    min_salary: Optional[float] = None
    max_salary: Optional[float] = None
    steps: Optional[float] = None
    salary_band_type: Optional[TeacherSalaryBandTypeGet] = None 