FROM ubuntu:20.04
LABEL maintainer="Saksham Phul (phuls@chop.edu)"
LABEL description="Install gcc, bcftools with plugins, python 3.10, pandas, pysam"

WORKDIR home/

RUN apt update && apt upgrade -y && \
        apt install -y software-properties-common -y && add-apt-repository ppa:deadsnakes/ppa

#apt install cannot be combined, need to link repo to OS to find required packages
RUN apt install -y curl gcc make liblzma-dev zlib1g-dev libbz2-dev wget python3.10 python3.10-distutils bzip2 && \
	curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10  && \
	update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1 && \
        wget https://github.com/samtools/bcftools/releases/download/1.16/bcftools-1.16.tar.bz2 && \
        tar -axf bcftools-1.16.tar.bz2 && \
        rm bcftools-1.16.tar.bz2 && \
	cd bcftools-1.16 && \
        sh configure --prefix=/home && \
        make && make install && \
        python3 -m pip install pysam regex pandas
 
ENV PATH="$PATH:/home/bin/"
ENV BCFTOOLS_PLUGINS="/home/bcftools-1.16/plugins"

ADD Dockerfile .
