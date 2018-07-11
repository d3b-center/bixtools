FROM ubuntu:18.04
MAINTAINER Miguel Brown (brownm28@email.chop.edu)

ENV PICARD_VERSION 2.18.9
ADD VcfSampleRename.py /VcfSampleRename.py
RUN apt update && apt install -y openjdk-8-jdk wget tabix python; \
wget https://github.com/broadinstitute/picard/releases/download/${PICARD_VERSION}/picard.jar; \
apt remove -y wget; \
