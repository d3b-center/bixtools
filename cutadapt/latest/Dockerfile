FROM ubuntu:18.04
MAINTAINER Miguel Brown (brownm28@email.chop.edu)

RUN apt update && apt install -y python-pip; \
pip install cutadapt; \
apt -y autoclean && apt -y autoremove;