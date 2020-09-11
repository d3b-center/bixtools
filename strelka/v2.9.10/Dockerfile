FROM ubuntu:18.04
LABEL maintainer="Daniel Miller (millerd15@email.chop.edu)"

ENV STRELKA_VERSION 2.9.10

RUN apt-get update && apt-get install -y \
    python \
    wget

RUN wget https://github.com/Illumina/strelka/releases/download/v${STRELKA_VERSION}/strelka-${STRELKA_VERSION}.centos6_x86_64.tar.bz2 && \
    tar xf strelka-${STRELKA_VERSION}.centos6_x86_64.tar.bz2 && \
    rm strelka-${STRELKA_VERSION}.centos6_x86_64.tar.bz2
