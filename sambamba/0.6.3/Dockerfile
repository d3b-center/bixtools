FROM ubuntu:16.04

# Install required packages
RUN apt-get update && apt-get install -y \
	autoconf \
	automake \
	make \
	g++ \
	gcc \
	build-essential \ 
	zlib1g-dev \
	libgsl0-dev \
	python \
	curl 

WORKDIR /opt
RUN mkdir sambamba_0.6.3
WORKDIR sambamba_0.6.3
RUN curl -L "https://github.com/lomereiter/sambamba/releases/download/v0.6.3/sambamba_v0.6.3_linux.tar.bz2" > sambamba_v0.6.3_linux.tar.bz2 
RUN tar xvf sambamba_v0.6.3_linux.tar.bz2 

COPY Dockerfile /opt/
