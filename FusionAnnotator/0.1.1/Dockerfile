FROM ubuntu:20.04
LABEL maintainer="brownm28@chop.edu"
LABEL description="Ported over from https://github.com/kgaonkar6/tools/blob/master/FusionAnnotator/Dockerfile. Release installed from commit between releases, so release version bumped"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
    autoconf \
    automake \
    build-essential \
    curl \
    tar \
    pigz \
    git \
    libreadline-gplv2-dev \
    libncursesw5-dev \
    libssl-dev \
    libsqlite3-dev \
    tk-dev \
    libgdbm-dev \
    libc6-dev \
    libbz2-dev

WORKDIR opt
# Install FusionAnnotator
# STARfusion 1.50 bundled FusionAnnotator
# STARfusion release 1.5.0 https://github.com/STAR-Fusion/STAR-Fusion/tree/ef595ad49a72ab860f1732223bb9274c98e9ebfb
# FusionAnnotator bundled https://github.com/FusionAnnotator/FusionAnnotator/tree/9cd889a87c838243555f14beabfc677f539084a3 

RUN git clone https://github.com/FusionAnnotator/FusionAnnotator.git && \
    cd FusionAnnotator && \
    git checkout 9cd889a 

RUN cd FusionAnnotator/PerlLib

RUN curl -SL "https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/Canary-Stability-2013.tar.gz" | tar -zx && \
    cd Canary-Stability-2013 && \
    perl Makefile.PL && \
    make && \
    make install 
 
RUN curl -SL "https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/common-sense-3.74.tar.gz" | tar -zx && \
    cd common-sense-3.74 && \
    perl Makefile.PL && \
    make && \
    make install 

RUN curl -SL "https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/Types-Serialiser-1.0.tar.gz" |  tar -zx && \
    cd Types-Serialiser-1.0 && \
    perl Makefile.PL && \
    make && \
    make install 

RUN curl -SL "https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/JSON-XS-4.02.tar.gz" | tar -zx && \
    cd JSON-XS-4.02 && \
    perl Makefile.PL && \
    make && \
    make install

RUN apt remove -y build-essential curl git && apt autoclean -y
WORKDIR /opt/FusionAnnotator/
ENV FUSION_ANNOTATOR /opt/FusionAnnotator/FusionAnnotator
