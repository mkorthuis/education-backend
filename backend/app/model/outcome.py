from typing import Optional, List, TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel
from .base import BaseMixin

# Use TYPE_CHECKING to avoid circular imports
if TYPE_CHECKING:
    from .location import School

# -------------------- Early Exit Models --------------------

class SchoolEarlyExit(BaseMixin, table=True):
    __tablename__ = "school_early_exit"

    school_id_fk: int = Field(foreign_key="school.id")
    year: int

    adjusted_fall_enrollment: Optional[int] = None
    earned_hiset: Optional[int] = None
    enrolled_in_college: Optional[int] = None
    dropped_out: Optional[int] = None
    missing: Optional[int] = None

    annual_early_exit_percentage: Optional[float] = None
    four_year_early_exit_percentage: Optional[float] = None
    annual_dropout_percentage: Optional[float] = None
    four_year_dropout_percentage: Optional[float] = None

    # Relationships
    school: "School" = Relationship(sa_relationship_kwargs={"foreign_keys": "SchoolEarlyExit.school_id_fk", "viewonly": True})


class StateEarlyExit(BaseMixin, table=True):
    __tablename__ = "state_early_exit"

    year: int

    adjusted_fall_enrollment: Optional[int] = None
    earned_hiset: Optional[int] = None
    enrolled_in_college: Optional[int] = None
    dropped_out: Optional[int] = None
    missing: Optional[int] = None

    annual_early_exit_percentage: Optional[float] = None
    four_year_early_exit_percentage: Optional[float] = None
    annual_dropout_percentage: Optional[float] = None
    four_year_dropout_percentage: Optional[float] = None


# -------------------- Post-Graduation Outcome Models --------------------

class PostGraduationType(BaseMixin, table=True):
    __tablename__ = "post_graduation_type"

    name: str = Field(max_length=255, unique=True)
    description: Optional[str] = None

    # Relationships
    school_post_graduation_records: List["SchoolPostGraduation"] = Relationship(back_populates="post_graduation_type")
    state_post_graduation_records: List["StatePostGraduation"] = Relationship(back_populates="post_graduation_type")


class SchoolPostGraduation(BaseMixin, table=True):
    __tablename__ = "school_post_graduation"

    school_id_fk: int = Field(foreign_key="school.id")
    year: int
    post_graduation_type_id_fk: int = Field(foreign_key="post_graduation_type.id")
    value: int

    # Relationships
    school: "School" = Relationship(sa_relationship_kwargs={"foreign_keys": "SchoolPostGraduation.school_id_fk", "viewonly": True})
    post_graduation_type: PostGraduationType = Relationship(back_populates="school_post_graduation_records", sa_relationship_kwargs={"foreign_keys": "SchoolPostGraduation.post_graduation_type_id_fk"})


class StatePostGraduation(BaseMixin, table=True):
    __tablename__ = "state_post_graduation"

    year: int
    post_graduation_type_id_fk: int = Field(foreign_key="post_graduation_type.id")
    value: int

    # Relationships
    post_graduation_type: PostGraduationType = Relationship(back_populates="state_post_graduation_records", sa_relationship_kwargs={"foreign_keys": "StatePostGraduation.post_graduation_type_id_fk"}) 