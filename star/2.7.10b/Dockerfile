FROM ubuntu:22.04
LABEL maintainer="Miguel Brown (brownm28@chop.edu)"

ENV STAR_VERSION 2.7.10b

RUN apt update && apt install -y wget pigz \
&& cd /usr/local && wget https://github.com/alexdobin/STAR/archive/${STAR_VERSION}.tar.gz \
&& tar -zxf ${STAR_VERSION}.tar.gz \
&& mv STAR-${STAR_VERSION}/bin/Linux_x86_64_static/STAR /usr/bin/STAR \
&& rm ${STAR_VERSION}.tar.gz \
&& apt -y remove wget

COPY Dockerfile .
