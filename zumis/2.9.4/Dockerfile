FROM ubuntu:20.04
MAINTAINER Alex Sickler (sicklera@email.chop.edu)

ENV ZUMIS_VERSION 2.9.4
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt update -y && apt install -y build-essential wget && wget https://github.com/sdparekh/zUMIs/archive/${ZUMIS_VERSION}.tar.gz && tar -xvzf ${ZUMIS_VERSION}.tar.gz && rm ${ZUMIS_VERSION}.tar.gz && mv zUMIs-${ZUMIS_VERSION} zumis &&cat /zumis/zUMIs-miniconda.parta* > /zumis/zUMIs-miniconda.tar.bz2 && mkdir -p /zumis/zUMIs-env && tar -xj --overwrite -f /zumis/zUMIs-miniconda.tar.bz2 -C /zumis/zUMIs-env && rm /zumis/zUMIs-miniconda.tar.bz2 /zumis/zUMIs-miniconda.parta* && apt remove -y build-essential wget && apt autoremove -y
