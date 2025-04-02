from sqlmodel import Field, Relationship
from .base import BaseMixin
from .location import School, Grade

class SchoolEnrollment(BaseMixin, table=True):
    __tablename__ = "school_enrollment"
    
    school_id_fk: int = Field(foreign_key="school.id")
    grade_id_fk: int = Field(foreign_key="grades.id")
    year: int
    enrollment: int
    
    school: School = Relationship()
    grade: Grade = Relationship() 