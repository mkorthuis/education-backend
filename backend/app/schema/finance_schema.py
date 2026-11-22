from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import date, datetime

# Remove circular import 
# from .location_schema import DistrictGet

# DOE Form ADM Schema
class DOEFormADMGet(BaseModel):
    id: int
    elementary: Optional[float] = None
    middle: Optional[float] = None
    high: Optional[float] = None
    total: Optional[float] = None

    class Config:
        from_attributes = True
        populate_by_name = True

# DOE Form ADM State Schema (for the materialized view)
class DOEFormADMStateGet(BaseModel):
    """State-level aggregated Average Daily Membership data by year"""
    year: int
    elementary: Optional[float] = None
    middle: Optional[float] = None
    high: Optional[float] = None
    total: Optional[float] = None

    class Config:
        from_attributes = True
        populate_by_name = True

# Balance Sheet Related Schemas
class BalanceFundTypeGet(BaseModel):
    id: int
    state_id: str
    state_name: str

    class Config:
        from_attributes = True


class BalanceSheetGet(BaseModel):
    id: int
    value: Optional[float] = None
    balance_entry_type_id_fk: Optional[int] = Field(alias='entry_type_id')
    balance_fund_type_id_fk: Optional[int] = Field(alias='fund_type_id')

    class Config:
        from_attributes = True
        populate_by_name = True

# Revenue Related Schemas
class RevenueFundTypeGet(BaseModel):
    id: int
    state_id: str
    state_name: str

    class Config:
        from_attributes = True

class RevenueGet(BaseModel):
    id: int
    value: Optional[float] = None
    revenue_entry_type_id_fk: Optional[int] = Field(alias='entry_type_id')
    revenue_fund_type_id_fk: Optional[int] = Field(alias='fund_type_id')

    class Config:
        from_attributes = True
        populate_by_name = True

# Expenditure Related Schemas
class ExpenditureFundTypeGet(BaseModel):
    id: int
    state_id: str
    state_name: str

    class Config:
        from_attributes = True

class ExpenditureGet(BaseModel):
    id: int
    value: Optional[float] = None
    expenditure_entry_type_id_fk: Optional[int] = Field(alias='entry_type_id')
    expenditure_fund_type_id_fk: Optional[int] = Field(alias='fund_type_id')

    class Config:
        from_attributes = True
        populate_by_name = True

class ExpenditureStateRollupGet(BaseModel):
    """State-level expenditure data by year and school level"""
    id: int
    year: int
    operating_elementary: Optional[float] = None
    operating_middle: Optional[float] = None
    operating_high: Optional[float] = None
    operating_total: Optional[float] = None
    current_elementary: Optional[float] = None 
    current_middle: Optional[float] = None
    current_high: Optional[float] = None
    current_total: Optional[float] = None
    total: Optional[float] = None
    date_created: datetime
    date_updated: datetime

    class Config:
        from_attributes = True

class ExpenditureStateTotalGet(BaseModel):
    """State-level expenditure data by year and entry type"""
    id: int
    year: int
    expenditure_entry_type_id_fk: int = Field(alias='entry_type_id')
    value: Optional[float] = None
    date_created: datetime
    date_updated: datetime

    class Config:
        from_attributes = True
        populate_by_name = True

class RevenueStateTotalGet(BaseModel):
    """State-level revenue data by year and entry type"""
    id: int
    year: int
    revenue_entry_type_id_fk: int = Field(alias='entry_type_id')
    value: Optional[float] = None
    date_created: datetime
    date_updated: datetime

    class Config:
        from_attributes = True
        populate_by_name = True

# DOE Form Schema
class DOEFormGet(BaseModel):
    id: int
    year: int
    date_created: datetime
    date_updated: datetime
    district_id_fk: int = Field(alias='district_id')
    balance_sheets: Optional[List[BalanceSheetGet]] = None
    revenues: Optional[List[RevenueGet]] = None
    expenditures: Optional[List[ExpenditureGet]] = None

    class Config:
        from_attributes = True
        populate_by_name = True

# Financial Report Schema (combines DOE Form with all related data)
class FinancialReportGet(BaseModel):
    doe_form: DOEFormGet
    balance_sheets: List[BalanceSheetGet] = []
    revenues: List[RevenueGet] = []
    expenditures: List[ExpenditureGet] = []
    adm: Optional[DOEFormADMGet] = None

    class Config:
        from_attributes = True


