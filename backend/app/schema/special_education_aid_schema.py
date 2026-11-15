from datetime import date
from typing import List, Optional

from pydantic import BaseModel


class SpecialEducationAidBandGet(BaseModel):
    """A band of a student's cost and the state's share of it"""
    band: int  # 1 is the lowest, which the district pays in full
    label: str  # "3.5 to 10 times the state average: 80% state aid"
    from_multiple: float  # of the state average cost per pupil
    to_multiple: Optional[float] = None  # none above the highest band
    state_share: float
    citation: str
    source_url: str


class SpecialEducationAidYearGet(BaseModel):
    fiscal_year: int  # 2026: paid in 2025-26 on 2024-25 costs, as the financial report's year
    cost_school_year: str  # 2024-25
    status: str  # final, or estimate
    as_of: Optional[date] = None
    state_average_cost: float  # the DOE's estimated state average cost per pupil
    threshold_cost: float  # the cost per student where state aid begins
    appropriation: Optional[float] = None
    proration_rate: float  # aid paid as a share of entitlement; 1 when paid in full
    minimum_share: Optional[float] = None  # the least share of its entitlement a district gets
    students_reported: Optional[float] = None  # statewide; the DOE gives no district counts
    students_highest_band: Optional[float] = None  # statewide, with costs over 10 times the state average
    total_cost: float  # statewide
    entitlement: float
    aid_paid: float
    districts: int  # districts with aid that year
    note: Optional[str] = None
    source_url: str  # the DOE's file
    page_url: str  # the DOE's Other State Aid Programs page
    bands: List[SpecialEducationAidBandGet]


class DistrictSpecialEducationAidBandGet(BaseModel):
    band: int
    label: str
    state_share: float
    cost: float
    students: Optional[float] = None  # where the DOE gives a count


class DistrictSpecialEducationAidGet(BaseModel):
    district_id: int
    district_name: str
    fiscal_year: int
    cost_school_year: str
    total_cost: float  # its costs for the students it reported
    cost_below_threshold: float  # what it pays in full, up to the threshold for each student
    cost_above_threshold: float  # the costs the state shares
    cost_over_10_times: float  # the part over 10 times the state average
    entitlement: float  # the state's share of its costs above the threshold
    aid_paid: float  # its entitlement, prorated when the appropriation falls short
    share_of_cost_paid: Optional[float] = None  # aid paid as a share of its total cost
    reported_aid: Optional[float] = None  # "Special Education Aid" in its financial report (DOE-25)
    reported_difference: Optional[float] = None  # reported minus paid
    source_name: str  # the DOE's name for it
    bands: List[DistrictSpecialEducationAidBandGet]
