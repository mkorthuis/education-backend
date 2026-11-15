from typing import Optional

from sqlmodel import Field

from .base import BaseMixin


# -------------------- NAEP (the Nation's Report Card) --------------------

class Jurisdiction(BaseMixin, table=True):
    """A place NAEP reports on, by NAEP's code: a state, DC, DoDEA (DS) or the national public average (NP)"""
    __tablename__ = "jurisdiction"

    code: str = Field(max_length=4)
    name: str = Field(max_length=255)
    kind: str = Field(max_length=20)  # state, nation or other


class NaepMeasure(BaseMixin, table=True):
    """What a NAEP figure measures, by NAEP's stattype code (MN:MN is the average scale score)"""
    __tablename__ = "naep_measure"

    code: str = Field(max_length=10)
    name: str = Field(max_length=255)
    unit: str = Field(max_length=20)  # score or percent


class NaepStudentGroup(BaseMixin, table=True):
    """A NAEP student group, by NAEP's variable and value (TOTAL, 1 is all students; GENDER, 2 is female)"""
    __tablename__ = "naep_student_group"

    variable: str = Field(max_length=20)
    value: str = Field(max_length=10)
    variable_name: str = Field(max_length=255)  # e.g. Sex, Economic status
    name: str = Field(max_length=255)


class NaepResult(BaseMixin, table=True):
    """One NAEP figure: a measure for a place, subject, grade, student group and year"""
    __tablename__ = "naep_result"

    year: int
    jurisdiction_id_fk: int = Field(foreign_key="jurisdiction.id")
    assessment_subject_id_fk: int = Field(foreign_key="assessment_subject.id")
    grade_id_fk: int = Field(foreign_key="grades.id")
    naep_measure_id_fk: int = Field(foreign_key="naep_measure.id")
    naep_student_group_id_fk: int = Field(foreign_key="naep_student_group.id")
    value: Optional[float] = None  # unrounded; null when NAEP's reporting standards weren't met
    is_displayable: bool = True


class NaepComparison(BaseMixin, table=True):
    """NAEP's significance test of one place and year against another place (same year) or another
    year (same place). basis is all_jurisdictions when NAEP adjusted for comparing many places at once,
    pair when only the two were compared; result is the first place or year against the other."""
    __tablename__ = "naep_comparison"

    year: int
    jurisdiction_id_fk: int = Field(foreign_key="jurisdiction.id")
    other_year: int
    other_jurisdiction_id_fk: int = Field(foreign_key="jurisdiction.id")
    assessment_subject_id_fk: int = Field(foreign_key="assessment_subject.id")
    grade_id_fk: int = Field(foreign_key="grades.id")
    naep_measure_id_fk: int = Field(foreign_key="naep_measure.id")
    naep_student_group_id_fk: int = Field(foreign_key="naep_student_group.id")
    basis: str = Field(max_length=20)  # all_jurisdictions or pair
    result: str = Field(max_length=20)  # higher, lower or not_significant
    difference: Optional[float] = None


class NaepStateStandard(BaseMixin, table=True):
    """NCES's state mapping study: a state's standard for proficient performance on its own test, placed on the NAEP
    scale (the NAEP score the same share of the state's students reached), for one NCES table, subject and grade"""
    __tablename__ = "naep_state_standard"

    year: int
    jurisdiction_id_fk: int = Field(foreign_key="jurisdiction.id")
    assessment_subject_id_fk: int = Field(foreign_key="assessment_subject.id")
    grade_id_fk: int = Field(foreign_key="grades.id")
    # NCES's table: <year>a/b, the per-year tables (2009 to 2022, unrounded); 1a/b, 2a/b, 3a/b, the 2005–2009
    # comparison study's (2009, 2007, 2005, rounded), so 2009 has both
    nces_table: str = Field(max_length=10)
    naep_equivalent: Optional[float] = None  # none when NCES left the state out
    standard_error: Optional[float] = None
    relative_error: Optional[float] = None  # the 2005–2009 study's tables print only the caution mark
    caution: bool = False  # NCES's mark: relative error greater than 0.5
    testing_program: Optional[str] = Field(default=None, max_length=10)  # SBAC, PARCC or ACT, from 2015; none: the state's own test
    note: Optional[str] = None  # NCES's footnotes on the state
