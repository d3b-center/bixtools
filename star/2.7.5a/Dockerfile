FROM ubuntu:20.04 AS build-env
MAINTAINER Alex Sickler (sicklera@email.chop.edu)


ENV STAR_VERSION 2.7.5a

RUN apt-get update; \ 
apt-get install --yes wget; \
apt-get clean; \
cd /usr/local && wget https://github.com/alexdobin/STAR/archive/${STAR_VERSION}.tar.gz; \
tar -zxf ${STAR_VERSION}.tar.gz; \
mv STAR-${STAR_VERSION}/bin/Linux_x86_64_static/STAR /usr/bin/STAR; \
