FROM ubuntu:18.04
LABEL maintainer="Miguel Brown (brownm28@email.chop.edu)"

ENV VARDICT_VERSION=1.5.8
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y wget openjdk-8-jdk r-base perl  && \
wget -q https://github.com/AstraZeneca-NGS/VarDictJava/releases/download/v${VARDICT_VERSION}/VarDict-${VARDICT_VERSION}.zip && \
unzip VarDict-${VARDICT_VERSION}.zip && \
rm VarDict-${VARDICT_VERSION}.zip && \
apt remove -y wget && apt clean -y && apt autoremove -y