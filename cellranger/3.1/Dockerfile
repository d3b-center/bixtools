FROM ubuntu:18.04
MAINTAINER Alex Sickler (sicklera@email.chop.edu)

ENV CELLRANGER_VERSION 3.1.0

#before building, get the link to download from:
#https://support.10xgenomics.com/single-cell-gene-expression/software/downloads/latest
ARG cellranger_uri

RUN apt update && apt install -y wget; \
wget -O ${CELLRANGER_VERSION}.tar.gz $cellranger_uri; \
tar -zxvf ${CELLRANGER_VERSION}.tar.gz; \
apt remove -y wget

ENV PATH /${CELLRANGER_VERSION}:$PATH
