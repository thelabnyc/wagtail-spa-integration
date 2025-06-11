FROM python:3.12-slim@sha256:e55523f127124e5edc03ba201e3dbbc85172a2ec40d8651ac752364b23dfd733
ENV PYTHONUNBUFFERED=1 \
  PORT=8080 \
  POETRY_VIRTUALENVS_CREATE=false \
  PIP_DISABLE_PIP_VERSION_CHECK=on
ARG IGNORE_DEV_DEPS

RUN mkdir /code
WORKDIR /code

RUN pip install poetry
COPY poetry.lock pyproject.toml /code/
RUN poetry install --no-interaction --no-ansi

ADD . /code/

RUN mkdir /tox
ENV TOX_WORK_DIR='/tox'
