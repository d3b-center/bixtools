FROM ubuntu:20.04

LABEL maintainer="Alex Sickler (sicklera@email.chop.edu)"

ENV PEDDY_VERSION v0.4.7

RUN apt-get update && apt upgrade -y \
&& apt-get install -y python python3-pip git \
&& git clone --depth 1 --branch ${PEDDY_VERSION} https://github.com/brentp/peddy && cd /peddy && pip3 install -r requirements.txt && pip3 install . \
&& apt-get clean build-essential \
&& apt-get autoremove -y \
&& apt-get remove -y python3-pip git \
&& update-alternatives --install /usr/bin/python python /usr/bin/python3 1
