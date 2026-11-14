from datetime import date
from typing import Optional

from sqlmodel import Field

from .base import BaseMixin


# -------------------- Adequacy aid (NH DOE's adequate education grants) --------------------
# Values are the DOE's, as published; town_adequacy_aid_summary and district_adequacy_aid are views built on them.

class AdequacyAidYear(BaseMixin, table=True):
    """A fiscal year of DOE calculations (2027: the 2026-27 school year, as doe_form.year)"""
    __tablename__ = "adequacy_aid_year"

    fiscal_year: int
    school_year: str = Field(max_length=7)  # 2026-27
    status: str = Field(max_length=10)  # final, or estimate (before April's final calculation)
    as_of: date  # the DOE's date on the calculation
    summary_url: str  # the DOE's workbook of every town's calculation
    split_url: Optional[str] = None  # the DOE's split of towns' grants among their districts
    explained_url: Optional[str] = None  # the DOE's explanation of the year's calculation


class AdequacyAidComponent(BaseMixin, table=True):
    """A part of the calculation in any year: frl_differentiated_aid, swept, adequacy_grant, ..."""
    __tablename__ = "adequacy_aid_component"

    code: str = Field(max_length=60)
    name: str = Field(max_length=150)
    description: str
    unit: str = Field(max_length=20)  # count, dollars, dollars_per_pupil, fraction
    # students, cost (an aid line), cost_total, swept, added_aid, hold_harmless, result, basis (used along the way)
    role: str = Field(max_length=20)
    sort: int  # its place on the page


class AdequacyAidParameter(BaseMixin, table=True):
    """A year's rate, threshold or share: base_per_pupil 4351, eng_ceiling 7,003,972, ..."""
    __tablename__ = "adequacy_aid_parameter"

    fiscal_year: int = Field(foreign_key="adequacy_aid_year.fiscal_year")
    code: str = Field(max_length=60)
    name: str = Field(max_length=150)
    value: float
    unit: str = Field(max_length=25)  # dollars_per_pupil, dollars, fraction, dollars_per_thousand, dollars_per_dollar
    citation: str
    source_url: str


class AdequacyAidStep(BaseMixin, table=True):
    """A step of a year's calculation: the part it produces, how, and why. A formula, over component and parameter
    codes, reproduces the DOE's value for every town within tolerance; a step without one is explained only."""
    __tablename__ = "adequacy_aid_step"

    fiscal_year: int = Field(foreign_key="adequacy_aid_year.fiscal_year")
    step: int
    component_id_fk: int = Field(foreign_key="adequacy_aid_component.id")
    formula: Optional[str] = None
    tolerance: float
    explanation: str
    citation: str


class TownAdequacyAid(BaseMixin, table=True):
    """A town's value for one part of a year's calculation, as the DOE publishes it"""
    __tablename__ = "town_adequacy_aid"

    town_id_fk: int = Field(foreign_key="town.id")
    fiscal_year: int = Field(foreign_key="adequacy_aid_year.fiscal_year")
    component_id_fk: int = Field(foreign_key="adequacy_aid_component.id")
    value: float


class StateAdequacyAid(BaseMixin, table=True):
    """The DOE's statewide total for one part of a year's calculation"""
    __tablename__ = "state_adequacy_aid"

    fiscal_year: int = Field(foreign_key="adequacy_aid_year.fiscal_year")
    component_id_fk: int = Field(foreign_key="adequacy_aid_component.id")
    value: float


class DistrictAdequacyAidShare(BaseMixin, table=True):
    """What a district receives from one member town in a year"""
    __tablename__ = "district_adequacy_aid_share"

    district_id_fk: int = Field(foreign_key="district.id")
    town_id_fk: int = Field(foreign_key="town.id")
    fiscal_year: int = Field(foreign_key="adequacy_aid_year.fiscal_year")
    adequacy_grant: float  # paid by the state
    swept_retained: float  # statewide education property tax kept locally
    source: str = Field(max_length=10)  # doe_split (the DOE's split file) or whole_town (the town's one district)
