FROM ubuntu:20.04
MAINTAINER Alex Sickler (sicklera@email.chop.edu)

ENV ZUMIS_VERSION 2.9.4

RUN apt update -y && apt install -y build-essential wget
RUN wget https://github.com/sdparekh/zUMIs/archive/${ZUMIS_VERSION}.tar.gz && tar -xvzf ${ZUMIS_VERSION}.tar.gz && rm ${ZUMIS_VERSION}.tar.gz && mv zUMIs-${ZUMIS_VERSION} zumis
RUN apt remove -y build-essential wget && apt autoremove -y
