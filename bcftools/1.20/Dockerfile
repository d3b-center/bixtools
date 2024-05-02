FROM ubuntu:22.04
LABEL maintainer="Miguel Brown (brownm28@chop.edu)"

ENV BCFTOOLS_VERSION 1.20
ENV HTSLIB_VERSION 1.20
ENV BCFTOOLS_PLUGINS=/bcftools-${BCFTOOLS_VERSION}/plugins
RUN apt update && apt install -y wget build-essential zlib1g-dev libncurses5-dev libbz2-dev liblzma-dev libcurl4-openssl-dev libssl-dev
RUN wget -q https://github.com/samtools/bcftools/releases/download/${BCFTOOLS_VERSION}/bcftools-${BCFTOOLS_VERSION}.tar.bz2
RUN tar xjvf bcftools-${BCFTOOLS_VERSION}.tar.bz2 && \
cd /bcftools-${BCFTOOLS_VERSION}/ && ./configure && make && make install
RUN cd /bcftools-${BCFTOOLS_VERSION}/htslib-${HTSLIB_VERSION}/ && ./configure && make && make install
RUN rm bcftools-${BCFTOOLS_VERSION}.tar.bz2 && apt clean build-essential zlib1g-dev wget && apt -y autoclean && apt -y autoremove
COPY Dockerfile .
