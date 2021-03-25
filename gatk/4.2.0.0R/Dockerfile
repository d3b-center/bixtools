FROM ubuntu:18.04
LABEL maintainer="Miguel Brown (brownm28@email.chop.edu)"
LABEL maintainer="Daniel Miller (millerd15@email.chop.edu)"

ENV PYTHON_VERSION 2.7.15~rc1-1
ENV WGET_VERSION 1.19.4-1ubuntu2.2
ENV UNZIP_VERSION 6.0-21ubuntu1
ENV LIBGOMP1_VERSION 8.4.0-1ubuntu1~18.04
ENV TABIX_VERSION 1.7-2
ENV SAMTOOLS_VERSION 1.7-1
ENV RBASE_VERSION 3.4.4-1ubuntu1
ENV GATK4_VERSION 4.2.0.0
ENV OPTPARSE_VERSION 1.6.6
ENV DATATABLE_VERSION 1.12.8
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update \
&& apt install -y \
openjdk-8-jdk \
python=${PYTHON_VERSION} \
wget=${WGET_VERSION} \
unzip=${UNZIP_VERSION} \
libgomp1=${LIBGOMP1_VERSION} \
tabix=${TABIX_VERSION} \
samtools=${SAMTOOLS_VERSION} \
r-base-dev=${RBASE_VERSION}; \
wget -q https://github.com/broadinstitute/gatk/releases/download/${GATK4_VERSION}/gatk-${GATK4_VERSION}.zip; \
unzip gatk-${GATK4_VERSION}.zip; \
mv gatk-${GATK4_VERSION}/gatk* . && rm -rf gatk-${GATK4_VERSION}*;

RUN R -e "install.packages('versions')"
RUN R -e "versions::install.versions(c('optparse','data.table'),c('${OPTPARSE_VERSION}','${DATATABLE_VERSION}'))"
