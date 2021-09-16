FROM ubuntu:20.04
LABEL maintainer="Nathan Johnson <johnsonn13@chop.edu>"
LABEL description="Install R in Miniconda with SoupX package for background removal in single-cell RNA"

ENV MINICONDA_VERSION=py38_4.8.3

RUN apt update -y && apt install -y curl \
    && curl -sL https://repo.anaconda.com/miniconda/Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh -o /tmp/miniconda.sh \
    && sh /tmp/miniconda.sh -bfp /usr \
    && conda config --add channels conda-forge \
    && conda install -y -c conda-forge r-base=4.1.0 r-hdf5r \
    && R -e "install.packages(c('optparse', 'codetools', 'survival', 'plyr', 'zoo', 'data.table', 'htmlwidgets', 'lazyeval', 'reshape2', 'SoupX', 'hdf5r'), dependencies=TRUE, repos='http://cran.us.r-project.org')" \
    && conda install -c bioconda bioconductor-dropletutils \
    && apt remove curl -y && apt autoclean -y && apt autoremove -y && conda clean -a -y

ADD Dockerfile .
