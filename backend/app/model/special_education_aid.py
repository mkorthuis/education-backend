from datetime import date
from typing import Optional

from sqlmodel import Field

from .base import BaseMixin


# -------------------- Special education aid (catastrophic aid until 2017) --------------------
# Values are the DOE's, as published; district_special_education_aid_summary is a view built on them.

class SpecialEducationAidYear(BaseMixin, table=True):
    """A fiscal year of aid (2026: paid in 2025-26 on 2024-25 costs, as doe_form.year), with the DOE's state totals"""
    __tablename__ = "special_education_aid_year"

    fiscal_year: int
    cost_school_year: str = Field(max_length=7)  # 2024-25: the costs it reimburses
    status: str = Field(max_length=10)  # final, or estimate
    as_of: Optional[date] = None  # the DOE's date on the file, when it gives one
    state_average_cost: float  # the DOE's estimated state average cost per pupil: 21,519.91 for FY2026
    threshold_cost: float  # the cost per student where state aid begins: 75,319.68 for FY2026
    appropriation: Optional[float] = None  # what the DOE distributed, when the file says
    proration_rate: float  # aid paid as a share of entitlement: 0.9114185 for FY2026, 1 when paid in full
    minimum_share: Optional[float] = None  # the least share of its entitlement a district gets (0.8 from FY2026)
    state_students_reported: Optional[float] = None  # 885 for FY2026; part-year students make fractions
    state_students_highest_band: Optional[float] = None  # students with costs over 10 times the state average
    state_total_cost: float
    state_entitlement: float
    state_aid_paid: float
    source_url: str  # the DOE's file
    page_url: str  # the DOE's Other State Aid Programs page
    note: Optional[str] = None


class SpecialEducationAidBand(BaseMixin, table=True):
    """A band of a student's cost in a year's formula, as multiples of the state average cost per pupil, and the state's
    share of the costs in it: 3.5 to 10 times, 80%"""
    __tablename__ = "special_education_aid_band"

    fiscal_year: int = Field(foreign_key="special_education_aid_year.fiscal_year")
    band: int  # 1 is the lowest, which the district pays in full
    from_multiple: float
    to_multiple: Optional[float] = None  # none above the highest band
    state_share: float
    label: str = Field(max_length=100)
    citation: str = Field(max_length=255)
    source_url: str


class DistrictSpecialEducationAid(BaseMixin, table=True):
    """A district's costs for high-cost special education students in a year, and its aid, as the DOE publishes them"""
    __tablename__ = "district_special_education_aid"

    district_id_fk: int = Field(foreign_key="district.id")
    fiscal_year: int = Field(foreign_key="special_education_aid_year.fiscal_year")
    source_name: str = Field(max_length=255)  # the DOE's "District of Liability", as written
    students_reported: Optional[float] = None  # the DOE leaves each district's count blank
    total_cost: float
    entitlement: float  # the state's share of its costs above the threshold
    aid_paid: float  # its entitlement, prorated when the appropriation falls short


class DistrictSpecialEducationAidBand(BaseMixin, table=True):
    """A district's costs in one band of its year's formula"""
    __tablename__ = "district_special_education_aid_band"

    district_special_education_aid_id_fk: int = Field(foreign_key="district_special_education_aid.id")
    band: int
    cost: float
    students: Optional[float] = None  # where the DOE gives a count
