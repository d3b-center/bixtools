FROM --platform=linux/amd64 ubuntu:22.04

LABEL maintainer="Jessica Wong <wongj4@chop.edu>"
LABEL description="pbfusion"

RUN apt-get update \
    && apt-get install -y wget gzip

ENV PBFUSION_VERSION 0.4.1

RUN wget https://github.com/PacificBiosciences/pbfusion/releases/download/${PBFUSION_VERSION}/pbfusion-v${PBFUSION_VERSION}-linux_x86_64.gz \
    && gunzip pbfusion-v${PBFUSION_VERSION}-linux_x86_64.gz \
    && mv pbfusion-v${PBFUSION_VERSION}-linux_x86_64 /bin/pbfusion \
    && chmod +x /bin/pbfusion

COPY Dockerfile .