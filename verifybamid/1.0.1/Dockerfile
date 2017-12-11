FROM alpine:3.6
MAINTAINER Yuankun Zhu (zhuy@email.chop.edu)

ENV VERIFYBAMID_VERSION 1.0.1

RUN apk add --no-cache build-base gcc cmake git wget ca-certificates autoconf bash zlib-dev bzip2-dev xz-dev ncurses-dev curl-dev openssl-dev; \
wget -q https://github.com/Griffan/VerifyBamID/archive/${VERIFYBAMID_VERSION}.tar.gz; \
tar -zxf ${VERIFYBAMID_VERSION}.tar.gz && cd VerifyBamID-${VERIFYBAMID_VERSION}/ && mkdir build && cd build; \
cmake .. && make; \
mv ../bin/VerifyBamID /bin/ && rm -rf /${VERIFYBAMID_VERSION}.tar.gz /VerifyBamID; \
apk del build-base cmake git wget ca-certificates autoconf bash curl-dev
