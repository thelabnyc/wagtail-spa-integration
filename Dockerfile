FROM python:3.12-slim@sha256:8a990901df5247f8b16c501717e935f2060db1fd824e640b4326a6c65f9ae68c
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
