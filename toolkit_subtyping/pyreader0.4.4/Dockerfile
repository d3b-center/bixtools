FROM ubuntu:20.04
LABEL maintainer="Alex Sickler <sicklera@chop.edu>"
LABEL description="Install R and Python in Miniconda with d3b medullo classifier modules and pyreadr"

ENV MINICONDA_VERSION=py38_4.8.3
ENV R_VERSION 4.1.0
ENV NUMPY_VERSION 1.20.2
ENV SCIPY_VERSION 1.6.2
ENV PANDAS_VERSION 1.2.4
ENV PYREADR_VERSION 0.4.4

RUN apt update -y && apt install -y curl \
    && curl -sL https://repo.anaconda.com/miniconda/Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh -o /tmp/miniconda.sh \
    && sh /tmp/miniconda.sh -bfp /usr \
    && conda config --add channels conda-forge \
    && conda install -y -c conda-forge r-base=${R_VERSION} \
    && conda install -c bioconda bioconductor-gsva r-devtools bioconductor-org.hs.eg.db bioconductor-sva r-r.utils \
    && R -e "install.packages(c('optparse', 'MM2S', 'tidyverse'), dependencies=TRUE, repos='http://cran.us.r-project.org')" \
	  && R -e "devtools::install_github('d3b-center/medullo-classifier-package')" \
    && pip install numpy==$NUMPY_VERSION scipy==$SCIPY_VERSION pandas==$PANDAS_VERSION pyreadr==$PYREADR_VERSION \
    && apt remove curl -y && apt autoclean -y && apt autoremove -y && conda clean -a -y

ADD Dockerfile .
