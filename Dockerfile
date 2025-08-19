FROM python:3.12-slim

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY pyproject.toml uv.lock ./
COPY app ./app

RUN uv sync --frozen

CMD ["uv", "run", "app/worker.py"]
