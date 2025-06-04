FROM python:3.12-slim@sha256:ffa7bd40c44292ed4d53b4595cba653583fc097e14308c7f379f5065d52853d3
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
