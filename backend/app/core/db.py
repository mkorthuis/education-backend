from sqlmodel import create_engine
from sqlalchemy.pool import QueuePool

from app.core.config import settings

# Pool per worker: DB_POOL_SIZE + DB_MAX_OVERFLOW connections (default 5 + 3). With the
# 2 uvicorn workers in scripts/start-heroku.sh that is at most 16 of the plan's 20 connections.
engine = create_engine(
    str(settings.SQLALCHEMY_DATABASE_URI),
    poolclass=QueuePool,
    pool_size=settings.DB_POOL_SIZE,
    max_overflow=settings.DB_MAX_OVERFLOW,
    pool_timeout=30,
    pool_pre_ping=True,  # Verify connections before using them
    pool_recycle=1800,   # Recycle connections after 30 minutes
)