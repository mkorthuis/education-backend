from typing import Annotated, List, Literal, Optional, Union

from pydantic import BaseModel, Field


# Sizes far past what the site sends (500-character questions, four short paragraphs an answer,
# ten earlier questions), so an oversized request is refused before it's read further
class AskEarlierTurn(BaseModel):
    """An earlier question on the visitor's Ask page and its answer, so a follow-up can refer to it"""
    question: str = Field(..., max_length=2000)
    answer: List[Annotated[str, Field(max_length=5000)]] = Field(default_factory=list, max_length=10)


class AskRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=5000, description="The visitor's question in plain English")
    history: List[AskEarlierTurn] = Field(
        default_factory=list,
        max_length=20,
        description="The visitor's earlier questions on the page, oldest first, with their answers; the last ten are used to understand a follow-up",
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
