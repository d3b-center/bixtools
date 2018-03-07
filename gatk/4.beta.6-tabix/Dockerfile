FROM alpine:3.6
MAINTAINER Yuankun Zhu (zhuy@email.chop.edu)

ENV GATK4_VERSION 4.beta.6

RUN apk add --update --no-cache openjdk8-jre python2 wget git build-base zlib-dev bzip2-dev xz-dev ncurses-dev; \
wget https://github.com/broadinstitute/gatk/releases/download/${GATK4_VERSION}/gatk-${GATK4_VERSION}.zip; \
unzip gatk-${GATK4_VERSION}.zip; \
mv gatk-${GATK4_VERSION}/gatk-* . && rm -rf gatk-package-4.beta.6-spark.jar; \
git clone https://github.com/samtools/tabix.git; \
cd tabix && make; \
apk del wget git build-base zlib-dev
