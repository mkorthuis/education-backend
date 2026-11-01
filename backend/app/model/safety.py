from typing import Optional
from sqlmodel import Field, SQLModel
from .base import BaseMixin


# -------------------- Type/Classification Models --------------------

class SafetySafetyType(BaseMixin, table=True):
    __tablename__ = "safety_safety_type"
    
    name: str = Field(max_length=255)
    description: Optional[str] = None


class SafetyDisciplineIncidentType(BaseMixin, table=True):
    __tablename__ = "safety_discipline_incident_type"
    
    name: str = Field(max_length=255)
    description: Optional[str] = None


class SafetyDisciplineCountType(BaseMixin, table=True):
    __tablename__ = "safety_discipline_count_type"
    
    name: str = Field(max_length=255)
    description: Optional[str] = None


class SafetyBullyingType(BaseMixin, table=True):
    __tablename__ = "safety_bullying_type"
    
    name: str = Field(max_length=255)
    description: Optional[str] = None


class SafetyBullyingClassificationType(BaseMixin, table=True):
    __tablename__ = "safety_bullying_classification_type"
    
    name: str = Field(max_length=255)
    description: Optional[str] = None


class SafetyBullyingImpactType(BaseMixin, table=True):
    __tablename__ = "safety_bullying_impact_type"
    
    name: str = Field(max_length=255)
    description: Optional[str] = None


class SafetyHarassmentClassification(BaseMixin, table=True):
    __tablename__ = "safety_harassment_classification"
    
    name: str = Field(max_length=255)
    description: Optional[str] = None

# -------------------- School-level Models --------------------

class SchoolSafety(BaseMixin, table=True):
    __tablename__ = "school_safety"
    
    school_id_fk: int = Field(foreign_key="school.id")
    year: int
    school_safety_type_id_fk: int = Field(foreign_key="safety_safety_type.id")
    count: Optional[int] = None


class SchoolTruancy(BaseMixin, table=True):
    __tablename__ = "school_truancy"
    
    school_id_fk: int = Field(foreign_key="school.id")
    year: int
    count: Optional[int] = None


class SchoolDisciplineIncident(BaseMixin, table=True):
    __tablename__ = "school_discipline_incident"
    
    school_id_fk: int = Field(foreign_key="school.id")
    year: int
    school_discipline_incident_type_id_fk: int = Field(foreign_key="safety_discipline_incident_type.id")
    count: Optional[int] = None


class SchoolDisciplineCount(BaseMixin, table=True):
    __tablename__ = "school_discipline_count"
    
    school_id_fk: int = Field(foreign_key="school.id")
    year: int
    school_discipline_count_type_id_fk: int = Field(foreign_key="safety_discipline_count_type.id")
    count: Optional[int] = None


class SchoolBullying(BaseMixin, table=True):
    __tablename__ = "school_bullying"
    
    school_id_fk: int = Field(foreign_key="school.id")
    year: int
    school_bullying_type_id_fk: int = Field(foreign_key="safety_bullying_type.id")
    reported: Optional[int] = None
    investigated_actual: Optional[int] = None


class SchoolBullyingClassification(BaseMixin, table=True):
    __tablename__ = "school_bullying_classification"
    
    school_id_fk: int = Field(foreign_key="school.id")
    year: int
    school_bullying_classification_type_id_fk: int = Field(foreign_key="safety_bullying_classification_type.id")
    count: Optional[int] = None


class SchoolBullyingImpact(BaseMixin, table=True):
    __tablename__ = "school_bullying_impact"
    
    school_id_fk: int = Field(foreign_key="school.id")
    year: int
    school_bullying_impact_type_id_fk: int = Field(foreign_key="safety_bullying_impact_type.id")
    count: Optional[int] = None


