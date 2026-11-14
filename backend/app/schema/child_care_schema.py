from datetime import date, time
from typing import List, Optional

from pydantic import BaseModel


class ChildCareTotalsGet(BaseModel):
    """A group of programs added up for one download (as_of)"""
    as_of: date
    programs: int
    capacity: int  # licensed capacity, all ages
    licensed_programs: int
    licensed_capacity: int
    infant_capacity: Optional[int] = None
    toddler_capacity: Optional[int] = None
    # The programs that serve each age group
    infant_programs: int
    toddler_programs: int
    preschool_programs: int
    school_age_programs: int
    # Openings the programs report on their pages, each as of its own vacancies_updated
    infant_vacancies: Optional[int] = None
    toddler_vacancies: Optional[int] = None
    preschool_vacancies: Optional[int] = None
    school_age_vacancies: Optional[int] = None


class StateChildCareGet(ChildCareTotalsGet):
    pass


class TownChildCareGet(ChildCareTotalsGet):
    town_id: int
    town_name: str


class DistrictChildCareGet(ChildCareTotalsGet):
    district_id: int
    district_name: str


class ChildCareProgramGet(BaseModel):
    """A program's latest details, with its latest download's license status, capacity and vacancies"""
    id: int
    provider_number: str
    name: str
    program_type: str
    is_licensed: bool
    license_status: Optional[str] = None
    license_issue_date: Optional[date] = None
    license_expiration_date: Optional[date] = None
    issued_to: Optional[str] = None
    main_contact: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None  # blank when the program hides it and the request asks hide_hidden_email
    email_hidden: Optional[bool] = None  # its page says it chose not to show its email
    street: Optional[str] = None
    city: Optional[str] = None
    zip: Optional[str] = None
    town_id: Optional[int] = None
    town_name: Optional[str] = None
    county: Optional[str] = None
    region: Optional[str] = None  # DHHS's child care region
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    min_age_months: Optional[float] = None
    max_age_months: Optional[float] = None
    infant: Optional[bool] = None
    toddler: Optional[bool] = None
    preschool: Optional[bool] = None
    school_age: Optional[bool] = None
    age_groups_source: Optional[str] = None  # listed, license or age_range
    head_start: Optional[bool] = None
    early_head_start: Optional[bool] = None
    accepts_scholarship: bool
    preventive_protective_care: Optional[bool] = None
    quality_rating: Optional[str] = None
    gsq_step: Optional[int] = None  # Granite Steps for Quality: 0 (Licensed) to 4
    as_of: date  # the latest download it's in
    capacity: int
    infant_capacity: Optional[int] = None
    toddler_capacity: Optional[int] = None
    availability: Optional[str] = None
    infant_vacancies: Optional[int] = None
    toddler_vacancies: Optional[int] = None
    preschool_vacancies: Optional[int] = None
    school_age_vacancies: Optional[int] = None
    vacancies_updated: Optional[date] = None
    details_updated: Optional[date] = None
    is_current: bool
    source_url: str  # its page on the DHHS Child Care Search


class ChildCareHoursGet(BaseModel):
    schedule: int  # the page's schedules have no names; each different one is numbered
    day_of_week: int  # 1 Monday to 7 Sunday
    day: str
    opens: Optional[time] = None
    closes: Optional[time] = None


class ChildCareRateGet(BaseModel):
    schedule: int
    age_group: str  # Infant, Toddler, Preschool, School Age
    period: str  # hourly, daily, weekly, monthly
    amount: float


class ChildCareFeatureGet(BaseModel):
    category: str  # license_type, financial_assistance, language, meals, ...
    category_name: str  # the list's heading on the program's page
    values: List[str]


class ChildCareInspectionGet(BaseModel):
    review_date: date
    review_type: Optional[str] = None
    items_reviewed: Optional[int] = None
    items_compliant: Optional[int] = None
    document_url: Optional[str] = None  # older visits have a document instead of counts


class ChildCareSnapshotGet(BaseModel):
    as_of: date
    license_status: Optional[str] = None
    capacity: int
    infant_capacity: Optional[int] = None
    toddler_capacity: Optional[int] = None
    availability: Optional[str] = None
    infant_vacancies: Optional[int] = None
    toddler_vacancies: Optional[int] = None
    preschool_vacancies: Optional[int] = None
    school_age_vacancies: Optional[int] = None
    vacancies_updated: Optional[date] = None


class ChildCareProgramDetailGet(ChildCareProgramGet):
    mailing_street: Optional[str] = None
    mailing_city: Optional[str] = None
    mailing_zip: Optional[str] = None
    hours: List[ChildCareHoursGet]
    rates: List[ChildCareRateGet]
    features: List[ChildCareFeatureGet]
    inspections: List[ChildCareInspectionGet]  # newest first
    snapshots: List[ChildCareSnapshotGet]  # every download it's in, oldest first
