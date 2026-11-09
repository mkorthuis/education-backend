from typing import Optional

from pydantic import BaseModel

from app.schema.naep_schema import JurisdictionGet


class CensusRevenueItemGet(BaseModel):
    """A Census revenue item, its source (federal, state or local) and the category Census's summary tables put it in"""
    id: int
    code: str
    name: str
    source: str
    category: str
    display_order: int


class CensusStateEnrollmentGet(BaseModel):
    """The fall enrollment Census divides by for a state's per-pupil amounts"""
    id: int
    year: int
    jurisdiction: JurisdictionGet
    enrollment: int


class CensusRevenueItemRef(BaseModel):
    id: int
    code: str
    name: str


class CensusRevenueGet(BaseModel):
    """Revenue from a source, a category or an item, for one place and fiscal year. amount is dollars. The
    shares and per_pupil are calculated here, not published by Census: share_of_source and share_of_total
    are percentages, and per_pupil is the amount divided by Census's fall enrollment. With in_dollars_of,
    the _adjusted amounts are in that year's dollars, by the consumer price index."""
    year: int
    jurisdiction: JurisdictionGet
    level: str
    source: str
    category: Optional[str] = None
    item: Optional[CensusRevenueItemRef] = None
    amount: int
    share_of_source: Optional[float] = None
    share_of_total: Optional[float] = None
    enrollment: Optional[int] = None
    per_pupil: Optional[float] = None
    in_dollars_of: Optional[int] = None
    amount_adjusted: Optional[int] = None
    per_pupil_adjusted: Optional[float] = None


class CensusSourceSummary(BaseModel):
    amount: int
    share_of_total: Optional[float] = None
    per_pupil: Optional[float] = None
    amount_adjusted: Optional[int] = None
    per_pupil_adjusted: Optional[float] = None


class CensusRevenueSummaryGet(BaseModel):
    """One place and fiscal year: total revenue and each source's amount, share and per-pupil amount
    (calculated, as in CensusRevenueGet)"""
    year: int
    jurisdiction: JurisdictionGet
    enrollment: Optional[int] = None
    in_dollars_of: Optional[int] = None
    total: CensusSourceSummary
    federal: CensusSourceSummary
    state: CensusSourceSummary
    local: CensusSourceSummary
