FROM ubuntu:20.04
LABEL maintainer="Saksham Phul (phuls@chop.edu)"
LABEL description="Install gcc, bcftools with plugins, python 3.10, pandas, g++, cmake, bam-readcount for LOH app"

WORKDIR home/

ENV BCFTOOLS_VERSION 1.16
ENV BAM_READCOUNT_VERSION 1.0.1
ENV SAMTOOL_VERSION 1.17
ENV HTSLIB_VERSION 1.17
RUN apt update && apt upgrade -y && \
        apt install -y software-properties-common -y && add-apt-repository ppa:deadsnakes/ppa

#apt install cannot be combined, need to link repo to OS to find required packages
RUN apt install -y curl gcc make liblzma-dev zlib1g-dev libbz2-dev wget python3.10 python3.10-distutils bzip2 g++ cmake git && \
	curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10  && \
	update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1 && \
        curl -SL https://github.com/samtools/bcftools/releases/download/${BCFTOOLS_VERSION}/bcftools-${BCFTOOLS_VERSION}.tar.bz2 | tar -jx && \
	cd bcftools-${BCFTOOLS_VERSION} && \
        sh configure --prefix=/home && \
        make && make install && \
        python3 -m pip install regex pandas && \
	cd ../ && \
	curl -SL https://github.com/genome/bam-readcount/archive/refs/tags/v1.0.1.tar.gz | tar -xz && \
	cd bam-readcount-${BAM_READCOUNT_VERSION} && \
	mkdir build && cd build && \
	cmake .. && make && \
	cp /home/bam-readcount-${BAM_READCOUNT_VERSION}/build/bin/bam-readcount /home/bin/ && \
	cd ../

RUN curl -SL https://github.com/samtools/htslib/releases/download/${HTSLIB_VERSION}/htslib-${HTSLIB_VERSION}.tar.bz2 | tar -jx && \
	cd htslib-${HTSLIB_VERSION} && sh configure --prefix=/home && make && make install && \
	curl -SL https://github.com/samtools/samtools/releases/download/${SAMTOOL_VERSION}/samtools-${SAMTOOL_VERSION}.tar.bz2 | tar -jx && \
	cd samtools-${SAMTOOL_VERSION} && sh configure --prefix=/home --without-curses && make && make install

ENV PATH=$PATH:"/home/bin/"
ENV PATH=$PATH:"/home/ubuntu/tools/htslib-${HTSLIB_VERSION}/build/bin/"
ENV PATH=$PATH:"/home/ubuntu/tools/samtools-${SAMTOOL_VERSION}/build/bin/"
ENV BCFTOOLS_PLUGINS="/home/bcftools-${BCFTOOLS_VERSION}/plugins"

COPY Dockerfile .
