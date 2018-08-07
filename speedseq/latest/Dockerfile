FROM ubuntu:16.04
MAINTAINER Miguel Brown (brownm28@email.chop.edu)

ENV SPEEDSEQ_VERSION latest

RUN apt update && apt install -y build-essential autoconf git cmake python curl libz-dev libtbb-dev libncurses5-dev
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python get-pip.py && rm get-pip.py
RUN pip install numpy pysam scipy

RUN git clone --recursive https://github.com/hall-lab/speedseq
WORKDIR /speedseq
RUN curl -OL https://root.cern.ch/download/root_v6.14.02.Linux-ubuntu16-x86_64-gcc5.4.tar.gz && tar -xzf root_v6.14.02.Linux-ubuntu16-x86_64-gcc5.4.tar.gz && rm root_v6.14.02.Linux-ubuntu16-x86_64-gcc5.4.tar.gz
# Need to replace samtools in speedseq with newer version to properly handle input cram
RUN rm -rf src/samtools-1.3.1
RUN curl -OL https://github.com/samtools/samtools/archive/1.8.tar.gz && tar -xzf 1.8.tar.gz && rm 1.8.tar.gz && mv samtools-1.8 src/
# update Makefiles
RUN cat Makefile | sed 's/1.3.1/1.8/' > temp && mv temp Makefile
RUN cat src/CNVnator/Makefile | sed 's/MathCore/MathCore -lcrypto -llzma -lbz2 -lcurl/' > temp && mv temp src/CNVnator/Makefile

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

RUN make sv
RUN echo 'source /speedseq/root/bin/thisroot.sh' >> /speedseq/bin/speedseq.config
RUN apt remove -y curl