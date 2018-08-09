FROM ubuntu:16.04
MAINTAINER Miguel Brown (brownm28@email.chop.edu)

ENV VEP_VERSION r93

RUN apt update -y && apt upgrade -y && apt install git cpanminus build-essential mysql-client curl libssl-dev wget openssl libmysqlclient-dev unzip wget -y \
&& cpanm -n install DBI DBD::mysql Set::IntervalTree JSON PerlIO::gzip Bio::Root::Version \
&& git clone https://github.com/Ensembl/ensembl-vep.git && cd ensembl-vep && git checkout release/93 \
&& perl INSTALL.pl --NO_TEST --NO_UPDATE --AUTO a \
&& apt remove curl wget git -y && apt autoclean &&  apt autoremove