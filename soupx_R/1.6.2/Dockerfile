FROM pgc-images.sbgenomics.com/d3b-bixu/scrna_qc:v1.0.1
LABEL maintainer="Miguel Brown (brownm28@chop.edu)"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt upgrade -y && apt install -y libhdf5-dev patch
RUN R -e 'install.packages(c("SoupX", "optparse", "Matrix", "Rcpp", "R.utils", "dqrng", "hdf5r"), Ncpus=8)'
RUN mkdir ~/.R && echo MAKEFLAGS = -j8 > ~/.R/Makevars \
&& R -e 'BiocManager::install("DropletUtils")'

COPY Dockerfile .
