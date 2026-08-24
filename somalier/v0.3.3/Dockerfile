ARG PLATFORM=linux/amd64
FROM --platform=${PLATFORM} ubuntu:24.04

LABEL maintainer="Miguel Brown <brownm28@chop.edu>"

ENV DEBIAN_FRONTEND=noninteractive
ENV SOMALIER_VERSION=v0.3.3

RUN apt update && apt install -y curl

RUN curl -L https://github.com/brentp/somalier/releases/download/${SOMALIER_VERSION}/somalier \
> /usr/local/bin/somalier && \
chmod 755 /usr/local/bin/somalier
RUN apt remove -y curl && apt clean && rm -rf /var/lib/apt/lists/*

COPY Dockerfile /Dockerfile
