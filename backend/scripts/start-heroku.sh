#!/bin/bash
set -e

echo "Starting application..."
echo "Current directory: $(pwd)"
echo "Python path: $PYTHONPATH"
echo "Port: $PORT"

# Migrations run in Heroku's release phase (heroku.yml), once per deploy, before this starts

# Run uvicorn with reduced workers and optimized timeout flags
echo "Starting uvicorn with optimized settings..."
exec uvicorn app.main:app \
    --host 0.0.0.0 \
    --port "$PORT" \
    --workers 2 \
    --timeout-keep-alive 75 \
    --proxy-headers \
    --log-level info