from typing import List, Optional
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


class PrivateSchoolEnrollmentGradeGet(BaseModel):
    grade_id: int
    grade_name: str
    enrollment: int


class PrivateSchoolEnrollmentGet(BaseModel):
    """A private school's students on October 1, from NHED's nonpublic enrollment report"""
    school_id: int
    year: int
    total: int
    ungraded_elementary: int
    ungraded_secondary: int
    # Only the grades with students
    grades: List[PrivateSchoolEnrollmentGradeGet]


class PrivateSchoolSurveyGradeGet(BaseModel):
    grade_id: int
    grade_name: str
    students: int


class PrivateSchoolSurveyGet(BaseModel):
    """A private school's answers to the NCES Private School Survey for a school year"""
    school_id: int
    year: int
    ppin: str
    typology: Optional[str] = None
    affiliation: Optional[str] = None
    religious_orientation: Optional[str] = None
    level: Optional[str] = None
    community_type: Optional[str] = None
    # Kindergarten to grade 12 and ungraded; and with preschool
    students: Optional[int] = None
    students_with_preschool: Optional[int] = None
    male_students: Optional[int] = None
    # The 12th graders the year before, and the share of those graduates who went to a four-year college
    seniors_prior_year: Optional[int] = None
    to_four_year_college_pct: Optional[int] = None
    teachers_fte: Optional[float] = None
    students_per_teacher: Optional[float] = None
    school_day_hours: Optional[float] = None
    pct_american_indian: Optional[float] = None
    pct_asian: Optional[float] = None
    pct_pacific_islander: Optional[float] = None
    pct_hispanic: Optional[float] = None
    pct_white: Optional[float] = None
    pct_black: Optional[float] = None
    pct_two_or_more_races: Optional[float] = None
    grades: List[PrivateSchoolSurveyGradeGet]
