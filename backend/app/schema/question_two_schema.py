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
    is_official: bool
