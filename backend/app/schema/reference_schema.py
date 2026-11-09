from datetime import date
from typing import List, Optional

from pydantic import BaseModel


class ReferenceTopicGet(BaseModel):
    """A topic in the reference library, with how many of its facts are current"""
    id: int
    slug: str
    title: str
    kind: str
    question_type: str
    description: str
    summary: Optional[str] = None
    current_facts: int


class ReferenceFactGet(BaseModel):
    id: int
    position: int
    statement: str
    citation: Optional[str] = None
    source_url: str
    site: str
    as_of: Optional[date] = None
    as_of_text: str
    review_by: date
    district_id: Optional[int] = None
    town_id: Optional[int] = None


class ReferenceTopicDetailGet(ReferenceTopicGet):
    """A topic and its current facts (those within their review date)"""
    facts: List[ReferenceFactGet]


class ReferenceReviewGet(BaseModel):
    """A fact past its review date, or due within the days asked for"""
    topic: str
    source_file: str
    position: int
    statement: str
    source_url: str
    review_by: date
    overdue: bool
