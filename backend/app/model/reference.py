from datetime import date
from typing import Any, List, Optional

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import JSONB
from sqlmodel import Field

from .base import BaseMixin


# -------------------- Reference library --------------------

class ReferenceTopic(BaseMixin, table=True):
    """A subject in the reference library, such as "What schools must do about bullying". A shared
    topic, such as district-transportation, gathers facts from many files, each fact with its place."""
    __tablename__ = "reference_topic"

    slug: str = Field(max_length=100)
    title: str = Field(max_length=255)
    kind: str = Field(max_length=20)  # rule, term, how_it_works, research, programs or local
    question_type: str = Field(max_length=30)
    description: str  # what the topic covers, which the Ask chooses topics by
    summary: Optional[str] = None  # a research brief's summary
    source_file: str = Field(max_length=200)  # the first file the topic appears in
    display_order: int


class ReferenceFact(BaseMixin, table=True):
    """One cited statement in the reference library, about one place at most: a district, a town, an
    SAU or a school outside New Hampshire. (The search column, a tsvector the database computes from
    the statement, isn't mapped here.)"""
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
    sau_id_fk: Optional[int] = Field(default=None, foreign_key="sau.id")
    outside_school_id_fk: Optional[int] = Field(default=None, foreign_key="outside_school.id")
    fact_key: str = Field(max_length=300)  # file#topic#position: the same fact keeps it across loads
    source_file: str = Field(max_length=200)
    section_title: str = Field(max_length=255)  # the file's own heading for the topic, e.g. "Albany's School Bus ..."


class ReferenceTable(BaseMixin, table=True):
    """A number table from the reference library, such as bus ride times or tuition by year: its
    columns and rows as written, and the topic and place it belongs to, if the file names them."""
    __tablename__ = "reference_table"

    slug: str = Field(max_length=100)
    title: str = Field(max_length=255)
    source_file: str = Field(max_length=200)
    unit: Optional[str] = None
    period: Optional[str] = None
    source: Optional[str] = None  # as written: often a name and a link
    source_url: Optional[str] = Field(default=None, max_length=1000)  # the first link in it
    as_of: Optional[date] = None
    as_of_text: Optional[str] = None
    note: Optional[str] = None
    reference_topic_id_fk: Optional[int] = Field(default=None, foreign_key="reference_topic.id")
    district_id_fk: Optional[int] = Field(default=None, foreign_key="district.id")
    town_id_fk: Optional[int] = Field(default=None, foreign_key="town.id")
    sau_id_fk: Optional[int] = Field(default=None, foreign_key="sau.id")
    outside_school_id_fk: Optional[int] = Field(default=None, foreign_key="outside_school.id")
    columns: List[str] = Field(sa_column=Column(JSONB, nullable=False))
    rows: List[List[Any]] = Field(sa_column=Column(JSONB, nullable=False))
    display_order: int


# -------------------- Who serves a district's students --------------------

class OutsideSchool(BaseMixin, table=True):
    """A school or school district outside New Hampshire that New Hampshire students attend on public
    tuition, such as Fryeburg Academy in Maine"""
    __tablename__ = "outside_school"

    name: str = Field(max_length=255)
    state: str = Field(max_length=2)
    kind: str = Field(max_length=30)  # public_district, public_school, private_academy or private_school
    url: Optional[str] = Field(default=None, max_length=500)


class DistrictService(BaseMixin, table=True):
    """Where a district's students go for grades it doesn't run itself: another New Hampshire district
    or a school outside the state, the grades, and the arrangement (a tuition contract, an AREA
    agreement, a cooperative, families' choice with the district paying, tuition paid without a
    written contract, an interstate district such as Dresden, or a joint maintenance agreement such as
    Prospect Mountain's)"""
    __tablename__ = "district_service"

    district_id_fk: int = Field(foreign_key="district.id")
    receiving_district_id_fk: Optional[int] = Field(default=None, foreign_key="district.id")
    outside_school_id_fk: Optional[int] = Field(default=None, foreign_key="outside_school.id")
    grade_low: int  # 0 is kindergarten
    grade_high: int
    arrangement: str = Field(max_length=30)  # tuition_contract, area_agreement, cooperative, choice, no_contract,
    # interstate_district or joint_maintenance
    starts: Optional[date] = None
    ends: Optional[date] = None
    source_url: str = Field(max_length=1000)
    note: Optional[str] = None
