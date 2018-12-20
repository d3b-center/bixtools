FROM ubuntu:18.04 AS build-env
MAINTAINER Yuankun Zhu (zhuy@email.chop.edu)


ENV STAR_VERSION 2.6.1d

RUN apt-get update; \ 
apt-get install --yes wget; \
apt-get clean; \
cd /usr/local && wget https://github.com/alexdobin/STAR/archive/${STAR_VERSION}.tar.gz; \
tar -zxf ${STAR_VERSION}.tar.gz; \
mv STAR-${STAR_VERSION}/bin/Linux_x86_64_static/STAR /usr/bin/STAR; \
