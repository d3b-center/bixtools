FROM python:3.9
LABEL maintainer="Daniel Miller (millerd15@chop.edu)"
LABEL description="Python3 base with all necessary packages installed. Includes bedtools for pybedtools integration."

RUN python -m pip install --upgrade pip && python -m pip install pandas pysam pybedtools pyyaml

ENV BEDTOOLS_VERSION 2.30.0

RUN apt update && apt install -y curl

RUN curl -sL https://github.com/arq5x/bedtools2/releases/download/v${BEDTOOLS_VERSION}/bedtools.static.binary > /usr/local/bin/bedtools && chmod 755 /usr/local/bin/bedtools

COPY Dockerfile .
