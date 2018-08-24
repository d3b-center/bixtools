FROM ubuntu:16.04

MAINTAINER Xiao Dang (dangx@email.chop.edu)

RUN apt-get update --fix-missing && apt upgrade -y &&  apt-get install -y wget python bzip2 git make sysstat g++ gcc zlib1g-dev zlib1g cmake build-essential libncurses5-dev libbz2-dev liblzma-dev libcurl4-gnutls-dev libcrypto++-dev libbamtools-dev libssl-dev python-pip python-dev build-essential \
&& git clone https://github.com/brentp/peddy && cd /peddy && pip install numpy==1.14.5 && pip install cyvcf2==0.8.9 && pip install -r requirements.txt && pip install --editable . \
&& apt-get clean build-essential libncurses5-dev libbz2-dev liblzma-dev libcurl4-gnutls-dev libcrypto++-dev libbamtools-dev libssl-dev && apt-get autoremove -y
