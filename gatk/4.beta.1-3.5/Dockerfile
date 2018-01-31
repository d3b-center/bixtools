FROM alpine:3.6
MAINTAINER Yuankun Zhu (zhuy@email.chop.edu)

ENV GATK4_VERSION 4.beta.1
ENV GATK_ARCHIVE_VERSION 3.5-0-g36282e4

RUN apk add --update --no-cache openjdk8-jre python2 wget curl; \
wget https://github.com/broadinstitute/gatk/releases/download/${GATK4_VERSION}/gatk-${GATK4_VERSION}.zip; \
unzip gatk-${GATK4_VERSION}.zip; \
mv gatk-${GATK4_VERSION}/gatk-* . && rm -rf gatk-${GATK4_VERSION}*; \
curl https://software.broadinstitute.org/gatk/download/auth\?package\=GATK-archive\&version\=${GATK_ARCHIVE_VERSION} \
| tar xjv && rm -rf resources/; \
apk del wget curl
