from typing import Optional

from sqlmodel import Field

from .base import BaseMixin


class DistrictQuestionTwo(BaseMixin, table=True):
    """A school district's vote on ballot Question 2 (HB 1300, 2026 chapter 324), which decides whether
    it caps its school property taxes (60% yes)."""
    __tablename__ = "district_question_two"

    district_id_fk: int = Field(foreign_key="district.id")
    year: int  # the general election's year (2026, 2028)
    yes_votes: int
    no_votes: int
    yes_percentage: float  # as the results report it, to a tenth of a percent
    passed: bool  # adopted the school tax cap: 60% yes or more
    towns: Optional[str] = None  # the towns whose votes make up the total, as the source counts them ("; " between)
    is_official: bool = False  # false until each school board ratifies its towns' results
    note: Optional[str] = None


class SauQuestionTwo(BaseMixin, table=True):
    """An SAU's vote on Question 2 across all its towns, which decides whether it caps its
    central-office spending (60% yes)."""
    __tablename__ = "sau_question_two"

    sau_id_fk: int = Field(foreign_key="sau.id")
    year: int
    yes_votes: int
    no_votes: int
    yes_percentage: float
    passed: bool  # adopted the SAU spending cap: 60% yes or more
    towns: Optional[str] = None
    is_official: bool = False
    note: Optional[str] = None  # where the source's listing leaves a town out or puts one in the wrong SAU


class TownQuestionTwo(BaseMixin, table=True):
    """A town's own vote on Question 2. It decides neither cap on its own: its districts' and SAU's
    votes do."""
    __tablename__ = "town_question_two"

    town_id_fk: int = Field(foreign_key="town.id")
    year: int
    yes_votes: int
    no_votes: int
    yes_percentage: float
    is_official: bool = False
    note: Optional[str] = None
