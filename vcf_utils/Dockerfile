FROM ubuntu:18.04
LABEL maintainer="Miguel Brown (brownm28@email.chop.edu)"

RUN apt update && apt install -y bcftools vcftools tabix git build-essential zlib1g-dev libbz2-dev liblzma-dev autoconf libcurl4-openssl-dev libssl-dev python3
RUN git clone https://github.com/atks/vt.git && cd vt && make -j8 && make test
RUN cd / && git clone --recursive https://github.com/vcflib/vcflib.git && cd vcflib && make -j8 && \
apt autoclean -y && apt remove git build-essential -y