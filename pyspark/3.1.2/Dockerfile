FROM ubuntu:20.04
LABEL maintainer="Miguel Brown (brownm28@email.chop.edu)"

ENV PYSPARK_VERSION 3.1.2
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y python-is-python3 python3-pip default-jre \
&& pip install pyspark==${PYSPARK_VERSION} glow.py dataclasses

RUN apt autoremove -y && apt autoclean -y
WORKDIR /
ADD Dockerfile /