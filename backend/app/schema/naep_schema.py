from typing import Optional

from pydantic import BaseModel

from app.schema.assessment_schema import AssessmentSubjectGet
from app.schema.location_schema import GradeGet


class JurisdictionGet(BaseModel):
    """A place NAEP reports on: a state, DC, DoDEA (DS) or the national public average (NP)"""
    id: int
    code: str
    name: str
    kind: str


class NaepMeasureGet(BaseModel):
    id: int
    code: str
    name: str
    unit: str


class NaepStudentGroupGet(BaseModel):
    id: int
    variable: str
    value: str
    name: str


class NaepResultGet(BaseModel):
    """One NAEP figure. value is unrounded (NAEP publishes whole numbers) and null when NAEP's
    reporting standards weren't met (is_displayable false)."""
    id: int
    year: int
    jurisdiction: JurisdictionGet
    subject: AssessmentSubjectGet
    grade: GradeGet
    measure: NaepMeasureGet
    student_group: NaepStudentGroupGet
    value: Optional[float] = None
    is_displayable: bool


class NaepComparisonGet(BaseModel):
    """NAEP's significance test of one place and year against another place or year. result is the
    first against the other: higher, lower or not_significant. basis is all_jurisdictions when NAEP
    adjusted for comparing every state at once (as in its state reports), pair when only the two were
    compared."""
    id: int
    year: int
    jurisdiction: JurisdictionGet
    other_year: int
    other_jurisdiction: JurisdictionGet
    subject: AssessmentSubjectGet
    grade: GradeGet
    measure: NaepMeasureGet
    student_group: NaepStudentGroupGet
    basis: str
    result: str
    difference: Optional[float] = None
