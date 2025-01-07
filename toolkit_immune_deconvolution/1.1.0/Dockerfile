FROM rocker/tidyverse:4.4.2
LABEL maintainer="Alex Sickler <sicklera@chop.edu>"
LABEL description="tidyverse image with requirments for immune deconvolution"

RUN R -e "install.packages(c('pheatmap','optparse','rlist','plyr','magrittr','remotes','BiocManager'))"
RUN R -e "BiocManager::install(c('S4Vectors','Biostrings','GenomicRanges','S4Arrays','DelayedArray','sva','GSVA'))"
RUN R -e "BiocManager::install('Biostrings')"
RUN R -e "remotes::install_github('omnideconv/immunedeconv', dependencies=TRUE, ref = '2.1.3')"

COPY Dockerfile .
