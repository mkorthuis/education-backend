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

class StateEnrollment(BaseMixin, table=True):
    """State-level enrollment data by year and grade level"""
    __tablename__ = "state_enrollment"
    
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
