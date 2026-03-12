ARG PLATFORM=linux/amd64
FROM --platform=${PLATFORM} ubuntu:24.04

LABEL maintainer="Miguel Brown <brownm28@chop.edu>"
LABEL description="Base software for ETL image"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
    apt-utils \
    git \
    curl \
    vim \
    python3 \
    python3-pip \
    python3-dev \
    pkg-config \
    build-essential \
    bedtools \
    && rm -rf /var/lib/apt/lists/*