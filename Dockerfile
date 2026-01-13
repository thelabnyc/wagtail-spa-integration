FROM python:3.14-slim@sha256:1f741aef81d09464251f4c52c83a02f93ece0a636db125d411bd827bf381a763
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
