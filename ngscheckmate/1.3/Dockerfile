FROM pgc-images.sbgenomics.com/d3b-bixu/samtools:1.9 AS build-env
LABEL maintainer="Miguel Brown (brownm28@chop.edu)"

ENV VCFTOOLS_VERSION 0.1.16
ENV BCF_VERSION 1.9
ENV NCM_HOME /NGSCheckMate
ENV COMMIT 8ea2c043896adf9bbd1dc5bb2136f3a1dab9b445

RUN apt update && apt install -y wget git python pkg-config build-essential automake \
&& wget -q https://github.com/samtools/bcftools/releases/download/1.9/bcftools-${BCF_VERSION}.tar.bz2 \
&& tar -xjf bcftools-${BCF_VERSION}.tar.bz2 \
&& cd /bcftools-${BCF_VERSION}/ && ./configure && make \
&& mv /bcftools-${BCF_VERSION}/bcftools /bin/ \
&& cd / && rm -rf /bcftools* \
&& git clone https://github.com/parklab/NGSCheckMate && cd NGSCheckMate && git checkout ${COMMIT} && cd /\
&& wget https://github.com/vcftools/vcftools/releases/download/v${VCFTOOLS_VERSION}/vcftools-${VCFTOOLS_VERSION}.tar.gz \
&& tar -xzf vcftools-${VCFTOOLS_VERSION}.tar.gz && cd vcftools-${VCFTOOLS_VERSION} && ./autogen.sh && ./configure && make && make install \
&& cd / && rm -rf /vcftools-${VCFTOOLS_VERSION}/ \
&& apt -y remove wget git pkg-config automake && apt -y autoclean && apt -y autoremove

ADD Dockerfile .