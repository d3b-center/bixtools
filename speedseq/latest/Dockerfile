FROM ubuntu:16.04
MAINTAINER Miguel Brown (brownm28@email.chop.edu)

ENV SPEEDSEQ_VERSION latest

RUN apt update && apt install -y build-essential apt-utils autoconf git cmake python curl libz-dev libtbb-dev libncurses5-dev bsdmainutils gawk libbz2-dev liblzma-dev libcurl4-openssl-dev libssl-dev \
&& curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python get-pip.py && rm get-pip.py \
&& pip install numpy pysam scipy \
&& git clone --recursive https://github.com/hall-lab/speedseq && cd /speedseq \
&& curl -OL https://root.cern.ch/download/root_v6.14.02.Linux-ubuntu16-x86_64-gcc5.4.tar.gz && tar -xzf root_v6.14.02.Linux-ubuntu16-x86_64-gcc5.4.tar.gz && rm root_v6.14.02.Linux-ubuntu16-x86_64-gcc5.4.tar.gz \
&& rm -rf src/samtools-1.3.1 \
&& curl -OL https://github.com/samtools/samtools/releases/download/1.8/samtools-1.8.tar.bz2 && tar -xjf samtools-1.8.tar.bz2 && rm samtools-1.8.tar.bz2 && mv samtools-1.8 src/ \
&& cat Makefile | sed 's/1.3.1/1.8/' > temp && mv temp Makefile \
&& cat src/CNVnator/Makefile | sed 's/MathCore/MathCore -lcrypto -llzma -lbz2 -lcurl/' > temp && mv temp src/CNVnator/Makefile

ENV ROOTSYS /speedseq/root
ENV PATH /speedseq/root/bin:$PATH
ENV LD_LIBRARY_PATH /speedseq/root/lib
ENV DYLD_LIBRARY_PATH /speedseq/root/lib
ENV SHLIB_PATH /speedseq/root/lib
ENV LIBPATH /speedseq/root/lib
ENV MANPATH /speedseq/root/man
ENV PYTHONPATH /speedseq/root/lib
ENV CMAKE_PREFIX_PATH /speedseq/root/lib
ENV JUPYTER_PATH /speedseq/root/etc/notebook

RUN cd /speedseq && make sv \
&& cat /speedseq/bin/speedseq.config | sed 's/SAMTOOLS=/SAMTOOLS=\/speedseq\/src\/samtools-1.8\/samtools/' > temp && mv temp /speedseq/bin/speedseq.config \
&& apt remove -y curl git