FROM ubuntu:20.04

RUN apt update && apt install -y python-is-python3 python3-pip curl libbz2-dev liblzma-dev libcurl4-openssl-dev libssl-dev

ENV BASENJI_VERSION=0.6

RUN curl -SL https://github.com/calico/basenji/archive/refs/tags/$BASENJI_VERSION.tar.gz | tar -xzC /opt/

RUN python -m pip install --upgrade pip && python -m pip install pyBigWig Cython numpy==1.23

WORKDIR /opt/basenji-$BASENJI_VERSION

RUN python setup.py develop || python setup.py develop

WORKDIR /

COPY Dockerfile .
