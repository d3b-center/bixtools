FROM ubuntu:18.04
LABEL maintainer="Miguel Brown (brownm28@chop.edu)"

ENV VEP_VERSION=93.7

RUN apt update -y && apt upgrade -y && apt install -y build-essential git cpanminus curl wget unzip automake samtools tabix libmysqlclient-dev libncurses5-dev zlib1g-dev libgsl0-dev libexpat1-dev libgd-dev pigz\
&& cpanm --notest LWP::Simple DBI DBD::mysql Archive::Zip Archive::Extract HTTP::Tiny Test::Simple File::Copy::Recursive Perl::OSType Module::Metadata version TAP::Harness CGI Encode CPAN::Meta JSON DBD::SQLite Set::IntervalTree Archive::Tar Time::HiRes Module::Build Bio::Root::Version \
&& wget -q https://github.com/Ensembl/ensembl-vep/archive/release/${VEP_VERSION}.tar.gz && tar -xzf ${VEP_VERSION}.tar.gz && rm ${VEP_VERSION}.tar.gz && cd ensembl-vep-release-${VEP_VERSION} \
&& perl INSTALL.pl --NO_TEST --NO_UPDATE --AUTO ap --PLUGINS LoF --CACHEDIR cache && cd cache \
&& wget -q https://raw.githubusercontent.com/konradjk/loftee/v0.3-beta/splice_module.pl && cd / \
&& apt remove curl wget -y && apt autoclean -y &&  apt autoremove -y
