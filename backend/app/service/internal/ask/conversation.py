"""
Ask conversations, saved to share by link (the ask_turn table). Each answered question is saved with
the turn it followed, so the address /ask/<share_id> shows the conversation to anyone with the link.

The server saves its own answers, never one a visitor sends, and a follow-up's earlier questions come
from the saved turns it follows, so no one can plant an answer at a link. The same question and answer
after the same turn reuse one row, so saved answers asked again add nothing. Turns are kept for a year,
like the question log (see question_log). A failure to save is logged and never stops a question being
answered: the answer just has no link.
"""
import hashlib
import json
import logging
import secrets
import string
from datetime import timedelta
from typing import List, Optional

from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, delete, select

from app.core.db import engine
from app.model.ask import AskTurn
from app.service.internal.ask.question_log import RETENTION_DAYS, _utc_now

logger = logging.getLogger(__name__)

# 62^10 links: too many to guess one
SHARE_ID_LENGTH = 10
SHARE_ID_ALPHABET = string.ascii_letters + string.digits
# A shared conversation shows as many turns as the Ask page keeps (askSlice MAX_TURNS)
MAX_SHARED_TURNS = 10


def new_share_id() -> str:
    return "".join(secrets.choice(SHARE_ID_ALPHABET) for _ in range(SHARE_ID_LENGTH))


def _find(session: Session, share_id: Optional[str]) -> Optional[AskTurn]:
    if not share_id:
        return None
    return session.exec(select(AskTurn).where(AskTurn.share_id == share_id)).first()


def _chain(session: Session, turn: AskTurn) -> List[AskTurn]:
    """The turn and those it followed, oldest first, at most MAX_SHARED_TURNS"""
    turns = [turn]
    while turns[-1].parent_id is not None and len(turns) < MAX_SHARED_TURNS:
        parent = session.get(AskTurn, turns[-1].parent_id)
        if parent is None:
            break
        turns.append(parent)
    return list(reversed(turns))


def _same_place(turn: AskTurn, place: Optional[dict]) -> bool:
    return (turn.place_kind, turn.place_id) == ((place["kind"], place["id"]) if place else (None, None))


def earlier_turns(share_id: str, place: Optional[dict]) -> Optional[List[dict]]:
    """
    The saved conversation a follow-up continues, as the earlier questions and answers it may refer to
    (oldest first, declined ones left out, as the site leaves them out), or None if there's no such
    turn on that page.
    """
    with Session(engine) as session:
        turn = _find(session, share_id)
        if turn is None or not _same_place(turn, place):
            return None
        return [{"question": earlier.question, "answer": earlier.answer.get("answer", [])}
                for earlier in _chain(session, turn) if earlier.answer.get("status") != "declined"]


def save_turn(question: str, answer: dict, deep: bool, place: Optional[dict], parent_share_id: Optional[str]) -> Optional[str]:
    """Saves an answered question after the turn it followed; its share_id, or None if it couldn't be saved"""
    try:
        with Session(engine) as session:
            # Turns older than the retention period go as new ones arrive
            session.exec(delete(AskTurn).where(AskTurn.date_created < _utc_now() - timedelta(days=RETENTION_DAYS)))
            session.commit()
            parent = _find(session, parent_share_id)
            shown = {key: value for key, value in answer.items() if key not in ("cached", "share_id")}
            fingerprint = hashlib.sha256(json.dumps(
                [parent.id if parent else None, deep, place and place["kind"], place and place["id"], question, shown],
                sort_keys=True, default=str,
            ).encode()).hexdigest()
            for _ in range(3):
                existing = session.exec(select(AskTurn).where(AskTurn.fingerprint == fingerprint)).first()
                if existing:
                    return existing.share_id
                turn = AskTurn(share_id=new_share_id(), parent_id=parent.id if parent else None, question=question, answer=shown,
                               deep=deep, place_kind=place and place["kind"], place_id=place and place["id"], fingerprint=fingerprint)
                session.add(turn)
                try:
                    session.commit()
                    return turn.share_id
                except IntegrityError:
                    # Saved at the same moment by another request, or (rarely) a share_id already taken
                    session.rollback()
            return None
    except Exception:
        logger.warning("Couldn't save an Ask turn", exc_info=True)
        return None


def shared_conversation(share_id: str) -> Optional[dict]:
    """The conversation a link shows: the turn and those it followed, oldest first, or None if there's no such turn"""
    with Session(engine) as session:
        turn = _find(session, share_id)
        if turn is None:
            return None
        return {"turns": [{
            "share_id": item.share_id,
            "question": item.question,
            "deep": item.deep,
            "place": {"kind": item.place_kind, "id": item.place_id} if item.place_kind else None,
            "asked_on": item.date_created.date().isoformat(),
            "answer": {**item.answer, "share_id": item.share_id},
        } for item in _chain(session, turn)]}
