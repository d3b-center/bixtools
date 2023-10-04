FROM ubuntu:22.04
LABEL maintainer="Saksham Phul (phuls@chop.edu)"
LABEL description="RTG tool for benchmarking vcf files & bcftools to play with VCFs, pandarallel to speed up pandas dataframes"

ENV DEBIAN_FRONTEND noninteractive
ENV BCFTOOLS_VERSION 1.17
ENV RTG_VERSION 3.12.1
ENV HTSLIB_VERSION 1.17

RUN apt update && apt upgrade -y && apt install default-jre wget unzip apache2 ant git -y && apt install build-essential libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev software-properties-common -y && add-apt-repository ppa:deadsnakes/ppa -y && apt install python3.11-distutils curl python3.11 -y && curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11 && python3.11 -m pip install pandas && wget https://github.com/RealTimeGenomics/rtg-tools/archive/refs/tags/${RTG_VERSION}.tar.gz -O - | tar -xz && cd rtg-tools-${RTG_VERSION} && ant zip-nojre && mkdir /home/RTG && cd /home/RTG/ && unzip /rtg-tools-${RTG_VERSION}/dist/rtg-tools-${RTG_VERSION}-*zip

RUN apt install -y bzip2 liblzma-dev && curl -SL https://github.com/samtools/bcftools/releases/download/${BCFTOOLS_VERSION}/bcftools-${BCFTOOLS_VERSION}.tar.bz2 | tar -jx  && cd bcftools-${BCFTOOLS_VERSION} && sh configure --prefix=/home && make && make install && apt install python3.11-dev -y && python3.11 -m pip install -U psutil pandarallel matplotlib

RUN curl -SL https://github.com/samtools/htslib/releases/download/${HTSLIB_VERSION}/htslib-${HTSLIB_VERSION}.tar.bz2 | tar -jx  && cd htslib-${HTSLIB_VERSION} && sh configure --prefix=/home && make && make install

RUN apt-get remove unzip git wget curl tar -y

ENV PATH=$PATH:"/home/RTG/rtg-tools-${RTG_VERSION}-unknown/"
ENV PATH=$PATH:"/home/bin/"
ENV PATH=$PATH:"/home/htslib-${HTSLIB_VERSION}/build/bin"
ENV BCFTOOLS_PLUGINS="/home/bcftools-${BCFTOOLS_VERSION}/plugins"

#run rtg to config, only required for 1st run
RUN rtg --help

COPY Dockerfile .
