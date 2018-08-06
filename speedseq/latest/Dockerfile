FROM ubuntu:16.04
MAINTAINER Miguel Brown (brownm28@email.chop.edu)

ENV SPEEDSEQ_VERSION latest

RUN apt update && apt install -y build-essential autoconf git cmake python curl libz-dev libtbb-dev libncurses5-dev
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python get-pip.py && rm get-pip.py
RUN pip install numpy pysam scipy

RUN git clone --recursive https://github.com/hall-lab/speedseq
WORKDIR /speedseq
RUN curl -OL https://root.cern.ch/download/root_v6.14.02.Linux-ubuntu16-x86_64-gcc5.4.tar.gz && tar -xzf root_v6.14.02.Linux-ubuntu16-x86_64-gcc5.4.tar.gz && rm root_v6.14.02.Linux-ubuntu16-x86_64-gcc5.4.tar.gz

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