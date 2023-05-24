FROM ubuntu:22.04
LABEL maintainer="Saksham Phul (phuls@chop.edu)"
LABEL description="RTG tool for benchmarking vcf files"

ENV DEBIAN_FRONTEND noninteractive

ENV RTG_VERSION 3.12.1

RUN apt update && apt upgrade -y && apt install default-jre wget unzip apache2 ant git -y && apt install build-essential libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev software-properties-common -y && add-apt-repository ppa:deadsnakes/ppa -y && apt install python3.11-distutils curl python3.11 -y && curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11 && python3.11 -m pip install pandas && wget https://github.com/RealTimeGenomics/rtg-tools/archive/refs/tags/${RTG_VERSION}.tar.gz -O - | tar -xz && cd rtg-tools-${RTG_VERSION} && ant zip-nojre && mkdir /home/RTG && cd /home/RTG/ && unzip /rtg-tools-${RTG_VERSION}/dist/rtg-tools-${RTG_VERSION}-*zip

ENV PATH=$PATH:"/home/RTG/rtg-tools-${RTG_VERSION}-unknown/"

COPY Dockerfile .
