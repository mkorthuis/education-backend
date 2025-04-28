from typing import Optional, List, TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel
from decimal import Decimal
from .base import BaseMixin

# Use TYPE_CHECKING to avoid circular imports
if TYPE_CHECKING:
    from .location import School, District


# -------------------- Type/Classification Models --------------------

class SchoolStaffType(BaseMixin, table=True):
    __tablename__ = "school_staff_type"
    
    name: str = Field(max_length=255)
    
    # Relationships
    district_staff_records: List["DistrictStaff"] = Relationship(back_populates="staff_type")
    state_staff_records: List["StateStaff"] = Relationship(back_populates="staff_type")


class TeacherEducationType(BaseMixin, table=True):
    __tablename__ = "teacher_education_type"
    
    name: str = Field(max_length=255)
    
    # Relationships
    district_teacher_education_records: List["DistrictTeacherEducation"] = Relationship(back_populates="teacher_type")
    state_teacher_education_records: List["StateTeacherEducation"] = Relationship(back_populates="teacher_type")


class TeacherSalaryBandType(BaseMixin, table=True):
    __tablename__ = "teacher_salary_band_type"
    
    name: str = Field(max_length=255)
    description: Optional[str] = None
    
    # Relationships
    district_teacher_salary_bands: List["DistrictTeacherSalaryBand"] = Relationship(back_populates="salary_band_type")
    state_teacher_salary_bands: List["StateTeacherSalaryBand"] = Relationship(back_populates="salary_band_type")


# -------------------- District-level Models --------------------

class DistrictStaff(BaseMixin, table=True):
    __tablename__ = "district_staff"
    
    school_staff_type_id_fk: int = Field(foreign_key="school_staff_type.id")
    district_id_fk: int = Field(foreign_key="district.id")
    year: int
    value: Optional[float] = None
    
    # Relationships
    staff_type: SchoolStaffType = Relationship(
        back_populates="district_staff_records",
        sa_relationship_kwargs={"foreign_keys": "DistrictStaff.school_staff_type_id_fk"}
    )
    # One-way relationship to District - no inverse relationship
    district: "District" = Relationship(
        sa_relationship_kwargs={"foreign_keys": "DistrictStaff.district_id_fk", "viewonly": True}
    )


class DistrictTeacherEducation(BaseMixin, table=True):
    __tablename__ = "district_teacher_education"
    
    teacher_type_id_fk: int = Field(foreign_key="teacher_education_type.id")
    district_id_fk: int = Field(foreign_key="district.id")
    year: int
    value: Optional[float] = None
    
    # Relationships
    teacher_type: TeacherEducationType = Relationship(
        back_populates="district_teacher_education_records",
        sa_relationship_kwargs={"foreign_keys": "DistrictTeacherEducation.teacher_type_id_fk"}
    )
    # One-way relationship to District - no inverse relationship
    district: "District" = Relationship(
        sa_relationship_kwargs={"foreign_keys": "DistrictTeacherEducation.district_id_fk", "viewonly": True}
    )


class DistrictTeacherAverageSalary(BaseMixin, table=True):
    __tablename__ = "district_teacher_average_salary"
    
    district_id_fk: int = Field(foreign_key="district.id")
    year: int
    salary: Optional[float] = None
    
    # One-way relationship to District - no inverse relationship
    district: "District" = Relationship(
        sa_relationship_kwargs={"foreign_keys": "DistrictTeacherAverageSalary.district_id_fk", "viewonly": True}
    )


class DistrictTeacherSalaryBand(BaseMixin, table=True):
    __tablename__ = "district_teacher_salary_band"
    
    district_id_fk: int = Field(foreign_key="district.id")
    teacher_salary_band_type_id_fk: int = Field(foreign_key="teacher_salary_band_type.id")
    year: int
    min_salary: Optional[float] = None
    max_salary: Optional[float] = None
    steps: Optional[int] = None
    
    # Relationships
    salary_band_type: TeacherSalaryBandType = Relationship(
        back_populates="district_teacher_salary_bands",
        sa_relationship_kwargs={"foreign_keys": "DistrictTeacherSalaryBand.teacher_salary_band_type_id_fk"}
    )
    # One-way relationship to District - no inverse relationship
    district: "District" = Relationship(
        sa_relationship_kwargs={"foreign_keys": "DistrictTeacherSalaryBand.district_id_fk", "viewonly": True}
    )


# -------------------- State-level Models --------------------

class StateStaff(BaseMixin, table=True):
    __tablename__ = "state_staff"
    
    school_staff_type_id_fk: int = Field(foreign_key="school_staff_type.id")
    year: int
    value: Optional[float] = None
    
    # Relationships
    staff_type: SchoolStaffType = Relationship(
        back_populates="state_staff_records",
        sa_relationship_kwargs={"foreign_keys": "StateStaff.school_staff_type_id_fk"}
    )


class StateTeacherEducation(BaseMixin, table=True):
    __tablename__ = "state_teacher_education"
    
    teacher_type_id_fk: int = Field(foreign_key="teacher_education_type.id")
    year: int
    value: Optional[float] = None
    
    # Relationships
    teacher_type: TeacherEducationType = Relationship(
        back_populates="state_teacher_education_records",
        sa_relationship_kwargs={"foreign_keys": "StateTeacherEducation.teacher_type_id_fk"}
    )


class StateTeacherAverageSalary(BaseMixin, table=True):
    __tablename__ = "state_teacher_average_salary"
    
    year: int
    salary: Optional[float] = None


# -------------------- Materialized View Models --------------------

class StateTeacherSalaryBand(SQLModel, table=True):
    """Materialized view for state teacher salary band data."""
    __tablename__ = "state_teacher_salary_band"
    
    # This is a materialized view, so we need to define primary key
    teacher_salary_band_type_id_fk: int = Field(primary_key=True, foreign_key="teacher_salary_band_type.id")
    year: int = Field(primary_key=True)
    min_salary: Optional[float] = None
    max_salary: Optional[float] = None
    steps: Optional[float] = None
    date_created: Optional[str] = None
    date_updated: Optional[str] = None
    
    # Relationships
    salary_band_type: TeacherSalaryBandType = Relationship(
        sa_relationship_kwargs={
            "foreign_keys": "StateTeacherSalaryBand.teacher_salary_band_type_id_fk", 
            "primaryjoin": "StateTeacherSalaryBand.teacher_salary_band_type_id_fk == TeacherSalaryBandType.id",
            "viewonly": True
        }
    ) 