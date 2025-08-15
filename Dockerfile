FROM python:3.12-slim@sha256:d67a7b66b989ad6b6d6b10d428dcc5e0bfc3e5f88906e67d490c4d3daac57047
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
