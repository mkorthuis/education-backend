from decimal import Decimal
from datetime import date
from typing import Optional, List, TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel
from .base import BaseMixin

if TYPE_CHECKING:
    from .location import District
else:
    # Need to use a string type hint at runtime
    District = "District"

class DOEForm(BaseMixin, table=True):
    __tablename__ = "doe_form"
    
    district_id_fk: int = Field(foreign_key="district.id")
    year: int
    
    district: District = Relationship()
    balance_sheets: List["BalanceSheet"] = Relationship(back_populates="doe_form")
    revenues: List["Revenue"] = Relationship(back_populates="doe_form")
    expenditures: List["Expenditure"] = Relationship(back_populates="doe_form")
    adm: Optional["DOEFormADM"] = Relationship(back_populates="doe_form")

class DOEFormADM(BaseMixin, table=True):
    """Average Daily Membership data associated with a DOE form"""
    __tablename__ = "doe_form_adm"
    
    doe_form_id_fk: int = Field(foreign_key="doe_form.id", index=True)
    elementary: Optional[float] = Field(default=None)
    middle: Optional[float] = Field(default=None)
    high: Optional[float] = Field(default=None)
    total: Optional[float] = Field(default=None)
    
    doe_form: DOEForm = Relationship(back_populates="adm")

class DOEFormADMState(SQLModel, table=True):
    """State-level aggregated Average Daily Membership data by year"""
    __tablename__ = "doe_form_adm_state"
    
    # Materialized view only has these columns
    year: int = Field(primary_key=True)
    elementary: Optional[float] = Field(default=None)
    middle: Optional[float] = Field(default=None)
    high: Optional[float] = Field(default=None)
    total: Optional[float] = Field(default=None)

# Balance Sheet Models
class BalanceEntrySuperCategory(BaseMixin, table=True):
    __tablename__ = "balance_entry_super_category_type"
    
    name: str = Field(max_length=255)
    categories: List["BalanceEntryCategory"] = Relationship(back_populates="super_category")

class BalanceEntryCategory(BaseMixin, table=True):
    __tablename__ = "balance_entry_category_type"
    
    name: str = Field(max_length=255)
    balance_entry_super_category_type_id_fk: int = Field(foreign_key="balance_entry_super_category_type.id")
    super_category: BalanceEntrySuperCategory = Relationship(back_populates="categories")
    entry_types: List["BalanceEntryType"] = Relationship(back_populates="category")

class BalanceEntryType(BaseMixin, table=True):
    __tablename__ = "balance_entry_type"
    
    name: str = Field(max_length=255)
    account_no: str = Field(max_length=50)
    page: Optional[str] = Field(max_length=50)
    line: Optional[str] = Field(max_length=50)
    balance_entry_category_type_id_fk: int = Field(foreign_key="balance_entry_category_type.id")
    
    category: BalanceEntryCategory = Relationship(back_populates="entry_types")
    balance_sheets: List["BalanceSheet"] = Relationship(back_populates="entry_type")

class BalanceFundType(BaseMixin, table=True):
    __tablename__ = "balance_fund_type"
    
    state_id: str = Field(max_length=50)
    state_name: str = Field(max_length=255)
    balance_sheets: List["BalanceSheet"] = Relationship(back_populates="fund_type")

class BalanceSheet(BaseMixin, table=True):
    __tablename__ = "balance_sheet"
    
    doe_form_id_fk: int = Field(foreign_key="doe_form.id")
    balance_entry_type_id_fk: int = Field(foreign_key="balance_entry_type.id")
    balance_fund_type_id_fk: int = Field(foreign_key="balance_fund_type.id")
    value: Optional[float]
    
    doe_form: DOEForm = Relationship(back_populates="balance_sheets")
    entry_type: BalanceEntryType = Relationship(back_populates="balance_sheets")
    fund_type: BalanceFundType = Relationship(back_populates="balance_sheets")

# Revenue Models
class RevenueEntrySuperCategory(BaseMixin, table=True):
    __tablename__ = "revenue_entry_super_category_type"
    
    name: str = Field(max_length=255)
    categories: List["RevenueEntryCategory"] = Relationship(back_populates="super_category")

class RevenueEntryCategory(BaseMixin, table=True):
    __tablename__ = "revenue_entry_category_type"
    
    name: str = Field(max_length=255)
    revenue_entry_super_category_type_id_fk: int = Field(foreign_key="revenue_entry_super_category_type.id")
    super_category: RevenueEntrySuperCategory = Relationship(back_populates="categories")
    entry_types: List["RevenueEntryType"] = Relationship(back_populates="category")

