FROM ubuntu:18.04 AS build-env
MAINTAINER Miguel Browm (brownm28@email.chop.edu)


ENV STAR_VERSION 2.6.1d
ENV STAR_FUSION_VERSION 1.5.0
ENV SAMTOOLS_VERSION 1.9
ENV HTSLIB_VERSION 1.9

RUN apt-get update; \
apt-get install --yes wget build-essential libgomp1 libz-dev zlib1g-dev libncurses5-dev libbz2-dev liblzma-dev libcurl4-openssl-dev libdb-dev; \
apt-get clean; \
wget -O - http://cpanmin.us | perl - --self-upgrade; \
cpanm DB_File URI::Escape Set::IntervalTree Carp::Assert JSON::XS PerlIO::gzip; \
cd /usr/local && wget -q https://github.com/alexdobin/STAR/archive/${STAR_VERSION}.tar.gz; \
tar -zxf ${STAR_VERSION}.tar.gz; \
mv STAR-${STAR_VERSION}/bin/Linux_x86_64_static/STAR /usr/local/bin/STAR; \
wget -q https://github.com/STAR-Fusion/STAR-Fusion/releases/download/STAR-Fusion-v${STAR_FUSION_VERSION}/STAR-Fusion-v${STAR_FUSION_VERSION}.FULL.tar.gz; \
tar -xzf STAR-Fusion-v${STAR_FUSION_VERSION}.FULL.tar.gz; \
mv STAR-Fusion-v${STAR_FUSION_VERSION} STAR-Fusion; \
rm STAR-Fusion-v${STAR_FUSION_VERSION}.FULL.tar.gz && rm ${STAR_VERSION}.tar.gz; \
cd /; \
wget -q https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2; \
tar xjf samtools-${SAMTOOLS_VERSION}.tar.bz2; \
cd /samtools-${SAMTOOLS_VERSION}/ && ./configure && make; \
mv /samtools-${SAMTOOLS_VERSION}/samtools /bin/; \
cd htslib-${HTSLIB_VERSION}/ && ./configure && make; \
mv htsfile libhts.so* tabix bgzip /bin; \
rm -rf /samtools*; \
apt clean build-essential zlib1g-dev wget && apt -y  autoclean && apt -y autoremove
