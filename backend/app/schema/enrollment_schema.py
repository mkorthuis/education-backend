from typing import List, Optional, Dict
from pydantic import BaseModel, Field
from app.schema.location_schema import GradeGet, SchoolGet

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
