from decimal import Decimal
from sqlmodel import Field, Relationship, SQLModel
from .base import BaseMixin
from .location import School, Grade, Town
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .location import Town

class SchoolEnrollment(BaseMixin, table=True):
    __tablename__ = "school_enrollment"
    
    school_id_fk: int = Field(foreign_key="school.id")
    grade_id_fk: int = Field(foreign_key="grades.id")
    year: int
    enrollment: int
    
    school: School = Relationship()
    grade: Grade = Relationship() 

class TownEnrollment(BaseMixin, table=True):
    """Town-level enrollment data by grade and year"""
    __tablename__ = "town_enrollment"
    
    town_id_fk: int = Field(foreign_key="town.id")
    grade_id_fk: int = Field(foreign_key="grades.id")
    year: int = Field(index=True)
    enrollment: int
    
    town: Town = Relationship()
    grade: Grade = Relationship()

class StateEnrollmentLevel(BaseMixin, table=True):
    """Statewide average daily membership by school level (elementary, middle, high) and in total"""
    __tablename__ = "state_enrollment_level"
    
    year: int = Field(index=True)
    elementary: Optional[float] = Field(default=None)
    middle: Optional[float] = Field(default=None)
    high: Optional[float] = Field(default=None)
    total: Optional[float] = Field(default=None)

class TownEnrollmentState(SQLModel, table=True):
    """Materialized view for state-level town enrollment data aggregated by year and grade."""
    __tablename__ = "town_enrollment_state"
    
    # This is a materialized view, so we need to define the primary key fields
    year: int = Field(primary_key=True)
    grade_id_fk: int = Field(primary_key=True)
    total_enrollment: int
    
    # One-way relationship to Grade
    grade: Grade = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "TownEnrollmentState.grade_id_fk",
            "primaryjoin": "TownEnrollmentState.grade_id_fk == Grade.id",
            "viewonly": True
        }
    ) 

# -------------------- Free and reduced-price lunch eligibility --------------------
# K-12 students, and those eligible for free or reduced-price lunch, as of October 1

class SchoolReducedLunch(BaseMixin, table=True):
    __tablename__ = "school_reduced_lunch"

    school_id_fk: int = Field(foreign_key="school.id")
    year: int
    enrollment: Optional[int] = None
    eligible: Optional[int] = None


class DistrictReducedLunch(BaseMixin, table=True):
    __tablename__ = "district_reduced_lunch"

    district_id_fk: int = Field(foreign_key="district.id")
    year: int
    enrollment: Optional[int] = None
    eligible: Optional[int] = None


class StateReducedLunch(BaseMixin, table=True):
    __tablename__ = "state_reduced_lunch"

    year: int
    enrollment: Optional[int] = None
    eligible: Optional[int] = None


# -------------------- English learners --------------------
# Students enrolled, English learners (eligible) and former English learners being monitored,
# as of October 1; the state reports them by district only

class DistrictEnglishLearner(BaseMixin, table=True):
    __tablename__ = "district_english_learner"

    district_id_fk: int = Field(foreign_key="district.id")
    year: int
    enrollment: Optional[int] = None
    eligible: Optional[int] = None
    monitor: Optional[int] = None


class StateEnglishLearner(BaseMixin, table=True):
    __tablename__ = "state_english_learner"

    year: int
    enrollment: Optional[int] = None
    eligible: Optional[int] = None
    monitor: Optional[int] = None


# -------------------- October 1 enrollment by type of school --------------------

class EnrollmentType(BaseMixin, table=True):
    """A type of school in the state's enrollment totals, such as Public Charter Schools"""
    __tablename__ = "enrollment_type"

    name: str = Field(max_length=255)


class StateEnrollmentType(BaseMixin, table=True):
    """Statewide October 1 enrollment by type of school and grade"""
    __tablename__ = "state_enrollment_type"

    year: int
    enrollment_type_id_fk: int = Field(foreign_key="enrollment_type.id")
    grade_id_fk: int = Field(foreign_key="grades.id")
    enrollment: int


class SchoolPrivateSurvey(BaseMixin, table=True):
    """A private school's answers to the NCES Private School Survey for a school year (by its end)"""
    __tablename__ = "school_private_survey"

    school_id_fk: int = Field(foreign_key="school.id")
    year: int
    ppin: str
    # The codebook's labels
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
    teachers_fte: Optional[Decimal] = None
    students_per_teacher: Optional[Decimal] = None
    school_day_hours: Optional[Decimal] = None
    pct_american_indian: Optional[Decimal] = None
    pct_asian: Optional[Decimal] = None
    pct_pacific_islander: Optional[Decimal] = None
    pct_hispanic: Optional[Decimal] = None
    pct_white: Optional[Decimal] = None
    pct_black: Optional[Decimal] = None
    pct_two_or_more_races: Optional[Decimal] = None


class SchoolPrivateSurveyGrade(BaseMixin, table=True):
    """A private school's students in a grade, as it answered the Private School Survey"""
    __tablename__ = "school_private_survey_grade"

    school_id_fk: int = Field(foreign_key="school.id")
    year: int
    grade_id_fk: int = Field(foreign_key="grades.id")
    students: int


class SchoolPrivateEnrollmentTotal(BaseMixin, table=True):
    """A private school's ungraded students and total on October 1, from NHED's nonpublic enrollment report"""
    __tablename__ = "school_private_enrollment_total"

    school_id_fk: int = Field(foreign_key="school.id")
    year: int
    ungraded_elementary: int
    ungraded_secondary: int
    total: int


class SchoolPrivateEnrollment(BaseMixin, table=True):
    """A private school's students in a grade on October 1; apart from the public schools' school_enrollment"""
    __tablename__ = "school_private_enrollment"

    school_id_fk: int = Field(foreign_key="school.id")
    grade_id_fk: int = Field(foreign_key="grades.id")
    year: int
    enrollment: int
