#!/bin/bash
# Startup script for Render deployment

echo "Starting USSD API..."

# Start the FastAPI application with gunicorn
exec gunicorn app.main:app --bind 0.0.0.0:$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker --timeout 120 