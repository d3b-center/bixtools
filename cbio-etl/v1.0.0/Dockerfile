FROM --platform=linux/amd64 ubuntu:22.04

LABEL maintainer="Jessica Wong <wongj4@chop.edu>"
LABEL description="cbio-etl"

RUN apt-get update && apt-get install -y \
    apt-utils \
    curl \
    git \
    python3 \
    python3-pip \
    python3-dev \
    pkg-config \
    libmysqlclient-dev \
    build-essential \
    perl \
    libtry-tiny-perl \
    bedtools \
    && rm -rf /var/lib/apt/lists/*

ENV CBIO_ETL_VERSION 1.0.0

WORKDIR /

RUN git clone https://github.com/kids-first/kf-cbioportal-etl.git /kf-cbioportal-etl \
    && pip install /kf-cbioportal-etl/
    
COPY Dockerfile .