#!/bin/bash
set -e

echo "Starting application..."
echo "Current directory: $(pwd)"
echo "Python path: $PYTHONPATH"
echo "Port: $PORT"

# Run migrations
echo "Running database migrations..."
python -m alembic upgrade head

# Run uvicorn with correct timeout flags
exec uvicorn app.main:app \
    --host 0.0.0.0 \
    --port "$PORT" \
    --workers 4 \
    --timeout-keep-alive 75 \
    --proxy-headers \
    --log-level info