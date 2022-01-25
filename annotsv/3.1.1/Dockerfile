FROM ubuntu:20.04
LABEL maintainer="Daniel Miller <millerd15@chop.edu>"
LABEL description="annotsv 3.1.1"

RUN apt update && \
  DEBIAN_FRONTEND=noninteractive apt install -y wget \
  git \
  make \
  gcc \
  zlib1g-dev \
  liblzma-dev \
  libbz2-dev \
  libcurl4-gnutls-dev \
  tcl \
  pigz

ENV BEDTOOLS_VERSION=2.30.0
RUN mkdir /opt/bedtools2
WORKDIR /opt/bedtools2
RUN wget https://github.com/arq5x/bedtools2/releases/download/v$BEDTOOLS_VERSION/bedtools.static.binary && \
  mv bedtools.static.binary bedtools && \
  chmod a+x bedtools && \
  ln -s /opt/bedtools2/bedtools /usr/bin

ENV SAMTOOLS_VERSION=1.14
WORKDIR /opt
RUN git clone --branch $SAMTOOLS_VERSION --recurse-submodules git://github.com/samtools/htslib.git && \
  git clone --branch $SAMTOOLS_VERSION git://github.com/samtools/bcftools.git
WORKDIR /opt/bcftools
RUN make

ENV ANNOTSV_VERSION=v3.1.1
WORKDIR /opt
RUN git clone --branch $ANNOTSV_VERSION https://github.com/lgmgeo/AnnotSV.git
WORKDIR /opt/AnnotSV
RUN make PREFIX=. install

RUN apt remove -y git wget
