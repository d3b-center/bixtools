FROM ubuntu:16.04
MAINTAINER Miguel Brown (brownm28@email.chop.edu)

ENV SV2_VERSION latest

RUN apt update && apt install -y git python python-pip libz-dev bedtools  \
&& pip install cython numpy pandas pybedtools pysam scikit-learn && pip install sv2