FROM alpine:latest
MAINTAINER Yuankun Zhu (zhuy@email.chop.edu)

ENV BWA_VERSION 0.7.17
ENV SAMTOOLS_VERSION 1.6

RUN apk add --no-cache build-base zlib-dev bzip2-dev xz-dev ncurses-dev ca-certificates wget; \
wget https://github.com/lh3/bwa/releases/download/v${BWA_VERSION}/bwa-${BWA_VERSION}.tar.bz2; \
wget https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2; \
tar xjvf bwa-${BWA_VERSION}.tar.bz2; \
tar xjvf samtools-${SAMTOOLS_VERSION}.tar.bz2; \
cd /bwa-${BWA_VERSION}/ && make; \
cd /samtools-${SAMTOOLS_VERSION}/ && make; \
mv /bwa-${BWA_VERSION}/bwa /samtools-${SAMTOOLS_VERSION}/samtools /bin/; \
rm -rf /bwa* /samtools*; \
apk del build-base zlib-dev ca-certificates wget
