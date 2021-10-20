FROM rocker/tidyverse:4.1

LABEL maintainer="Miguel Brown (brownm28@chop.edu)"

RUN apt update && apt upgrade -y \
&& apt install -y python3-pip build-essential libbz2-dev liblzma-dev libxt-dev libproj-dev  cpanminus \
&& R -e "install.packages(c('BiocManager','pheatmap','optparse','hrbrthemes','viridis','plyr','ggstatsplot'), dependencies=TRUE, repos='http://cran.us.r-project.org')" \
&& R -e 'BiocManager::install("maftools", "ConsensusClusterPlus", "sva", "EnhancedVolcano", "DESeq2")' \
&& pip3 install numpy pandas seaborn matplotlib pyplot pyreadr \
&& cpanm install Statistics::Lite \
&& apt remove -y python3-pip build-essential && apt autoclean && apt autoremove -y
