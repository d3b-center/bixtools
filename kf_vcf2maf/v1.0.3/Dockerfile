FROM ubuntu:20.04

LABEL maintainer="Miguel Brown <brownm28@email.chop.edu>"
LABEL description="This docker was ported over from https://github.com/mskcc/vcf2maf/releases/tag/v1.6.19 and modified to pull from local port of the repo"
LABEL original_creator="Cyriac Kandoth <ckandoth@gmail.com>"

# Download and install conda into /usr/bin
ENV MINICONDA_VERSION=py37_4.8.3 \
    MAF_VERSION=1.0.3 \
    HTSLIB_VERSION=1.9 \
    BCFTOOLS_VERSION=1.9 \
    SAMTOOLS_VERSION=1.9
RUN apt update -y && apt install curl -y && \
    curl -sL https://github.com/kids-first/kf-mskcc-vcf2maf/archive/v${MAF_VERSION}.tar.gz -o v${MAF_VERSION}.tar.gz && \
    tar -xzf v${MAF_VERSION}.tar.gz && \
    rm v${MAF_VERSION}.tar.gz && \
    mv kf-mskcc-vcf2maf-${MAF_VERSION} vcf2maf && chmod 755 vcf2maf/vcf2maf.pl && \
    curl -sL https://repo.anaconda.com/miniconda/Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh -o /tmp/miniconda.sh && \
    sh /tmp/miniconda.sh -bfp /usr && \   
    conda create -qy -p /usr/local \
        -c conda-forge \
        -c bioconda \
        -c defaults \
        htslib==${HTSLIB_VERSION} \
        bcftools==${BCFTOOLS_VERSION} \
        samtools==${SAMTOOLS_VERSION} && \
        conda clean -a -y && \
        apt remove curl -y && apt autoclean -y

ADD Dockerfile .
