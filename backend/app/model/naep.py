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
