FROM --platform=linux/amd64 ubuntu:22.04

LABEL maintainer="Jessica Wong <wongj4@chop.edu>"
LABEL description="lima"

RUN apt-get update \
    && apt-get install -y wget 

ENV LIMA_VERSION 2.9.0

RUN wget https://github.com/PacificBiosciences/barcoding/releases/download/v${LIMA_VERSION}/lima.tar.gz \
    && tar -xzvf lima.tar.gz -C /bin \
    && chmod +x /bin/lima

COPY Dockerfile .