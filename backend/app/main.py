import logging
import os


# Create logs directory if it doesn't exist
logs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs")
os.makedirs(logs_dir, exist_ok=True)
# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(os.path.join(logs_dir, 'app.log')),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Log application startup
logger.info("Starting application...")

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.api.v1.main import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)


class UnhandledErrorMiddleware:
    """
    Turn unexpected exceptions into a JSON 500 inside the CORS middleware.

    Starlette sends unhandled-exception responses from its outermost layer, outside
    CORSMiddleware, so they had no CORS headers and browsers reported a CORS error instead
    of the 500. Added before CORSMiddleware so it sits inside it.
    """
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        response_started = False

        async def send_tracking_start(message):
            nonlocal response_started
            if message["type"] == "http.response.start":
                response_started = True
            await send(message)

        try:
            await self.app(scope, receive, send_tracking_start)
        except Exception:
            if response_started:
                # Too late to send a different response; let the server handle it
                raise
            logger.exception("Unhandled exception occurred:")
            response = JSONResponse(status_code=500, content={"detail": "Internal server error"})
            await response(scope, receive, send)


app.add_middleware(UnhandledErrorMiddleware)

# Set all CORS enabled origins
if settings.all_cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.all_cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["*"],
    )

# Add custom exception handlers
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    # 4xx responses (unknown routes, missing ids) are normal traffic; only 5xx are errors
    level = logging.ERROR if exc.status_code >= 500 else logging.INFO
    logger.log(level, f"HTTP error occurred: {exc.detail} (status code: {exc.status_code})")
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": str(exc.detail)},
    )

# Last resort for errors outside UnhandledErrorMiddleware (e.g. in other middleware)
@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    logger.exception("Unhandled exception occurred:", exc_info=exc)
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"},
    )

app.include_router(api_router, prefix=settings.API_V1_STR)
