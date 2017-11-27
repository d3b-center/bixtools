FROM alpine:3.6
MAINTAINER Yuankun Zhu (zhuy@email.chop.edu)

ENV GATK_ARCHIVE_VERSION 3.6-0-g89b7209

RUN apk add --update --no-cache openjdk8-jre curl; \
curl https://software.broadinstitute.org/gatk/download/auth\?package\=GATK-archive\&version\=${GATK_ARCHIVE_VERSION} \
| tar xjv && rm -rf resources/ \
apk del curl
