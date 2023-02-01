FROM rocker/tidyverse:4.2.1
LABEL maintainer="Alex Sickler <sicklera@chop.edu>"
LABEL description="tidyverse image with tmb 1.0.0 package"

ENV OPTPARSE_VERSION 1.7.3
ENV BIOC_VERSION 3.16

ENV DEBIAN_FRONTEND=noninteractive

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get update -y \
    && R -e "BiocManager::install(version = \"${BIOC_VERSION}\")" \
    && R -e "BiocManager::install('GenomicRanges', version = \"${BIOC_VERSION}\")" \
    && R -e "remotes::install_version('optparse', version = \"${OPTPARSE_VERSION}\", dependencies=TRUE, repos='http://cran.us.r-project.org')" \
    && R -e "remotes::install_github('d3b-center/d3b-analysis-toolkit', ref = 'main', subdir = 'tmb')" \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

COPY Dockerfile .
