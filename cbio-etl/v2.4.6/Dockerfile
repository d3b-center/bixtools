FROM --platform=linux/amd64 ubuntu:24.04

LABEL maintainer="Miguel Brown <brownm28@chop.edu>"
LABEL description="cbio-etl"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
    apt-utils \
    git \
    curl \
    vim \
    python3 \
    python3-pip \
    python3-dev \
    pkg-config \
    build-essential \
    bedtools \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /

ENV CBIO_ETL_VERSION=2.4.6
ENV CBIO_REFS_VERSION=1.1.1

RUN git clone https://github.com/kids-first/kf-cbioportal-etl.git \
    && cd kf-cbioportal-etl \
    && git checkout v${CBIO_ETL_VERSION} \
    && curl -L https://github.com/kids-first/kf-cbioportal-etl-refs/archive/refs/tags/v${CBIO_REFS_VERSION}.tar.gz | tar -xz -C cbioportal_etl/ --wildcards '*REFS/*' --strip-components=1 \
    && curl -L https://github.com/kids-first/kf-cbioportal-etl-refs/archive/refs/tags/v${CBIO_REFS_VERSION}.tar.gz | tar -xz -C cbioportal_etl/ --wildcards '*STUDY_CONFIGS/*' --strip-components=1 \
    && pip install --break-system-packages .
    
COPY Dockerfile .
