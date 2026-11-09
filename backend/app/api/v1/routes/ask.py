import asyncio
import json
import logging
from typing import List

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from sqlmodel import Session
from starlette.concurrency import run_in_threadpool

from app.core.config import settings
from app.core.db import engine
from app.schema.ask_schema import AskRequest, AskResponse
from app.service.internal.ask.ask_service import AskFailed, AskLimitReached, AskUnavailable, answer_afresh, prepare_question

logger = logging.getLogger(__name__)

router = APIRouter(tags=["Ask"])

# Heroku ends a request that sends nothing back for 30 seconds, and some answers take longer, so a
# new answer is streamed: a space every few seconds while Claude works (JSON may start with spaces),
# then the answer. A failure after that point can't change the status, so it comes back as 200 with
# only a "detail", which the site treats as an error.
KEEP_ALIVE_SECONDS = 5
FAILED = "We couldn't answer that question right now. Please try again."


async def stream_answer(question: str, earlier: List[dict], deep: bool):
    def answer() -> dict:
        with Session(engine) as session:
            return answer_afresh(session, question, earlier, deep)

    task = asyncio.ensure_future(run_in_threadpool(answer))
    while True:
        done, _ = await asyncio.wait({task}, timeout=KEEP_ALIVE_SECONDS)
        if done:
            break
        yield " "
    try:
        yield AskResponse(**task.result()).model_dump_json()
    except AskFailed as error:
        logger.warning("Ask failed: %s", error)
        yield json.dumps({"detail": FAILED})
    except Exception:
        logger.exception("Ask failed")
        yield json.dumps({"detail": FAILED})


@router.post(
    "",
    response_model=AskResponse,
    summary="Answer a question about New Hampshire public schools",
    description=(
        "Answers a visitor's question in plain English from the site's data, with charts and tables "
        "built from the database and links to the site's pages. Limited per day across the site. "
        "A new answer can start with spaces, sent while it's being written; if it then fails, the "
        "body has only a \"detail\" message."
    ),
)
def ask(request: AskRequest):
    question = request.question.strip()
    if not question:
        raise HTTPException(status_code=400, detail="Type a question to ask.")
    if len(question) > settings.ASK_MAX_QUESTION_LENGTH:
        raise HTTPException(status_code=400, detail=f"Questions can be up to {settings.ASK_MAX_QUESTION_LENGTH} characters.")
    try:
        earlier, saved = prepare_question(question, [turn.model_dump() for turn in request.history], request.deep)
    except AskUnavailable:
        raise HTTPException(status_code=503, detail="Asking questions isn't available right now.")
    except AskLimitReached:
        raise HTTPException(status_code=429, detail="We've answered as many questions as we can today. Please try again tomorrow.")
    if saved:
        return saved
    return StreamingResponse(stream_answer(question, earlier, request.deep), media_type="application/json")
