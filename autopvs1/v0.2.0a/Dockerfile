FROM ubuntu:20.04
LABEL maintainer="Miguel Browmn <brownm28@chop.edu>"
LABEL description="Docker file with modified version of autopvs1"

ENV REPO_RELEASE=v0.1.0

RUN apt update -y && apt install -y wget python3 python3-pip pigz git libbz2-dev liblzma-dev zlib1g-dev \ 
&& git clone https://github.com/d3b-center/D3b-Pathogenicity-Preprocessing \
&& cd D3b-Pathogenicity-Preprocessing && git checkout ${REPO_RELEASE} \ 
&& mv autopvs1 ../autopvs1 && cd ../ && rm -rf D3b-Pathogenicity-Preprocessing \ 
&& pip3 install pysam==0.17.0 pyfaidx && \
apt remove -y wget git
