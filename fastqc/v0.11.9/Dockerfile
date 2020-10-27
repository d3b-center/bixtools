FROM ubuntu:20.04
LABEL maintainer="Alex Sickler (sicklera@email.chop.edu)"

ARG DEBIAN_FRONTEND=noninteractive
ENV FASTQC_VERSION v0.11.9
ENV PATH /FastQC:$PATH

RUN apt update && apt install -y wget zip build-essential openjdk-8-jdk; \
wget https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_${FASTQC_VERSION}.zip; \
unzip fastqc_${FASTQC_VERSION}.zip && rm fastqc_${FASTQC_VERSION}.zip; \
chmod a+x /FastQC/fastqc; \
apt clean build-essential zlib1g-dev wget && apt -y  autoclean && apt -y autoremove
