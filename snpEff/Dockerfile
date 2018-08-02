FROM ubuntu
MAINTAINER Miguel Brown (brownm28@email.chop.edu)

ENV SNPEFF_VERSION 4_3t

RUN apt update && apt install -y openjdk-8-jdk wget tabix unzip;
RUN wget -q https://sourceforge.net/projects/snpeff/files/snpEff_v${SNPEFF_VERSION}_core.zip/download;
RUN unzip download && rm download;
RUN apt remove -y  wget
