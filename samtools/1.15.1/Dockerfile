FROM ubuntu:20.04
LABEL maintainer="Miguel Brown (brownm28@email.chop.edu)"

ENV SAMTOOLS_VERSION 1.15.1
ENV HTSLIB_VERSION 1.15.1
RUN apt update && apt install -y wget build-essential zlib1g-dev libncurses5-dev libbz2-dev liblzma-dev libcurl4-openssl-dev libssl-dev; \
wget -q https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2; \
tar xjvf samtools-${SAMTOOLS_VERSION}.tar.bz2; \
cd /samtools-${SAMTOOLS_VERSION}/ && ./configure && make; \
mv /samtools-${SAMTOOLS_VERSION}/samtools /bin/; \
cd htslib-${HTSLIB_VERSION}/ && ./configure && make; \
mv htsfile libhts.so* tabix bgzip /bin; \
rm -rf /samtools*; \
apt clean build-essential zlib1g-dev wget && apt -y  autoclean && apt -y autoremove
