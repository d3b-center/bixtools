FROM ubuntu:18.04
LABEL maintainer="Saksham Phul(phuls@chop.edu)"
LABEL description="ubuntu image with tmb 1.0.0 package"
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /home

ADD tmb_1.0.0.tar.gz .

RUN apt update \
    && apt install r-base -y \
    && R CMD INSTALL tmb \
    && rm -R tmb

ADD Dockerfile .
