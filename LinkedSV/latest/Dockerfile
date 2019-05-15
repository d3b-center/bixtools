FROM ubuntu:18.04
LABEL maintainer="Miguel Brown (brownm28@email.chop.edu)"

RUN apt update && apt install -y wget build-essential git samtools bedtools python-pip zlib1g-dev && \
pip install sklearn scipy numpy psutil argparse pandas seaborn datetime && \
git clone https://github.com/WGLab/LinkedSV.git && cd LinkedSV/ && sh build.sh && cd / && \
apt remove -y wget git python-pip