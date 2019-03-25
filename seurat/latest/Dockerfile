FROM ubuntu:18.04
MAINTAINER Miguel Brown (brownm28@email.chop.edu)

ENV SEURAT_VERSION=2.6

RUN apt update && apt install -y wget default-jre && \
wget -q https://github.com/tgen/seurat/raw/master/jar_files/v2.5/Seurat-2.6.jar && \
apt remove -y wget && apt clean -y && apt autoremove -y