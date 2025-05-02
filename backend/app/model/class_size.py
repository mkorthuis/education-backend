from typing import Optional, TYPE_CHECKING, List
from sqlmodel import Field, Relationship, SQLModel
from .base import BaseMixin

# Avoid circular imports for type hints
if TYPE_CHECKING:
    from .location import District, School


class DistrictClassSize(BaseMixin, table=True):
    """ORM model for district average class size records."""
    __tablename__ = "district_class_size"

    district_id_fk: int = Field(foreign_key="district.id")
    year: int

    grade_1_2: Optional[float] = None
    grade_3_4: Optional[float] = None
    grade_5_8: Optional[float] = None

    # Relationships (one-way to avoid circular navigation)
    district: "District" = Relationship(sa_relationship_kwargs={
        "foreign_keys": "DistrictClassSize.district_id_fk",
        "viewonly": True,
    })


class SchoolClassSize(BaseMixin, table=True):
    """ORM model for school average class size records."""
    __tablename__ = "school_class_size"

    school_id_fk: int = Field(foreign_key="school.id")
    year: int

    grade_1_2: Optional[float] = None
    grade_3_4: Optional[float] = None
    grade_5_8: Optional[float] = None

    school: "School" = Relationship(sa_relationship_kwargs={
        "foreign_keys": "SchoolClassSize.school_id_fk",
        "viewonly": True,
    })


class StateClassSize(BaseMixin, table=True):
    """ORM model for state-level average class size records."""
    __tablename__ = "state_class_size"

    year: int

    grade_1_2: Optional[float] = None
    grade_3_4: Optional[float] = None
    grade_5_8: Optional[float] = None 