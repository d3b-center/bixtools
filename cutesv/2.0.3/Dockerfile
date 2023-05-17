FROM ubuntu:20.04

LABEL maintainer="Daniel Miller (millerd15@chop.edu)"

RUN apt update && \
    apt install -y python-is-python3 python3-pip libbz2-dev

ENV CUTESV_VERSION 2.0.3
RUN python -m pip install --upgrade pip && python -m pip install cuteSV==${CUTESV_VERSION}

COPY Dockerfile .
