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