class SchoolHarassment(BaseMixin, table=True):
    __tablename__ = "school_harassment"
    
    school_id_fk: int = Field(foreign_key="school.id")
    year: int
    school_harassment_classification_id_fk: int = Field(foreign_key="safety_harassment_classification.id")
    incident_count: Optional[int] = None
    student_impact_count: Optional[int] = None
    student_engaged_count: Optional[int] = None


class SchoolRestraint(BaseMixin, table=True):
    __tablename__ = "school_restraint"
    
    school_id_fk: int = Field(foreign_key="school.id")
    year: int
    generated: Optional[int] = None
    active_investigation: Optional[int] = None
    closed_investigation: Optional[int] = None
    bodily_injury: Optional[int] = None
    serious_injury: Optional[int] = None


class SchoolSeclusion(BaseMixin, table=True):
    __tablename__ = "school_seclusion"
    
    school_id_fk: int = Field(foreign_key="school.id")
    year: int
    generated: Optional[int] = None
    active_investigation: Optional[int] = None
    closed_investigation: Optional[int] = None


# -------------------- State-level Models --------------------

class StateTruancy(BaseMixin, table=True):
    __tablename__ = "state_truancy"
    
    year: int
    count: Optional[int] = None


class StateSafety(BaseMixin, table=True):
    __tablename__ = "state_safety"
    
    year: int
    school_safety_type_id_fk: int = Field(foreign_key="safety_safety_type.id")
    count: Optional[int] = None


class StateDisciplineIncident(BaseMixin, table=True):
    __tablename__ = "state_discipline_incident"
    
    year: int
    school_discipline_incident_type_id_fk: int = Field(foreign_key="safety_discipline_incident_type.id")
    count: Optional[int] = None


class StateDisciplineCount(BaseMixin, table=True):
    __tablename__ = "state_discipline_count"
    
    year: int
    school_discipline_count_type_id_fk: int = Field(foreign_key="safety_discipline_count_type.id")
    count: Optional[int] = None


class StateBullying(BaseMixin, table=True):
    __tablename__ = "state_bullying"
    
    year: int
    school_bullying_type_id_fk: int = Field(foreign_key="safety_bullying_type.id")
    reported: Optional[int] = None
    investigated_actual: Optional[int] = None


class StateBullyingClassification(BaseMixin, table=True):
    __tablename__ = "state_bullying_classification"
    
    year: int
    school_bullying_classification_type_id_fk: int = Field(foreign_key="safety_bullying_classification_type.id")
    count: Optional[int] = None


class StateBullyingImpact(BaseMixin, table=True):
    __tablename__ = "state_bullying_impact"
    
    year: int
    school_bullying_impact_type_id_fk: int = Field(foreign_key="safety_bullying_impact_type.id")
    count: Optional[int] = None


class StateHarassment(BaseMixin, table=True):
    __tablename__ = "state_harassment"
    
    year: int
    school_harassment_classification_id_fk: int = Field(foreign_key="safety_harassment_classification.id")
    incident_count: Optional[int] = None
    student_impact_count: Optional[int] = None
    student_engaged_count: Optional[int] = None


class StateRestraint(BaseMixin, table=True):
    __tablename__ = "state_restraint"
    
    year: int
    generated: Optional[int] = None
    active_investigation: Optional[int] = None
    closed_investigation: Optional[int] = None
    bodily_injury: Optional[int] = None
    serious_injury: Optional[int] = None


class StateSeclusion(BaseMixin, table=True):
    __tablename__ = "state_seclusion"
    
    year: int
    generated: Optional[int] = None
    active_investigation: Optional[int] = None
    closed_investigation: Optional[int] = None


# -------------------- District-level Models --------------------

class DistrictTruancy(BaseMixin, table=True):
    __tablename__ = "district_truancy"
    
    district_id_fk: int = Field(foreign_key="district.id")
    year: int
    count: Optional[int] = None


class DistrictSafety(BaseMixin, table=True):
    __tablename__ = "district_safety"
    
    district_id_fk: int = Field(foreign_key="district.id")
    year: int
    school_safety_type_id_fk: int = Field(foreign_key="safety_safety_type.id")
    count: Optional[int] = None


