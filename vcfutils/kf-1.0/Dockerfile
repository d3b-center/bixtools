FROM ubuntu:18.04
LABEL maintainer="Miguel Brown (brownm28@chop.edu)"
LABEL description="Re-tag of vcfutils:latest with matching commits where available"

RUN apt update && apt install -y bcftools vcftools tabix git build-essential zlib1g-dev libbz2-dev liblzma-dev autoconf libcurl4-openssl-dev libssl-dev python3 bedtools
RUN git clone https://github.com/atks/vt.git \
&& cd vt \
&& git checkout 88da43649b5a39ddfc00d8a8f4d494fad50d5eec \
&& make -j8 \
&& make test
RUN cd / \
&& git clone  https://github.com/vcflib/vcflib.git \
&& cd vcflib \
&& git checkout 8bc93d8a74735b0fe6303f78b2764d6987ba1cde \
&& git submodule update --init --recursive \
&& make -j8
RUN apt autoclean -y \
&& apt remove git build-essential -y