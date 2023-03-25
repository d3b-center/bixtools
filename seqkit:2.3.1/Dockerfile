FROM ubuntu:20.04

RUN apt update && apt install -y curl

WORKDIR /opt
ENV SEQKIT_VERSION 2.4.0
RUN curl -sL https://github.com/shenwei356/seqkit/releases/download/v${SEQKIT_VERSION}/seqkit_linux_amd64.tar.gz | tar -xz && cp seqkit /usr/local/bin

WORKDIR / 
COPY Dockerfile .
