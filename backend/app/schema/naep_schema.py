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
    """A NAEP student group: its variable (e.g. ECONDIS, "Economic status") and category"""
    id: int
    variable: str
    value: str
    variable_name: str
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


class NaepStateStandardGet(BaseModel):
    """NCES's state mapping study: the NAEP score equivalent to a state's standard for proficient performance on its
    own test (the score the same share of the state's students reached). nces_table is NCES's table: <year>a/b for the
    per-year tables (2009 to 2022, unrounded), 1a/b, 2a/b and 3a/b for the 2005–2009 comparison study (2009, 2007 and
    2005, rounded), so 2009 has two rows per state. naep_equivalent is null when NCES left the state out (note says
    why); caution marks a relative error over 0.5."""
    id: int
    year: int
    jurisdiction: JurisdictionGet
    subject: AssessmentSubjectGet
    grade: GradeGet
    nces_table: str
    naep_equivalent: Optional[float] = None
    standard_error: Optional[float] = None
    relative_error: Optional[float] = None
    caution: bool
    testing_program: Optional[str] = None
    note: Optional[str] = None
