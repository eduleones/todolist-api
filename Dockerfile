FROM python:3.10.3-slim

ARG INDEX_URL
ARG POETRY_VERSION=1.1.8
ARG environment=cluster

WORKDIR /src

RUN apt-get update \
 && apt-get install -y --no-install-recommends  \
 git libmagic-dev build-essential curl \
 && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=. \
    POETRY_VERSION=${POETRY_VERSION} \
    ENVIRONMENT=${environment} \
    PIP_EXTRA_INDEX_URL=${INDEX_URL}


RUN pip install -U pip setuptools "poetry==$POETRY_VERSION"

COPY *.toml *.lock ./

RUN poetry config virtualenvs.create false

RUN poetry export --without-hashes -f requirements.txt --output requirements.txt && \
         pip install -r requirements.txt; fi


COPY . /src

EXPOSE 8000

ENV PIP_EXTRA_INDEX_URL=""

CMD $DOCKER_CMD