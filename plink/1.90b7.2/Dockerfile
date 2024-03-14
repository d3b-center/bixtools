FROM ubuntu:22.04

RUN apt update && apt install -y curl unzip

WORKDIR /opt

RUN curl -so temp.zip -L https://s3.amazonaws.com/plink1-assets/plink_linux_x86_64_20231211.zip \
    && unzip -d plink temp.zip \
    && rm temp.zip

ENV PATH $PATH:/opt/plink

WORKDIR /

COPY Dockerfile .
