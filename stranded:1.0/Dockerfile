FROM ubuntu:20.04

ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"
RUN apt-get update
RUN apt-get -y install gcc git wget
RUN rm -rf /var/lib/apt/lists/*

RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh 
RUN conda --version
 
# Configure Services and Port
COPY start.sh /start.sh
CMD ["./start.sh"]

RUN conda install -c bioconda samtools
RUN conda install -c bioconda kallisto=0.44.0
RUN pip install RSeQC
RUN pip install git+https://github.com/zoomzoom1011/how_are_we_stranded_here.git
