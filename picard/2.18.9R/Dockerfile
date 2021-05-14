FROM ubuntu:18.04
LABEL maintainer = "Alex Sickler (sicklera@email.chop.edu)"

ARG DEBIAN_FRONTEND=noninteractive

ENV PICARD_VERSION 2.18.9

ADD VcfSampleRename.py /VcfSampleRename.py
RUN apt update && apt install -y r-base openjdk-8-jdk wget tabix python; \
wget https://github.com/broadinstitute/picard/releases/download/${PICARD_VERSION}/picard.jar; \
apt remove -y wget;

ADD Dockerfile .
