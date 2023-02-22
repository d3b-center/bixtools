FROM staphb/bcftools:1.10.2
MAINTAINER Daniel Miller (millerd15@chop.edu)

ENV SNPEFF_VERSION 4_3t
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y wget openjdk-8-jdk unzip

RUN mkdir -p /tmp/scratch/build && cd /tmp/scratch && \
wget -q -t 3 http://downloads.sourceforge.net/project/snpeff/snpEff_v${SNPEFF_VERSION}_core.zip && \
unzip snpEff_v${SNPEFF_VERSION}_core.zip && mv snpEff /opt/ && \
cd / && rm -rf /tmp/scratch

RUN apt remove -y wget && apt clean -y && apt autoremove -y

WORKDIR /

COPY Dockerfile .
