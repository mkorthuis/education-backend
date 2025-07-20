FROM python:3.13

WORKDIR /app/

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY ./requirements.txt /app/
COPY ./scripts /app/scripts
COPY ./alembic.ini /app/
COPY ./app /app/app
COPY ./certs /app/certs

ENV UV_COMPILE_BYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH=/app

# Install Redis
RUN apt-get update && apt-get install -y redis-server && rm -rf /var/lib/apt/lists/*

RUN uv pip install -r requirements.txt --system
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload", "--ssl-keyfile=./certs/key.pem", "--ssl-certfile=./certs/cert.pem"]

RUN pip install debugpy

# Create startup script
RUN echo '#!/bin/bash\nredis-server --daemonize yes\npython -Xfrozen_modules=off -m debugpy --listen 0.0.0.0:5678 -m uvicorn app.main:app --host 0.0.0.0 --reload --ssl-keyfile=./certs/key.pem --ssl-certfile=./certs/cert.pem' > /app/start.sh && chmod +x /app/start.sh

CMD ["/app/start.sh"]
