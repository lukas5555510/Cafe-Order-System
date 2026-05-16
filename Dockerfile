FROM python:3.13-slim AS builder

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV UV_PYTHON_DOWNLOADS=never
ENV UV_PYTHON=python3.13

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

COPY src ./src


FROM python:3.13-slim

WORKDIR /app

COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app/src /app/src

ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH="/app/src"
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["/app/.venv/bin/uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
