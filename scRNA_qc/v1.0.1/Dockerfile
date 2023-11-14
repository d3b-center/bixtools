FROM rocker/tidyverse:4.2.3
LABEL maintainer="Miguel Brown (brownm28@chop.edu)"

ENV DEBIAN_FRONTEND=noninteractive
ENV SCOOTER_COMMIT=cff289d
ENV SEURAT_VERSION=4.3.0.1
ENV SEURAT_URL=https://cran.r-project.org/src/contrib/Archive/Seurat/Seurat_${SEURAT_VERSION}.tar.gz
RUN apt update -y && apt install -y libglpk40 libxt6 \
&& git clone https://github.com/igordot/scooter && cd scooter &&  git checkout ${SCOOTER_COMMIT}
# Install dependencies so that a specific version of Seurat can be installed
RUN R -e "install.packages(c('fitdistrplus', 'ggridges', 'ica', 'igraph', 'irlba', 'leiden', 'lmtest', 'matrixStats', 'patchwork', 'pbapply', 'plotly', 'png', 'RANN', 'RcppAnnoy', 'reticulate', 'ROCR', 'Rtsne', 'scattermore', 'sctransform', 'spatstat.explore', 'spatstat.geom', 'uwot', 'RcppProgress', 'cowplot', 'ggrepel', 'progressr', 'SeuratObject', 'RcppEigen'), Ncpus=8)" \
&& R -e "install.packages('${SEURAT_URL}', repos=NULL, type='source', Ncpus=8)" \
&& R -e "install.packages(c('GGally', 'ggpmisc', 'ggsci'), Ncpus=8)"
COPY Dockerfile .
