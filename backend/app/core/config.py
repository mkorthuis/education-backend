from typing import Annotated, Any, Optional

from pydantic import (
    AnyUrl,
    BeforeValidator,
    computed_field,
    PostgresDsn,
)
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict

def parse_cors(v: Any) -> list[str] | str:
    if isinstance(v, str) and not v.startswith("["):
        return [i.strip() for i in v.split(",")]
    elif isinstance(v, list | str):
        return v
    raise ValueError(v)

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        # Use top level .env file (one level above ./backend/)
        env_file="../.env",
        env_ignore_empty=True,
        extra="ignore",
    )
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str
    FRONTEND_HOST: str = "https://localhost:5174"

    BACKEND_CORS_ORIGINS: Annotated[
        list[AnyUrl] | str, BeforeValidator(parse_cors)
    ] = []
    @computed_field  # type: ignore[prop-decorator]
    @property
    def all_cors_origins(self) -> list[str]:
        return [str(origin).rstrip("/") for origin in self.BACKEND_CORS_ORIGINS] + [
            self.FRONTEND_HOST
        ]
    
    POSTGRES_SERVER: str
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str = ""
    POSTGRES_DB: str = ""

    @computed_field  # type: ignore[prop-decorator]
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme="postgresql+psycopg",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )

    # Database connection pool, per uvicorn worker. Requests run in a threadpool, so several
    # can query at once; keep workers x (pool size + overflow) below the plan's connection
    # limit (Heroku essential-1: 20) with room for migrations and psql sessions.
    DB_POOL_SIZE: int = 5
    DB_MAX_OVERFLOW: int = 3

    # Redis Cache Configuration
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    REDIS_PASSWORD: str = ""
    REDIS_SSL: bool = False
    REDIS_SSL_CERT_REQS: str = "required"
    REDIS_SSL_CA_CERTS: str = ""
    REDIS_SSL_CERTFILE: str = ""
    REDIS_SSL_KEYFILE: str = ""
    REDIS_SSL_CHECK_HOSTNAME: bool = True
    
    # Cache Configuration
    CACHE_ENABLED: bool = True
    CACHE_DEFAULT_TTL: int = 3600  # 1 hour default TTL
    CACHE_KEY_PREFIX: str = "education_api:"

    # Ask NH Education Facts: visitors' questions, answered by Claude from the site's data. With no
    # API key the endpoint says the feature isn't available.
    ANTHROPIC_API_KEY: str = ""
    ASK_MODEL: str = "claude-haiku-5-5"
    ASK_EFFORT: str = "high"
    # Questions answered per day across the whole site (cached repeats don't count); 0 turns asking off
    ASK_DAILY_LIMIT: int = 500
    ASK_MAX_QUESTION_LENGTH: int = 500
    # How long an answer is reused for the same question; data reloads clear it sooner
    ASK_CACHE_TTL: int = 86400

    # Gemini API Configuration
    GEMINI_API_KEY: str = ""
    GEMINI_MODEL: str = "gemini-2.0-flash"
    GEMINI_TEMPERATURE: float = 0.7
    GEMINI_MAX_TOKENS: Optional[int] = None
    GEMINI_TOP_P: Optional[float] = 0.95

settings = Settings() 
