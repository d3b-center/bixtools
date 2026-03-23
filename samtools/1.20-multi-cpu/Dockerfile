ARG PLATFORM=linux/amd64
FROM --platform=${PLATFORM} samtools:base

LABEL maintainer="Miguel Brown <brownm28@chop.edu>"
LABEL description="Multi-cpu compilations. Generic also available"

ENV SAMTOOLS_VERSION=1.20
ENV HTSLIB_VERSION=1.20

ENV GENERIC_PREFIX=/opt/samtools-1.20
ENV C5_PREFIX=/opt/samtools-1.20-skylake-c5
ENV C6_PREFIX=/opt/samtools-1.20-icelake-server-c6
ENV C7_PREFIX=/opt/samtools-1.20-sapphirerapids-c7


RUN curl -sL https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2 \
 tar xjf -
# Build generic
WORKDIR /samtools-${SAMTOOLS_VERSION}/htslib-${HTSLIB_VERSION}/
RUN ./configure --prefix=${GENERIC_PREFIX} && make -j"$(nproc)" && cp htsfile libhts.so* tabix bgzip ${GENERIC_PREFIX}/bin/

WORKDIR /samtools-${SAMTOOLS_VERSION}
RUN ./configure --prefix=${GENERIC_PREFIX} && make -j"$(nproc)" && cp samtools ${GENERIC_PREFIX}/bin/