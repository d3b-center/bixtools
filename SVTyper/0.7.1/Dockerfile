FROM ubuntu:18.04
LABEL maintainer="Miguel Brown (brownm28@email.chop.edu)"

ENV SVTYPER_VERSION 0.7.1
RUN apt update && apt install -y build-essential curl python python-pip libcurl4-openssl-dev libz-dev liblzma-dev libssl-dev libbz2-dev \
&& pip install pysam numpy==1.16.5 \
&& curl -OL https://github.com/hall-lab/svtyper/archive/v${SVTYPER_VERSION}.tar.gz && tar -xzf v${SVTYPER_VERSION}.tar.gz && rm v${SVTYPER_VERSION}.tar.gz \
&& pip install svtyper-${SVTYPER_VERSION}/ \
&& apt remove -y curl && apt clean -y 
