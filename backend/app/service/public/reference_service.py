from datetime import date, timedelta
from typing import List, Optional

from fastapi import HTTPException
from sqlmodel import Session, select

from app.model.reference import ReferenceFact, ReferenceTopic
from app.service.internal.ask.reference_tools import site


def _topic(topic: ReferenceTopic, current: int) -> dict:
    return {"id": topic.id, "slug": topic.slug, "title": topic.title, "kind": topic.kind, "question_type": topic.question_type,
            "description": topic.description, "summary": topic.summary, "current_facts": current}


def _fact(fact: ReferenceFact) -> dict:
    return {"id": fact.id, "position": fact.position, "statement": fact.statement, "citation": fact.citation,
            "source_url": fact.source_url, "site": site(fact.source_url), "as_of": fact.as_of, "as_of_text": fact.as_of_text,
            "review_by": fact.review_by, "district_id": fact.district_id_fk, "town_id": fact.town_id_fk}


class ReferenceService:
    def get_topics(self, session: Session, kind: Optional[str] = None) -> List[dict]:
        statement = select(ReferenceTopic).order_by(ReferenceTopic.display_order)
        if kind is not None:
            statement = statement.where(ReferenceTopic.kind == kind)
        topics = session.exec(statement).all()
        today = date.today()
        current = {}
        for fact in session.exec(select(ReferenceFact).where(ReferenceFact.review_by >= today)).all():
            current[fact.reference_topic_id_fk] = current.get(fact.reference_topic_id_fk, 0) + 1
        return [_topic(t, current.get(t.id, 0)) for t in topics]

    def get_topic(self, session: Session, slug: str, district_id: Optional[int] = None) -> dict:
        topic = session.exec(select(ReferenceTopic).where(ReferenceTopic.slug == slug)).first()
        if topic is None:
            raise HTTPException(status_code=404, detail=f"No reference topic {slug}")
        statement = (select(ReferenceFact)
                     .where(ReferenceFact.reference_topic_id_fk == topic.id, ReferenceFact.review_by >= date.today())
                     .order_by(ReferenceFact.position))
        if district_id is not None:
            statement = statement.where((ReferenceFact.district_id_fk == district_id) | (ReferenceFact.district_id_fk.is_(None)))
        facts = session.exec(statement).all()
        return {**_topic(topic, len(facts)), "facts": [_fact(f) for f in facts]}

    def get_review(self, session: Session, within_days: int = 60) -> List[dict]:
        """Facts past their review date or due within the days given, soonest first."""
        due = date.today() + timedelta(days=within_days)
        rows = session.exec(
            select(ReferenceFact, ReferenceTopic)
            .join(ReferenceTopic, ReferenceTopic.id == ReferenceFact.reference_topic_id_fk)
            .where(ReferenceFact.review_by <= due)
            .order_by(ReferenceFact.review_by, ReferenceTopic.display_order, ReferenceFact.position)
        ).all()
        today = date.today()
        return [{"topic": topic.slug, "source_file": topic.source_file, "position": fact.position, "statement": fact.statement,
                 "source_url": fact.source_url, "review_by": fact.review_by, "overdue": fact.review_by < today}
                for fact, topic in rows]


reference_service = ReferenceService()
