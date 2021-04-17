FROM python:3.8-alpine
RUN apk add --no-cache build-base
WORKDIR /app
COPY api.py .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
CMD uvicorn api:app --host 0.0.0.0 --port 8000
