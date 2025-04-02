from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from .location_schema import DistrictGet

# Balance Sheet Related Schemas
class BalanceFundTypeGet(BaseModel):
    id: int
    state_id: str
    state_name: str

    class Config:
        from_attributes = True

class BalanceEntryTypeGet(BaseModel):
    id: int
    name: str
    account_no: str
    page: Optional[str] = None
    line: Optional[str] = None
    balance_entry_category_type_id_fk: int = Field(alias='balance_entry_category_type_id')

    class Config:
        from_attributes = True
        populate_by_name = True

class BalanceEntryCategoryGet(BaseModel):
    id: int
    name: str
    balance_entry_super_category_id_fk: int = Field(alias='balance_entry_super_category_id')

    class Config:
        from_attributes = True
        populate_by_name = True

class BalanceEntrySuperCategoryGet(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class BalanceSheetGet(BaseModel):
    id: int
    value: Optional[float] = None
    entry_type: Optional[BalanceEntryTypeGet] = None
    fund_type: Optional[BalanceFundTypeGet] = None

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

class RevenueEntryTypeGet(BaseModel):
    id: int
    name: str
    account_no: str
    page: Optional[str] = None
    line: Optional[str] = None
    revenue_entry_category_type_id_fk: int = Field(alias='revenue_entry_category_type_id')

    class Config:
        from_attributes = True
        populate_by_name = True

class RevenueEntryCategoryGet(BaseModel):
    id: int
    name: str
    revenue_entry_super_category_id_fk: int = Field(alias='revenue_entry_super_category_id')

    class Config:
        from_attributes = True
        populate_by_name = True

class RevenueEntrySuperCategoryGet(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class RevenueGet(BaseModel):
    id: int
    value: Optional[float] = None
    entry_type: Optional[RevenueEntryTypeGet] = None
    fund_type: Optional[RevenueFundTypeGet] = None

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

class ExpenditureEntryTypeGet(BaseModel):
    id: int
    name: str
    account_no: str
    page: Optional[str] = None
    line: Optional[str] = None
    expenditure_entry_category_type_id_fk: int = Field(alias='expenditure_entry_category_type_id')

    class Config:
        from_attributes = True
        populate_by_name = True

class ExpenditureEntryCategoryGet(BaseModel):
    id: int
    name: str
    expenditure_entry_super_category_id_fk: int = Field(alias='expenditure_entry_super_category_id')

    class Config:
        from_attributes = True
        populate_by_name = True

class ExpenditureEntrySuperCategoryGet(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class ExpenditureGet(BaseModel):
    id: int
    value: Optional[float] = None
    entry_type: Optional[ExpenditureEntryTypeGet] = None
    fund_type: Optional[ExpenditureFundTypeGet] = None

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

    class Config:
        from_attributes = True
