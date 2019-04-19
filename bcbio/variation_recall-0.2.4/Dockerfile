FROM ubuntu:18.04
LABEL maintainer="Miguel Brown (brownm28@email.chop.edu)"

ENV BCBIO_VR_VERSION 0.2.4

RUN apt update && apt install -y openjdk-8-jdk wget libgomp1 tabix samtools bcftools bedtools; \
wget -q https://github.com/bcbio/bcbio.variation.recall/releases/download/v${BCBIO_VR_VERSION}/bcbio-variation-recall; \
chmod 755 bcbio-variation-recall; \
apt remove -y wget
