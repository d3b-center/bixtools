FROM ubuntu:18.04
MAINTAINER Miguel Brown (brownm28@email.chop.edu)

RUN apt update && apt install -y python3-pip; \
pip3 install cutadapt; \
apt -y autoclean && apt -y autoremove;