FROM pgc-images.sbgenomics.com/d3b-bixu/samtools:1.15.1
LABEL maintainer="Miguel Browm <brownm28@chop.edu>"

ENV PATH="${PATH}:/hisat2-2.2.1"

RUN apt update && apt install -y python3 python-is-python3 wget unzip && \
wget https://cloud.biohpc.swmed.edu/index.php/s/oTtGWbWjaxsQ2Ho/download && \
unzip download && rm download && apt remove -y wget unzip

COPY Dockerfile .
