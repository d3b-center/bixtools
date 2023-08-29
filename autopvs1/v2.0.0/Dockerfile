FROM ubuntu:22.04
LABEL maintainer="Miguel Brown <brownm28@chop.edu>"
LABEL description="Docker file with modified version of autopvs1"

ENV REPO_RELEASE=2.0.0

RUN apt update -y && apt install -y curl wget python3 python3-pip pigz libbz2-dev liblzma-dev zlib1g-dev \ 
&& mkdir autopvs1 && curl -sL https://github.com/d3b-center/D3b-autoPVS1/archive/refs/tags/v${REPO_RELEASE}.tar.gz | tar xz --strip-components=1 -C autopvs1 \
&& pip3 install pysam==0.17.0 pyfaidx && \
apt remove -y wget curl

COPY Dockerfile .