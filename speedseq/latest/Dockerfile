FROM ubuntu:16.04
MAINTAINER Miguel Brown (brownm28@email.chop.edu)

ENV SPEEDSEQ_VERSION latest

RUN apt update && apt install -y build-essential autoconf git cmake python curl libz-dev libtbb-dev libncurses5-dev wget
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python get-pip.py && rm get-pip.py
RUN pip install numpy pysam scipy
RUN git clone --recursive https://github.com/hall-lab/speedseq
WORKDIR /speedseq
RUN wget https://root.cern.ch/download/root_v6.12.06.Linux-ubuntu17-x86_64-gcc7.2.tar.gz && tar -xzf root_v6.12.06.Linux-ubuntu17-x86_64-gcc7.2.tar.gz && rm root_v6.12.06.Linux-ubuntu17-x86_64-gcc7.2.tar.gz
RUN source root/bin/thisroot.sh
RUN make sv
RUN apt remove -y wget curl