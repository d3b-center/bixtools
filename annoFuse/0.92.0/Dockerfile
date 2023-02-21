FROM rocker/tidyverse:4.2
LABEL maintainer="Miguel Browm (brownm28@chop.edu)"

WORKDIR /rocker-build/

ENV ANNOFUSE_VER v0.92.0
ENV ANNOFUSE_DATA_VER v0.1.0

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils \
&& apt-get install dialog apt-utils libbz2-dev -y \
&& R -e "install.packages(c('optparse', 'rjson', 'gdata', 'ggpubr', 'remotes', 'data.table'), dependencies = TRUE)" \
&& R -e "remotes::install_github('d3b-center/annoFuseData@${ANNOFUSE_DATA_VER}', dependencies = TRUE)" \
&& R -e "remotes::install_github('d3b-center/annoFuse@${ANNOFUSE_VER}', dependencies = TRUE)"

ADD Dockerfile .
