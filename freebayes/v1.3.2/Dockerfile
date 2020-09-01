FROM ubuntu:18.04
LABEL maintainer="Daniel Miller (millerd15@email.chop.edu)"

ENV CMAKE_VERSION 3.10.2-1ubuntu2.18.04.1
ENV FREEBAYES_VERSION v1.3.2
ENV G_VERSION 4:7.4.0-1ubuntu2.3
ENV GIT_VERSION 1:2.17.1-1ubuntu0.7
ENV LIBLZMA_VERSION 5.2.2-1.3
ENV LIBBZ2_VERSION 1.0.6-8.1ubuntu0.2
ENV WGET_VERSION 1.19.4-1ubuntu2.2
ENV ZLIB1G_VERSION 1:1.2.11.dfsg-0ubuntu2

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update \
&& apt install -y \
cmake=${CMAKE_VERSION} \
g++=${G_VERSION} \
git=${GIT_VERSION} \
liblzma-dev=${LIBLZMA_VERSION} \
libbz2-dev=${LIBBZ2_VERSION} \
wget=${WGET_VERSION} \
zlib1g-dev=${ZLIB1G_VERSION} \
&& git clone --recursive --depth 1 --branch ${FREEBAYES_VERSION} https://github.com/ekg/freebayes.git \
&& cd freebayes \
&& make \
&& make install 
