FROM ubuntu:18.04
LABEL maintainer="Miguel Brown (brownm28@email.chop.edu)"

ENV SAMBAMBA_VERSION 0.7.1

RUN apt update && apt install -y wget; \
wget -q https://github.com/biod/sambamba/releases/download/v${SAMBAMBA_VERSION}/sambamba-${SAMBAMBA_VERSION}-linux-static.gz; \
gunzip sambamba-${SAMBAMBA_VERSION}-linux-static.gz; \
chmod 755 sambamba-${SAMBAMBA_VERSION}-linux-static; \
mv sambamba-${SAMBAMBA_VERSION}-linux-static /usr/bin/sambamba; \
apt remove -y wget
