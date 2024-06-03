FROM python:3.10-slim

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

WORKDIR /app

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.8.2

RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock README.md ./

COPY . /app

RUN poetry config virtualenvs.in-project true && \
    poetry install

ENTRYPOINT ["poetry", "run", "hatchet"]