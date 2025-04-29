from typing import Optional
from pydantic import BaseModel, Field

# -------------------- Post-Graduation Schemas --------------------

class PostGraduationTypeGet(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


class SchoolPostGraduationGet(BaseModel):
    id: int
    school_id: int = Field(alias="school_id_fk")
    year: int
    value: int
    post_graduation_type: PostGraduationTypeGet

    class Config:
        populate_by_name = True


class StatePostGraduationGet(BaseModel):
    id: int
    year: int
    value: int
    post_graduation_type: PostGraduationTypeGet


# -------------------- Early Exit Schemas --------------------

class SchoolEarlyExitGet(BaseModel):
    id: int
    school_id: int = Field(alias="school_id_fk")
    year: int

    adjusted_fall_enrollment: Optional[int] = None
    earned_hiset: Optional[int] = None
    enrolled_in_college: Optional[int] = None
    dropped_out: Optional[int] = None
    missing: Optional[int] = None

    annual_early_exit_percentage: Optional[float] = None
    four_year_early_exit_percentage: Optional[float] = Field(alias="4_year_early_exit_percentage", default=None)
    annual_dropout_percentage: Optional[float] = None
    four_year_dropout_percentage: Optional[float] = Field(alias="4_year_dropout_percentage", default=None)

    class Config:
        populate_by_name = True


class StateEarlyExitGet(BaseModel):
    id: int
    year: int

    adjusted_fall_enrollment: Optional[int] = None
    earned_hiset: Optional[int] = None
    enrolled_in_college: Optional[int] = None
    dropped_out: Optional[int] = None
    missing: Optional[int] = None

    annual_early_exit_percentage: Optional[float] = None
    four_year_early_exit_percentage: Optional[float] = Field(alias="4_year_early_exit_percentage", default=None)
    annual_dropout_percentage: Optional[float] = None
    four_year_dropout_percentage: Optional[float] = Field(alias="4_year_dropout_percentage", default=None)

    class Config:
        populate_by_name = True 