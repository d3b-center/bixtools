FROM alpine:3.6
MAINTAINER Yuankun Zhu (zhuy@email.chop.edu)

ENV GATK4_VERSION 4.0.1.2
ENV PICARD_VERSION 2.8.3

RUN apk add --update --no-cache openjdk8-jre python2 ca-certificates wget; \
wget https://github.com/broadinstitute/gatk/releases/download/${GATK4_VERSION}/gatk-${GATK4_VERSION}.zip; \
unzip gatk-${GATK4_VERSION}.zip; \
mv gatk-${GATK4_VERSION}/gatk-* . && rm -rf gatk-${GATK4_VERSION}*; \
wget -q https://github.com/broadinstitute/picard/releases/download/${PICARD_VERSION}/picard.jar; \
apk del wget ca-certificates