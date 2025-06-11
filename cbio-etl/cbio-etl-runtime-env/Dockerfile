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

RUN git clone https://github.com/kids-first/kf-cbioportal-etl.git
    
COPY Dockerfile .
