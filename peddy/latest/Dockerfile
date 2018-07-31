FROM ubuntu

MAINTAINER Xiao Dang (dangx@email.chop.edu)

RUN apt-get update --fix-missing
RUN apt-get install -y wget python bzip2 git make sysstat g++ gcc zlib1g-dev zlib1g cmake build-essential libncurses5-dev libbz2-dev liblzma-dev libcurl4-gnutls-dev libcrypto++-dev libbamtools-dev libssl-dev python-pip python-dev build-essential
RUN pip install --upgrade pip 
RUN git clone https://github.com/brentp/peddy
WORKDIR /peddy
RUN pip install -r requirements.txt
RUN pip install --editable .
RUN apt-get clean build-essential libncurses5-dev libbz2-dev liblzma-dev libcurl4-gnutls-dev libcrypto++-dev libbamtools-dev libssl-dev
