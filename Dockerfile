FROM python:3.12-slim@sha256:6a78a0dce3dd2ec7ee40bffc8b47c10592ece101aea2953e2b28dbab3ed724d8
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
