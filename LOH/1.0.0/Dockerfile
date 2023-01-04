FROM ubuntu:22.04
LABEL maintainer="Saksham Phul (phuls@chop.edu)"
LABEL description="Install gcc, bcftools with plugins, python 3.10, pandas, pysam"

WORKDIR home/

RUN apt update && apt upgrade -y && \
        apt install -y gcc make liblzma-dev zlib1g-dev libbz2-dev wget python3.10 bzip2 pip && \
        wget https://github.com/samtools/bcftools/releases/download/1.16/bcftools-1.16.tar.bz2 && \
        tar -axf bcftools*.tar.bz2 && \
        rm bcftools-1.16.tar.bz2 && \
	cd bcftools-1.16 && \
        sh configure --prefix=/home && \
        make && make install && \
        python3 -m pip install pysam regex pandas


ENV PATH="$PATH:/home/bin/"
ENV BCFTOOLS_PLUGINS="/home/bcftools-1.16/plugins"

ADD Dockerfile .
