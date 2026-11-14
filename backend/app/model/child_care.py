from datetime import date, time
from typing import Optional

from sqlmodel import Field, SQLModel

from .base import BaseMixin


# -------------------- Child care programs (NH DHHS Child Care Search) --------------------

class ChildCareProgramType(BaseMixin, table=True):
    """The search's type of care: licensed group or family program, or a license-exempt one"""
    __tablename__ = "child_care_program_type"

    name: str = Field(max_length=100)
    is_licensed: bool


class ChildCareQualityRating(BaseMixin, table=True):
    """The older QRIS rating: Licensed, Licensed Plus, Accreditation (lowest first)"""
    __tablename__ = "child_care_quality_rating"

    name: str = Field(max_length=30)


class ChildCareRegion(BaseMixin, table=True):
    """DHHS's child care regions, by their number (not the region table's school regions)"""
    __tablename__ = "child_care_region"

    name: str = Field(max_length=100)


class ChildCareLicenseStatus(BaseMixin, table=True):
    """Active, or Permit Issued for a new program"""
    __tablename__ = "child_care_license_status"

    name: str = Field(max_length=30)


class ChildCareAvailability(BaseMixin, table=True):
    """What a program's page says about taking children: accepting, accepting on a wait list, not accepting"""
    __tablename__ = "child_care_availability"

    name: str = Field(max_length=100)


class ChildCareReviewType(BaseMixin, table=True):
    """A type of licensing visit: Monitoring Visit, Renewal Visit, ..."""
    __tablename__ = "child_care_review_type"

    name: str = Field(max_length=50)


class ChildCareFeatureCategory(BaseMixin, table=True):
    """One of the lists programs have: their license's program types, and their pages' Other Information lists"""
    __tablename__ = "child_care_feature_category"

    code: str = Field(max_length=30)  # license_type, financial_assistance, language, meals, ...
    name: str = Field(max_length=100)  # the list's heading on a program's page: Language Spoken by Staff


class ChildCareFeature(BaseMixin, table=True):
    """One value of one of the lists programs have"""
    __tablename__ = "child_care_feature"

    category_id_fk: int = Field(foreign_key="child_care_feature_category.id")
    name: str = Field(max_length=255)


class ChildCareProgram(BaseMixin, table=True):
    """A child care program with its latest details. Its capacity over time is in ChildCareProgramSnapshot."""
    __tablename__ = "child_care_program"

    source_id: str = Field(max_length=18)  # the portal's record id (its page's ?id=)
    provider_number: str = Field(max_length=20)  # CCCB-… (group), CCFB-… (family), LE-… (license exempt)
    name: str = Field(max_length=255)
    program_type_id_fk: int = Field(foreign_key="child_care_program_type.id")
    license_issue_date: Optional[date] = None
    license_expiration_date: Optional[date] = None
    min_age_months: Optional[float] = None  # the source's weeks, or years and months, as months
    max_age_months: Optional[float] = None  # the source's years, as months
    # Whether it serves each age group, by what age_groups_source says: "listed" (the age groups it lists
    # in the search), "license" (its license's program types) or "age_range"
    infant: Optional[bool] = None
    toddler: Optional[bool] = None
    preschool: Optional[bool] = None
    school_age: Optional[bool] = None
    age_groups_source: Optional[str] = Field(max_length=10, default=None)
    head_start: Optional[bool] = None  # from its page
    early_head_start: Optional[bool] = None  # from its page
    accepts_scholarship: bool  # an Active NH Child Care Scholarship provider
    preventive_protective_care: Optional[bool] = None
    quality_rating_id_fk: Optional[int] = Field(foreign_key="child_care_quality_rating.id", default=None)
    gsq_step: Optional[int] = None  # Granite Steps for Quality: 0 (Licensed) to 4
    issued_to: Optional[str] = Field(max_length=255, default=None)  # the licensee
    main_contact: Optional[str] = Field(max_length=255, default=None)  # from its page
    phone: Optional[str] = Field(max_length=50, default=None)
    email: Optional[str] = Field(max_length=255, default=None)
    email_hidden: Optional[bool] = None  # its page says it chose not to show its email
    street: Optional[str] = Field(max_length=255, default=None)
    city: Optional[str] = Field(max_length=100, default=None)  # as the source spells it
    zip: Optional[str] = Field(max_length=10, default=None)
    town_id_fk: Optional[int] = Field(foreign_key="town.id", default=None)
    county_id_fk: Optional[int] = Field(foreign_key="county.id", default=None)
    region_id_fk: Optional[int] = Field(foreign_key="child_care_region.id", default=None)
    mailing_street: Optional[str] = Field(max_length=255, default=None)
    mailing_city: Optional[str] = Field(max_length=100, default=None)
    mailing_zip: Optional[str] = Field(max_length=10, default=None)
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    details_updated: Optional[date] = None  # its page's "Last Updated"
    is_current: bool  # in the latest download


