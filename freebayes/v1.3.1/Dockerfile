FROM ubuntu:18.04
LABEL maintainer="Daniel Miller (millerd15@email.chop.edu)"

ENV WGET_VERSION 1.19.4-1ubuntu2.2
ENV FREEBAYES_VERSION v1.3.1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update \
&& apt install -y \
wget=${WGET_VERSION} \
&& wget -q https://github.com/ekg/freebayes/releases/download/${FREEBAYES_VERSION}/freebayes-${FREEBAYES_VERSION} -O /bin/freebayes \
&& chmod 777 /bin/freebayes
