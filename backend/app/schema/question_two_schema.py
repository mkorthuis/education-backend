from typing import List, Optional

from pydantic import BaseModel


class DistrictQuestionTwoGet(BaseModel):
    id: int
    district_id: int
    district_name: str
    year: int
    yes_votes: int
    no_votes: int
    yes_percentage: float
    passed: bool
    towns: List[str] = []  # the towns whose votes make up the total, as the source counts them
    is_official: bool
    note: Optional[str] = None


class SauQuestionTwoGet(BaseModel):
    id: int
    sau_id: int  # the SAU's number
    sau_name: str
    districts: List[str]  # the SAU's school districts that voted
    year: int
    yes_votes: int
    no_votes: int
    yes_percentage: float
    passed: bool
    towns: List[str] = []  # the towns the source lists under the SAU
    is_official: bool
    note: Optional[str] = None


class TownQuestionTwoGet(BaseModel):
    id: int
    town_id: int
    town_name: str
    year: int
    yes_votes: int
    no_votes: int
    yes_percentage: float
    is_official: bool
    note: Optional[str] = None
