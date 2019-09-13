FROM ubuntu:18.04
LABEL maintainer="Miguel Brown (brownm28@email.chop.edu)"

ENV BEDOPS_VERSION 2.4.36

RUN apt update && apt install -y wget tabix bedtools; \
wget -q https://github.com/bedops/bedops/releases/download/v2.4.36/bedops_linux_x86_64-v${BEDOPS_VERSION}.tar.bz2; \
mkdir BEDOPS_v${BEDOPS_VERSION}; \
tar -xjf bedops_linux_x86_64-v${BEDOPS_VERSION}.tar.bz2 --directory /BEDOPS_v${BEDOPS_VERSION};\
rm bedops_linux_x86_64-v${BEDOPS_VERSION}.tar.bz2; \
mv BEDOPS_v${BEDOPS_VERSION}/bin/* /usr/local/bin; \
rm -rf BEDOPS_v${BEDOPS_VERSION}; \
apt remove -y wget
