from typing import List, Optional

from fastapi import APIRouter, Query

from app.api.v1.deps import SessionDep
from app.core.cache import cache_response
from app.schema.acs_schema import (
    AcsMeasureGet, AcsReleaseGet, AcsTopicGet, AcsVariableGet, DistrictAcsSummaryGet, DistrictAcsTopicGet,
    StateAcsSummaryGet, StateAcsTopicGet, TownAcsSummaryGet, TownAcsTopicGet,
)
from app.service.public.acs_service import acs_service

router = APIRouter()

RELEASE = Query(default=None, description="Only this release, by its last year (2024: 2020-2024); see /acs/release")
COMPARE_TO = Query(
    default=None,
    description="Compare each measure with this earlier release (it can't overlap: 2019 for 2024). Each measure gets "
                "compare: the earlier value, the change and whether it's significant at 90% confidence. With no "
                "release, the latest is compared. Dollar amounts are each release's own dollars.")
CENSUS_TYPE = Query(default=None, pattern="^(elementary|secondary|unified)$",
                    description="Only districts of this Census type. Elementary and unified districts cover the state "
                                "once; secondary (cooperative high school) districts overlap them.")
TIER = Query(default="core", pattern="^(core|all)$", description="core (the default): the values likely to be used; all: every value")
VARIABLES = Query(default=None, description="Only these values, by column name, comma-separated (see /acs/variable); overrides tier")
SUMMARY = (
    "The summary measures (see /acs/measure) for each place and release: rates, shares, medians and counts, each with "
    "its 90% margin of error and a reliability rating by coefficient of variation (high up to 15%, caution up to 30%, "
    "low above). Show low-reliability figures with a warning rather than leaving them out."
)
TOPIC = (
    "A topic's values (see /acs/topic) for each place and release, each with its 90% margin of error, keyed by column "
    "name; /acs/variable describes each. A value an earlier release doesn't have, or that meant something else in it, "
    "is blank there."
)


@router.get("/release", response_model=List[AcsReleaseGet], summary="Get the ACS releases",
            description="The American Community Survey 5-year releases loaded, by their last year, with the dollars "
                        "their amounts are in. Census advises against comparing releases whose years overlap.")
@cache_response("acs_release")
def get_acs_releases(session: SessionDep):
    return acs_service.get_releases(session=session)


@router.get("/topic", response_model=List[AcsTopicGet], summary="Get the ACS topics and their tables",
            description="The topics the /acs/{level}/{topic} endpoints take, with the Census tables in each.")
@cache_response("acs_topic")
def get_acs_topics(session: SessionDep):
    return acs_service.get_topics(session=session)


@router.get("/variable", response_model=List[AcsVariableGet], summary="Get the ACS values",
            description="Every value loaded: its Census line, its column name in the topic endpoints, its label, "
                        "description and unit, and the releases that have it.")
@cache_response("acs_variable")
def get_acs_variables(
    session: SessionDep,
    topic: Optional[str] = Query(default=None, description="Only this topic's values"),
    tier: Optional[str] = Query(default=None, pattern="^(core|extended)$", description="Only core or extended values"),
    table: Optional[str] = Query(default=None, description="Only this Census table's values (B25004)"),
):
    return acs_service.get_variables(session=session, topic=topic, tier=tier, table=table)


@router.get("/measure", response_model=List[AcsMeasureGet], summary="Get the ACS summary measures",
            description="The measures in the summary endpoints, in order, with their labels, descriptions, units and "
                        "how each is worked out from Census's lines.")
@cache_response("acs_measure")
def get_acs_measures(session: SessionDep):
    return acs_service.get_measures(session=session)


@router.get("/town/summary", response_model=List[TownAcsSummaryGet], summary="Get towns' ACS summary",
            description=SUMMARY, response_description="ACS summary by town and release")
@cache_response("acs_town_summary")
def get_town_acs_summary(
    session: SessionDep,
    release: Optional[int] = RELEASE,
    compare_to: Optional[int] = COMPARE_TO,
    town_id: Optional[int] = Query(default=None, description="Filter by town ID"),
    district_id: Optional[int] = Query(default=None, description="Only the towns of this school district"),
):
    return acs_service.get_summary(session, "town", release=release, compare_to=compare_to, place_id=town_id,
                                   district_id=district_id)


@router.get("/district/summary", response_model=List[DistrictAcsSummaryGet], summary="Get school districts' ACS summary",
            description=SUMMARY + " Census's district figures overlap: a town in an elementary and a secondary "
                                  "district counts in both, so don't add districts up.",
            response_description="ACS summary by school district and release")
@cache_response("acs_district_summary")
def get_district_acs_summary(
    session: SessionDep,
    release: Optional[int] = RELEASE,
    compare_to: Optional[int] = COMPARE_TO,
    district_id: Optional[int] = Query(default=None, description="Filter by district ID"),
    census_type: Optional[str] = CENSUS_TYPE,
):
    return acs_service.get_summary(session, "district", release=release, compare_to=compare_to, place_id=district_id,
                                   census_type=census_type)


@router.get("/state/summary", response_model=List[StateAcsSummaryGet], summary="Get New Hampshire's ACS summary",
            description=SUMMARY, response_description="ACS summary by release")
@cache_response("acs_state_summary")
def get_state_acs_summary(
    session: SessionDep,
    release: Optional[int] = RELEASE,
    compare_to: Optional[int] = COMPARE_TO,
):
    return acs_service.get_summary(session, "state", release=release, compare_to=compare_to)


@router.get("/town/{topic}", response_model=List[TownAcsTopicGet], summary="Get towns' ACS values in a topic",
            description=TOPIC, response_description="ACS values by town and release")
@cache_response("acs_town_topic")
def get_town_acs_topic(
    topic: str,
    session: SessionDep,
    release: Optional[int] = RELEASE,
    tier: str = TIER,
    variables: Optional[str] = VARIABLES,
    town_id: Optional[int] = Query(default=None, description="Filter by town ID"),
    district_id: Optional[int] = Query(default=None, description="Only the towns of this school district"),
):
    return acs_service.get_topic(session, "town", topic, release=release, tier=tier, variables=variables,
                                 place_id=town_id, district_id=district_id)


@router.get("/district/{topic}", response_model=List[DistrictAcsTopicGet], summary="Get school districts' ACS values in a topic",
            description=TOPIC + " Census's district figures overlap, so don't add districts up.",
            response_description="ACS values by school district and release")
@cache_response("acs_district_topic")
def get_district_acs_topic(
    topic: str,
    session: SessionDep,
    release: Optional[int] = RELEASE,
    tier: str = TIER,
    variables: Optional[str] = VARIABLES,
    district_id: Optional[int] = Query(default=None, description="Filter by district ID"),
    census_type: Optional[str] = CENSUS_TYPE,
):
    return acs_service.get_topic(session, "district", topic, release=release, tier=tier, variables=variables,
                                 place_id=district_id, census_type=census_type)


@router.get("/state/{topic}", response_model=List[StateAcsTopicGet], summary="Get New Hampshire's ACS values in a topic",
            description=TOPIC, response_description="ACS values by release")
@cache_response("acs_state_topic")
def get_state_acs_topic(
    topic: str,
    session: SessionDep,
    release: Optional[int] = RELEASE,
    tier: str = TIER,
    variables: Optional[str] = VARIABLES,
):
    return acs_service.get_topic(session, "state", topic, release=release, tier=tier, variables=variables)
