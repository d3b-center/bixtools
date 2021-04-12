FROM ubuntu:18.04
LABEL maintainer="Daniel Miller <dmiller15@chop.edu>"

ENV PYSAM_VERSION 0.16.0.1

RUN apt update && \
    apt upgrade -y && \
    apt install -y \
    wget \
    python3-dev \
    python3-pip && \
    python3 -m pip install 'pysam>=${PYSAM_VERSION}' && \
    wget https://raw.githubusercontent.com/kids-first/kf-somatic-workflow/9868648597ff4d878708689080c4ca0b0b4615c0/scripts/hotspot.py && \
    chmod +x hotspot.py && \
    apt remove -y wget

ADD Dockerfile .
