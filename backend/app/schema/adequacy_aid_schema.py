from datetime import date
from typing import Dict, List, Optional

from pydantic import BaseModel


class AdequacyAidYearGet(BaseModel):
    fiscal_year: int  # 2027: the 2026-27 school year, as the financial report's year
    school_year: str
    status: str  # final, or estimate (before the DOE's April final calculation)
    as_of: date  # the DOE's date on the calculation
    summary_url: str  # the DOE's workbook of every town's calculation
    split_url: Optional[str] = None  # the DOE's split of towns' grants among their districts
    explained_url: Optional[str] = None  # the DOE's explanation of the year


class AdequacyAidParameterGet(BaseModel):
    code: str  # base_per_pupil
    name: str
    value: float
    unit: str  # dollars_per_pupil, dollars, fraction, dollars_per_thousand, dollars_per_dollar
    citation: str
    source_url: str


class AdequacyAidStepGet(BaseModel):
    step: int
    code: str  # the part it produces
    name: str
    description: str
    unit: str  # count, dollars, dollars_per_pupil, fraction
    role: str  # students, cost, cost_total, swept, added_aid, hold_harmless, result, basis
    formula: Optional[str] = None  # over component and parameter codes; none: explained, not checked
    uses: List[str] = []  # the codes the formula uses
    tolerance: float  # dollars the DOE's figure may differ from the formula by
    explanation: str
    citation: str


class AdequacyAidComponentGet(BaseModel):
    code: str  # resident_adm_base
    name: str
    description: str
    unit: str  # count, dollars, dollars_per_pupil, fraction
    role: str  # students, cost, cost_total, swept, added_aid, hold_harmless, result, basis


class AdequacyAidFormulaGet(BaseModel):
    year: AdequacyAidYearGet
    parameters: List[AdequacyAidParameterGet]
    steps: List[AdequacyAidStepGet]
    components: List[AdequacyAidComponentGet] = []  # every part the year's towns have or its formulas use, in page order


class AdequacyAidYearFields(BaseModel):
    fiscal_year: int
    school_year: str
    status: str
    as_of: date


class DistrictAdequacyAidGet(AdequacyAidYearFields):
    district_id: int
    district_name: str
    adequacy_grant: float  # paid by the state, from all member towns
    swept_retained: float  # statewide education property tax kept locally
    total_state_aid: float
    member_towns: int
    reported_adequacy_grant: Optional[float] = None  # "Adequacy Aid Grant" in its financial report (DOE-25)
    reported_difference: Optional[float] = None  # reported minus calculated


class AdequacyAidLineGet(BaseModel):
    """A step of a town's calculation with the town's values"""
    step: int
    code: str
    name: str
    unit: str
    role: str
    value: float  # the DOE's published figure
    formula: Optional[str] = None
    inputs: Dict[str, float] = {}  # each name the formula uses: the town's value or the year's parameter
    explanation: str
    citation: str


class TownAdequacyAidTotals(BaseModel):
    adequacy_grant: float
    swept: float
    total_state_aid: float


class AdequacyAidShareGet(BaseModel):
    adequacy_grant: float
    swept_retained: float
    source: str  # doe_split (the DOE's split file) or whole_town (the town's one district)
    share_of_town: Optional[float] = None  # of the town's grant plus SWEPT


class DistrictTownCalculationGet(BaseModel):
    town_id: int
    town_name: str
    share: AdequacyAidShareGet  # what this district receives from the town
    town_totals: TownAdequacyAidTotals
    steps: List[AdequacyAidLineGet]
    values: Dict[str, float]  # every part the DOE published for the town and year


class DistrictAdequacyAidCalculationGet(DistrictAdequacyAidGet):
    towns: List[DistrictTownCalculationGet]


class TownAdequacyAidGet(AdequacyAidYearFields):
    town_id: int
    town_name: str
    resident_adm: Optional[float] = None
    base_aid: Optional[float] = None
    frl_adm: Optional[float] = None
    frl_aid: Optional[float] = None
    sped_adm: Optional[float] = None
    sped_aid: Optional[float] = None
    ell_adm: Optional[float] = None
    ell_aid: Optional[float] = None
    home_education_adm: Optional[float] = None
    home_education_aid: Optional[float] = None
    grade3_reading_adm: Optional[float] = None
    grade3_reading_aid: Optional[float] = None
    total_cost: Optional[float] = None
    swept: Optional[float] = None
    equalized_valuation: Optional[float] = None
    extraordinary_need_grant: Optional[float] = None
    fiscal_capacity_disparity_aid: Optional[float] = None
    other_added_aid: Optional[float] = None  # stabilization, relief aid and other years' programs
    preliminary_grant: Optional[float] = None
    hold_harmless: Optional[float] = None
    adequacy_grant: Optional[float] = None
    total_state_aid: Optional[float] = None
    swept_above_cost: Optional[float] = None


class TownDistrictShareGet(AdequacyAidShareGet):
    district_id: int
    district_name: str


class TownAdequacyAidCalculationGet(AdequacyAidYearFields):
    town_id: int
    town_name: str
    totals: TownAdequacyAidTotals
    districts: List[TownDistrictShareGet]  # where the town's grant and SWEPT go
    steps: List[AdequacyAidLineGet]
    values: Dict[str, float]


class StateAdequacyAidGet(AdequacyAidYearFields):
    adequacy_grant: Optional[float] = None
    swept: Optional[float] = None
    total_state_aid: Optional[float] = None
    values: Dict[str, float]  # the DOE's statewide total for every part
