from pydantic import BaseModel
from typing import Optional


class DistrictClassSizeGet(BaseModel):
    id: int
    district_id: int
    year: int
    grades_1_2: Optional[float] = None
    grades_3_4: Optional[float] = None
    grades_5_8: Optional[float] = None
    all_grades: Optional[float] = None


class SchoolClassSizeGet(BaseModel):
    id: int
    school_id: int
    district_id: Optional[int] = None  # Included for filtering convenience
    year: int
    grades_1_2: Optional[float] = None
    grades_3_4: Optional[float] = None
    grades_5_8: Optional[float] = None
    all_grades: Optional[float] = None


class StateClassSizeGet(BaseModel):
    id: int
    year: int
    grades_1_2: Optional[float] = None
    grades_3_4: Optional[float] = None
    grades_5_8: Optional[float] = None
    all_grades: Optional[float] = None 