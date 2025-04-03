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