class RevenueEntryType(BaseMixin, table=True):
    __tablename__ = "revenue_entry_type"
    
    name: str = Field(max_length=255)
    account_no: str = Field(max_length=50)
    page: Optional[str] = Field(max_length=50)
    line: Optional[str] = Field(max_length=50)
    revenue_entry_category_type_id_fk: int = Field(foreign_key="revenue_entry_category_type.id")
    
    category: RevenueEntryCategory = Relationship(back_populates="entry_types")
    revenues: List["Revenue"] = Relationship(back_populates="entry_type")

class RevenueFundType(BaseMixin, table=True):
    __tablename__ = "revenue_fund_type"
    
    state_id: str = Field(max_length=50)
    state_name: str = Field(max_length=255)
    revenues: List["Revenue"] = Relationship(back_populates="fund_type")

class Revenue(BaseMixin, table=True):
    __tablename__ = "revenue"
    
    doe_form_id_fk: int = Field(foreign_key="doe_form.id")
    revenue_entry_type_id_fk: int = Field(foreign_key="revenue_entry_type.id")
    revenue_fund_type_id_fk: int = Field(foreign_key="revenue_fund_type.id")
    value: Optional[float]
    
    doe_form: DOEForm = Relationship(back_populates="revenues")
    entry_type: RevenueEntryType = Relationship(back_populates="revenues")
    fund_type: RevenueFundType = Relationship(back_populates="revenues")

class RevenueStateTotal(BaseMixin, table=True):
    """State-level revenue data by year and entry type"""
    __tablename__ = "revenue_state_total"
    
    revenue_entry_type_id_fk: int = Field(foreign_key="revenue_entry_type.id", index=True)
    year: int = Field(index=True)
    value: Optional[float] = Field(default=None)

# Expenditure Models
class ExpenditureEntrySuperCategory(BaseMixin, table=True):
    __tablename__ = "expenditure_entry_super_category_type"
    
    name: str = Field(max_length=255)
    categories: List["ExpenditureEntryCategory"] = Relationship(back_populates="super_category")

class ExpenditureEntryCategory(BaseMixin, table=True):
    __tablename__ = "expenditure_entry_category_type"
    
    name: str = Field(max_length=255)
    expenditure_entry_super_category_type_id_fk: int = Field(foreign_key="expenditure_entry_super_category_type.id")
    super_category: ExpenditureEntrySuperCategory = Relationship(back_populates="categories")
    entry_types: List["ExpenditureEntryType"] = Relationship(back_populates="category")

class ExpenditureEntryType(BaseMixin, table=True):
    __tablename__ = "expenditure_entry_type"
    
    name: str = Field(max_length=255)
    account_no: str = Field(max_length=50)
    page: Optional[str] = Field(max_length=50)
    line: Optional[str] = Field(max_length=50)
    expenditure_entry_category_type_id_fk: int = Field(foreign_key="expenditure_entry_category_type.id")
    
    category: ExpenditureEntryCategory = Relationship(back_populates="entry_types")
    expenditures: List["Expenditure"] = Relationship(back_populates="entry_type")

class ExpenditureFundType(BaseMixin, table=True):
    __tablename__ = "expenditure_fund_type"
    
    state_id: str = Field(max_length=50)
    state_name: str = Field(max_length=255)
    expenditures: List["Expenditure"] = Relationship(back_populates="fund_type")

class Expenditure(BaseMixin, table=True):
    __tablename__ = "expenditure"
    
    doe_form_id_fk: int = Field(foreign_key="doe_form.id")
    expenditure_entry_type_id_fk: int = Field(foreign_key="expenditure_entry_type.id")
    expenditure_fund_type_id_fk: int = Field(foreign_key="expenditure_fund_type.id")
    value: Optional[float]
    
    doe_form: DOEForm = Relationship(back_populates="expenditures")
    entry_type: ExpenditureEntryType = Relationship(back_populates="expenditures")
    fund_type: ExpenditureFundType = Relationship(back_populates="expenditures")

class ExpenditureStateRollup(BaseMixin, table=True):
    """State-level expenditure data by year and school level"""
    __tablename__ = "expenditure_state_rollup"
    
    year: int = Field(index=True)
    operating_elementary: Optional[float] = Field(default=None)
    operating_middle: Optional[float] = Field(default=None)
    operating_high: Optional[float] = Field(default=None)
    operating_total: Optional[float] = Field(default=None)
    current_elementary: Optional[float] = Field(default=None) 
    current_middle: Optional[float] = Field(default=None)
    current_high: Optional[float] = Field(default=None)
    current_total: Optional[float] = Field(default=None)
    total: Optional[float] = Field(default=None)

