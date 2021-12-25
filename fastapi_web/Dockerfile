FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-alpine3.14

COPY  ./app /app
WORKDIR /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt
