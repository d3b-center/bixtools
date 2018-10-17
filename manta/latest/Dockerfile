FROM ubuntu:16.04
MAINTAINER Miguel Brown (brownm28@email.chop.edu)

ENV MANTA_VERSION latest
RUN apt update && apt upgrade -y && apt install -y wget python bzip2 \
&& wget https://github.com/Illumina/manta/releases/download/v1.4.0/manta-1.4.0.centos6_x86_64.tar.bz2 \
&& tar -jxvf /manta-1.4.0.centos6_x86_64.tar.bz2 && rm /manta-1.4.0.centos6_x86_64.tar.bz2 \
&& apt remove wget bzip2 -y && apt autoclean -y && apt autoremove -y