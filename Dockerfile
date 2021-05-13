FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1 \
  PORT=8080 \
  POETRY_VERSION=1.1.6 \
  POETRY_VIRTUALENVS_CREATE=false \
  PIP_DISABLE_PIP_VERSION_CHECK=on
ARG IGNORE_DEV_DEPS

RUN mkdir /code
WORKDIR /code

RUN pip install "poetry==$POETRY_VERSION"
COPY poetry.lock pyproject.toml /code/
RUN poetry install --no-interaction --no-ansi

ADD . /code/

