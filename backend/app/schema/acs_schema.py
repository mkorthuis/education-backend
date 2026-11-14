from typing import Dict, List, Optional, Union

from pydantic import BaseModel

Number = Optional[Union[int, float]]


class AcsReleaseGet(BaseModel):
    year: int  # the last year of the five (2024: 2020-2024)
    period: str
    dollars_year: int  # dollar amounts are in this year's dollars


class AcsTableGet(BaseModel):
    code: str  # Census's table id: B25004
    title: str
    universe: str  # who or what it counts
    tier: str  # core or extended
    why: str


class AcsTopicGet(BaseModel):
    code: str  # the {level}/{topic} endpoints' topic
    name: str
    tables: List[AcsTableGet]


class AcsVariableReleaseGet(BaseModel):
    year: int
    # same; dollars (the same, in that release's dollars); years_move (the same line, its years moved with
    # the release: "Built 2014 or later" for "Built 2020 or later")
    comparability: str


class AcsVariableGet(BaseModel):
    code: str  # Census's line id: B25004_006
    column_name: str  # its key in the {level}/{topic} endpoints' values
    table: str
    table_title: str
    topic: str
    tier: str
    label: str  # Census's label, with those it's nested under
    description: str
    unit: str  # count, dollars, years, year, people, index (0-1), percent
    releases: List[AcsVariableReleaseGet]


class AcsMeasureGet(BaseModel):
    name: str  # its key in the summary endpoints' measures
    label: str
    description: str
    unit: str  # percent for a share
    kind: str  # value, sum or share
    formula: str  # by Census's line ids


class AcsComparison(BaseModel):
    """The measure in an earlier release, and whether the change is more than the margins of error allow"""
    release_year: int
    value: Number = None
    moe: Number = None
    reliability: Optional[str] = None
    change: Number = None
    # Census's test at 90% confidence: the change is larger than the square root of the sum of the two
    # margins of error squared. None when either is missing.
    significant: Optional[bool] = None


class AcsMeasureValue(BaseModel):
    value: Number = None
    moe: Number = None  # 90% margin of error
    reliability: Optional[str] = None  # high, caution or low, by coefficient of variation
    compare: Optional[AcsComparison] = None


class AcsSummaryGet(BaseModel):
    release_year: int
    period: str
    measures: Dict[str, AcsMeasureValue]  # by acs_measure name, in its order


class TownAcsSummaryGet(AcsSummaryGet):
    town_id: int
    town_name: str


class DistrictAcsSummaryGet(AcsSummaryGet):
    district_id: int
    district_name: str
    census_type: str  # elementary, secondary or unified


class StateAcsSummaryGet(AcsSummaryGet):
    pass


class AcsValue(BaseModel):
    estimate: Number = None
    moe: Number = None  # 90% margin of error


class AcsTopicValuesGet(BaseModel):
    release_year: int
    period: str
    values: Dict[str, AcsValue]  # by column name (see /acs/variable)


class TownAcsTopicGet(AcsTopicValuesGet):
    town_id: int
    town_name: str


class DistrictAcsTopicGet(AcsTopicValuesGet):
    district_id: int
    district_name: str
    census_type: str


class StateAcsTopicGet(AcsTopicValuesGet):
    pass
