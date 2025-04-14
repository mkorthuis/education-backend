from fastapi import APIRouter, Depends
from app.api.v1.deps import SessionDep
from app.core.db import engine

router = APIRouter()

@router.get("/health-check",
    summary="Health check endpoint",
    description="Simple endpoint to verify API is running",
    response_description="Status indicating API health")
async def health_check():
    return {"status": "ok"}

# Add connection pool stats function to get pool information
@router.get("/database/pool-stats", tags=["utility"])
def get_pool_stats():
    """Get database connection pool statistics."""
    return {
        "pool_size": engine.pool.size(),  # Current size of the pool
        "checkedin": engine.pool.checkedin(),  # Number of connections checked in
        "checkedout": engine.pool.checkedout(),  # Number of connections checked out
        "overflow": engine.pool.overflow(),  # Number of overflow connections
        "configured_max_overflow": engine.pool._max_overflow,  # Max configured overflow
        "configured_pool_size": engine.pool._pool_size,  # Configured pool size
    }