FROM ubuntu:18.04
LABEL maintainer="Miguel Brown (brownm28@email.chop.edu)"

ENV LUMPY_VERSION 0.3.0
ENV SAMTOOLS_VERSION 1.9
RUN apt update && apt install -y build-essential git cmake curl python python-pip gawk autoconf libcurl4-openssl-dev libz-dev liblzma-dev libssl-dev bsdmainutils libncurses5-dev libbz2-dev \
&& pip install pysam numpy==1.16.5 \
&& curl -OL https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2 && tar -xjf samtools-${SAMTOOLS_VERSION}.tar.bz2 && rm samtools-${SAMTOOLS_VERSION}.tar.bz2 \
&& cd /samtools-${SAMTOOLS_VERSION} && ./configure && make && make install \
&& cd / && git clone https://github.com/GregoryFaust/samblaster && cd samblaster && make && cp samblaster /usr/local/bin/. && cd / && rm -rf samblaster \
&& curl -OL https://github.com/biod/sambamba/releases/download/v0.6.7/sambamba_v0.6.7_linux.tar.bz2 && tar -xjf sambamba_v0.6.7_linux.tar.bz2 && rm sambamba_v0.6.7_linux.tar.bz2 && mv ./sambamba /usr/local/bin/ \
&& curl -OL https://github.com/arq5x/lumpy-sv/releases/download/${LUMPY_VERSION}/lumpy-sv.tar.gz && tar -xzf lumpy-sv.tar.gz && rm lumpy-sv.tar.gz && cd lumpy-sv \
&& make && cp bin/* /usr/local/bin/. \
&& apt remove -y curl git && apt clean -y 
