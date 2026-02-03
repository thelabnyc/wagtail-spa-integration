FROM python:3.14-slim@sha256:1a3c6dbfd2173971abba880c3cc2ec4643690901f6ad6742d0827bae6cefc925
ENV PYTHONUNBUFFERED=1 \
    PORT=8080 \
    PIP_DISABLE_PIP_VERSION_CHECK=on
ARG IGNORE_DEV_DEPS

RUN mkdir /code
WORKDIR /code

COPY uv.lock pyproject.toml /code/
RUN uv sync

ADD . /code/

RUN mkdir /tox
ENV TOX_WORK_DIR='/tox'
