FROM ubuntu:18.04
MAINTAINER Miguel Brown (brownm28@email.chop.edu)

ENV SAMTOOLS_VERSION 1.9
ENV BEDTOOLS_VERSION 2.27.0
ENV HTSLIB_VERSION 1.9
RUN apt update && apt install -y wget build-essential zlib1g-dev libncurses5-dev libbz2-dev liblzma-dev libcurl4-openssl-dev python; \
wget -q https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2; \
tar xjvf samtools-${SAMTOOLS_VERSION}.tar.bz2; \
cd /samtools-${SAMTOOLS_VERSION}/ && ./configure && make; \
mv /samtools-${SAMTOOLS_VERSION}/samtools /bin/; \
cd htslib-${HTSLIB_VERSION}/ && ./configure && make; \
mv htsfile libhts.so* tabix bgzip /bin; \
rm -rf /samtools*; \
cd / && wget -q https://github.com/arq5x/bedtools2/releases/download/v${BEDTOOLS_VERSION}/bedtools-${BEDTOOLS_VERSION}.tar.gz; \
tar -zxvf bedtools-${BEDTOOLS_VERSION}.tar.gz; cd bedtools2; make; \
mv bin/* /bin && cd / && rm -rf /bedtools*;\
apt clean build-essential zlib1g-dev wget && apt -y  autoclean && apt -y autoremove