FROM alpine:3.6
MAINTAINER Yuankun Zhu (zhuy@email.chop.edu)

ENV SAMTOOLS_VERSION 1.6

RUN apk add --no-cache build-base zlib-dev bzip2-dev xz-dev ncurses-dev ca-certificates wget; \
wget -q https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2; \
tar xjvf samtools-${SAMTOOLS_VERSION}.tar.bz2; \
cd /samtools-${SAMTOOLS_VERSION}/ && make; \
mv /samtools-${SAMTOOLS_VERSION}/samtools /bin/; \
rm -rf /samtools*; \
apk del build-base zlib-dev ca-certificates wget
