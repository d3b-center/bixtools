FROM rocker/tidyverse:4.4.2
LABEL maintainer="Alex Sickler <sicklera@chop.edu>"
LABEL description="tidyverse image with requirments for immune deconvolution"

RUN R -e "install.packages(c('pheatmap','optparse','tidyverse','rlist','plyr','magrittr'))"
RUN R -e "remotes::install_github('omnideconv/immunedeconv', dependencies=TRUE, ref = '2.1.3')"

COPY Dockerfile .
