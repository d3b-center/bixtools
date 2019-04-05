FROM ubuntu:18.04
LABEL maintainer="Miguel Brown (brownm28@email.chop.edu)"

ENV DEBIAN_FRONTEND=noninteractive
COPY /get_config.pl /
RUN apt update && apt install -y wget build-essential zlib1g-dev libncurses5-dev libbz2-dev libxml2-dev liblzma-dev libcurl4-openssl-dev samtools bedtools r-base; \
chmod 755 get_config.pl \ 
&& wget -q https://github.com/BoevaLab/FREEC/archive/v11.5.tar.gz \
&& tar -xzf v11.5.tar.gz && cd FREEC-11.5/src && make && cd / \
&& wget https://github.com/biod/sambamba/releases/download/v0.6.9/sambamba-0.6.9-linux-static.gz && gunzip -q sambamba-0.6.9-linux-static.gz && chmod 755 sambamba-0.6.9-linux-static && mv sambamba-0.6.9-linux-static /usr/local/bin/sambamba \
&& Rscript -e 'install.packages("XML")' && Rscript -e 'source("https://bioconductor.org/biocLite.R")' && Rscript -e 'BiocInstaller::biocLite(c("rtracklayer"))'
