FROM rocker/tidyverse:4.2
LABEL maintainer="Alex Sickler (sicklera@email.chop.edu)"

WORKDIR /rocker-build/

ENV ANNOFUSE_URI https://github.com/d3b-center/annoFuse/tarball/
ENV ANNOFUSE_VER Add-Custom-Type-Annotation

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils \
&& apt-get install dialog apt-utils libbz2-dev -y \
&& R -e "install.packages(c('optparse', 'rjson', 'gdata', 'ggpubr', 'remotes'), dependencies = TRUE)" \
&& R -e "BiocManager::install(c('Rhtslib', 'Rsamtools', 'EnsDb.Hsapiens.v86', 'ensembldb','ggthemes','qdapRegex','shinyBS', 'shinydashboard', 'shinycssloaders', 'rintrojs', 'shinythemes', 'DT', 'reshape2'))" \
&& R -e "remotes::install_github('federicomarini/annoFuseData')"

ADD formatFusionCalls.R .
ADD annoFusePerSample.R .
ADD Dockerfile .

WORKDIR /opt/formatFusionCalls

RUN wget -O annoFuse_${ANNOFUSE_VER}.tar.gz "${ANNOFUSE_URI}/${ANNOFUSE_VER}" \
&& R -e "install.packages(\"annoFuse_${ANNOFUSE_VER}.tar.gz\", repos = NULL)"
