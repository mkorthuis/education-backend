from sqlmodel import Field, Relationship, SQLModel
from .base import BaseMixin
from .location import School, Grade, Town
from typing import Optional, List, TYPE_CHECKING

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