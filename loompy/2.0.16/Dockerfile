FROM python:3.9.1
LABEL maintainer = "Alex Sickler (sicklera@email.chop.edu)"

ENV LOOMPY_VERSION 2.0.16
ENV SCIPY_VERSION 1.6.2
ENV NUMPY_VERSION 1.20.2
ENV PANDAS_VERSION 1.2.4

RUN apt update -y && pip install --no-cache-dir scipy==$SCIPY_VERSION numpy==$NUMPY_VERSION pandas==$PANDAS_VERSION loompy==$LOOMPY_VERSION

ADD Dockerfile .
