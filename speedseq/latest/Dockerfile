FROM ubuntu:16.04
MAINTAINER Miguel Brown (brownm28@email.chop.edu)

ENV SPEEDSEQ_VERSION latest

RUN apt update && apt install -y build-essential autoconf git cmake python curl libz-dev libtbb-dev libncurses5-dev wget software-properties-common
RUN add-apt-repository ppa:ubuntu-toolchain-r/test -y && apt update && apt install -y gcc-6 g++-6 && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-6 60 --slave /usr/bin/g++ g++ /usr/bin/g++-6
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python get-pip.py && rm get-pip.py
RUN pip install numpy pysam scipy

RUN git clone --recursive https://github.com/hall-lab/speedseq
WORKDIR /speedseq
RUN wget https://root.cern.ch/download/root_v6.12.06.Linux-ubuntu17-x86_64-gcc7.2.tar.gz && tar -xzf root_v6.12.06.Linux-ubuntu17-x86_64-gcc7.2.tar.gz && rm root_v6.12.06.Linux-ubuntu17-x86_64-gcc7.2.tar.gz

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
RUN apt remove -y wget curl software-properties-common