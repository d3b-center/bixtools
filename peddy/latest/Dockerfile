FROM ubuntu

MAINTAINER Xiao Dang (dangx@email.chop.edu)

RUN apt-get update --fix-missing
RUN apt-get install -y wget
RUN INSTALL_PATH=/anaconda
RUN wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
bash Miniconda2-latest* -fbp $INSTALL_PATH
PATH=$INSTALL_PATH/bin:$PATH

conda update -y conda
conda config --add channels bioconda

conda install -y peddy