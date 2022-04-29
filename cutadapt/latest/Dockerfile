FROM ubuntu:18.04
LABEL maintainer="Miguel Brown (brownm28@email.chop.edu)"

RUN apt update && apt install -y python3-pip pigz; \
pip3 install cutadapt; \
apt -y autoclean && apt -y autoremove;