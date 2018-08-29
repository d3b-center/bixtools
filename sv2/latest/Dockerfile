FROM ubuntu:16.04
MAINTAINER Miguel Brown (brownm28@email.chop.edu)

ENV SV2_VERSION latest
ADD seq_cache_populate.pl /seq_cache_populate.pl
RUN apt update && apt install -y python python-pip libz-dev bedtools tabix  \
&& pip install cython numpy pandas pybedtools pysam scikit-learn scipy && pip install sv2 \
&& apt autoclean -y && apt autoremove -y