from typing import Annotated, List, Literal, Optional, Union

from pydantic import BaseModel, Field


# Sizes far past what the site sends (500-character questions, four short paragraphs an answer,
# ten earlier questions), so an oversized request is refused before it's read further
class AskEarlierTurn(BaseModel):
    """An earlier question on the visitor's Ask page and its answer, so a follow-up can refer to it"""
    question: str = Field(..., max_length=2000)
    answer: List[Annotated[str, Field(max_length=5000)]] = Field(default_factory=list, max_length=10)


class AskPlace(BaseModel):
    """The district or school page on the site a question was asked from"""
    kind: Literal["district", "school"]
    id: int


class AskRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=5000, description="The visitor's question in plain English")
    history: List[AskEarlierTurn] = Field(
        default_factory=list,
        max_length=20,
        description="The visitor's earlier questions on the page, oldest first, with their answers; the last ten are used to understand a follow-up",
    )
    deep: bool = Field(default=False, description="Take More Time: Claude thinks longer before answering; slower, for complex questions")
    place: Optional[AskPlace] = Field(
        default=None,
        description="The district or school page the question was asked from: a question that names no place is about it",
    )
    stream: bool = Field(
        default=False,
        description='Show the answer as it\'s written: a new answer comes as lines of JSON, {"partial": [paragraphs so far]} while it\'s written, then the answer',
    )
    parent: Optional[str] = Field(
        default=None,
        max_length=32,
        description="The share_id of the answer it follows up: its earlier questions are that saved conversation's, and history is ignored",
    )


class AskChartPoint(BaseModel):
    label: str
    values: List[Optional[float]]


class AskChart(BaseModel):
    title: str
    kind: Literal["line", "bar"]
    unit: str
    x_label: str
    series: List[str]
    points: List[AskChartPoint]
    note: Optional[str] = None


class AskTable(BaseModel):
    title: str
    unit: str
    columns: List[str]
    units: List[Optional[str]] = []
    rows: List[List[Union[float, int, str, None]]]
    note: Optional[str] = None


class AskReference(BaseModel):
    label: str
    path: str


class AskSource(BaseModel):
    """A page outside this site an answer relies on: a law, a study, an organization's page. Only links
    stored with the site's reference facts and national datasets appear here."""
    label: str
    url: str
    site: str
    as_of: Optional[str] = None
    # What in the answer the source supports, one line per fact, written by AI with the answer
    reasons: List[str] = []


class AskResponse(BaseModel):
    # general: an explanation from general knowledge, not from the site's data
    status: Literal["answered", "partial", "no_data", "general", "declined"]
    answer: List[str]
    charts: List[AskChart] = []
    tables: List[AskTable] = []
    references: List[AskReference] = []
    follow_ups: List[str] = []
    sources: List[AskSource] = []
    cached: bool = False
    # Its conversation's link, /ask/<share_id>; none if it couldn't be saved, or it follows questions sent as history
    share_id: Optional[str] = None


class AskConversationTurn(BaseModel):
    """A saved turn of a shared conversation: the question, how and where it was asked, when, and its answer"""
    share_id: str
    question: str
    deep: bool
    place: Optional[AskPlace] = None
    # The day it was answered (YYYY-MM-DD); the answer is as it was then
    asked_on: str
    answer: AskResponse


class AskConversation(BaseModel):
    """A shared conversation: the linked turn and those it followed, oldest first"""
    turns: List[AskConversationTurn]
