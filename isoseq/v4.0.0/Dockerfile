FROM --platform=linux/amd64 ubuntu:22.04

LABEL maintainer="Jessica Wong <wongj4@chop.edu>"
LABEL description="isoseq"

RUN apt-get update \
    && apt-get install -y wget

ENV ISOSEQ_VERSION 4.0.0

RUN wget -O /bin/isoseq https://github.com/PacificBiosciences/IsoSeq/releases/download/v${ISOSEQ_VERSION}/isoseq \
    && chmod +x /bin/isoseq

COPY Dockerfile .