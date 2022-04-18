FROM ubuntu:18.04
LABEL maintainer="Miguel Brown (brownm28@chop.edu)"

ENV SAMTOOLS_VERSION 1.9
ENV BCF_VERSION 1.9
ENV NCM_HOME /NGSCheckMate
ENV COMMIT 8ea2c043896adf9bbd1dc5bb2136f3a1dab9b445

RUN apt update && apt install -y wget git python build-essential zlib1g-dev automake libncurses5-dev libbz2-dev liblzma-dev libcurl4-openssl-dev pkg-config \
&& wget -q https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2 \
&& tar xjvf samtools-${SAMTOOLS_VERSION}.tar.bz2 \
&& cd /samtools-${SAMTOOLS_VERSION}/ && ./configure && make \
&& mv /samtools-${SAMTOOLS_VERSION}/samtools /bin/ \
&& cd / && rm -rf /samtools* \
&& wget -q https://github.com/samtools/bcftools/releases/download/1.9/bcftools-${BCF_VERSION}.tar.bz2 \
&& tar -xjf bcftools-${BCF_VERSION}.tar.bz2 \
&& cd /bcftools-${BCF_VERSION}/ && ./configure && make \
&& mv /bcftools-${BCF_VERSION}/bcftools /bin/ \
&& cd / && rm -rf /bcftools* \
&& git clone https://github.com/parklab/NGSCheckMate && cd NGSCheckMate && git checkout ${COMMIT} && cd /\
&& git clone https://github.com/vcftools/vcftools \
&& cd vcftools && ./autogen.sh && ./configure && make && make install \
&& cd / && rm -rf /vcftools/ \
&& apt -y remove zlib1g-dev wget git automake pkg-config && apt -y autoclean && apt -y autoremove

ADD Dockerfile .