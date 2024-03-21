FROM --platform=linux/amd64 ubuntu:22.04

LABEL maintainer="Jessica Wong <wongj4@chop.edu>"
LABEL description="pigeon"

RUN apt-get update \
    && apt-get install -y wget 

ENV PIGEON_VERSION 1.2.0

RUN wget -O /bin/pigeon https://github.com/PacificBiosciences/pigeon/releases/download/v${PIGEON_VERSION}/pigeon \
    && chmod +x /bin/pigeon

COPY Dockerfile .