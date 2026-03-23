ARG PLATFORM=linux/amd64
FROM --platform=${PLATFORM} ubuntu:24.04

LABEL maintainer="Miguel Brown <brownm28@chop.edu>"
LABEL description="Base software for samtools image"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
    autoconf \
    automake \
    make \
    gcc \
    perl \
    zlib1g-dev \
    libbz2-dev \
    liblzma-dev \
    libcurl4-gnutls-dev \
    libssl-dev \
    libncurses5-dev \
    libdeflate-dev \
    bzip2 \
    curl \
