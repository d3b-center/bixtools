FROM ubuntu:20.04

# Get all apt dependencies
RUN apt-get -y update
RUN apt-get -y install software-properties-common
RUN apt-get install -y --no-install-recommends apt-utils
RUN add-apt-repository -y ppa:ubuntu-toolchain-r/test
RUN apt-get -y install \
    gcc-8 g++-8 \
    build-essential \
    make \
    wget \
    autotools-dev \
    libicu-dev \
    git \
    curl \
    libcurl4-openssl-dev \
    pkg-config \
    autoconf \
    libbz2-dev \
    liblzma-dev \
    zlib1g-dev \
    openssl \
    libssl-dev \
    libgmp3-dev \
    libcrypto++-dev
ENV CC gcc-8
ENV CXX g++-8

# Install CMake
RUN cd /tmp \
    && curl -L https://cmake.org/files/v3.11/cmake-3.11.4.tar.gz | tar -xzv \
    && cd cmake-3.11.4 \
    && ./bootstrap --prefix=/usr/local \
    && make -j$(nproc) \
    && make install

# Install Boost
RUN cd /tmp \
    && curl -L http://sourceforge.net/projects/boost/files/boost/1.68.0/boost_1_68_0.tar.gz/download | tar -xzv \
    && cd boost_1_68_0 \
    && ./bootstrap.sh --prefix=/usr/local --without-libraries=python,mpi \
    && ./b2 -j$(nproc) toolset=gcc-8 cxxflags="-std=c++14" \
    && ./b2 install

# Install htslib
ENV HTSLIB_VERSION 1.10.2
RUN cd /tmp \
    && git clone --recursive -b $HTSLIB_VERSION https://github.com/samtools/htslib.git \
    && cd htslib \
    && autoheader \
    && autoconf \
    && ./configure \
    && make -j$(nproc) \
    && make install

# Install Octopus
ENV OCTOPUS_VERSION v0.6.3-beta
RUN cd /tmp \
    && git clone -b ${OCTOPUS_VERSION} https://github.com/luntergroup/octopus.git \
    && cd octopus \
    && ./scripts/install.py --threads=$(nproc) \
    && ldconfig \
    && cp /bin/octopus /usr/bin

WORKDIR /

COPY Dockerfile .
