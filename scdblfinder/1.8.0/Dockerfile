FROM pgc-images.sbgenomics.com/brownm28/scrna_qc:v1.0.0

LABEL maintainer="Miguel Brown (brownm28@chop.edu)"
LABEL description="scDblFinder - use qc docker as base image as usage in workflow os wrapped in an R markdown notebook. Heavy stuff"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt upgrade -y

RUN R -e "BiocManager::install('scDblFinder')"
RUN R -e "install.packages('tidyverse', repos='http://cran.rstudio.com/')"

COPY Dockerfile .
