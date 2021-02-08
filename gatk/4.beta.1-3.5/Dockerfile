FROM alpine:3.6
MAINTAINER Yuankun Zhu (zhuy@email.chop.edu)

ENV GATK4_VERSION 4.beta.1
ENV GATK_ARCHIVE_VERSION 3.5-0-g36282e4

RUN apk add --update --no-cache openjdk8-jre python2 wget curl bash; \
wget https://github.com/broadinstitute/gatk/releases/download/${GATK4_VERSION}/gatk-${GATK4_VERSION}.zip; \
unzip gatk-${GATK4_VERSION}.zip; \
mv gatk-${GATK4_VERSION}/gatk-* . && rm -rf gatk-${GATK4_VERSION}*; \
curl https://sdk.cloud.google.com > install.sh; bash install.sh --disable-prompts && rm install.sh; \
export PATH=$PATH:/root/google-cloud-sdk/bin; \
gsutil cp gs://gatk-software/package-archive/gatk/GenomeAnalysisTK-${GATK_ARCHIVE_VERSION}.tar.bz2 - | tar xjv && rm -rf resources/; \
apk del wget curl
