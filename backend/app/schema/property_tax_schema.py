from datetime import date
from typing import List, Optional

from pydantic import BaseModel


class PropertyTaxYearGet(BaseModel):
    tax_year: int  # the starting year: set in the fall of 2025, paying for 2025-26
    school_year: str  # 2025-26
    dra_towns: int  # towns with DRA's rates that year
    doe_towns: int  # towns in the DOE's valuations report


class DraTaxRatesGet(BaseModel):
    """NH DRA's figures for the town: rates per $1,000 of assessed value"""
    name: str  # as DRA prints it
    municipal_rate: Optional[float] = None
    county_rate: Optional[float] = None
    local_education_rate: float
    state_education_rate: float
    total_rate: Optional[float] = None
    equalization_ratio: Optional[float] = None  # percent: assessed value as a share of market value
    full_value_tax_rate: Optional[float] = None  # the total rate on equalized value, from 2018
    assessed_valuation: Optional[float] = None
    assessed_valuation_with_utilities: Optional[float] = None
    total_tax_commitment: Optional[float] = None
    local_school_tax_effort: Optional[float] = None  # dollars, from 2018
    state_education_tax_effort: Optional[float] = None
    date_rate_set: date
    note: Optional[str] = None


class CoopShareGet(BaseModel):
    district_id: int
    district_name: str
    footnote: str  # C: the town's own row carries the totals; B: Hanover's share of Dresden
    local_education_tax: float  # the part of the town's local school tax that goes to the cooperative


class DoeSchoolTaxGet(BaseModel):
    """NH DOE's valuations report row for the town"""
    cooperative_district_id: Optional[int] = None  # the cooperative (or county district) a member town's row is under
    cooperative_district_name: Optional[str] = None
    assessed_valuation: float
    assessed_valuation_with_utilities: float
    equalized_valuation: float
    equalized_valuation_with_utilities: float
    local_education_tax: float  # including any part that goes to a cooperative
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
    cooperative_shares: List[CoopShareGet]


class TownPropertyTaxGet(BaseModel):
    town_id: int
    town_name: str
    tax_year: int
    school_year: str
    district_id: Optional[int] = None  # the DOE report's district for the town that year, when it's a site district
    district_name: Optional[str] = None
    school_share_of_total_rate: Optional[float] = None  # percent: local and state education of the total rate
    dra: Optional[DraTaxRatesGet] = None  # tax years 2014 on
    doe: Optional[DoeSchoolTaxGet] = None  # tax years 2011 on
