FROM --platform=linux/amd64 ubuntu:22.04

LABEL maintainer="Jessica Wong <wongj4@chop.edu>"
LABEL description="nanocount"

RUN apt update && apt install -y \
    curl \
    build-essential \
    zlib1g-dev \
    liblzma-dev \
    libbz2-dev \
    libncurses5-dev \
    libcurl4-gnutls-dev \
    libssl-dev \
    python3 \
    python3-pip \
    git

ENV NANOCOUNT_VERSION 1.1.0

RUN curl -sL 'https://github.com/pysam-developers/pysam/archive/refs/tags/v0.22.0.tar.gz' | tar xz && cd pysam-0.22.0 && pip3 install .

RUN pip3 install git+https://github.com/a-slide/NanoCount.git

WORKDIR /
COPY Dockerfile .