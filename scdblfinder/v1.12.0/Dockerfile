FROM pgc-images.sbgenomics.com/d3b-bixu/scrna_qc:v1.0.1

LABEL maintainer="Miguel Brown (brownm28@chop.edu)"
LABEL description="scDblFinder - use qc docker as base image as usage in workflow is wrapped in an R markdown notebook. Heavy stuff"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt upgrade -y && apt install -y libbz2-dev libxt-dev
RUN mkdir ~/.R && echo MAKEFLAGS = -j8 > ~/.R/Makevars
RUN R -e "BiocManager::install('scDblFinder', update=FALSE, checkBuilt=FALSE)"
RUN apt autoremove

COPY Dockerfile .
