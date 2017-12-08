FROM alpine:3.6
MAINTAINER Yuankun Zhu (zhuy@email.chop.edu)

ENV BWA_VERSION 0.7.17

RUN apk add --no-cache build-base zlib-dev ca-certificates wget; \
wget -q https://github.com/lh3/bwa/releases/download/v${BWA_VERSION}/bwa-${BWA_VERSION}.tar.bz2; \
tar xjvf bwa-${BWA_VERSION}.tar.bz2; \
cd /bwa-${BWA_VERSION}/ && make; \
mv /bwa-${BWA_VERSION}/bwa /bin/; \
rm -rf /bwa*; \
apk del build-base zlib-dev ca-certificates wget
