FROM ubuntu:18.04
LABEL maintainer="Miguel Brown (brownm28@email.chop.edu)"
LABEL maintainer="Daniel Miller (millerd15@email.chop.edu)"

ENV GATK4_VERSION 4.1.7.0
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y openjdk-8-jdk python wget unzip libgomp1 tabix samtools r-base-dev; \
wget -q https://github.com/broadinstitute/gatk/releases/download/${GATK4_VERSION}/gatk-${GATK4_VERSION}.zip; \
unzip gatk-${GATK4_VERSION}.zip; \
mv gatk-${GATK4_VERSION}/gatk* . && rm -rf gatk-${GATK4_VERSION}*;

RUN R -e "install.packages(c('optparse','data.table'))"
