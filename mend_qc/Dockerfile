FROM ubuntu:18.04
LABEL mantainer="zhangb1@email.chop.edu"
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
  r-base \
  wget \
  build-essential \
  zlib1g-dev \
  time \
  python2.7 python-pip python-dev\
  python-setuptools \
  libbz2-dev liblzma-dev git

RUN git clone https://github.com/UCSC-Treehouse/mend_qc
RUN wget -qO- https://github.com/lomereiter/sambamba/releases/download/v0.6.7/sambamba_v0.6.7_linux.tar.bz2 \
  | tar xj -C /usr/local/bin
RUN wget -qO- https://github.com/GregoryFaust/samblaster/releases/download/v.0.1.24/samblaster-v.0.1.24.tar.gz \
  | tar xz -C /tmp \
  && cd /tmp/samblaster-v.0.1.24/ && make && mv samblaster /usr/local/bin && rm -rf /tmp/samblaster-v-0.1.24
WORKDIR /ref
# RUN wget https://sourceforge.net/projects/rseqc/files/BED/Human_Homo_sapiens/hg38_Gencode_V28.bed.gz/download &&  gunzip download -c > /ref/hg38_GENCODE_v28_basic.bed
RUN pip install --no-cache-dir -r /mend_qc/requirements.txt
RUN R -e 'install.packages(c("rjson"), repos="http://cran.us.r-project.org")' && apt -y remove git && apt autoclean
