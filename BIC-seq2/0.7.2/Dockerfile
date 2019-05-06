FROM debian:latest
LABEL maintainer="Miguel Brown (brownm28@email.chop.edu)"
LABEL description="Modified from Ding lab dockerfile: https://github.com/ding-lab/BICSEQ2/blob/master/docker/v7/Dockerfile#L18"

ENV SEG_VERSION 0.7.2
ENV NORM_VERSION 0.2.4
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update --fix-missing && apt install -y wget bzip2 ca-certificates curl tar libxt-dev r-base parallel samtools build-essential zlib1g-dev \
libncurses5-dev libbz2-dev liblzma-dev libcurl4-openssl-dev libcrypto++-dev libcurl4-openssl-dev libssl-dev

RUN wget -q http://compbio.med.harvard.edu/BIC-seq/NBICseq-norm_v${NORM_VERSION}.tar.gz && \
wget -q http://compbio.med.harvard.edu/BIC-seq/NBICseq-seg_v${SEG_VERSION}.tar.gz && \
tar -xzf NBICseq-norm_v${NORM_VERSION}.tar.gz && rm NBICseq-norm_v${NORM_VERSION}.tar.gz && cd NBICseq-norm_v${NORM_VERSION} && \
make clean && make && cd / && \
tar -xzf NBICseq-seg_v${SEG_VERSION}.tar.gz && rm NBICseq-seg_v${SEG_VERSION}.tar.gz && cd NBICseq-seg_v${SEG_VERSION} && \
make clean && make && cd / && \
apt remove -y wget