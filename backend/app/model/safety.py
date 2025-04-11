from typing import Optional, List, TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel
from .base import BaseMixin

# Use TYPE_CHECKING to avoid circular imports
if TYPE_CHECKING:
    from .location import School


class SchoolSafetyType(BaseMixin, table=True):
    __tablename__ = "school_safety_type"
    
    name: str = Field(max_length=255)
    description: Optional[str] = None
    
    # Relationships
    school_safety_records: List["SchoolSafety"] = Relationship(back_populates="safety_type")


class SchoolSafety(BaseMixin, table=True):
    __tablename__ = "school_safety"
    
    school_id_fk: int = Field(foreign_key="school.id")
    year: int
    school_safety_type_id_fk: int = Field(foreign_key="school_safety_type.id")
    count: Optional[int] = None
    
    # Relationships
    safety_type: SchoolSafetyType = Relationship(
        back_populates="school_safety_records",
        sa_relationship_kwargs={"foreign_keys": "SchoolSafety.school_safety_type_id_fk"}
    )
    # One-way relationship to School - no inverse relationship
    school: "School" = Relationship(
        sa_relationship_kwargs={"foreign_keys": "SchoolSafety.school_id_fk", "viewonly": True}
    )


class SchoolTruancy(BaseMixin, table=True):
    __tablename__ = "school_truancy"
    
    school_id_fk: int = Field(foreign_key="school.id")
    year: int
    count: Optional[int] = None
    
    # One-way relationship to School - no inverse relationship
    school: "School" = Relationship(
        sa_relationship_kwargs={"foreign_keys": "SchoolTruancy.school_id_fk", "viewonly": True}
    )


class SchoolDisciplineIncidentType(BaseMixin, table=True):
    __tablename__ = "school_discipline_incident_type"
    
    name: str = Field(max_length=255)
    description: Optional[str] = None
    
    # Relationships
    discipline_incidents: List["SchoolDisciplineIncident"] = Relationship(back_populates="incident_type")


class SchoolDisciplineIncident(BaseMixin, table=True):
    __tablename__ = "school_discipline_incident"
    
    school_id_fk: int = Field(foreign_key="school.id")
    year: int
    school_discipline_incident_type_id_fk: int = Field(foreign_key="school_discipline_incident_type.id")
    count: Optional[int] = None
    
    # Relationships
    incident_type: SchoolDisciplineIncidentType = Relationship(
        back_populates="discipline_incidents",
        sa_relationship_kwargs={"foreign_keys": "SchoolDisciplineIncident.school_discipline_incident_type_id_fk"}
    )
    # One-way relationship to School - no inverse relationship
    school: "School" = Relationship(
        sa_relationship_kwargs={"foreign_keys": "SchoolDisciplineIncident.school_id_fk", "viewonly": True}
    )


class SchoolDisciplineCountType(BaseMixin, table=True):
    __tablename__ = "school_discipline_count_type"
    
    name: str = Field(max_length=255)
    description: Optional[str] = None
    
    # Relationships
    discipline_counts: List["SchoolDisciplineCount"] = Relationship(back_populates="count_type")


class SchoolDisciplineCount(BaseMixin, table=True):
    __tablename__ = "school_discipline_count"
    
    school_id_fk: int = Field(foreign_key="school.id")
    year: int
    school_discipline_count_type_id_fk: int = Field(foreign_key="school_discipline_count_type.id")
    count: Optional[int] = None
    
    # Relationships
    count_type: SchoolDisciplineCountType = Relationship(
        back_populates="discipline_counts",
        sa_relationship_kwargs={"foreign_keys": "SchoolDisciplineCount.school_discipline_count_type_id_fk"}
    )
    # One-way relationship to School - no inverse relationship
    school: "School" = Relationship(
        sa_relationship_kwargs={"foreign_keys": "SchoolDisciplineCount.school_id_fk", "viewonly": True}
    )


class SchoolBullyingType(BaseMixin, table=True):
    __tablename__ = "school_bullying_type"
    
    name: str = Field(max_length=255)
    description: Optional[str] = None
    
    # Relationships
    bullying_records: List["SchoolBullying"] = Relationship(back_populates="bullying_type")


class SchoolBullying(BaseMixin, table=True):
    __tablename__ = "school_bullying"
    
    school_id_fk: int = Field(foreign_key="school.id")
    year: int
    school_bullying_type_id_fk: int = Field(foreign_key="school_bullying_type.id")
    reported: Optional[int] = None
    investigated_actual: Optional[int] = None
    
    # Relationships
    bullying_type: SchoolBullyingType = Relationship(
        back_populates="bullying_records",
        sa_relationship_kwargs={"foreign_keys": "SchoolBullying.school_bullying_type_id_fk"}
    )
    # One-way relationship to School - no inverse relationship
    school: "School" = Relationship(
        sa_relationship_kwargs={"foreign_keys": "SchoolBullying.school_id_fk", "viewonly": True}
    )


