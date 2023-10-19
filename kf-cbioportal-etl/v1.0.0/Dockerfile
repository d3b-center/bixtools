FROM ubuntu:22.04
LABEL maintainer="Miguel Brown (brownm28@chop.edu)"
LABEL description="Kids First cBioportal Load ETL"

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt upgrade -y && apt install -y python-is-python3 python3-pip cpanminus r-base libxml2-dev \
 libharfbuzz-dev \
 libfontconfig1-dev \
 libfribidi-dev \
 libfreetype6-dev libpng-dev libtiff5-dev libjpeg-dev \
 libssl-dev libcurl4-openssl-dev

RUN pip install psycopg2-binary scipy numpy pandas botocore boto3 sevenbridges-python

RUN cpanm install Try::Tiny

RUN R -e "install.packages('devtools', repos='http://cran.rstudio.com/')"
RUN R -e "install.packages('Rcpp', repos='http://cran.rstudio.com/')"
RUN R -e "install.packages('optparse', repos='http://cran.rstudio.com/')"
RUN R -e "install.packages('readr', repos='http://cran.rstudio.com/')"
RUN R -e "install.packages('tidyr', repos='http://cran.rstudio.com/')"
RUN R -e "install.packages('tidyverse', repos='http://cran.rstudio.com/')"
RUN R -e "install.packages('data.table', repos='http://cran.rstudio.com/')"
RUN R -e "install.packages('funr', repos='http://cran.rstudio.com/')"