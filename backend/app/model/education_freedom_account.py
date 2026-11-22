from decimal import Decimal
from typing import Optional, List, TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel
from .base import BaseMixin

if TYPE_CHECKING:
    from .location import Town
else:
    # Need to use a string type hint at runtime
    Town = "Town"

class EducationFreedomAccountEntryType(BaseMixin, table=True):
    """Education Freedom Account entry type model"""
    __tablename__ = "education_freedom_account_entry_type"
    
    name: str = Field(max_length=255)
    description: Optional[str] = None
    
    # Relationships
    entry_type_values: List["EducationFreedomAccountEntryTypeValue"] = Relationship(
        back_populates="entry_type",
        sa_relationship_kwargs={"cascade": "all, delete-orphan"}
    )
    entries: List["EducationFreedomAccountEntry"] = Relationship(
        back_populates="entry_type",
        sa_relationship_kwargs={"cascade": "all, delete-orphan"}
    )

class EducationFreedomAccountEntryTypeValue(BaseMixin, table=True):
    """Education Freedom Account entry type value model"""
    __tablename__ = "education_freedom_account_entry_type_value"
    
    education_freedom_account_entry_type_id_fk: int = Field(
        foreign_key="education_freedom_account_entry_type.id"
    )
    year: int
    value: Optional[float] = None
    
    # Relationships
    entry_type: EducationFreedomAccountEntryType = Relationship(back_populates="entry_type_values")

class EducationFreedomAccountEntry(BaseMixin, table=True):
    """Education Freedom Account entry model"""
    __tablename__ = "education_freedom_account_entry"
    
    town_id_fk: int = Field(foreign_key="town.id")
    year: int
    education_freedom_account_entry_type_id_fk: int = Field(
        foreign_key="education_freedom_account_entry_type.id"
    )
    value: Optional[float] = None
    
    # Relationships
    town: Town = Relationship(back_populates="education_freedom_account_entries")
    entry_type: EducationFreedomAccountEntryType = Relationship(back_populates="entries")

class EducationFreedomAccountEntryState(SQLModel, table=True):
    """State-level aggregated Education Freedom Account entry data by year and type"""
    __tablename__ = "education_freedom_account_entry_state"
    
    # Materialized view columns - composite primary key
    year: int = Field(primary_key=True)
    education_freedom_account_entry_type_id_fk: int = Field(primary_key=True)
    value: Optional[float] = Field(default=None)


class EducationFreedomAccountCategory(BaseMixin, table=True):
    """An allowable EFA category, or a combination a purchase charged to several was published under ("A & B")"""
    __tablename__ = "education_freedom_account_category"

    code: str = Field(unique=True)
    name: str
    combined: bool


class EducationFreedomAccountProvider(BaseMixin, table=True):
    """A provider EFA money went to, by its name key; linked to the private school it is when it's one on the state's list"""
    __tablename__ = "education_freedom_account_provider"

    name_key: str = Field(unique=True)
    name: str
    school_id_fk: Optional[int] = Field(default=None, foreign_key="school.id")


class EducationFreedomAccountExpenditure(BaseMixin, table=True):
    """A provider line of the Children's Scholarship Fund's EFA Expenditure Report for a school year (by its end)"""
    __tablename__ = "education_freedom_account_expenditure"

    year: int
    line_no: int
    category_id: int = Field(foreign_key="education_freedom_account_category.id")
    provider_id: int = Field(foreign_key="education_freedom_account_provider.id")
    provider_as_published: str
    amount: Decimal


class EducationFreedomAccountServed(BaseMixin, table=True):
    """A line of the list of students providers served in a calendar year, for providers that served 10 or more"""
    __tablename__ = "education_freedom_account_served"

    calendar_year: int
    line_no: int
    provider_id: int = Field(foreign_key="education_freedom_account_provider.id")
    provider_as_published: str
    students: int
