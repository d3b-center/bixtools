FROM alpine:3.6
MAINTAINER Yuankun Zhu (zhuy@email.chop.edu)

ENV GATK4_VERSION 4.beta.6

RUN apk add --update --no-cache openjdk8-jre python2 wget; \
wget -q https://github.com/broadinstitute/gatk/releases/download/${GATK4_VERSION}/gatk-${GATK4_VERSION}.zip; \
unzip gatk-${GATK4_VERSION}.zip; \
mv gatk-${GATK4_VERSION}/gatk-* . && rm -rf gatk-${GATK4_VERSION}*; \
apk del wget
