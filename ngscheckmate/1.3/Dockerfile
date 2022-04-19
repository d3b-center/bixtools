FROM pgc-images.sbgenomics.com/d3b-bixu/samtools:1.9 AS build-env
LABEL maintainer="Miguel Brown (brownm28@chop.edu)"

ENV VCFTOOLS_VERSION 0.1.16
ENV NCM_HOME /NGSCheckMate
ENV COMMIT 8ea2c043896adf9bbd1dc5bb2136f3a1dab9b445

RUN apt update && apt install -y wget git python pkg-config build-essential automake \
&& git clone https://github.com/parklab/NGSCheckMate && cd NGSCheckMate && git checkout ${COMMIT} && cd /\
&& wget https://github.com/vcftools/vcftools/releases/download/v${VCFTOOLS_VERSION}/vcftools-${VCFTOOLS_VERSION}.tar.gz \
&& tar -xzf vcftools-${VCFTOOLS_VERSION}.tar.gz && cd vcftools-${VCFTOOLS_VERSION} && ./autogen.sh && ./configure && make && make install \
&& cd / && rm -rf /vcftools-${VCFTOOLS_VERSION}/ \
&& apt -y remove wget git build-essential automake && apt -y autoclean && apt -y autoremove

ADD Dockerfile .