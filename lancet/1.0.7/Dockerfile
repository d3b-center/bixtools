FROM ubuntu:18.04
LABEL maintainer="Miguel Brown (brownm28@email.chop.edu)"

ENV LANCET_VERSION 1.0.7
RUN apt update && apt install -y wget build-essential zlib1g-dev libbz2-dev liblzma-dev libcurl4-openssl-dev cmake libcrypto++-dev libbamtools-dev libssl-dev; \
wget https://github.com/nygenome/lancet/archive/v${LANCET_VERSION}.tar.gz && tar -xzf v${LANCET_VERSION}.tar.gz && rm v${LANCET_VERSION}.tar.gz && cd lancet-${LANCET_VERSION}; \
make; \
apt remove -y build-essential libncurses5-dev libbz2-dev liblzma-dev libcurl4-gnutls-dev libcrypto++-dev libbamtools-dev libssl-dev;