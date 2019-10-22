FROM ubuntu:18.04

MAINTAINER David Curley (curleyd@email.chop.edu)

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONPATH=:/bnpy-dev

RUN apt-get update -y && apt-get install -y 	python default-jdk 	curl 	gcc 	python-matplotlib 	python-dev 	git 	python-pip 	python-sklearn

RUN pip install numpy scipy joblib psutil pandas

RUN git clone https://github.com/raphael-group/THetA.git && 	cd /THetA && 	./install

RUN git clone https://bitbucket.org/michaelchughes/bnpy-dev.git
