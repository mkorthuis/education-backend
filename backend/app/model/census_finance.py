from sqlmodel import Field

from .base import BaseMixin


# -------------------- Census school finance by state --------------------

class CensusRevenueItem(BaseMixin, table=True):
    """A Census school finance revenue item (C14 is Title I, T06 property taxes), with its source and
    the category Census's summary tables put it in"""
    __tablename__ = "census_revenue_item"

    code: str = Field(max_length=10)
    name: str = Field(max_length=255)
    source: str = Field(max_length=10)  # federal, state or local
    category: str = Field(max_length=100)
    display_order: int


class CensusStateRevenue(BaseMixin, table=True):
    """A state's (or the nation's) school system revenue from one item in one fiscal year"""
    __tablename__ = "census_state_revenue"

    year: int
    jurisdiction_id_fk: int = Field(foreign_key="jurisdiction.id")
    census_revenue_item_id_fk: int = Field(foreign_key="census_revenue_item.id")
    amount_thousands: int  # thousand dollars, as Census publishes it


class CensusStateEnrollment(BaseMixin, table=True):
    """The fall enrollment Census uses for a state's per-pupil amounts in one fiscal year"""
    __tablename__ = "census_state_enrollment"

    year: int
    jurisdiction_id_fk: int = Field(foreign_key="jurisdiction.id")
    enrollment: int
