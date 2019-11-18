FROM ubuntu:16.04
LABEL maintainer="Miguel Brown (brownm28@email.chop.edu)"

ENV LUMPY_VERSION 0.2.13
ADD lumpyexpress_mod /lumpyexpress_mod
RUN apt update && apt install -y build-essential git cmake curl python python-pip gawk autoconf libcurl4-openssl-dev libz-dev liblzma-dev libssl-dev bsdmainutils libncurses5-dev libbz2-dev \
&& pip install pysam numpy==1.16.5 \
&& curl -OL https://github.com/samtools/samtools/releases/download/1.8/samtools-1.8.tar.bz2 && tar -xjf samtools-1.8.tar.bz2 && rm samtools-1.8.tar.bz2 \
&& cd /samtools-1.8 && ./configure && make && make install \
&& cd / && git clone https://github.com/GregoryFaust/samblaster && cd samblaster && make && cp samblaster /usr/local/bin/. && cd / && rm -rf samblaster \
&& curl -OL https://github.com/biod/sambamba/releases/download/v0.6.7/sambamba_v0.6.7_linux.tar.bz2 && tar -xjf sambamba_v0.6.7_linux.tar.bz2 && rm sambamba_v0.6.7_linux.tar.bz2 && mv ./sambamba /usr/local/bin/ \
&& curl -OL https://github.com/arq5x/lumpy-sv/releases/download/${LUMPY_VERSION}/lumpy-sv-v${LUMPY_VERSION}.tar.gz && tar -xzf lumpy-sv-v${LUMPY_VERSION}.tar.gz && rm lumpy-sv-v${LUMPY_VERSION}.tar.gz && mv lumpy-sv-v${LUMPY_VERSION} lumpy-sv && cd lumpy-sv \
&& make && mv /lumpyexpress_mod bin/lumpyexpress && chmod 755 bin/lumpyexpress && cp bin/* /usr/local/bin/. \
&& apt remove -y curl && apt autoclean -y  && apt autoremove -y
