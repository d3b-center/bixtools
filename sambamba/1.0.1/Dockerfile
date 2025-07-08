FROM ubuntu:22.04
LABEL maintainer="Miguel Brown (brownm28@chop.edu)"

ENV SAMBAMBA_VERSION=1.0.1

RUN apt update && apt install -y wget \
&& wget -q https://github.com/biod/sambamba/releases/download/v${SAMBAMBA_VERSION}/sambamba-${SAMBAMBA_VERSION}-linux-amd64-static.gz \
&& gunzip sambamba-${SAMBAMBA_VERSION}-linux-amd64-static.gz \
&& chmod 755 sambamba-${SAMBAMBA_VERSION}-linux-amd64-static \
&& mv sambamba-${SAMBAMBA_VERSION}-linux-amd64-static /usr/bin/sambamba \
&& apt remove -y wget
