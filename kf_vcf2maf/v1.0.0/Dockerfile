FROM clearlinux:latest AS builder

# Install a minimal versioned OS into /install_root, and bundled tools if any
ENV CLEAR_VERSION=33910
RUN swupd os-install --no-progress --no-boot-update --no-scripts \
    --version ${CLEAR_VERSION} \
    --path /install_root \
    --statedir /swupd-state \
    --bundles os-core-update,which

# Download and install conda into /usr/bin
ENV MINICONDA_VERSION=py37_4.8.3 \
    MAF_VERSION=1.0.0
RUN swupd bundle-add --no-progress curl && \
    curl -sL https://github.com/kids-first/kf-mskcc-vcf2maf/archive/v${MAF_VERSION}.tar.gz -o v${MAF_VERSION}.tar.gz && \
    tar -xzf v${MAF_VERSION}.tar.gz && \
    rm v${MAF_VERSION}.tar.gz && \
    mv kf-mskcc-vcf2maf-${MAF_VERSION} vcf2maf && \
    curl -sL https://repo.anaconda.com/miniconda/Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh -o /tmp/miniconda.sh && \
    sh /tmp/miniconda.sh -bfp /usr

# Use conda to install remaining tools/dependencies into /usr/local
ENV HTSLIB_VERSION=1.9 \
    BCFTOOLS_VERSION=1.9 \
    SAMTOOLS_VERSION=1.9
    
RUN conda create -qy -p /usr/local \
        -c conda-forge \
        -c bioconda \
        -c defaults \
        htslib==${HTSLIB_VERSION} \
        bcftools==${BCFTOOLS_VERSION} \
        samtools==${SAMTOOLS_VERSION} 

# Deploy the minimal OS and tools into a clean target layer
FROM scratch

LABEL maintainer="Miguel Brown <brownm28@email.chop.edu>"
LABEL description="This docker was ported over from https://github.com/mskcc/vcf2maf/releases/tag/v1.6.19 and modified to pull from local port of the repo"
LABEL original_creator="Cyriac Kandoth <ckandoth@gmail.com>"

COPY --from=builder /install_root /
COPY --from=builder /usr/local /usr/local
COPY --from=builder vcf2maf/data /opt/data
COPY --from=builder vcf2maf/*.pl /opt/
WORKDIR /opt
