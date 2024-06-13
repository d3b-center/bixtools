FROM rocker/tidyverse:4.4.0
LABEL maintainer="Miguel Brown (brownm28@chop.edu)"
LABEL description="Docker image to run Harvard Bioinformatics Core (HBC) scRNA QC as defined here: https://github.com/hbctraining/scRNA-seq_online?tab=readme-ov-file#installation-requirements. Install specific version of Seurat for downstream compatibility"

ENV DEBIAN_FRONTEND=noninteractive
# Install dependencies so that a specific version of Seurat can be installed
ENV SEURAT_VERSION=4.3.0.1
ENV SEURATOBJECT_VERSION=4.1.3
ENV SEURAT_URL=https://cran.r-project.org/src/contrib/Archive/Seurat/Seurat_${SEURAT_VERSION}.tar.gz
ENV SEURATOBJECT_URL=https://cran.r-project.org/src/contrib/Archive/SeuratObject/SeuratObject_${SEURATOBJECT_VERSION}.tar.gz

RUN apt update -y && apt install -y libbz2-dev libglpk40 libhdf5-dev patch
RUN  mkdir ~/.R && echo MAKEFLAGS = -j8 > ~/.R/Makevars && R -e "BiocManager::install(c('AnnotationHub', 'ensembldb', 'multtest', 'glmGamPoi'))"
RUN R -e "install.packages(c('optparse', 'cowplot', 'fitdistrplus', 'future', 'future.apply', 'ggrepel', 'ggridges', 'ica', 'igraph', 'irlba', 'leiden', 'lmtest', 'matrixStats', 'patchwork', 'pbapply', 'plotly', 'png', 'progressr', 'RANN', 'RcppAnnoy', 'reticulate', 'ROCR', 'Rtsne', 'scattermore', 'sctransform', 'spatstat.explore', 'spatstat.geom', 'uwot', 'RcppEigen', 'RcppProgress', 'sp', 'metap', 'hdf5r', 'patch'), type='source', Ncpus=8)"
RUN R -e "install.packages(c('${SEURATOBJECT_URL}','${SEURAT_URL}'), repos=NULL, type='source', Ncpus=8)"
COPY Dockerfile .