FROM ubuntu:18.04
LABEL maintainer="Miguel Brown (brownm28@email.chop.edu)"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y build-essential software-properties-common libcurl4-openssl-dev libssl-dev libxml2-dev \
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9 \
&&  add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/' \
&& apt update && apt install -y r-base

RUN mkdir ~/.R && echo "MAKEFLAGS = -j8" > ~/.R/Makevars
RUN Rscript -e 'install.packages("BiocManager")'
RUN Rscript -e 'install.packages(c("BiocParallel", "XML", "optparse"))'
RUN Rscript -e 'BiocManager::install("PureCN")'
RUN apt autoclean -y && apt autoremove -y
