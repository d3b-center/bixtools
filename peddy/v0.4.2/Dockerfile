FROM ubuntu:16.04

LABEL maintainer="Alex Sickler (sicklera@email.chop.edu)"

ENV PEDDY_VERSION v0.4.2
ENV BACKPORTS_VERSION 1.5
ENV NUMPY_VERSION 1.14.5
ENV CLICK_VERSION 6.7
ENV COLOREDLOGS_VERSION 10.0
ENV CYCLER_VERSION 0.10.0
ENV CYTHON_VERSION 0.28.5
ENV DECORATOR_VERSION 4.3.0
ENV HUMANFRIENDLY_VERSION 4.16.1
ENV KIWISOLVER_VERSION 1.0.1
ENV MATPLOTLIB_VERSION 2.2.3
ENV MONOTONIC_VERSION 1.5
ENV NETWORKX_VERSION 2.1
ENV PANDAS_VERSION 0.23.4
ENV PYPARSING_VERSION 2.2.0
ENV DATEUTIL_VERSION 2.7.3
ENV PYTZ_VERSION 2018.5
ENV SCIKIT_VERSION 0.19.2
ENV SCIPY_VERSION 1.1.0
ENV SEABORN_VERSION 0.9.0
ENV SIX_VERSION 1.11.0
ENV SUBPROCESS_VERSION 3.5.2
ENV TOOLSHED_VERSION 0.4.6
ENV CYVCF2_VERSION 0.8.9

RUN apt-get update && apt upgrade -y \
&&  apt-get install -y python git build-essential libbamtools-dev python-pip python-dev build-essential libssl-dev \
&& pip install backports.functools-lru-cache==${BACKPORTS_VERSION} numpy==${NUMPY_VERSION} click==${CLICK_VERSION} coloredlogs==${COLOREDLOGS_VERSION} \
cycler==${CYCLER_VERSION} Cython==${CYTHON_VERSION} decorator==${DECORATOR_VERSION} humanfriendly==${HUMANFRIENDLY_VERSION} kiwisolver==${KIWISOLVER_VERSION} \
matplotlib==${MATPLOTLIB_VERSION} monotonic==${MONOTONIC_VERSION} networkx==${NETWORKX_VERSION} pandas==${PANDAS_VERSION} pyparsing==${PYPARSING_VERSION} \
python-dateutil==${DATEUTIL_VERSION} pytz==${PYTZ_VERSION} scikit-learn==${SCIKIT_VERSION} scipy==${SCIPY_VERSION} seaborn==${SEABORN_VERSION} six==${SIX_VERSION} \
subprocess32==${SUBPROCESS_VERSION} toolshed==${TOOLSHED_VERSION} \
&& pip install cyvcf2==${CYVCF2_VERSION} \
&& git clone --depth 1 --branch ${PEDDY_VERSION} https://github.com/brentp/peddy && cd /peddy && pip install . \
&& apt-get remove -y build-essential libbamtools-dev git libssl-dev \
&& apt-get autoremove -y
