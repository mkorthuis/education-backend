from collections.abc import Generator
from typing import Annotated
import logging

from fastapi import Depends
from sqlmodel import Session

from app.core.db import engine

logger = logging.getLogger(__name__)

def get_db() -> Generator[Session, None, None]:
    """
    Get a database session with proper connection handling.
    The session automatically closes when the request is complete.
    """
    with Session(engine) as session:
        try:
            yield session
        except Exception as e:
            logger.error(f"Database session error: {str(e)}")
            # Roll back on error
            session.rollback()
            raise
        finally:
            # Make sure session is closed
            session.close()

SessionDep = Annotated[Session, Depends(get_db)]
