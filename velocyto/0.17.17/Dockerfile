FROM ubuntu:18.04
MAINTAINER Alex Sickler (sicklera@email.chop.edu)

ENV VELOCYTO_VERSION 0.17.17
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get update && apt-get install -y python3-pip make zlib1g-dev libbz2-dev liblzma-dev samtools; \
pip3 install cython; \
pip3 install numpy; \
pip3 install velocyto==$VELOCYTO_VERSION; \
apt-get remove -y make zlib1g-dev libbz2-dev liblzma-dev
