FROM ubuntu:22.04
LABEL maintainer="Miguel Brown (brownm28@chop.edu)"

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update -y && apt install -y libcurl4-openssl-dev curl pandoc libfreetype6-dev libfontconfig1-dev libxml2-dev r-base
RUN mkdir ~/.R && echo MAKEFLAGS = -j4 > ~/.R/Makevars \
&&  R -e "install.packages(c('rmarkdown', 'pkgdown', 'devtools'), dependencies=TRUE, repos='http://cran.us.r-project.org')"