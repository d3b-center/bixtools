FROM ubuntu:20.04
LABEL maintainer="Alex Sickler <sicklera@chop.edu>"
LABEL description="Install R in Miniconda with MM2S and d3b medullo classifier modules"

ENV MINICONDA_VERSION=py38_4.8.3

RUN apt update -y && apt install -y curl \
    && curl -sL https://repo.anaconda.com/miniconda/Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh -o /tmp/miniconda.sh \
    && sh /tmp/miniconda.sh -bfp /usr \
    && conda config --add channels conda-forge \
    && conda install -y -c conda-forge r-base=4.1.0 \
    && conda install -c bioconda bioconductor-gsva r-devtools bioconductor-org.hs.eg.db bioconductor-sva r-r.utils \
    && R -e "install.packages(c('optparse', 'MM2S', 'tidyverse'), dependencies=TRUE, repos='http://cran.us.r-project.org')" \
	&& R -e "devtools::install_github('d3b-center/medullo-classifier-package')" \
    && apt remove curl -y && apt autoclean -y && apt autoremove -y && conda clean -a -y

ADD Dockerfile .
