FROM ubuntu:18.04
LABEL maintainer="Miguel Brown (brownm28@email.chop.edu)"

ENV VEP_VERSION=94
ENV SNPEFF_VERSION 4_3t
ENV ANNOVAR_VERSION 20180416
ENV HTSLIB_VERSION 1.9
ENV LOFTEE_VERSION 1.0.2
ENV WGSA_DIR /WGSA

RUN apt update -y && apt upgrade -y && apt install git apt-utils cpanminus build-essential automake mysql-client curl libssl-dev wget openssl libexpat1-dev libmysqlclient-dev unzip wget openjdk-11-jdk zlib1g-dev libncurses5-dev libbz2-dev liblzma-dev libcurl4-openssl-dev -y
RUN cpanm --notest LWP::Simple DBI DBD::mysql Archive::Zip Archive::Extract HTTP::Tiny Test::Simple File::Copy::Recursive Perl::OSType Module::Metadata version TAP::Harness CGI Encode CPAN::Meta JSON DBD::SQLite Set::IntervalTree Archive::Tar Time::HiRes Module::Build Bio::Root::Version
RUN mkdir ${WGSA_DIR} 
RUN cd ${WGSA_DIR} && mkdir htslib && cd htslib && wget https://github.com/samtools/htslib/releases/download/1.9/htslib-1.9.tar.bz2 && tar -xjf htslib-${HTSLIB_VERSION}.tar.bz2 && rm htslib-${HTSLIB_VERSION}.tar.bz2 \
&& cd htslib-${HTSLIB_VERSION} && make prefix=/usr/ install
RUN cd ${WGSA_DIR} && mkdir vep && cd vep && git clone https://github.com/Ensembl/ensembl-vep.git && cd ensembl-vep && git checkout release/${VEP_VERSION} \
&& perl INSTALL.pl --NO_TEST --NO_UPDATE --AUTO ap --PLUGINS LoF --CACHEDIR ${WGSA_DIR}/.vep
RUN cd /${WGSA_DIR}/.vep/Plugins && rm * && wget https://github.com/konradjk/loftee/archive/v${LOFTEE_VERSION}.zip && unzip -oj v${LOFTEE_VERSION}.zip && rm v${LOFTEE_VERSION}.zip 
RUN cd /WGSA && mkdir snpeff && cd snpeff && wget -q https://sourceforge.net/projects/snpeff/files/snpEff_v${SNPEFF_VERSION}_core.zip/download
RUN cd ${WGSA_DIR} && mkdir annovar${ANNOVAR_VERSION} && cd annovar${ANNOVAR_VERSION} && wget -q http://www.openbioinformatics.org/annovar/download/0wgxR2rIVP/annovar.latest.tar.gz && tar -zxf annovar.latest.tar.gz && rm annovar.latest.tar.gz
RUN cd ${WGSA_DIR} && wget http://web.corral.tacc.utexas.edu/WGSAdownload/WGSA08.class \
&& apt remove curl wget git -y && apt autoclean -y &&  apt autoremove -y
