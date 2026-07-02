FROM python:3.11-slim AS builder

WORKDIR /code

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip wheel --no-cache-dir --wheel-dir /code/wheels -r requirements.txt

FROM python:3.11-slim AS runtime

RUN useradd -u 8888 -m appuser

WORKDIR /code

COPY --from=builder /code/wheels /code/wheels

RUN pip install --no-cache-dir /code/wheels/* \
    && rm -rf /code/wheels

COPY ./models /code/models
COPY ./app /code/app

RUN chown -R appuser:appuser /code

USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]