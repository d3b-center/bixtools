FROM ubuntu:20.04
LABEL maintainer="Alex Sickler (sicklera@email.chop.edu)"

ENV NUMPY_VERSION 1.20.3
ENV SCRUBLET_VERSION 0.2.3
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get update && apt-get install -y python3-pip; \
pip3 install numpy==$NUMPY_VERSION; \
pip3 install scrublet==$SCRUBLET_VERSION; \
ln -s /usr/bin/python3 /usr/local/bin/python;
