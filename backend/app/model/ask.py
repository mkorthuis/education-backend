from typing import List, Optional

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import JSONB
from sqlmodel import Field

from .base import BaseMixin


# -------------------- Ask a Question --------------------

class AskQuestion(BaseMixin, table=True):
    """
    A question asked on Ask a Question, and how it was answered, so we can see what visitors ask.
    Nothing about who asked: no address, account or device. date_created is when it was asked.
    """
    __tablename__ = "ask_question"

    question: str
    # The earlier questions on the visitor's page that it may follow up, oldest first (their text only)
    earlier_questions: List[str] = Field(default_factory=list, sa_column=Column(JSONB, nullable=False, server_default="[]"))
    deep: bool  # asked taking more time
    cached: bool = False  # answered from the saved answers
    # asked (no outcome recorded, e.g. the visitor left first), an answer's status (answered, partial,
    # no_data, general, declined), failed, limit (the daily limit was reached) or unavailable
    status: str = Field(default="asked", max_length=20)
    seconds: Optional[float] = None  # how long a new answer took
    # The district or school page it was asked from, if any: district or school, and its id
    place_kind: Optional[str] = Field(default=None, max_length=10)
    place_id: Optional[int] = None


class AskTurn(BaseMixin, table=True):
    """
    An answered question on Ask a Question, saved so its conversation can be shared by link: the
    address /ask/<share_id> shows it after the turns it followed (parent). The server saves its own
    answer, never one a visitor sends. Nothing about who asked. Kept for a year, like the question log.
    """
    __tablename__ = "ask_turn"

    share_id: str = Field(unique=True, max_length=16)
    # The turn it followed up, if any; gone (None) once that turn has passed the retention period
    parent_id: Optional[int] = Field(default=None, foreign_key="ask_turn.id")
    question: str
    # The answer as the site showed it (AskResponse, without cached or share_id)
    answer: dict = Field(sa_column=Column(JSONB, nullable=False))
    deep: bool = False
    # The district or school page it was asked from, if any
    place_kind: Optional[str] = Field(default=None, max_length=10)
    place_id: Optional[int] = None
    # One link for the same question and answer after the same turn: a digest of them all
    fingerprint: str = Field(unique=True, max_length=64)
