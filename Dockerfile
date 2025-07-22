FROM python:3.12-slim@sha256:d96f9e885481d78f4337bfa64a8522df060a17f1d68782ad7bc0712b3d33a3ae
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
