from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime

class EducationFreedomAccountEntryGet(BaseModel):
    """Education Freedom Account entry schema"""
    id: int
    town_id_fk: int = Field(alias='town_id')
    year: int
    education_freedom_account_entry_type_id_fk: int = Field(alias='entry_type_id')
    value: Optional[float] = None
    date_created: datetime
    date_updated: datetime
    
    class Config:
        from_attributes = True
        populate_by_name = True

class EFAEntryTypeGet(BaseModel):
    """Combined Education Freedom Account entry type with its value for a specific year"""
    id: int
    name: str
    description: Optional[str] = None
    year: int
    value: Optional[float] = None
    
    class Config:
        from_attributes = True

class EFAEntryStateGet(BaseModel):
    """State-level aggregated Education Freedom Account entry data by year and type"""
    year: int
    education_freedom_account_entry_type_id_fk: int = Field(alias='entry_type_id')
    value: Optional[float] = None
    
    class Config:
        from_attributes = True
        populate_by_name = True


class PrivateSchoolEducationFreedomAccountPaymentGet(BaseModel):
    """EFA money paid to the school in a school year, for one category ("private_school" is tuition and fees)"""
    year: int
    category_code: str
    category_name: str
    amount: float


class PrivateSchoolEducationFreedomAccountServedGet(BaseModel):
    calendar_year: int
    students: int


class PrivateSchoolEducationFreedomAccountGet(BaseModel):
    """A private school's EFA payments and students, from the Children's Scholarship Fund's reports"""
    school_id: int
    # The names the reports give it
    providers: List[str]
    payments: List[PrivateSchoolEducationFreedomAccountPaymentGet]
    # Listed only for providers that served 10 or more
    served: List[PrivateSchoolEducationFreedomAccountServedGet]
