FROM rocker/tidyverse:3.5.1
WORKDIR /rocker-build/

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils

RUN apt-get install dialog apt-utils -y

RUN R -e "install.packages('optparse', dependencies = TRUE)"

RUN R -e "BiocManager::install(c('EnsDb.Hsapiens.v86', 'ensembldb','ggthemes','qdapRegex','shinyBS', 'shinydashboard', 'shinycssloaders', 'rintrojs', 'shinythemes', 'DT','tidyverse'))"

WORKDIR /opt/formatFusionCalls

RUN wget -O annoFuse_0.90.0.tar.gz "https://github.com/d3b-center/annoFuse/archive/v0.90.0.tar.gz"

RUN R -e "install.packages('ggpubr', dependencies = TRUE)" 

ADD formatFusionCalls.R /rocker-build/formatFusionCalls.R
ADD annoFusePerSample.R /rocker-build/annoFusePerSample.R
