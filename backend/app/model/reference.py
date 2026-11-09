from datetime import date
from typing import Optional

from sqlmodel import Field

from .base import BaseMixin


# -------------------- Reference library --------------------

class ReferenceTopic(BaseMixin, table=True):
    """A subject in the reference library, such as "What schools must do about bullying" """
    __tablename__ = "reference_topic"

    slug: str = Field(max_length=100)
    title: str = Field(max_length=255)
    kind: str = Field(max_length=20)  # rule, term, how_it_works, research, programs or local
    question_type: str = Field(max_length=30)
    description: str  # what the topic covers, which the Ask chooses topics by
    summary: Optional[str] = None  # a research brief's summary
    source_file: str = Field(max_length=100)
    display_order: int


class ReferenceFact(BaseMixin, table=True):
    """One cited statement in the reference library"""
    __tablename__ = "reference_fact"

    reference_topic_id_fk: int = Field(foreign_key="reference_topic.id")
    position: int
    statement: str
    citation: Optional[str] = Field(default=None, max_length=500)  # e.g. "RSA 193-F:4, II(i)"; organizations' pages have none
    source_url: str = Field(max_length=1000)
    as_of: Optional[date] = None  # when it was checked against the source
    as_of_text: str = Field(max_length=255)  # as written, e.g. "Wayback snapshot 2026-10-30"
    review_by: date  # after this it isn't used until someone checks it again
    note: Optional[str] = None  # for reviewers
    district_id_fk: Optional[int] = Field(default=None, foreign_key="district.id")
    town_id_fk: Optional[int] = Field(default=None, foreign_key="town.id")
