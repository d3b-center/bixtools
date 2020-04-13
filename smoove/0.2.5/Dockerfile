FROM ubuntu:18.04
LABEL maintainer="Miguel Brown (brownm28@email.chop.edu)"
LABEL description="Custom build of smoove from https://github.com/brentp/smoove/releases for control/consistency in sw versions"

ENV LUMPY_VERSION 0.3.0
ENV SAMTOOLS_VERSION 1.9
ENV SVTYPER_VERSION 0.7.1
ENV SMOOVE_VERSION 0.2.5
ENV GSORT_VERSION 0.1.3
ENV MOSDEPTH_VERSION 0.2.6
ENV DUPHOLD_VERSION 0.2.1
ENV SAMBAMBA_VERSION 0.6.7
ENV SAMBLASTER_VERSION 0.1.24

RUN apt update && apt install -y build-essential git cmake curl zip python python-pip tabix gawk autoconf libcurl4-openssl-dev libz-dev liblzma-dev libssl-dev bsdmainutils libncurses5-dev libbz2-dev bcftools
RUN pip install cython
RUN pip install pysam numpy==1.16.5
RUN curl -OL https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2 && tar -xjf samtools-${SAMTOOLS_VERSION}.tar.bz2 && rm samtools-${SAMTOOLS_VERSION}.tar.bz2 \
&& cd /samtools-${SAMTOOLS_VERSION} && ./configure && make && make install
RUN cd / && curl -OL https://github.com/GregoryFaust/samblaster/releases/download/v.${SAMBLASTER_VERSION}/samblaster-v.${SAMBLASTER_VERSION}.tar.gz && tar -xzf samblaster-v.${SAMBLASTER_VERSION}.tar.gz && cd samblaster-v.${SAMBLASTER_VERSION} && make && cp samblaster /usr/local/bin/. && cd / && rm -rf samblaster-v.${SAMBLASTER_VERSION}.tar.gz
RUN curl -OL https://github.com/biod/sambamba/releases/download/v${SAMBAMBA_VERSION}/sambamba_v${SAMBAMBA_VERSION}_linux.tar.bz2 && tar -xjf sambamba_v${SAMBAMBA_VERSION}_linux.tar.bz2 && rm sambamba_v${SAMBAMBA_VERSION}_linux.tar.bz2 && mv ./sambamba /usr/local/bin/
RUN curl -OL https://github.com/arq5x/lumpy-sv/releases/download/${LUMPY_VERSION}/lumpy-sv.tar.gz && tar -xzf lumpy-sv.tar.gz && rm lumpy-sv.tar.gz && cd lumpy-sv \
&& make && cp bin/* /usr/local/bin/.
RUN cd / && curl -OL https://github.com/hall-lab/svtyper/archive/v${SVTYPER_VERSION}.tar.gz && tar -xzf v${SVTYPER_VERSION}.tar.gz && rm v${SVTYPER_VERSION}.tar.gz \
&& pip install svtyper-${SVTYPER_VERSION}/
RUN curl -OL https://github.com/brentp/gsort/releases/download/v${GSORT_VERSION}/gsort_linux_amd64 && chmod 755 gsort_linux_amd64 && mv gsort_linux_amd64 /usr/local/bin/gsort \
&& curl -OL https://github.com/brentp/mosdepth/releases/download/v${MOSDEPTH_VERSION}/mosdepth && chmod 755 mosdepth && mv mosdepth /usr/local/bin/ \
&& curl -OL https://github.com/brentp/duphold/releases/download/v0.2.1/duphold && chmod 755 duphold && mv duphold /usr/local/bin/ \
&& curl -OL https://github.com/brentp/smoove/releases/download/v${SMOOVE_VERSION}/smoove && chmod 755 smoove && mv smoove /usr/local/bin/
RUN apt remove -y curl git zip && apt clean -y 
