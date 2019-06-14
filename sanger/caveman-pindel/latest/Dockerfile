FROM ubuntu:18.04
LABEL maintainer="Miguel Brown (brownm28@email.chop.edu)"

ENV SAMTOOLS_VERSION=1.9
ENV HTSLIB_VERSION=1.9
ENV CAVEMAN_VERSION=1.13.15
ENV PINDEL_VERSION=0.2.5b9
ENV PINDEL_COMMIT=70c1bb4a75503da39e206e02178fe3d8a0afdf81
ENV CGP_VCF_VERSION=2.2.1
ENV CGP_POST_PROCESS_VERSION=1.8.8
ENV LD_LIBRARY_PATH=/samtools-1.9/htslib-1.9
ENV BEDTOOLS_VERSION=2.21.0
ENV PATH="/usr/local/bin/cgpVcf-${CGP_VCF_VERSION}/bin:${PATH}"
ENV PERL5LIB="/usr/local/bin/cgpVcf-${CGP_VCF_VERSION}/lib/perl5${PERL5LIB}"

RUN apt update && apt install -y wget build-essential zlib1g-dev libncurses5-dev libbz2-dev liblzma-dev libcurl4-openssl-dev libexpat1-dev pkg-config libgd-gd2-perl curl cpanminus python && \
wget -q https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2; \
tar xjvf samtools-${SAMTOOLS_VERSION}.tar.bz2 && rm samtools-${SAMTOOLS_VERSION}.tar.bz2 && \
cd /samtools-${SAMTOOLS_VERSION}/ && ./configure && make && make install && \
cd htslib-${HTSLIB_VERSION}/ && ./configure && make && make install && \
cd / && wget -q https://github.com/cancerit/CaVEMan/archive/${CAVEMAN_VERSION}.tar.gz
RUN tar -xzf ${CAVEMAN_VERSION}.tar.gz && rm ${CAVEMAN_VERSION}.tar.gz && cd CaVEMan-${CAVEMAN_VERSION} && make && cd / && \
wget -q https://github.com/genome/pindel/archive/${PINDEL_COMMIT}.tar.gz && tar -xzf ${PINDEL_COMMIT}.tar.gz && rm ${PINDEL_COMMIT}.tar.gz && \
mv pindel-${PINDEL_COMMIT} pindel-${PINDEL_VERSION} && cd pindel-${PINDEL_VERSION} && ./INSTALL $LD_LIBRARY_PATH && \
cpanm --notest Bio::DB::HTS && cd / && \
wget -q  https://github.com/cancerit/cgpVcf/archive/v${CGP_VCF_VERSION}.tar.gz && tar -xzf v${CGP_VCF_VERSION}.tar.gz && rm v${CGP_VCF_VERSION}.tar.gz && cd cgpVcf-${CGP_VCF_VERSION} && \
./setup.sh /usr/local/bin/cgpVcf-${CGP_VCF_VERSION} && cd /
RUN wget -q https://github.com/arq5x/bedtools2/releases/download/v${BEDTOOLS_VERSION}/bedtools-${BEDTOOLS_VERSION}.tar.gz && tar -xzf bedtools-${BEDTOOLS_VERSION}.tar.gz && rm bedtools-${BEDTOOLS_VERSION}.tar.gz && cd bedtools2 && \
make && cp bin/* /usr/local/bin && cd / && \
wget -q https://github.com/cancerit/cgpCaVEManPostProcessing/archive/${CGP_POST_PROCESS_VERSION}.tar.gz && tar -xzf ${CGP_POST_PROCESS_VERSION}.tar.gz && rm ${CGP_POST_PROCESS_VERSION}.tar.gz && cd cgpCaVEManPostProcessing-${CGP_POST_PROCESS_VERSION} && \
./setup.sh /usr/local/bin/cgpVcf-${CGP_VCF_VERSION} && \
apt autoclean