class SchoolBullyingClassificationType(BaseMixin, table=True):
    __tablename__ = "school_bullying_classification_type"
    
    name: str = Field(max_length=255)
    description: Optional[str] = None
    
    # Relationships
    bullying_classifications: List["SchoolBullyingClassification"] = Relationship(back_populates="classification_type")


class SchoolBullyingClassification(BaseMixin, table=True):
    __tablename__ = "school_bullying_classification"
    
    school_id_fk: int = Field(foreign_key="school.id")
    year: int
    school_bullying_classification_type_id_fk: int = Field(foreign_key="school_bullying_classification_type.id")
    count: Optional[int] = None
    
    # Relationships
    classification_type: SchoolBullyingClassificationType = Relationship(
        back_populates="bullying_classifications",
        sa_relationship_kwargs={"foreign_keys": "SchoolBullyingClassification.school_bullying_classification_type_id_fk"}
    )
    # One-way relationship to School - no inverse relationship
    school: "School" = Relationship(
        sa_relationship_kwargs={"foreign_keys": "SchoolBullyingClassification.school_id_fk", "viewonly": True}
    )


class SchoolBullyingImpactType(BaseMixin, table=True):
    __tablename__ = "school_bullying_impact_type"
    
    name: str = Field(max_length=255)
    description: Optional[str] = None
    
    # Relationships
    bullying_impacts: List["SchoolBullyingImpact"] = Relationship(back_populates="impact_type")


class SchoolBullyingImpact(BaseMixin, table=True):
    __tablename__ = "school_bullying_impact"
    
    school_id_fk: int = Field(foreign_key="school.id")
    year: int
    school_bullying_impact_type_id_fk: int = Field(foreign_key="school_bullying_impact_type.id")
    count: Optional[int] = None
    
    # Relationships
    impact_type: SchoolBullyingImpactType = Relationship(
        back_populates="bullying_impacts",
        sa_relationship_kwargs={"foreign_keys": "SchoolBullyingImpact.school_bullying_impact_type_id_fk"}
    )
    # One-way relationship to School - no inverse relationship
    school: "School" = Relationship(
        sa_relationship_kwargs={"foreign_keys": "SchoolBullyingImpact.school_id_fk", "viewonly": True}
    )


class SchoolHarassmentClassification(BaseMixin, table=True):
    __tablename__ = "school_harassment_classification"
    
    name: str = Field(max_length=255)
    description: Optional[str] = None
    
    # Relationships
    harassment_records: List["SchoolHarassment"] = Relationship(back_populates="classification")


class SchoolHarassment(BaseMixin, table=True):
    __tablename__ = "school_harassment"
    
    school_id_fk: int = Field(foreign_key="school.id")
    year: int
    school_harassment_classification_id_fk: int = Field(foreign_key="school_harassment_classification.id")
    incident_count: Optional[int] = None
    student_impact_count: Optional[int] = None
    student_engaged_count: Optional[int] = None
    
    # Relationships
    classification: SchoolHarassmentClassification = Relationship(
        back_populates="harassment_records",
        sa_relationship_kwargs={"foreign_keys": "SchoolHarassment.school_harassment_classification_id_fk"}
    )
    # One-way relationship to School - no inverse relationship
    school: "School" = Relationship(
        sa_relationship_kwargs={"foreign_keys": "SchoolHarassment.school_id_fk", "viewonly": True}
    )


class SchoolRestraint(BaseMixin, table=True):
    __tablename__ = "school_restraint"
    
    school_id_fk: int = Field(foreign_key="school.id")
    year: int
    generated: Optional[int] = None
    active_investigation: Optional[int] = None
    closed_investigation: Optional[int] = None
    bodily_injury: Optional[int] = None
    serious_injury: Optional[int] = None
    
    # One-way relationship to School - no inverse relationship
    school: "School" = Relationship(
        sa_relationship_kwargs={"foreign_keys": "SchoolRestraint.school_id_fk", "viewonly": True}
    )


class SchoolSeclusion(BaseMixin, table=True):
    __tablename__ = "school_seclusion"
    
    school_id_fk: int = Field(foreign_key="school.id")
    year: int
    generated: Optional[int] = None
    active_investigation: Optional[int] = None
    closed_investigation: Optional[int] = None
    
    # One-way relationship to School - no inverse relationship
    school: "School" = Relationship(
        sa_relationship_kwargs={"foreign_keys": "SchoolSeclusion.school_id_fk", "viewonly": True}
    ) 