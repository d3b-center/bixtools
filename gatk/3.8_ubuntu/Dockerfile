FROM ubuntu:18.04
MAINTAINER Miguel Brown (brownm28@email.chop.edu)

ENV GATK3_VERSION 3.8

RUN apt update && apt install -y openjdk-8-jdk curl tabix; \
curl https://software.broadinstitute.org/gatk/download/auth\?package\=GATK | tar xjv; \
mv GenomeAnalysisTK-3.8-*/GenomeAnalysisTK.jar . && rm -rf GenomeAnalysisTK-3.8-*/; \
apt remove -y curl