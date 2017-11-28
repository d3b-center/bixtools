FROM alpine:3.6
MAINTAINER Yuankun Zhu (zhuy@email.chop.edu)

ENV BWA_VERSION 0.7.17
ENV PICARD_VERSION 2.15.0

RUN apk add --no-cache build-base zlib-dev bzip2-dev ca-certificates wget openjdk8-jre; \
wget -q https://github.com/lh3/bwa/releases/download/v${BWA_VERSION}/bwa-${BWA_VERSION}.tar.bz2; \
wget -q https://github.com/broadinstitute/picard/releases/download/${PICARD_VERSION}/picard.jar; \
tar xjf bwa-${BWA_VERSION}.tar.bz2; \
cd /bwa-${BWA_VERSION}/ \
&& make; \
mv /bwa-${BWA_VERSION}/bwa /bin/ \
&& rm -rf /bwa-${BWA_VERSION}* \
&& apk del build-base zlib-dev bzip2-dev ca-certificates wget;
