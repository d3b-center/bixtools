FROM ubuntu:22.04
LABEL maintainer="Miguel Brown (brownm28@chop.edu)"
LABEL description="Builds T1K HLA Typer image"

ENV T1K_VERSION=1.0.2

RUN apt update && apt install -y curl build-essential zlib1g-dev libncurses5-dev libbz2-dev liblzma-dev libcurl4-openssl-dev libssl-dev libpthread-stubs0-dev

RUN curl -sL https://github.com/mourisl/T1K/archive/refs/tags/v${T1K_VERSION}.tar.gz | tar -xz && cd T1K-${T1K_VERSION} && make

COPY Dockerfile .