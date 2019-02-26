FROM ubuntu:18.04
MAINTAINER Miguel Brown (brownm28@email.chop.edu)

RUN apt update && apt install -y git cmake g++ libz-dev; \
git clone https://github.com/pmelsted/pizzly.git; \
cd pizzly; \
mkdir build && cd build && cmake .. && make && make install; \
apt remove -y git && apt autoclean -y  && apt autoremove -y