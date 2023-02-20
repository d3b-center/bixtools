FROM ubuntu:20.04
LABEL maintainer="Daniel Miller (millerd15@chop.edu)"

# Versions
ARG MSISENSOR_VER=1.1.a
ARG SAMTOOLS_VER=1.10

# Installing pre requisits for SAMtools
RUN apt update && apt install -y \
    curl \
    make \
    gcc \
    zlib1g-dev \
    libncurses5-dev \
    libcurl4-openssl-dev \
    libbz2-dev \
    liblzma-dev \
    && apt autoremove -y

# Download and install SAMtools
RUN curl -sL https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VER}/samtools-${SAMTOOLS_VER}.tar.bz2 | tar -jx &&\
    cd samtools-${SAMTOOLS_VER} &&\
    ./configure &&\
    make &&\
    make install &&\
    cd / &&\
    rm -rf samtools-${SAMTOOLS_VER}

# Download and install MSIsensor
RUN curl -sL https://github.com/xjtu-omics/msisensor-pro/archive/refs/tags/${MSISENSOR_VER}.tar.gz | tar -zx

ENV PATH=/msisensor-pro-${MSISENSOR_VER}/binary:$PATH

COPY Dockerfile .
