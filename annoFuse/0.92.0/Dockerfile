FROM rocker/tidyverse:4.0
LABEL maintainer="Miguel Browm (brownm28@chop.edu)"

WORKDIR /rocker-build/

ENV ANNOFUSE_VER=v0.92.0
ENV ANNOFUSE_DATA_VER=v1.0.0

RUN apt update && apt install -y --no-install-recommends apt-utils \
&& apt install dialog apt-utils libbz2-dev -y \
&& R -e "install.packages(c('optparse', 'rjson', 'gdata', 'ggpubr', 'remotes', 'data.table'), dependencies = TRUE)" \
&& R -e "remotes::install_github('d3b-center/annoFuseData@${ANNOFUSE_DATA_VER}', dependencies = TRUE)" \
&& R -e "remotes::install_github('d3b-center/annoFuse@${ANNOFUSE_VER}', dependencies = TRUE)"

COPY Dockerfile .
