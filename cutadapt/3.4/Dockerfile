FROM ubuntu:20.04
LABEL maintainer="Miguel Brown (brownm28@chop.edu)"

ENV CUTADAPT_VERSION 3.4
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y python3-pip pigz samtools bc \
&& python3 -m pip install cutadapt==${CUTADAPT_VERSION} \
&& apt -y autoclean &&  apt -y autoremove

ADD Dockerfile ./