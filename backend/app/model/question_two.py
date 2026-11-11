from sqlmodel import Field

from .base import BaseMixin


class DistrictQuestionTwo(BaseMixin, table=True):
    """A school district's vote on ballot Question 2 (HB 1300, 2026 chapter 324), which decides whether
    it caps its school property taxes (60% yes). The SAU central-office cap on the same question is
    decided by the vote across the SAU's towns."""
    __tablename__ = "district_question_two"

    district_id_fk: int = Field(foreign_key="district.id")
    year: int  # the general election's year (2026, 2028)
    yes_votes: int
    no_votes: int
    yes_percentage: float  # as the results report it, to a tenth of a percent
    passed: bool  # adopted the school tax cap: 60% yes or more
    is_official: bool = False  # false until each school board ratifies its towns' results
