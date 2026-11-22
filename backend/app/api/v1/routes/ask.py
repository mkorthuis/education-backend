import asyncio
import json
import logging
from typing import List, Optional

from fastapi import APIRouter, HTTPException, Path
from fastapi.responses import StreamingResponse
from sqlmodel import Session
from starlette.concurrency import run_in_threadpool

from app.core.config import settings
from app.core.db import engine
from app.schema.ask_schema import AskConversation, AskRequest, AskResponse
from app.service.internal.ask.ask_service import MAX_EARLIER, AskFailed, AskLimitReached, AskUnavailable, answer_afresh, prepare_question
from app.service.internal.ask.conversation import earlier_turns, save_turn, shared_conversation
from app.service.internal.ask.data_tools import DataToolError, page_place
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


async def stream_answer(question: str, earlier: List[dict], deep: bool, show_text: bool, question_id: Optional[int] = None,
                        place: Optional[dict] = None, shareable: bool = True, parent: Optional[str] = None):
    # The paragraphs written so far, set by the thread answering
    written: List[List[str]] = [[]]

    def write(paragraphs: List[str]) -> None:
        written[0] = paragraphs

    def answer() -> dict:
        with Session(engine) as session:
            return answer_afresh(session, question, earlier, deep, write if show_text else None, place)

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
        # Saved so its conversation can be shared by link (see conversation)
        share_id = await run_in_threadpool(save_turn, question, result, deep, place, parent) if shareable else None
        response = AskResponse(**{**result, "share_id": share_id}).model_dump_json()
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
        "they're written, each update a line of JSON with \"partial\", and the answer is the last line. "
        "With \"place\", the district or school page it was asked from, a question that names no place is about that one. "
        "Each answer is saved with a \"share_id\" for its conversation's link; with \"parent\", the share_id of the "
        "answer it follows, a follow-up continues that saved conversation."
    ),
)
def ask(request: AskRequest):
    question = request.question.strip()
    if not question:
        raise HTTPException(status_code=400, detail="Type a question to ask.")
    if len(question) > settings.ASK_MAX_QUESTION_LENGTH:
        raise HTTPException(status_code=400, detail=f"Questions can be up to {settings.ASK_MAX_QUESTION_LENGTH} characters.")
    # The place's name and details come from the database, never from the request
    place = None
    if request.place:
        with Session(engine) as session:
            try:
                place = page_place(session, request.place.kind, request.place.id)
            except DataToolError as error:
                raise HTTPException(status_code=400, detail=str(error))
    # A follow-up on a saved conversation continues it from the saved turns, never from what the visitor
    # sends; an unknown parent starts afresh. Questions sent as history (without a parent) are used, but
    # the answer then has no link, since the questions it follows aren't saved.
    history = [turn.model_dump() for turn in request.history]
    parent = None
    if request.parent:
        history = earlier_turns(request.parent, place)
        parent = request.parent if history is not None else None
        history = history or []
    shareable = bool(request.parent) or not request.history
    # Every question goes in the log (question_log) with its outcome: its text, never who asked
    question_id = record_question(question, [turn["question"] for turn in history][-MAX_EARLIER:], request.deep, place)
    try:
        earlier, saved = prepare_question(question, history, request.deep, place)
    except AskUnavailable:
        record_outcome(question_id, "unavailable")
        raise HTTPException(status_code=503, detail="Asking questions isn't available right now.")
    except AskLimitReached:
        record_outcome(question_id, "limit")
        raise HTTPException(status_code=429, detail="We've answered as many questions as we can today. Please try again tomorrow.")
    if saved:
        record_outcome(question_id, saved.get("status", "answered"), cached=True)
        return {**saved, "share_id": save_turn(question, saved, request.deep, place, parent) if shareable else None}
    return StreamingResponse(
        stream_answer(question, earlier, request.deep, request.stream, question_id, place, shareable, parent),
        media_type="application/x-ndjson" if request.stream else "application/json",
    )


@router.get(
    "/conversation/{share_id}",
    response_model=AskConversation,
    summary="A shared Ask conversation",
    description="The conversation a link to Ask a Question shows: the linked answer and the questions it followed, oldest "
                "first, as they were answered. Kept for a year.",
)
def get_conversation(share_id: str = Path(..., pattern=r"^[A-Za-z0-9]{1,16}$")):
    found = shared_conversation(share_id)
    if found is None:
        raise HTTPException(status_code=404, detail="That conversation wasn't found. Links to answers last a year.")
    return found
