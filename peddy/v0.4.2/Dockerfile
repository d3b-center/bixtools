FROM ubuntu:16.04

LABEL maintainer="Alex Sickler (sicklera@email.chop.edu)"

ENV PEDDY_VERSION v0.4.2

RUN apt-get update && apt upgrade -y \
&&  apt-get install -y python git build-essential libbamtools-dev python-pip python-dev build-essential libssl-dev \
&& pip install backports.functools-lru-cache==1.5 numpy==1.14.5 click==6.7 coloredlogs==10.0 cycler==0.10.0 \
Cython==0.28.5 decorator==4.3.0 humanfriendly==4.16.1 kiwisolver==1.0.1 \
matplotlib==2.2.3 monotonic==1.5 networkx==2.1 pandas==0.23.4 pyparsing==2.2.0 \
python-dateutil==2.7.3 pytz==2018.5 scikit-learn==0.19.2 scipy==1.1.0 seaborn==0.9.0 six==1.11.0 subprocess32==3.5.2 toolshed==0.4.6 \
&& pip install cyvcf2==0.8.9 \
&& git clone --depth 1 --branch ${PEDDY_VERSION} https://github.com/brentp/peddy && cd /peddy && pip install numpy==1.14.5 && pip install cyvcf2==0.8.9 && pip install . \
&& apt-get remove -y build-essential libbamtools-dev git libssl-dev \
&& apt-get autoremove -y
