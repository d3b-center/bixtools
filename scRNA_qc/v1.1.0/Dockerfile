FROM rocker/tidyverse:4.3.2
LABEL maintainer="Miguel Brown (brownm28@chop.edu)"
LABEL description="Docker image to run scRNA QC. Install specific version of Seurat for downstream compatibility"

ENV DEBIAN_FRONTEND=noninteractive
ENV SCOOTER_COMMIT=cff289d
RUN apt update -y && apt install -y libglpk40 libxt6 libxt-dev \
&& git clone https://github.com/igordot/scooter && cd scooter &&  git checkout ${SCOOTER_COMMIT}
# Install dependencies so that a specific version of Seurat can be installed
ENV SEURAT_VERSION=4.3.0.1
ENV SEURATOBJECT_VERSION=4.1.3
ENV SEURAT_URL=https://cran.r-project.org/src/contrib/Archive/Seurat/Seurat_${SEURAT_VERSION}.tar.gz
ENV SEURATOBJECT_URL=https://cran.r-project.org/src/contrib/Archive/SeuratObject/SeuratObject_${SEURATOBJECT_VERSION}.tar.gz
RUN R -e "install.packages(c('Matrix', 'fitdistrplus', 'ggridges', 'ica', 'igraph', 'irlba', 'leiden', 'lmtest', 'matrixStats', 'patchwork', 'pbapply', 'plotly', 'png', 'RANN', 'RcppAnnoy', 'reticulate', 'ROCR', 'Rtsne', 'scattermore', 'sctransform', 'spatstat.explore', 'spatstat.geom', 'uwot', 'RcppProgress', 'cowplot', 'ggrepel', 'progressr', 'RcppEigen', 'sp', 'GGally', 'ggpmisc', 'ggsci', 'Cairo', 'R.utils', 'flexmix'), Ncpus=8, type='source')" \
&& R -e "install.packages(c('${SEURATOBJECT_URL}','${SEURAT_URL}'), repos=NULL, type='source', Ncpus=8)"
RUN mkdir ~/.R && echo MAKEFLAGS = -j8 > ~/.R/Makevars && R -e 'BiocManager::install(c("miQC", "scater"))'

COPY Dockerfile .
