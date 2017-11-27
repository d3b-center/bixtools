FROM alpine:3.6
MAINTAINER Yuankun Zhu (zhuy@email.chop.edu)

RUN apk add --update --no-cache openjdk8-jre curl; \
curl https://software.broadinstitute.org/gatk/download/auth\?package\=GATK | tar xjv; \
mv GenomeAnalysisTK-3.8-*/GenomeAnalysisTK.jar . && rm -rf GenomeAnalysisTK-3.8-*/; \
apk del curl
