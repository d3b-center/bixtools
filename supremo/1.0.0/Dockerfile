FROM continuumio/miniconda3:23.9.0-0
LABEL maintainer="Daniel Miller (millerd15@chop.edu)"
LABEL descrption="SuPreMo - Pipeline for scoring simple and structural variants using Akita"

RUN apt update \
    && apt install -y build-essential curl

WORKDIR /opt

RUN conda install --name base python=3.10 numpy scipy pandas jupyter tensorflow Cython

RUN git clone https://github.com/calico/basenji.git

RUN cd /opt/basenji \
    && python setup.py develop --no-deps

ENV BASENJIDIR /opt/basenji
ENV PATH $BASENJIDIR/bin:$PATH
ENV PYTHONPATH $BASENJIDIR/bin:$PYTHONPATH

ENV SUPREMO_VERSION 1.0
RUN curl -sL https://github.com/ketringjoni/SuPreMo/archive/refs/tags/v${SUPREMO_VERSION}.tar.gz | tar xf && mv SuPreMo-${SUPREMO_VERSION} SuPreMo

RUN cd /opt/SuPreMo \
    && conda env update --name base --file get_Akita_scores_env.yml

WORKDIR /

COPY Dockerfile .


