FROM ubuntu:20.04

LABEL maintainer="Daniel Miller (millerd15@email.chop.edu)"

ENV CUTESV_VERSION 1.0.13

RUN apt update && \
    apt install -y python-is-python3 python3-pip && \
    python -m pip install cuteSV==${CUTESV_VERSION}

ADD Dockerfile .
