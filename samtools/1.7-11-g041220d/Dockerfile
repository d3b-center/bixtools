FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
autoconf \
automake \
make \
g++ \
gcc \
build-essential \
zlib1g-dev \
libgsl0-dev \
libbz2-dev \
liblzma-dev \
python \
curl \
git \
cmake \
wget \
libncurses5-dev \
libncursesw5-dev

WORKDIR /opt

RUN git clone https://github.com/samtools/htslib.git 
WORKDIR /opt/htslib
RUN git checkout 53241915fa8b6a3e807f2ac85d8701f27a7fe528
RUN autoheader ; autoconf ; ./configure ; make ; make install

WORKDIR /opt/

RUN git clone https://github.com/samtools/samtools.git
WORKDIR /opt/samtools
RUN git checkout 041220db3e9e38966b2b5c1cbfdc688479710f68

RUN autoheader ; autoconf ; ./configure ; make ; make install

COPY Dockerfile /opt/
