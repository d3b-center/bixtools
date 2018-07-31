FROM ubuntu

MAINTAINER Xiao Dang (dangx@email.chop.edu)

RUN apt-get update --fix-missing
RUN apt-get install -y wget
ENV INSTALL_PATH="/anaconda"
RUN wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
RUN bash Miniconda2-latest* -fbp $INSTALL_PATH
ENV PATH="${INSTALL_PATH}/bin:${PATH}"

RUN conda update -y conda
RUN conda config --add channels bioconda

RUN conda install -y peddy