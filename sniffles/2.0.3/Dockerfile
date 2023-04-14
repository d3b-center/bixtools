FROM ubuntu:20.04

LABEL maintainer="Daniel Miller (millerd15@email.chop.edu)"


RUN apt update && \
    apt install -y python-is-python3 python3-pip libbz2-dev 

ENV SNIFFLES_VERSION 2.0.3

RUN python -m pip install --upgrade pip && \
    python -m pip install sniffles==${SNIFFLES_VERSION}

ADD Dockerfile .
