FROM ubuntu:20.04

LABEL maintainer="Daniel Miller (millerd15@chop.edu)"

RUN apt update && \
    apt install -y python-is-python3 python3-pip

ENV SNIFFLES_VERSION 2.0.7
RUN python -m pip install --upgrade pip && python -m pip install sniffles==${SNIFFLES_VERSION}

COPY Dockerfile .
