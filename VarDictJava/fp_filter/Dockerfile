FROM ubuntu:18.04
LABEL maintainer="Miguel Brown (brownm28@email.chop.edu)"
LABEL description="Modified and adapted from https://github.com/bcbio/bcbio-nextgen/tree/master/bcbio"

ENV DEBIAN_FRONTEND=noninteractive
COPY /utils.py /
COPY /bcbio_vardict_filter.py .
RUN apt update && apt install -y python python-pip tabix && \
pip install toolz pyyaml && \
apt clean -y && apt autoremove -y