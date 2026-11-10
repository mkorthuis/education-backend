import asyncio
import json
import logging
from typing import List, Optional

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from sqlmodel import Session
from starlette.concurrency import run_in_threadpool

from app.core.config import settings
from app.core.db import engine
from app.schema.ask_schema import AskRequest, AskResponse
from app.service.internal.ask.ask_service import MAX_EARLIER, AskFailed, AskLimitReached, AskUnavailable, answer_afresh, prepare_question
from app.service.internal.ask.question_log import record_outcome, record_question

logger = logging.getLogger(__name__)

router = APIRouter(tags=["Ask"])

# Heroku ends a request that sends nothing back for 30 seconds, and some answers take longer, so a
# new answer is streamed: a space every few seconds while Claude works (JSON may start with spaces),
# then the answer. A failure after that point can't change the status, so it comes back as 200 with
# only a "detail", which the site treats as an error. Asked to show the answer as it's written, it
# also sends a line {"partial": [paragraphs so far]} as they grow, at most every TEXT_SECONDS.
KEEP_ALIVE_SECONDS = 5
TEXT_SECONDS = 0.1
FAILED = "We couldn't answer that question right now. Please try again."


async def stream_answer(question: str, earlier: List[dict], deep: bool, show_text: bool, question_id: Optional[int] = None):
    # The paragraphs written so far, set by the thread answering
    written: List[List[str]] = [[]]

    def write(paragraphs: List[str]) -> None:
        written[0] = paragraphs

    def answer() -> dict:
        with Session(engine) as session:
            return answer_afresh(session, question, earlier, deep, write if show_text else None)

    task = asyncio.ensure_future(run_in_threadpool(answer))
    clock = asyncio.get_running_loop().time
    started = clock()
    shown, last_sent = written[0], clock()
    while True:
        done, _ = await asyncio.wait({task}, timeout=TEXT_SECONDS)
        if done:
            break
        if written[0] is not shown:
            shown = written[0]
            yield json.dumps({"partial": shown}) + "\n"
            last_sent = clock()
        elif clock() - last_sent >= KEEP_ALIVE_SECONDS:
            yield " "
            last_sent = clock()
    try:
        result = task.result()
        response = AskResponse(**result).model_dump_json()
    except Exception as error:
        if isinstance(error, AskFailed):
            logger.warning("Ask failed: %s", error)
        else:
            logger.exception("Ask failed")
        await run_in_threadpool(record_outcome, question_id, "failed")
        yield json.dumps({"detail": FAILED})
        return
    await run_in_threadpool(record_outcome, question_id, result.get("status", "answered"), False, clock() - started)
    yield response


@router.post(
    "",
    response_model=AskResponse,
    summary="Answer a question about New Hampshire public schools",
    description=(
        "Answers a visitor's question in plain English from the site's data, with charts and tables "
        "built from the database and links to the site's pages. Limited per day across the site. "
        "A new answer can start with spaces, sent while it's being written; if it then fails, the "
        "body has only a \"detail\" message. With \"stream\", the answer's paragraphs come first as "
        "they're written, each update a line of JSON with \"partial\", and the answer is the last line."
    ),
)
def ask(request: AskRequest):
    question = request.question.strip()
    if not question:
        raise HTTPException(status_code=400, detail="Type a question to ask.")
    if len(question) > settings.ASK_MAX_QUESTION_LENGTH:
        raise HTTPException(status_code=400, detail=f"Questions can be up to {settings.ASK_MAX_QUESTION_LENGTH} characters.")
    # Every question goes in the log (question_log) with its outcome: its text, never who asked
    question_id = record_question(question, [turn.question for turn in request.history][-MAX_EARLIER:], request.deep)
    try:
        earlier, saved = prepare_question(question, [turn.model_dump() for turn in request.history], request.deep)
    except AskUnavailable:
        record_outcome(question_id, "unavailable")
        raise HTTPException(status_code=503, detail="Asking questions isn't available right now.")
    except AskLimitReached:
        record_outcome(question_id, "limit")
        raise HTTPException(status_code=429, detail="We've answered as many questions as we can today. Please try again tomorrow.")
    if saved:
        record_outcome(question_id, saved.get("status", "answered"), cached=True)
        return saved
    return StreamingResponse(
        stream_answer(question, earlier, request.deep, request.stream, question_id),
        media_type="application/x-ndjson" if request.stream else "application/json",
    )
