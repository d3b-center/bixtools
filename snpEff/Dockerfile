FROM ubuntu:16.04
MAINTAINER Miguel Brown (brownm28@email.chop.edu)

ENV SNPEFF_VERSION 4_3t

RUN apt update && apt install -y openjdk-8-jdk wget tabix unzip \
&& wget -q https://sourceforge.net/projects/snpeff/files/snpEff_v${SNPEFF_VERSION}_core.zip/download \
&& unzip download && rm download \
&& apt remove -y wget && apt autoclean -y && apt autoremove -y