class DistrictDisciplineIncident(BaseMixin, table=True):
    __tablename__ = "district_discipline_incident"
    
    district_id_fk: int = Field(foreign_key="district.id")
    year: int
    school_discipline_incident_type_id_fk: int = Field(foreign_key="safety_discipline_incident_type.id")
    count: Optional[int] = None


class DistrictDisciplineCount(BaseMixin, table=True):
    __tablename__ = "district_discipline_count"
    
    district_id_fk: int = Field(foreign_key="district.id")
    year: int
    school_discipline_count_type_id_fk: int = Field(foreign_key="safety_discipline_count_type.id")
    count: Optional[int] = None


class DistrictBullying(BaseMixin, table=True):
    __tablename__ = "district_bullying"
    
    district_id_fk: int = Field(foreign_key="district.id")
    year: int
    school_bullying_type_id_fk: int = Field(foreign_key="safety_bullying_type.id")
    reported: Optional[int] = None
    investigated_actual: Optional[int] = None


class DistrictBullyingClassification(BaseMixin, table=True):
    __tablename__ = "district_bullying_classification"
    
    district_id_fk: int = Field(foreign_key="district.id")
    year: int
    school_bullying_classification_type_id_fk: int = Field(foreign_key="safety_bullying_classification_type.id")
    count: Optional[int] = None


class DistrictBullyingImpact(BaseMixin, table=True):
    __tablename__ = "district_bullying_impact"
    
    district_id_fk: int = Field(foreign_key="district.id")
    year: int
    school_bullying_impact_type_id_fk: int = Field(foreign_key="safety_bullying_impact_type.id")
    count: Optional[int] = None


class DistrictHarassment(BaseMixin, table=True):
    __tablename__ = "district_harassment"
    
    district_id_fk: int = Field(foreign_key="district.id")
    year: int
    school_harassment_classification_id_fk: int = Field(foreign_key="safety_harassment_classification.id")
    incident_count: Optional[int] = None
    student_impact_count: Optional[int] = None
    student_engaged_count: Optional[int] = None


class DistrictRestraint(BaseMixin, table=True):
    __tablename__ = "district_restraint"
    
    district_id_fk: int = Field(foreign_key="district.id")
    year: int
    generated: Optional[int] = None
    active_investigation: Optional[int] = None
    closed_investigation: Optional[int] = None
    bodily_injury: Optional[int] = None
    serious_injury: Optional[int] = None


class DistrictSeclusion(BaseMixin, table=True):
    __tablename__ = "district_seclusion"
    
    district_id_fk: int = Field(foreign_key="district.id")
    year: int
    generated: Optional[int] = None
    active_investigation: Optional[int] = None
    closed_investigation: Optional[int] = None


# -------------------- Materialized View Models --------------------

class SchoolSafetyEnrollment(SQLModel, table=True):
    """Materialized view for school safety enrollment data."""
    __tablename__ = "school_safety_enrollment"
    
    # This is a materialized view, so we need to define primary key
    school_id_fk: int = Field(primary_key=True)
    year: int = Field(primary_key=True)
    total_enrollment: Optional[int] = None


class StateSafetyEnrollment(SQLModel, table=True):
    """Materialized view for state safety enrollment data."""
    __tablename__ = "state_safety_enrollment"
    
    # This is a materialized view, so we need to define primary key
    year: int = Field(primary_key=True)
    total_enrollment: Optional[int] = None


class DistrictSafetyEnrollment(SQLModel, table=True):
    """Materialized view for district safety enrollment data."""
    __tablename__ = "district_safety_enrollment"
    
    # This is a materialized view, so we need to define primary key
    district_id_fk: int = Field(primary_key=True)
    year: int = Field(primary_key=True)
    total_enrollment: Optional[int] = None
    