FROM ubuntu:22.04
LABEL maintainer="Saksham Phul (phuls@chop.edu)"

WORKDIR home/

RUN apt update && apt upgrade -y && \
        apt install -y gcc make liblzma-dev zlib1g-dev libbz2-dev wget python3.10 bzip2 pip && \
        wget https://github.com/samtools/bcftools/releases/download/1.16/bcftools-1.16.tar.bz2 && \
        tar -axf bcftools*.tar.bz2 && rm bcftools*.tar.bz2 && bash && \
        cd bcftools-1.16 && \
#	apt install -y gcc make liblzma-dev zlib1g-dev libbz2-dev && \
        sh configure --prefix=/home && \
        make && make install && \
        python3 -m pip install pysam regex pandas


ENV PATH="$PATH:/home/bin/"
ENV BCFTOOLS_PLUGINS="/home/bcftools-1.16/plugins"

ADD Dockerfile .
