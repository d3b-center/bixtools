FROM ubuntu:18.04

RUN apt update && apt install -y --no-install-recommends \
  ca-certificates \
  g++ \
  libbz2-dev \
  libcurl3-dev \
  libfreetype6-dev \
  liblzma-dev \
  libncurses5-dev \
  libreadline-dev \
  libpython2.7 \
  libz-dev \
  make \
  python-matplotlib \
  python-scipy \
  python-tk \
  curl \
 && rm -rf /var/lib/apt/lists/*

RUN curl https://root.cern/download/root_v6.18.04.Linux-ubuntu18-x86_64-gcc7.4.tar.gz | \
 tar -C /opt -xzf -

ENV PYTHONPATH=/opt/root/lib

RUN echo '/opt/root/lib' > /etc/ld.so.conf.d/root.conf \
 && ldconfig

ENV SAMTOOLS_VERSION=1.9 \
    CNVNATOR_VERSION=v0.4.1

RUN curl -L https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2 | \
 tar -C /tmp -xjf - \
 && cd /tmp/samtools-* \
 && make \
 && (cd htslib-* && make mostlyclean) \
 && make mostlyclean \
 && find /tmp -name test -type d -exec rm -rf {} +

RUN curl -L https://github.com/abyzovlab/CNVnator/archive/refs/tags/${CNVNATOR_VERSION}.tar.gz | \
 tar -C /tmp -xzf - \ 
 && cd /tmp/CNVnator-* \
 && curl -O https://raw.githubusercontent.com/abyzovlab/CNVnator/1590eedf921552e0463de43cabc3a388af5ab549/Makefile \ 
 && ln -s /tmp/samtools-* samtools \
 && ROOTSYS=/opt/root make \
 && mv cnvnator *.py *.pl /usr/local/bin \
 && mv pytools /usr/local/lib/python*/dist-packages \
 && cd - \
 && rm -rf /tmp/*