class ExpenditureStateTotal(BaseMixin, table=True):
    """State-level expenditure data by year and entry type"""
    __tablename__ = "expenditure_state_total"
    
    expenditure_entry_type_id_fk: int = Field(foreign_key="expenditure_entry_type.id", index=True)
    year: int = Field(index=True)
    value: Optional[float] = Field(default=None)

class StateCostPerPupil(BaseMixin, table=True):
    """State level cost per pupil data by year"""
    __tablename__ = "state_cost_per_pupil"
    
    year: int = Field(index=True)
    elementary: Optional[int] = None
    middle: Optional[int] = None
    high: Optional[int] = None
    total: Optional[int] = None

class DistrictCostPerPupil(BaseMixin, table=True):
    """District level cost per pupil data by year"""
    __tablename__ = "district_cost_per_pupil"
    
    district_id_fk: int = Field(foreign_key="district.id", index=True)
    year: int = Field(index=True)
    elementary: Optional[int] = None
    middle: Optional[int] = None
    high: Optional[int] = None
    total: Optional[int] = None
    
    district: "District" = Relationship(back_populates="cost_per_pupil")


class PrivateOrg(BaseMixin, table=True):
    """An organization that files, or needn't file, a private school's Form 990: the school itself or its operator"""
    __tablename__ = "private_org"

    ein: str = Field(unique=True)
    name: str
    founded: Optional[int] = None
    # From its latest return that gives one
    mission: Optional[str] = None


class School990Link(BaseMixin, table=True):
    """Who files a private school's Form 990: the school, an operator whose one return covers it, or no one (and why)"""
    __tablename__ = "school_990_link"

    school_id_fk: int = Field(foreign_key="school.id")
    # own_return, operator_return, postcard_only, not_required_religious, no_irs_record or placeholder
    status: str
    ein: Optional[str] = Field(default=None, foreign_key="private_org.ein")
    note: Optional[str] = None


class PrivateOrg990(BaseMixin, table=True):
    """The figures from one of a private school organization's 990 or 990-EZ returns, as filed"""
    __tablename__ = "private_org_990"

    ein: str = Field(foreign_key="private_org.ein")
    tax_period_end: date
    form: str
    total_revenue: Optional[int] = None
    prior_total_revenue: Optional[int] = None
    program_service_revenue: Optional[int] = None
    contributions: Optional[int] = None
    government_grants: Optional[int] = None
    investment_income: Optional[int] = None
    # Realized and unrealized, apart from interest and dividends; part of total revenue
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
    # A count of people, not who they are
    paid_over_100k: Optional[int] = None
    endowment_eoy: Optional[int] = None
    endowment_board_designated_share: Optional[float] = None
    endowment_permanent_share: Optional[float] = None
    endowment_term_share: Optional[float] = None
    object_id: str


class PrivateOrg990RevenueLine(BaseMixin, table=True):
    """A return's program service revenue line, as filed, with the category the config's rules give it"""
    __tablename__ = "private_org_990_revenue_line"

    return_id: int = Field(foreign_key="private_org_990.id")
    line_no: int
    description: str
    business_code: Optional[str] = None
    amount: int
    # tuition, school_program, room_and_board, summer_auxiliary, extended_care, student_activities,
    # transportation, therapy_tutoring, human_services, unspecified_program, rental or other
    category: str


class SchoolTuitionSource(BaseMixin, table=True):
    """Whether a private school publishes its tuition for a school year, where, and who gets financial aid"""
    __tablename__ = "school_tuition_source"

    school_id_fk: int = Field(foreign_key="school.id")
    year: int
    # published, not_published or site_unavailable
    status: str
    source_url: Optional[str] = None
    retrieved_on: date
    # Who gets financial aid, as the school words it: "37% of students", "Nearly 35% of families", "74%"
    with_aid: Optional[str] = None
    note: Optional[str] = None


class SchoolTuition(BaseMixin, table=True):
    """A private school's published tuition for a grade band and kind of rate, with the fees every student pays"""
    __tablename__ = "school_tuition"

    school_id_fk: int = Field(foreign_key="school.id")
    year: int
    rate_no: int
    band: str
    lowest_grade_id_fk: int = Field(foreign_key="grades.id")
    highest_grade_id_fk: int = Field(foreign_key="grades.id")
    # standard, day, boarding, parishioner, non_parishioner, international, half_day, full_day or other
    rate_type: str
    rate_label: Optional[str] = None
    tuition: Decimal
    # None where the school names a required fee but not its amount
    required_fee: Optional[Decimal] = None
    fee_note: Optional[str] = None
    rate_note: Optional[str] = None
