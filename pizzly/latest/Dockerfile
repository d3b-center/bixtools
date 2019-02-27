FROM ubuntu:18.04
MAINTAINER Miguel Brown (brownm28@email.chop.edu)

ENV PIZZLY_VERSION=0.37.3

RUN apt update && apt install -y git cmake g++ libz-dev python3 python3-pip; \
ln -s /usr/bin/python3 /usr/local/bin/python; \
pip3 install h5py numpy; \
git clone https://github.com/pmelsted/pizzly.git; \
cd pizzly; \
mkdir build && cd build && cmake .. && make && make install; \
apt remove -y git  && apt autoclean -y  && apt autoremove -y