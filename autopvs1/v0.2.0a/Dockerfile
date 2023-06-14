FROM ubuntu:20.04
LABEL maintainer="Miguel Browmn <brownm28@chop.edu>"
LABEL description="Docker file with modified version of autopvs1"

ENV REPO_RELEASE=0.1.0

RUN apt update -y && apt install -y curl wget python3 python3-pip pigz git libbz2-dev liblzma-dev zlib1g-dev \ 
&& curl -sL https://github.com/d3b-center/D3b-Pathogenicity-Preprocessing/archive/refs/tags/v${REPO_RELEASE}.tar.gz | tar xz --strip-components=1 D3b-Pathogenicity-Preprocessing-${REPO_RELEASE}/autopvs1
&& pip3 install pysam==0.17.0 pyfaidx && \
apt remove -y wget git

COPY Dockerfile .