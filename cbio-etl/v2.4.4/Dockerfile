FROM --platform=linux/amd64 ubuntu:22.04

LABEL maintainer="Jessica Wong <wongj4@chop.edu>"
LABEL description="cbio-etl"

RUN apt-get update && apt-get install -y \
    apt-utils \
    git \
    curl \
    vim \
    python3 \
    python3-pip \
    python3-dev \
    pkg-config \
    libmysqlclient-dev \
    build-essential \
    bedtools \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --upgrade pip setuptools wheel

WORKDIR /

ENV CBIO_ETL_VERSION=2.4.4
ENV CBIO_REFS_VERSION=1.1.1

RUN git clone https://github.com/kids-first/kf-cbioportal-etl.git \
    && cd kf-cbioportal-etl \
    && git checkout v${CBIO_ETL_VERSION} \
    && curl -L https://github.com/kids-first/kf-cbioportal-etl-refs/archive/refs/tags/v${CBIO_REFS_VERSION}.tar.gz | tar -xz -C cbioportal_etl/ --wildcards '*REFS/*' --strip-components=1 \
    && curl -L https://github.com/kids-first/kf-cbioportal-etl-refs/archive/refs/tags/v${CBIO_REFS_VERSION}.tar.gz | tar -xz -C cbioportal_etl/ --wildcards '*STUDY_CONFIGS/*' --strip-components=1 \
    && pip install .
    
COPY Dockerfile .
