FROM ubuntu:20.04
LABEL maintainer="Nathan Johnson <johnsonn13@chop.edu>"
LABEL description="This is a script to create a single merged VCF from multiple single-caller somatic VCFs"

RUN apt update -y && apt install -y curl

# Download and install conda into /usr/bin
ENV MINICONDA_VERSION=py38_4.9.2
RUN curl -sL https://repo.anaconda.com/miniconda/Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh -o /tmp/miniconda.sh && \
    sh /tmp/miniconda.sh -bfp /usr

# Use conda to install remaining tools/dependencies into /usr/local
ENV HTSLIB_VERSION=1.9 \
    SAMTOOLS_VERSION=1.9 \
    PYSAM_VERSION=0.16.0.1 \
    NUMPY_VERSION=1.18.1

RUN conda config --add channels conda-forge
RUN conda config --add channels bioconda
RUN conda install -qy htslib==${HTSLIB_VERSION} samtools==${SAMTOOLS_VERSION} pysam==${PYSAM_VERSION} numpy==${NUMPY_VERSION}
RUN curl -sL -o /usr/bin/consensus_merge.py https://raw.githubusercontent.com/kids-first/kf-somatic-workflow/52b8ac4a1786a1406b6f9ddda99e8f2b7444b631/scripts/consensus_merge.py  && \
    conda clean -a -y && \
    apt remove curl -y && apt autoclean -y

RUN chmod +x /usr/bin/consensus_merge.py

WORKDIR /usr/bin/
