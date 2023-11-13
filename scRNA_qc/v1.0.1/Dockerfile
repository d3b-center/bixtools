FROM rocker/tidyverse:4.2.3
LABEL maintainer="Miguel Brown (brownm28@chop.edu)"

ENV DEBIAN_FRONTEND=noninteractive
ENV SCOOTER_COMMIT=cff289d
RUN apt update -y && apt install -y libglpk40 libxt6 \
&& git clone https://github.com/igordot/scooter && cd scooter &&  git checkout ${SCOOTER_COMMIT}
RUN R -e "install.packages(c('Seurat', 'SeuratObject', 'GGally', 'ggpmisc', 'ggsci'), Ncpus=4)"
COPY Dockerfile .
