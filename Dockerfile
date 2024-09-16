FROM python:3.11-slim AS builder

RUN pip install poetry==1.7.1

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN touch README.md
#RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR
RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR


FROM python:3.11-slim AS runtime

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY . ./app

EXPOSE 5000
#ENTRYPOINT ["python", "-u", "app/main.py"]
WORKDIR /app/
ENTRYPOINT ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "main:app"]
