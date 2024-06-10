FROM ubuntu:22.04
LABEL maintainer="Miguel Brown (brownm28@chop.edu)"
LABEL description="Builds T1K HLA Typer image"

ENV T1K_VERSION=1.0.5
ENV HTSLIB_VERSION=1.20

RUN apt update \
    && apt install -y \
       build-essential \
       curl \
       libbz2-dev \
       libcurl4-openssl-dev \
       libdeflate-dev \
       liblzma-dev \
       libncurses5-dev \
       libpthread-stubs0-dev \
       libssl-dev \
       zlib1g-dev

RUN curl -sL https://github.com/mourisl/T1K/archive/refs/tags/v${T1K_VERSION}.tar.gz | tar -xz && cd T1K-${T1K_VERSION} \
    && curl -sL https://github.com/samtools/htslib/releases/download/${HTSLIB_VERSION}/htslib-${HTSLIB_VERSION}.tar.bz2 | tar -xj

RUN cd /T1K-${T1K_VERSION}/htslib-${HTSLIB_VERSION} \
    && ./configure && make && make install \
    && cd /T1K-${T1K_VERSION} \
    && sed -i "s#htslib-1.15.1#htslib-${HTSLIB_VERSION}#g" Makefile alignments.hpp && make htslib=1

ENV LD_LIBRARY_PATH=/T1K-${T1K_VERSION}/htslib-${HTSLIB_VERSION}
ENV PATH=$PATH:/T1K-${T1K_VERSION}/

RUN cd /opt \
    && curl -OL https://raw.githubusercontent.com/samtools/samtools/develop/misc/seq_cache_populate.pl

COPY Dockerfile .
