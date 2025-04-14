from sqlmodel import create_engine
from sqlalchemy.pool import QueuePool

from app.core.config import settings

# Create engine with connection pooling configuration
engine = create_engine(
    str(settings.SQLALCHEMY_DATABASE_URI),
    # Set pool size to be safely under the Heroku's connection limit
    # Min connections to keep open
    pool_size=5,
    # Max overflow connections allowed
    max_overflow=10,
    # Use QueuePool - the default pool but we're explicit here
    poolclass=QueuePool,
    # Time (seconds) connections are recycled
    pool_recycle=3600,
    # Timeout (seconds) to wait for a connection from pool
    pool_timeout=30,
)