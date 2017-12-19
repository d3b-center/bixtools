FROM alpine:3.6
MAINTAINER Yuankun Zhu (zhuy@email.chop.edu)

ENV PICARD_VERSION 2.8.3

RUN apk add --no-cache R openjdk8-jre ca-certificates wget; \
wget -q https://github.com/broadinstitute/picard/releases/download/${PICARD_VERSION}/picard.jar; \
apk del ca-certificates wget
