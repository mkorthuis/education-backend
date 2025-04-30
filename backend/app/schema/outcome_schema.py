from typing import Optional
from pydantic import BaseModel, Field

# -------------------- Post-Graduation Schemas --------------------

class PostGraduationTypeGet(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


class SchoolPostGraduationGet(BaseModel):
    id: int
    school_id: int
    year: int
    value: int
    post_graduation_type: PostGraduationTypeGet


class StatePostGraduationGet(BaseModel):
    id: int
    year: int
    value: int
    post_graduation_type: PostGraduationTypeGet


# -------------------- Early Exit Schemas --------------------

class SchoolEarlyExitGet(BaseModel):
    id: int
    school_id: int
    year: int

    adjusted_fall_enrollment: Optional[int] = None
    earned_hiset: Optional[int] = None
    enrolled_in_college: Optional[int] = None
    dropped_out: Optional[int] = None
    missing: Optional[int] = None

    annual_early_exit_percentage: Optional[float] = None
    four_year_early_exit_percentage: Optional[float] = None
    annual_dropout_percentage: Optional[float] = None
    four_year_dropout_percentage: Optional[float] = None


class StateEarlyExitGet(BaseModel):
    id: int
    year: int

    adjusted_fall_enrollment: Optional[int] = None
    earned_hiset: Optional[int] = None
    enrolled_in_college: Optional[int] = None
    dropped_out: Optional[int] = None
    missing: Optional[int] = None

    annual_early_exit_percentage: Optional[float] = None
    four_year_early_exit_percentage: Optional[float] = None
    annual_dropout_percentage: Optional[float] = None
    four_year_dropout_percentage: Optional[float] = None


# -------------------- Cohort Graduation Schemas --------------------

class SchoolGraduationCohortGet(BaseModel):
    id: int
    school_id: int
    year: int

    cohort_size: Optional[int] = None
    graduate: Optional[int] = None
    earned_hiset: Optional[int] = None
    dropped_out: Optional[int] = None


class StateGraduationCohortGet(BaseModel):
    id: int
    year: int

    cohort_size: Optional[int] = None
    graduate: Optional[int] = None
    earned_hiset: Optional[int] = None
    dropped_out: Optional[int] = None


# -------------------- District Post-Graduation Schema --------------------

class DistrictPostGraduationGet(BaseModel):
    district_id: int
    year: int
    value: int
    post_graduation_type: PostGraduationTypeGet


# -------------------- District Early Exit Schema --------------------

class DistrictEarlyExitGet(BaseModel):
    district_id: int
    year: int

    adjusted_fall_enrollment: Optional[int] = None
    earned_hiset: Optional[int] = None
    enrolled_in_college: Optional[int] = None
    dropped_out: Optional[int] = None
    missing: Optional[int] = None

    annual_early_exit_percentage: Optional[float] = None
    four_year_early_exit_percentage: Optional[float] = None
    annual_dropout_percentage: Optional[float] = None
    four_year_dropout_percentage: Optional[float] = None


# -------------------- District Cohort Graduation Schema --------------------

class DistrictGraduationCohortGet(BaseModel):
    district_id: int
    year: int

    cohort_size: Optional[int] = None
    graduate: Optional[int] = None
    earned_hiset: Optional[int] = None
    dropped_out: Optional[int] = None 