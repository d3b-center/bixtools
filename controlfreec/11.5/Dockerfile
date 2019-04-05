FROM ubuntu:18.04
MAINTAINER Miguel Brown (brownm28@email.chop.edu)

COPY /get_config.pl .
RUN apt update && apt install -y wget build-essential zlib1g-dev libncurses5-dev libbz2-dev liblzma-dev libcurl4-openssl-dev samtools; \
chmod 755 get_config.pl \ 
&& wget -q https://github.com/BoevaLab/FREEC/archive/v11.5.tar.gz \
&& tar -xzf v11.5.tar.gz && cd FREEC-11.5/src && make && cd / \
&& wget https://github.com/biod/sambamba/releases/download/v0.6.9/sambamba-0.6.9-linux-static.gz && gunzip sambamba-0.6.9-linux-static.gz && chmod 755 sambamba-0.6.9-linux-static && mv sambamba-0.6.9-linux-static /usr/local/bin/sambamba
