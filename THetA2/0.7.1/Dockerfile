FROM ubuntu:18.04

LABEL maintainer="Nathan Johnson <johnsonn13@chop.edu>"

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONPATH=:/bnpy-dev

RUN apt-get update -y && apt-get install -y python default-jdk curl gcc python-matplotlib python-dev git python-pip python-sklearn ant && \
    pip install numpy scipy joblib psutil pandas && \
    git clone https://github.com/kids-first/THetA.git --branch v0.7.1 && cd /THetA && ./install && \
    git clone https://bitbucket.org/michaelchughes/bnpy-dev.git
