FROM ubuntu:20.04
LABEL maintainer="Alex Sickler <sicklera@chop.edu>"
LABEL description="Install R, Python, and libraries needed to run subtyping"

ENV MINICONDA_VERSION=py38_4.8.3
ENV R_VERSION 4.1.1
ENV NUMPY_VERSION 1.20.2
ENV SCIPY_VERSION 1.6.2
ENV PANDAS_VERSION 1.2.4
ENV PYREADR_VERSION 0.4.4
ENV PYTEST_VERSION 7.1.2
ENV OPTPARSE_VERSION 1.7.3
ENV TIDYVERSE_VERSION 1.3.2
ENV RPY2_VERSION 3.5.10
ENV MEDULLO_CLASSIFIER_VERSION v0.1.1

RUN apt-get update -y && apt-get install -y curl \
    && curl -sL https://repo.anaconda.com/miniconda/Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh -o /tmp/miniconda.sh \
    && sh /tmp/miniconda.sh -bfp /usr \
    && conda config --add channels conda-forge \
    && conda install -y -c conda-forge r-base=${R_VERSION} \
    && conda install -c bioconda bioconductor-gsva r-devtools bioconductor-org.hs.eg.db bioconductor-sva r-r.utils \
    && R -e "install.packages('processx', repos = 'http://cran.us.r-project.org')" \
    && R -e "install.packages('cli', repos = 'http://cran.us.r-project.org')" \
    && R -e "install.packages('rlang', repos = 'http://cran.us.r-project.org')" \
    && R -e "devtools::install_version('optparse', version = \"${OPTPARSE_VERSION}\", dependencies=TRUE, repos='http://cran.us.r-project.org')" \
    && R -e "devtools::install_version('MM2S', dependencies=TRUE, repos='http://cran.us.r-project.org')" \
    && R -e "devtools::install_version('tidyverse', version = \"${TIDYVERSE_VERSION}\" ,dependencies=TRUE, repos='http://cran.us.r-project.org')" \
    && R -e "devtools::install_github(\"d3b-center/medullo-classifier-package@${MEDULLO_CLASSIFIER_VERSION}\")" \
    && pip install numpy==$NUMPY_VERSION scipy==$SCIPY_VERSION pandas==$PANDAS_VERSION pyreadr==$PYREADR_VERSION pytest==$PYTEST_VERSION rpy2==$RPY2_VERSION \
    && apt-get remove curl -y && apt-get autoclean -y && apt-get autoremove -y && conda clean -a -y

COPY Dockerfile .
