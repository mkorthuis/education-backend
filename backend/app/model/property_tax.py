from datetime import date
from typing import Optional

from sqlmodel import Field

from .base import BaseMixin


# -------------------- Property tax rates and school taxes by town --------------------
# From NH DRA's tax rates and NH DOE's valuations report, as published; town_property_tax_summary is a view built
# on them. A tax year's rates are set in the fall and pay for the school year that starts then (2025: 2025-26).

class TownPropertyTax(BaseMixin, table=True):
    """DRA's tax rates for a town and tax year, per $1,000 of assessed value"""
    __tablename__ = "town_property_tax"

    town_id_fk: int = Field(foreign_key="town.id")
    tax_year: int  # the starting year: rates set in the fall of 2025 are 2025, paying for 2025-26 (FY2026 elsewhere)
    dra_name: str = Field(max_length=100)  # the town as DRA prints it
    municipal_rate: Optional[float] = None  # a few towns' are negative (Benton)
    county_rate: Optional[float] = None
    local_education_rate: float
    state_education_rate: float
    total_rate: Optional[float] = None  # none for Penacook in 2015
    equalization_ratio: Optional[float] = None  # percent: assessed value as a share of market value
    full_value_tax_rate: Optional[float] = None  # DRA's rate on equalized value, from 2018
    assessed_valuation: Optional[float] = None
    assessed_valuation_with_utilities: Optional[float] = None
    total_tax_commitment: Optional[float] = None
    local_school_tax_effort: Optional[float] = None  # dollars, from 2018
    state_education_tax_effort: Optional[float] = None
    date_rate_set: date
    note: Optional[str] = None


class TownSchoolTax(BaseMixin, table=True):
    """The DOE valuations report's row for a town and tax year: its school tax dollars, valuations and rates"""
    __tablename__ = "town_school_tax"

    town_id_fk: int = Field(foreign_key="town.id")
    tax_year: int  # the starting year: rates set in the fall of 2025 are 2025, paying for 2025-26 (FY2026 elsewhere)
    # The report's district: its number (none on a few towns' rows), as a site
    # district id; and a member town's cooperative (or county district), from the report's name for it
    district_id_fk: Optional[int] = Field(default=None, foreign_key="district.id")
    cooperative_district_id_fk: Optional[int] = Field(default=None, foreign_key="district.id")  # none for a single-town district
    assessed_valuation: float
    assessed_valuation_with_utilities: float
    equalized_valuation: float
    equalized_valuation_with_utilities: float
    local_education_tax: float  # including any part that goes to a cooperative (town_school_tax_coop_share)
    other_local_tax: float  # municipal and county
    state_education_tax: float  # the SWEPT for the next fiscal year
    rate_local_education: float  # per $1,000 of assessed value
    rate_other_local: float
    rate_state_education: float
    rate_total: float
    equalized_rate_local_education: float  # per $1,000 of equalized value
    equalized_rate_other_local: float
    equalized_rate_state_education: float
    equalized_rate_total: float
    note: Optional[str] = None


class TownSchoolTaxCoopShare(BaseMixin, table=True):
    """The part of a town's local school tax that goes to a cooperative, from the report's "reference only" rows"""
    __tablename__ = "town_school_tax_coop_share"

    town_school_tax_id_fk: int = Field(foreign_key="town_school_tax.id")
    district_id_fk: int = Field(foreign_key="district.id")
    footnote: str = Field(max_length=1)  # C: the town's own row carries the totals; B: Hanover's share of Dresden
    local_education_tax: float
