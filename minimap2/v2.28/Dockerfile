FROM --platform=linux/amd64 ubuntu:22.04

LABEL maintainer="Jessica Wong <wongj4@chop.edu>"
LABEL description="minimap2"

RUN apt update && apt install -y \
    wget \
    build-essential \
    samtools

ENV MINIMAP2_VERSION 2.28

RUN wget https://github.com/lh3/minimap2/releases/download/v${MINIMAP2_VERSION}/minimap2-${MINIMAP2_VERSION}_x64-linux.tar.bz2 \
    && tar -jxvf minimap2-${MINIMAP2_VERSION}_x64-linux.tar.bz2

WORKDIR /minimap2-${MINIMAP2_VERSION}_x64-linux

RUN cp minimap2 /usr/local/bin/

COPY Dockerfile .