FROM rocker/tidyverse:4.3.3
LABEL maintainer="Daniel Miller (millerd15@chop.edu)"
LABEL descrption="Docker for running lgg xcell analyses from https://github.com/d3b-center/radiomics_imaging_analyses/tree/main/lgg_xcell_analyses on CAVATICA"

RUN install2.r optparse R.utils caret glmnet

RUN R -e 'remotes::install_github("igordot/msigdbr", ref = "v25.1.1")'

COPY Dockerfile .
