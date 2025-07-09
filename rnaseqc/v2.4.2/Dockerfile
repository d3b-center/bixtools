FROM ubuntu:20.04
LABEL maintainer="Miguel Brown (brownm28@chop.edu)"
LABEL description="RNASeQC, best built with platform linux/amd64"

ADD --chmod=755 https://github.com/getzlab/rnaseqc/releases/download/v2.4.2/rnaseqc.v2.4.2.linux.gz /usr/local/bin/rnaseqc.gz
RUN gzip -d /usr/local/bin/rnaseqc.gz
COPY Dockerfile .