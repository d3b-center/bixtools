FROM rocker/tidyverse:4.4.2
LABEL maintainer="Alex Sickler <sicklera@chop.edu>"
LABEL description="tidyverse image with requirments for splicing data product"

RUN R -e "install.packages(c('optparse','ggforce'))"

COPY Dockerfile .
