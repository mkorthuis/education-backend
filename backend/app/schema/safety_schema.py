from pydantic import BaseModel, Field
from typing import Optional, List


class SchoolSafetyTypeGet(BaseModel):
    id: int
    name: str


class DisciplineIncidentTypeGet(BaseModel):
    id: int
    name: str


class DisciplineCountTypeGet(BaseModel):
    id: int
    name: str


class BullyingTypeGet(BaseModel):
    id: int
    name: str


class BullyingClassificationTypeGet(BaseModel):
    id: int
    name: str


class BullyingImpactTypeGet(BaseModel):
    id: int
    name: str


class HarassmentClassificationGet(BaseModel):
    id: int
    name: str


class SchoolSafetyGet(BaseModel):
    id: int
    school_id: int
    year: int
    count: Optional[int] = None
    safety_type: Optional[SchoolSafetyTypeGet] = None


class TruancyGet(BaseModel):
    id: int
    school_id: int
    year: int
    count: Optional[int] = None


class DisciplineIncidentGet(BaseModel):
    id: int
    school_id: int
    year: int
    count: Optional[int] = None
    incident_type: Optional[DisciplineIncidentTypeGet] = None


class DisciplineCountGet(BaseModel):
    id: int
    school_id: int
    year: int
    count: Optional[int] = None
    count_type: Optional[DisciplineCountTypeGet] = None


class BullyingGet(BaseModel):
    id: int
    school_id: int
    year: int
    reported: Optional[int] = None
    investigated_actual: Optional[int] = None
    bullying_type: Optional[BullyingTypeGet] = None


class BullyingClassificationGet(BaseModel):
    id: int
    school_id: int
    year: int
    count: Optional[int] = None
    classification_type: Optional[BullyingClassificationTypeGet] = None


class BullyingImpactGet(BaseModel):
    id: int
    school_id: int
    year: int
    count: Optional[int] = None
    impact_type: Optional[BullyingImpactTypeGet] = None


class HarassmentGet(BaseModel):
    id: int
    school_id: int
    year: int
    incident_count: Optional[int] = None
    student_impact_count: Optional[int] = None
    student_engaged_count: Optional[int] = None
    classification: Optional[HarassmentClassificationGet] = None


class RestraintGet(BaseModel):
    id: int
    school_id: int
    year: int
    generated: Optional[int] = None
    active_investigation: Optional[int] = None
    closed_investigation: Optional[int] = None
    bodily_injury: Optional[int] = None
    serious_injury: Optional[int] = None


class SeclusionGet(BaseModel):
    id: int
    school_id: int
    year: int
    generated: Optional[int] = None
    active_investigation: Optional[int] = None
    closed_investigation: Optional[int] = None 