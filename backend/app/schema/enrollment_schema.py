from typing import Optional
from pydantic import BaseModel, Field
from app.schema.location_schema import GradeGet
from datetime import datetime

class SchoolEnrollmentGet(BaseModel):
    id: int
    school_id_fk: int = Field(alias='school_id')
    grade_id_fk: int = Field(alias='grade_id')
    year: int
    enrollment: int
    grade: Optional[GradeGet] = None

    class Config:
        from_attributes = True
        populate_by_name = True

class TownEnrollmentGet(BaseModel):
    id: int
    town_id_fk: int = Field(alias='town_id')
    grade_id_fk: int = Field(alias='grade_id')
    year: int
    enrollment: int
    grade: Optional[GradeGet] = None

    class Config:
        from_attributes = True
        populate_by_name = True

class TownEnrollmentStateGet(BaseModel):
    """Schema for town enrollment state materialized view data"""
    year: int
    grade_id_fk: int = Field(alias='grade_id')
    total_enrollment: int
    grade: Optional[GradeGet] = None

    class Config:
        from_attributes = True
        populate_by_name = True

class StateSchoolCountGet(BaseModel):
    """How many public schools and school districts had students in kindergarten to grade 12 in a year"""
    year: int
    schools: int
    districts: int

class StateEnrollmentGet(BaseModel):
    """State-level enrollment data by year and grade level"""
    id: int
    year: int
    elementary: Optional[float] = None
    middle: Optional[float] = None
    high: Optional[float] = None
    total: Optional[float] = None
    date_created: datetime
    date_updated: datetime

    class Config:
        from_attributes = True


class SchoolReducedLunchGet(BaseModel):
    """A school's K-12 students and those eligible for free or reduced-price lunch, as of October 1"""
    id: int
    school_id: int
    year: int
    enrollment: Optional[int] = None
    eligible: Optional[int] = None

class DistrictReducedLunchGet(BaseModel):
    """A district's K-12 students and those eligible for free or reduced-price lunch: its schools' sum"""
    id: int
    district_id: int
    year: int
    enrollment: Optional[int] = None
    eligible: Optional[int] = None

class StateReducedLunchGet(BaseModel):
    """Every public school's K-12 students and those eligible for free or reduced-price lunch"""
    id: int
    year: int
    enrollment: Optional[int] = None
    eligible: Optional[int] = None

class DistrictEnglishLearnerGet(BaseModel):
    """A district's students, English learners (eligible) and former English learners being monitored"""
    id: int
    district_id: int
    year: int
    enrollment: Optional[int] = None
    eligible: Optional[int] = None
    monitor: Optional[int] = None

class StateEnglishLearnerGet(BaseModel):
    """Statewide students, English learners (eligible) and former English learners being monitored"""
    id: int
    year: int
    enrollment: Optional[int] = None
    eligible: Optional[int] = None
    monitor: Optional[int] = None


class EnrollmentTypeGet(BaseModel):
    id: int
    name: str

class StateEnrollmentTypeGet(BaseModel):
    """Statewide October 1 enrollment for one type of school and grade"""
    id: int
    year: int
    enrollment_type: EnrollmentTypeGet
    grade: GradeGet
    enrollment: int
