FROM ubuntu:18.04
LABEL maintainer="Miguel Brown (brownm28@email.chop.edu)"

ENV DEBIAN_FRONTEND=noninteractive
ENV R_VERSION=3.5.2-1bionic

RUN apt update --fix-missing && apt install -y software-properties-common build-essential curl gfortran libcurl4-openssl-dev libxml2-dev zlib1g-dev libxmlsec1 libblas-dev liblapack-dev libssl-dev && \
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9 && \
add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/' && \
apt update && apt install -y r-base-core=${R_VERSION} && \
Rscript -e 'if (!requireNamespace("BiocManager", quietly = TRUE)) install.packages("BiocManager"); \
BiocManager::install("CODEX", version = "3.8"); \
BiocManager::install("WES.1KG.WUGSC", version = "3.8"); \
install.packages("devtools"); \
devtools::install_github("yuchaojiang/CODEX2/package")'