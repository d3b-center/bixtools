FROM ubuntu:20.04
LABEL maintainer="Miguel Brown (brownm28@chop.edu)"

ENV CUTADAPT_VERSION 3.4

RUN apt update && apt install -y python3-pip pigz \
&& python3 -m pip install cutadapt==${CUTADAPT_VERSION} \
&& apt -y autoclean &&  apt -y autoremove

ADD Dockerfile ./