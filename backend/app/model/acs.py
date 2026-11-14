from typing import Optional

from sqlmodel import Field

from .base import BaseMixin


# -------------------- American Community Survey 5-year estimates (Census Bureau) --------------------
# The API reads the materialized views built on these (app.etl.acs.view_statements): for each level
# (town, district, state), one per topic ({level}_acs_{topic}) and a summary ({level}_acs_summary).

class AcsTopic(BaseMixin, table=True):
    """A group of tables, with a view per level: population, children, households, race_language, ..."""
    __tablename__ = "acs_topic"

    code: str = Field(max_length=30)
    name: str = Field(max_length=100)


class AcsAnnotation(BaseMixin, table=True):
    """A code the summary files give in place of a number ("too few sample observations")"""
    __tablename__ = "acs_annotation"

    code: int
    name: str = Field(max_length=255)


class AcsRelease(BaseMixin, table=True):
    """A 5-year release, by its last year (2024: 2020-2024)"""
    __tablename__ = "acs_release"

    year: int
    period: str = Field(max_length=9)
    dollars_year: int  # dollar amounts are in this year's dollars
    source_url: str


class AcsTable(BaseMixin, table=True):
    """A Census table loaded (B25004 Vacancy Status)"""
    __tablename__ = "acs_table"

    code: str = Field(max_length=10)
    title: str
    universe: str  # who or what it counts
    topic_id_fk: int = Field(foreign_key="acs_topic.id")
    tier: str = Field(max_length=10)  # core: likely to be used soon; extended: kept for later
    why: str


class AcsVariable(BaseMixin, table=True):
    """One value of a table (B25004_006: vacant homes held for seasonal use), and its column in the views"""
    __tablename__ = "acs_variable"

    code: str = Field(max_length=12)
    table_id_fk: int = Field(foreign_key="acs_table.id")
    line: int
    column_name: str = Field(max_length=59)  # its estimate's column; its margin of error's is <column_name>_moe
    label: str  # Census's label, with those it's nested under ("Total > Vacant > For seasonal...")
    description: str
    unit: str = Field(max_length=20)  # count, dollars, years, year, people, index (0-1), percent


class AcsVariableRelease(BaseMixin, table=True):
    """A release that has a value: the latest has them all; an earlier one, those that mean the same in it"""
    __tablename__ = "acs_variable_release"

    variable_id_fk: int = Field(foreign_key="acs_variable.id")
    release_year: int = Field(foreign_key="acs_release.year")
    label: str  # the label in that release
    # same; dollars (the same, in that release's dollars); years_move (the same line with its years moved
    # with the release: "Built 2014 or later" for "Built 2020 or later")
    comparability: str = Field(max_length=10)


class AcsMeasure(BaseMixin, table=True):
    """A measure in the {level}_acs_summary views: its columns are <name>, <name>_moe and <name>_reliability"""
    __tablename__ = "acs_measure"

    name: str = Field(max_length=59)
    sort: int  # its place in the summary
    label: str = Field(max_length=100)
    description: str
    unit: str = Field(max_length=20)  # percent for a share; a value's or sum's lines' unit otherwise
    kind: str = Field(max_length=5)  # value, sum or share
    formula: str  # by Census's line ids: "(B25004_006) / (B25001_001)"


class AcsTown(BaseMixin, table=True):
    """The Census county subdivision a town is"""
    __tablename__ = "acs_town"

    town_id_fk: int = Field(foreign_key="town.id")
    census_geo_id: str = Field(max_length=20)
    census_name: str


class AcsDistrict(BaseMixin, table=True):
    """The Census school district a district is"""
    __tablename__ = "acs_district"

    district_id_fk: int = Field(foreign_key="district.id")
    census_geo_id: str = Field(max_length=20)
    census_name: str
    census_type: str = Field(max_length=10)  # elementary, secondary or unified


class TownAcsEstimate(BaseMixin, table=True):
    """A value for a town in a release, with its margin of error (90%)"""
    __tablename__ = "town_acs_estimate"

    town_id_fk: int = Field(foreign_key="town.id")
    release_year: int = Field(foreign_key="acs_release.year")
    variable_id_fk: int = Field(foreign_key="acs_variable.id")
    estimate: Optional[float] = None  # blank when Census gives a code instead (estimate_annotation_id_fk)
    moe: Optional[float] = None  # 0 for a controlled estimate
    estimate_annotation_id_fk: Optional[int] = Field(foreign_key="acs_annotation.id", default=None)
    moe_annotation_id_fk: Optional[int] = Field(foreign_key="acs_annotation.id", default=None)


class DistrictAcsEstimate(BaseMixin, table=True):
    """A value for a school district in a release, with its margin of error (90%)"""
    __tablename__ = "district_acs_estimate"

    district_id_fk: int = Field(foreign_key="district.id")
    release_year: int = Field(foreign_key="acs_release.year")
    variable_id_fk: int = Field(foreign_key="acs_variable.id")
    estimate: Optional[float] = None
    moe: Optional[float] = None
    estimate_annotation_id_fk: Optional[int] = Field(foreign_key="acs_annotation.id", default=None)
    moe_annotation_id_fk: Optional[int] = Field(foreign_key="acs_annotation.id", default=None)


class StateAcsEstimate(BaseMixin, table=True):
    """A value for New Hampshire in a release, with its margin of error (90%)"""
    __tablename__ = "state_acs_estimate"

    release_year: int = Field(foreign_key="acs_release.year")
    variable_id_fk: int = Field(foreign_key="acs_variable.id")
    estimate: Optional[float] = None
    moe: Optional[float] = None
    estimate_annotation_id_fk: Optional[int] = Field(foreign_key="acs_annotation.id", default=None)
    moe_annotation_id_fk: Optional[int] = Field(foreign_key="acs_annotation.id", default=None)
