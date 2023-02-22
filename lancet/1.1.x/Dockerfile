FROM ubuntu:20.04
LABEL maintainer="Daniel Miller (millerd15@chop.edu)"

ENV DEBIAN_FRONTEND=noninteractive
ENV LANCET_COMMIT=b6c90672edb181a39687d9f4d31f3b9a09364655

RUN apt-get update && apt-get install -y git g++ cmake liblzma-dev zlib1g-dev libbz2-dev libcurl3-dev libssl-dev

WORKDIR /opt

RUN git clone --recursive https://github.com/nygenome/lancet && cd lancet && git checkout $LANCET_COMMIT && make all -j$(nproc) && make lancet -j$(nproc) && cp /opt/lancet/lancet /usr/local/bin

ENV PATH $PATH:/lancet/bin

WORKDIR /

COPY Dockerfile .
