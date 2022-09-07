FROM ubuntu:18.04
LABEL maintainer="Daniel Miller <millerd15@email.chop.edu>"

ENV SVABA_VERSION 1.1.0

RUN apt update && \
    apt upgrade -y && \
    apt install -y make gcc g++ && \
    apt install -y build-essential zlib1g-dev libbz2-dev liblzma-dev ncurses-dev && \
    apt install -y git wget bzip2 libdigest-md5-perl

RUN git clone --recursive -b ${SVABA_VERSION} https://github.com/walaj/svaba.git && \
    cd svaba && \
    ./configure && \
    make && \
    make install

RUN wget -O /svaba/bin/seq_cache_populate.pl https://raw.githubusercontent.com/samtools/samtools/1.16/misc/seq_cache_populate.pl && chmod 777 /svaba/bin/seq_cache_populate.pl

ENV PATH "$PATH:/svaba/bin"

RUN apt remove git wget bzip2 -y && apt autoclean -y && apt autoremove -y
