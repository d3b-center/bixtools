FROM --platform=linux/amd64 ubuntu:22.04
LABEL maintainer="Jessica Wong <wongj4@chop.edu>"
LABEL description="isoseq"
RUN apt-get update \
    && apt-get install -y build-essential wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV CONDA_DIR /opt/conda
ENV PATH=$CONDA_DIR/bin:$PATH

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda

RUN conda install -y -c bioconda isoseq lima pbmm2 
RUN conda install -y -c conda-forge pbpigeon=1.1.0