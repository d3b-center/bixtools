FROM ubuntu:18.04
label maintainer="Miguel Brown (brownm28@email.chop.edu)"

ENV VEP_VERSION=93
ENV MAF_VERSION=1.6.16

RUN apt update -y && apt upgrade -y && apt install -y  build-essential git cpanminus curl wget unzip automake samtools tabix libmysqlclient-dev libncurses5-dev zlib1g-dev libgsl0-dev libexpat1-dev libgd-dev\
&& cpanm --notest LWP::Simple DBI DBD::mysql Archive::Zip Archive::Extract HTTP::Tiny Test::Simple File::Copy::Recursive Perl::OSType Module::Metadata version TAP::Harness CGI Encode CPAN::Meta JSON DBD::SQLite Set::IntervalTree Archive::Tar Time::HiRes Module::Build Bio::Root::Version \
&& git clone https://github.com/Ensembl/ensembl-vep.git && cd ensembl-vep && git checkout release/${VEP_VERSION} \
&& perl INSTALL.pl --NO_TEST --NO_UPDATE --AUTO ap --PLUGINS LoF --CACHEDIR cache && cd /ensembl-vep/cache \
&& wget -q https://raw.githubusercontent.com/konradjk/loftee/v0.3-beta/splice_module.pl && cd / \
&& wget https://github.com/mskcc/vcf2maf/archive/v${MAF_VERSION}.tar.gz && tar -xzf v${MAF_VERSION}.tar.gz && rm v${MAF_VERSION}.tar.gz && mv vcf2maf-${MAF_VERSION} vcf2maf \
&& apt remove curl wget git -y && apt autoclean -y &&  apt autoremove -y