class ChildCareProgramSnapshot(BaseMixin, table=True):
    """What one download says about a program's license and capacity"""
    __tablename__ = "child_care_program_snapshot"

    program_id_fk: int = Field(foreign_key="child_care_program.id")
    as_of: date  # the download's date
    license_status_id_fk: Optional[int] = Field(foreign_key="child_care_license_status.id", default=None)
    capacity: int  # licensed, all ages
    infant_capacity: Optional[int] = None
    toddler_capacity: Optional[int] = None
    # From its page
    availability_id_fk: Optional[int] = Field(foreign_key="child_care_availability.id", default=None)
    infant_vacancies: Optional[int] = None
    toddler_vacancies: Optional[int] = None
    preschool_vacancies: Optional[int] = None
    school_age_vacancies: Optional[int] = None
    vacancies_updated: Optional[date] = None


class ChildCareProgramHours(BaseMixin, table=True):
    """When a program is open on a day of the week (1 Monday to 7 Sunday), from its latest page. A day can
    have more than one session (8 to 1 and 8 to 4)."""
    __tablename__ = "child_care_program_hours"

    program_id_fk: int = Field(foreign_key="child_care_program.id")
    schedule: int = 1  # the page's schedules have no names; each different one is numbered
    day_of_week: int
    opens: Optional[time] = None
    closes: Optional[time] = None


class ChildCareProgramRate(BaseMixin, table=True):
    """What a program charges for an age group by the hour, day, week or month, from its latest page"""
    __tablename__ = "child_care_program_rate"

    program_id_fk: int = Field(foreign_key="child_care_program.id")
    schedule: int = 1  # the schedule it's listed with
    age_group: str = Field(max_length=20)  # Infant, Toddler, Preschool, School Age
    period: str = Field(max_length=10)  # hourly, daily, weekly or monthly
    amount: float  # dollars


class ChildCareProgramFeatureLink(BaseMixin, table=True):
    """A program's license type, or a value of one of its latest page's lists"""
    __tablename__ = "child_care_program_feature_xref"

    program_id_fk: int = Field(foreign_key="child_care_program.id")
    feature_id_fk: int = Field(foreign_key="child_care_feature.id")


class ChildCareInspection(BaseMixin, table=True):
    """A licensing visit to a program, from its pages (each shows three years; every saved download's are kept)"""
    __tablename__ = "child_care_inspection"

    program_id_fk: int = Field(foreign_key="child_care_program.id")
    visit_id: Optional[str] = Field(max_length=18, default=None)
    review_date: date
    review_type_id_fk: Optional[int] = Field(foreign_key="child_care_review_type.id", default=None)
    items_reviewed: Optional[int] = None
    items_compliant: Optional[int] = None
    document_url: Optional[str] = None  # older visits have a document instead of counts


# -------------------- Views --------------------

class ChildCareTotals(SQLModel):
    """A group of programs added up for one download"""
    programs: int
    capacity: int
    licensed_programs: int
    licensed_capacity: int
    infant_capacity: Optional[int] = None
    toddler_capacity: Optional[int] = None
    # The programs that serve each age group
    infant_programs: int
    toddler_programs: int
    preschool_programs: int
    school_age_programs: int
    infant_vacancies: Optional[int] = None
    toddler_vacancies: Optional[int] = None
    preschool_vacancies: Optional[int] = None
    school_age_vacancies: Optional[int] = None


class TownChildCare(ChildCareTotals, table=True):
    """View: each download's programs added up by town"""
    __tablename__ = "town_child_care"

    town_id_fk: int = Field(primary_key=True)
    as_of: date = Field(primary_key=True)


class DistrictChildCare(ChildCareTotals, table=True):
    """View: each download's programs added up by the district that teaches each town's kindergarten"""
    __tablename__ = "district_child_care"

    district_id_fk: int = Field(primary_key=True)
    as_of: date = Field(primary_key=True)


class StateChildCare(ChildCareTotals, table=True):
    """View: each download's programs added up statewide"""
    __tablename__ = "state_child_care"

    as_of: date = Field(primary_key=True)
