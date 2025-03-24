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

ENV CBIO_ETL_VERSION 2.2.0

WORKDIR /

RUN curl -L https://github.com/kids-first/kf-cbioportal-etl/archive/refs/tags/v${CBIO_ETL_VERSION}.tar.gz | tar xz \
    && pip install /kf-cbioportal-etl-${CBIO_ETL_VERSION}/
    
COPY Dockerfile .
