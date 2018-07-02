FROM alpine:3.6
MAINTAINER Miguel Brown (brownm28@email.chop.edu)

ENV SNPEFF_VERSION 4_3t

RUN apk add --update --no-cache openjdk8-jre ca-certificates wget libc6-compat; \
wget -q https://sourceforge.net/projects/snpeff/files/snpEff_v${SNPEFF_VERSION}_core.zip/download; \
unzip download && rm download; \
apk del ca-certificates wget
