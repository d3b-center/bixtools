FROM migbro/star:2.7.10a AS build-env
LABEL maintainer="Miguel Browm (brownm28@email.chop.edu)"
LABEL description="Creates docker for STAR Fusion using some commands from  \
https://github.com/STAR-Fusion/STAR-Fusion/blob/master/Docker/Dockerfile, leverages existing STAR docker"

ENV STAR_VERSION 2.7.10a
ENV STAR_FUSION_VERSION 1.10.1
ENV SAMTOOLS_VERSION 1.9
ENV HTSLIB_VERSION 1.9
ENV BLAST_VERSION 2.9.0
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update; \
apt install --yes wget pigz build-essential libgomp1 libz-dev zlib1g-dev libncurses5-dev libbz2-dev liblzma-dev libcurl4-openssl-dev libdb-dev littler libxml2-dev libssl-dev \
&& apt clean
RUN wget -O - http://cpanmin.us | perl - --self-upgrade; \
cpanm DB_File URI::Escape Set::IntervalTree Carp::Assert JSON::XS PerlIO::gzip
RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${BLAST_VERSION}/ncbi-blast-${BLAST_VERSION}+-x64-linux.tar.gz && \
    tar xvf ncbi-blast-${BLAST_VERSION}+-x64-linux.tar.gz && \
        cp ncbi-blast-${BLAST_VERSION}+/bin/* /usr/local/bin/ && \
        rm ncbi-blast-${BLAST_VERSION}+-x64-linux.tar.gz
RUN wget http://eddylab.org/software/hmmer3/3.1b2/hmmer-3.1b2-linux-intel-x86_64.tar.gz && \
    tar xvf hmmer-3.1b2-linux-intel-x86_64.tar.gz && \
        cp hmmer-3.1b2-linux-intel-x86_64/binaries/* /usr/local/bin/ && \
        rm hmmer-3.1b2-linux-intel-x86_64.tar.gz
RUN wget https://dfam.org/releases/Dfam_3.1/infrastructure/dfamscan.pl.gz && \
     gunzip dfamscan.pl.gz && \
     chmod 755 dfamscan.pl && \
     mv dfamscan.pl /usr/local/bin
RUN wget https://github.com/broadinstitute/picard/releases/download/2.20.3/picard.jar && mv picard.jar /usr/local/bin/
RUN Rscript -e 'install.packages(c("ranger", "tidyverse"))'
RUN wget -q https://github.com/STAR-Fusion/STAR-Fusion/releases/download/STAR-Fusion-v${STAR_FUSION_VERSION}/STAR-Fusion.v${STAR_FUSION_VERSION}.tar.gz; \
tar -xzf STAR-Fusion.v${STAR_FUSION_VERSION}.tar.gz; \
mv STAR-Fusion.v${STAR_FUSION_VERSION} STAR-Fusion \
&& cd STAR-Fusion && make \
&& rm STAR-Fusion.v${STAR_FUSION_VERSION}.tar.gz; \
cd /; \
wget -q https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2; \
tar xjf samtools-${SAMTOOLS_VERSION}.tar.bz2; \
cd /samtools-${SAMTOOLS_VERSION}/ && ./configure && make; \
mv /samtools-${SAMTOOLS_VERSION}/samtools /bin/; \
cd htslib-${HTSLIB_VERSION}/ && ./configure && make; \
mv htsfile libhts.so* tabix bgzip /bin; \
rm -rf /samtools*; \
apt clean build-essential zlib1g-dev wget && apt -y autoclean && apt -y autoremove

ADD Dockerfile .