from typing import List, Optional

from fastapi import APIRouter, Query

from app.api.v1.deps import SessionDep
from app.core.cache import cache_response
from app.schema.reference_schema import ReferenceReviewGet, ReferenceTopicDetailGet, ReferenceTopicGet
from app.service.public.reference_service import reference_service

router = APIRouter()


@router.get("/topic",
    response_model=List[ReferenceTopicGet],
    summary="Get the reference library's topics",
    description="Topics of cited facts about New Hampshire schools: rules and rights (rule), terms (term), how schools are run and paid for (how_it_works), research (research), programs and help (programs), and district practices (local)")
@cache_response("reference_topics")
def get_topics(
    session: SessionDep,
    kind: Optional[str] = Query(default=None, pattern="^(rule|term|how_it_works|research|programs|local)$", description="Filter by kind"),
):
    return reference_service.get_topics(session=session, kind=kind)


@router.get("/topic/{slug}",
    response_model=ReferenceTopicDetailGet,
    summary="Get a reference topic and its facts",
    description="A topic's facts that are within their review date, each with its citation, source link and the date it was checked. For district practices, district_id narrows the facts to one district.")
@cache_response("reference_topic")
def get_topic(
    slug: str,
    session: SessionDep,
    district_id: Optional[int] = Query(default=None, description="Only facts about this district, and those about no district"),
):
    return reference_service.get_topic(session=session, slug=slug, district_id=district_id)


@router.get("/review",
    response_model=List[ReferenceReviewGet],
    summary="Get facts due for review",
    description="Facts past their review date, which the Ask no longer uses, and those due within the days given, soonest first")
def get_review(
    session: SessionDep,
    within_days: int = Query(default=60, ge=0, le=730, description="Include facts due within this many days"),
):
    return reference_service.get_review(session=session, within_days=within_days)
