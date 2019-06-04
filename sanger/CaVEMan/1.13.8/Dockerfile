FROM ubuntu:18.04
LABEL maintainer="Miguel Brown (brownm28@email.chop.edu)"

ENV SAMTOOLS_VERSION=1.9
ENV HTSLIB_VERSION=1.9
ENV CAVEMAN_VERSION=1.13.8
ENV LD_LIBRARY_PATH=/samtools-1.9/htslib-1.9

RUN apt update && apt install -y wget build-essential zlib1g-dev libncurses5-dev libbz2-dev liblzma-dev libcurl4-openssl-dev && \
wget -q https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2; \
tar xjvf samtools-${SAMTOOLS_VERSION}.tar.bz2 && rm samtools-${SAMTOOLS_VERSION}.tar.bz2 && \
cd /samtools-${SAMTOOLS_VERSION}/ && ./configure && make && make install && \
cd htslib-${HTSLIB_VERSION}/ && ./configure && make && make install && \
cd / && wget -q https://github.com/cancerit/CaVEMan/archive/${CAVEMAN_VERSION}.tar.gz && \
tar -xzf ${CAVEMAN_VERSION}.tar.gz && rm ${CAVEMAN_VERSION}.tar.gz && cd CaVEMan-${CAVEMAN_VERSION} && make && cd / && \
apt remove -y build-essential zlib1g-dev wget