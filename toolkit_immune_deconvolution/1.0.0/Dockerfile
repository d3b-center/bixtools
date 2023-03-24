FROM rocker/tidyverse:4.2.1
LABEL maintainer="Saksham Phul <phuls@chop.edu>"
LABEL description="tidyverse image with requirments for immune deconvolution"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y \
 && R -e "install.packages(c('pheatmap','optparse','tidyverse','rlist','plyr','magrittr'))"\
 && R -e "remotes::install_github('omnideconv/immunedeconv',dependencies=TRUE,ref = '493bcaa9e1f73554ac2d25aff6e6a7925b0ea7a6')"

COPY Dockerfile .