class BalanceEntrySuperCategoryGet(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class RevenueEntrySuperCategoryGet(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class ExpenditureEntrySuperCategoryGet(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class BalanceEntryCategoryGet(BaseModel):
    id: int
    name: str
    super_category: Optional[BalanceEntrySuperCategoryGet] = None

    class Config:
        from_attributes = True
        populate_by_name = True

class RevenueEntryCategoryGet(BaseModel):
    id: int
    name: str
    super_category: Optional[RevenueEntrySuperCategoryGet] = None

    class Config:
        from_attributes = True
        populate_by_name = True

class ExpenditureEntryCategoryGet(BaseModel):
    id: int
    name: str
    super_category: Optional[ExpenditureEntrySuperCategoryGet] = None

    class Config:
        from_attributes = True
        populate_by_name = True

# Enhanced schemas for entry types with nested categories
class BalanceEntryTypeGet(BaseModel):
    id: int
    name: str
    account_no: str
    page: Optional[str] = None
    line: Optional[str] = None
    category: Optional[BalanceEntryCategoryGet] = None

    class Config:
        from_attributes = True
        populate_by_name = True

class RevenueEntryTypeGet(BaseModel):
    id: int
    name: str
    account_no: str
    page: Optional[str] = None
    line: Optional[str] = None
    category: Optional[RevenueEntryCategoryGet] = None

    class Config:
        from_attributes = True
        populate_by_name = True

class ExpenditureEntryTypeGet(BaseModel):
    id: int
    name: str
    account_no: str
    page: Optional[str] = None
    line: Optional[str] = None
    category: Optional[ExpenditureEntryCategoryGet] = None

    class Config:
        from_attributes = True
        populate_by_name = True

# Combined schema for all entry types
class AllEntryTypesGet(BaseModel):
    balance_entry_types: List[BalanceEntryTypeGet] = []
    revenue_entry_types: List[RevenueEntryTypeGet] = []
    expenditure_entry_types: List[ExpenditureEntryTypeGet] = []

    class Config:
        from_attributes = True

# Combined schema for all fund types
class AllFundTypesGet(BaseModel):
    balance_fund_types: List[BalanceFundTypeGet] = []
    revenue_fund_types: List[RevenueFundTypeGet] = []
    expenditure_fund_types: List[ExpenditureFundTypeGet] = []

    class Config:
        from_attributes = True

# Cost Per Pupil Schemas
class StateCostPerPupilGet(BaseModel):
    id: int
    year: int
    elementary: Optional[int] = None
    middle: Optional[int] = None
    high: Optional[int] = None
    total: Optional[int] = None
    date_created: datetime
    date_updated: datetime
    
    class Config:
        from_attributes = True


class DistrictCostPerPupilGet(BaseModel):
    id: int
    year: int
    elementary: Optional[int] = None
    middle: Optional[int] = None
    high: Optional[int] = None
    total: Optional[int] = None
    district_id_fk: int = Field(alias='district_id')
    date_created: datetime
    date_updated: datetime
    
    class Config:
        from_attributes = True
        populate_by_name = True


class PrivateOrgGet(BaseModel):
    """An organization that files, or needn't file, a private school's Form 990"""
    ein: str
    name: str
    founded: Optional[int] = None
    mission: Optional[str] = None


class PrivateOrg990RevenueLineGet(BaseModel):
    line_no: int
    description: str
    business_code: Optional[str] = None
    amount: int
    # tuition, school_program, room_and_board, summer_auxiliary, extended_care, student_activities,
    # transportation, therapy_tutoring, human_services, unspecified_program, rental or other
    category: str


class PrivateOrg990Get(BaseModel):
    """One of the filer's 990 or 990-EZ returns, as filed"""
    tax_period_end: date
    form: str
    total_revenue: Optional[int] = None
    prior_total_revenue: Optional[int] = None
    program_service_revenue: Optional[int] = None
    contributions: Optional[int] = None
    government_grants: Optional[int] = None
    investment_income: Optional[int] = None
    investment_gains: Optional[int] = None
    fundraising_event_income: Optional[int] = None
    total_expenses: Optional[int] = None
    prior_total_expenses: Optional[int] = None
    program_expenses: Optional[int] = None
    management_expenses: Optional[int] = None
    fundraising_expenses: Optional[int] = None
    salaries_benefits: Optional[int] = None
    total_assets_eoy: Optional[int] = None
    total_liabilities_eoy: Optional[int] = None
    net_assets_eoy: Optional[int] = None
    land_buildings_equipment_eoy: Optional[int] = None
    public_investments_eoy: Optional[int] = None
    tax_exempt_bonds_eoy: Optional[int] = None
    employees: Optional[int] = None
    volunteers: Optional[int] = None
    paid_over_100k: Optional[int] = None
    endowment_eoy: Optional[int] = None
    endowment_board_designated_share: Optional[float] = None
    endowment_permanent_share: Optional[float] = None
    endowment_term_share: Optional[float] = None
    object_id: str
    revenue_lines: List[PrivateOrg990RevenueLineGet]


class PrivateSchool990Get(BaseModel):
    """Who files a private school's Form 990, and its returns, oldest first"""
    school_id: int
    # own_return, operator_return, postcard_only, not_required_religious, no_irs_record or placeholder
    status: str
    note: Optional[str] = None
    organization: Optional[PrivateOrgGet] = None
    returns: List[PrivateOrg990Get]


class PrivateSchoolTuitionRateGet(BaseModel):
    rate_no: int
    band: str
    lowest_grade_id: int
    lowest_grade: str
    highest_grade_id: int
    highest_grade: str
    # standard, day, boarding, parishioner, non_parishioner, international, half_day, full_day or other
    rate_type: str
    rate_label: Optional[str] = None
    tuition: float
    # None where the school names a required fee but not its amount
    required_fee: Optional[float] = None
    fee_note: Optional[str] = None
    rate_note: Optional[str] = None


class PrivateSchoolTuitionGet(BaseModel):
    """A private school's tuition for a school year, as it publishes it on its website"""
    school_id: int
    year: int
    # published, not_published or site_unavailable
    status: str
    source_url: Optional[str] = None
    retrieved_on: date
    # Who gets financial aid, as the school words it: "37% of students", "Nearly 35% of families", "74%"
    with_aid: Optional[str] = None
    note: Optional[str] = None
    rates: List[PrivateSchoolTuitionRateGet]
