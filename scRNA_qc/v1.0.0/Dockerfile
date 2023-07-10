FROM ubuntu:22.04
LABEL maintainer="Miguel Brown (brownm28@chop.edu)"

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update -y && apt install -y libcurl4-openssl-dev libharfbuzz-dev libfribidi-dev libssl-dev curl pandoc libfreetype6-dev libtiff5-dev libjpeg-dev libpng-dev libfontconfig1-dev libxml2-dev r-base default-jre default-jdk libcairo2-dev libtesseract-dev libleptonica-dev tesseract-ocr-eng libgsl-dev libfftw3-dev libhdf5-dev libudunits2-dev libgdal-dev
RUN mkdir ~/.R && echo MAKEFLAGS = -j4 > ~/.R/Makevars \
&&  R -e "install.packages(c('rmarkdown', 'pkgdown', 'devtools', 'future', 'cowplot', 'forcats', 'GGally', 'ggpmisc', 'ggrepel', 'ggsci', 'irlba', 'matrixStats', 'Rtsne', 'sctransform', 'Seurat', 'SeuratObject', 'uwot'), dependencies=TRUE, repos='http://cran.us.r-project.org')"
RUN apt install git && git clone https://github.com/igordot/scooter && git checkout cff289d

COPY Dockerfile .