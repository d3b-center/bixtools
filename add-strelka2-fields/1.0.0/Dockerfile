FROM ubuntu:20.04
LABEL maintainer="Nathan Johnson <johnsonn13@chop.edu>"
LABEL description="This is a script to add canonical fields like GT and AD to a Strelka2 tumor-normal VCF"

RUN apt update -y && apt install -y curl 

# Download and install conda into /usr/bin
ENV MINICONDA_VERSION=py38_4.8.3
RUN curl -sL https://repo.anaconda.com/miniconda/Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh -o /tmp/miniconda.sh && \
    sh /tmp/miniconda.sh -bfp /usr

# Use conda to install remaining tools/dependencies into /usr/local
ENV HTSLIB_VERSION=1.9 \
    SAMTOOLS_VERSION=1.9 \
    PYSAM_VERSION=0.16.0
RUN conda create -qy -p /usr/local \
        -c conda-forge \
        -c bioconda \
        -c defaults \
        htslib==${HTSLIB_VERSION} \
        samtools==${SAMTOOLS_VERSION} \
        pysam==${PYSAM_VERSION} \
        && curl -sL -o /usr/bin/add_strelka2_fields.py https://raw.githubusercontent.com/kids-first/kf-somatic-workflow/master/scripts/add_strelka2_fields.py

RUN chmod +x /usr/bin/add_strelka2_fields.py

WORKDIR /usr/bin/
