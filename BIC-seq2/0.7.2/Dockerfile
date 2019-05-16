FROM debian:latest
LABEL maintainer="Miguel Brown (brownm28@email.chop.edu)"
LABEL description="Modified from Ding lab dockerfile: https://github.com/ding-lab/BICSEQ2/blob/master/docker/v7/Dockerfile#L18"

ENV SEG_VERSION 0.7.2
ENV NORM_VERSION 0.2.4
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update --fix-missing && apt install -y wget bzip2 ca-certificates curl tar libxt-dev r-base parallel samtools build-essential zlib1g-dev \
libncurses5-dev libbz2-dev liblzma-dev libcurl4-openssl-dev libcrypto++-dev libcurl4-openssl-dev libssl-dev && \
wget -q http://compbio.med.harvard.edu/BIC-seq/NBICseq-norm_v${NORM_VERSION}.tar.gz && \
wget -q http://compbio.med.harvard.edu/BIC-seq/NBICseq-seg_v${SEG_VERSION}.tar.gz && \
tar -xzf NBICseq-norm_v${NORM_VERSION}.tar.gz && rm NBICseq-norm_v${NORM_VERSION}.tar.gz && cd NBICseq-norm_v${NORM_VERSION} && \
make clean && make && cd / && \
tar -xzf NBICseq-seg_v${SEG_VERSION}.tar.gz && rm NBICseq-seg_v${SEG_VERSION}.tar.gz && cd NBICseq-seg_v${SEG_VERSION} && \
make clean && make && cd / && \
wget -q http://compbio.med.harvard.edu/BIC-seq/BICseq2/samtools-0.1.7a_getUnique-0.1.3.tar.gz && \
tar -xzf samtools-0.1.7a_getUnique-0.1.3.tar.gz && rm samtools-0.1.7a_getUnique-0.1.3.tar.gz && \
chown -R root:root NBICseq-norm_v${NORM_VERSION} && chown -R root:root NBICseq-seg_v${SEG_VERSION} && chown -R root:root samtools-0.1.7a_getUnique-0.1.3 && \
chmod -R 755 NBICseq-norm_v${NORM_VERSION} && chmod -R 755 NBICseq-seg_v${SEG_VERSION} && chmod -R 755 samtools-0.1.7a_getUnique-0.1.3 && \
apt remove -y wget