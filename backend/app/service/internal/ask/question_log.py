"""
The log of questions asked on Ask a Question (the ask_question table): each question's text when it
arrives, then its outcome. Nothing about who asked. A failure to log is logged and never stops a
question being answered.

Export it as CSV, newest first:

    python -m app.service.internal.ask.question_log --days 30 > asks.csv
    heroku run -a education-backend python -m app.service.internal.ask.question_log --days 30 > asks.csv
"""
import argparse
import csv
import logging
import sys
from datetime import datetime, timedelta, timezone
from typing import List, Optional

from sqlmodel import Session, select

from app.core.db import engine
from app.model.ask import AskQuestion

logger = logging.getLogger(__name__)


def _utc_now() -> datetime:
    """Now in UTC, without a time zone, as the tables store times"""
    return datetime.now(timezone.utc).replace(tzinfo=None)


def record_question(question: str, earlier_questions: List[str], deep: bool) -> Optional[int]:
    """Logs a question as it arrives; its id, for record_outcome, or None if it couldn't be logged"""
    try:
        with Session(engine) as session:
            row = AskQuestion(question=question, earlier_questions=earlier_questions, deep=deep)
            session.add(row)
            session.commit()
            return row.id
    except Exception:
        logger.warning("Couldn't log an Ask question", exc_info=True)
        return None


def record_outcome(question_id: Optional[int], status: str, cached: bool = False, seconds: Optional[float] = None) -> None:
    """Logs how a logged question was answered"""
    if question_id is None:
        return
    try:
        with Session(engine) as session:
            row = session.get(AskQuestion, question_id)
            if row is None:
                return
            row.status = status
            row.cached = cached
            row.seconds = None if seconds is None else round(seconds, 1)
            row.date_updated = _utc_now()
            session.add(row)
            session.commit()
    except Exception:
        logger.warning("Couldn't log an Ask question's outcome", exc_info=True)


def export_csv(days: int, out=sys.stdout) -> int:
    """Writes the last `days` days' questions as CSV, newest first; returns how many"""
    since = _utc_now() - timedelta(days=days)
    with Session(engine) as session:
        rows = session.exec(select(AskQuestion).where(AskQuestion.date_created >= since).order_by(AskQuestion.date_created.desc())).all()
    writer = csv.writer(out)
    writer.writerow(["asked_at_utc", "question", "earlier_questions", "status", "cached", "more_time", "seconds"])
    for row in rows:
        writer.writerow([
            row.date_created.isoformat(timespec="seconds"), row.question, " | ".join(row.earlier_questions or []),
            row.status, row.cached, row.deep, row.seconds,
        ])
    return len(rows)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export Ask a Question's question log as CSV")
    parser.add_argument("--days", type=int, default=30, help="how many days back (default 30)")
    # Only the CSV: heroku run sends everything the command prints into the file
    export_csv(parser.parse_args().days)
