ARG PLATFORM=linux/amd64
FROM --platform=${PLATFORM} pgc-images.sbgenomics.com/d3b-bixu/samtools:base

LABEL maintainer="Miguel Brown <brownm28@chop.edu>"
LABEL description="Multi-cpu compilations. Generic also available"

ENV SAMTOOLS_VERSION=1.20
ENV HTSLIB_VERSION=1.20

ENV GENERIC_PREFIX=/opt/samtools-1.20
ENV C5_PREFIX=/opt/samtools-1.20-skylake-avx512
ENV C6_PREFIX=/opt/samtools-1.20-icelake-server
ENV C7_PREFIX=/opt/samtools-1.20-sapphirerapids

RUN curl -sL https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2 \
 | tar xjf -
# Build htslibs
WORKDIR /samtools-${SAMTOOLS_VERSION}/htslib-${HTSLIB_VERSION}/
# Generic
RUN ./configure --prefix=${GENERIC_PREFIX} \
&& make -j"$(nproc)" \
&& make install \
&& mv libhts.so* ${GENERIC_PREFIX}/bin/ \
&& make clean
# C5
RUN ./configure --prefix=${C5_PREFIX} CFLAGS='-O3 -march=skylake-avx512' \
&& make -j"$(nproc)" \
&& make install \
&& mv libhts.so* ${C5_PREFIX}/bin/ \
&& make clean
# C6
RUN ./configure --prefix=${C6_PREFIX} CFLAGS='-O3 -march=icelake-server' \
&& make -j"$(nproc)" \
&& make install \
&& mv libhts.so* ${C6_PREFIX}/bin/ \
&& make clean
# C7
RUN ./configure --prefix=${C7_PREFIX} CFLAGS='-O3 -march=sapphirerapids' \
&& make -j"$(nproc)" \
&& make install \
&& mv libhts.so* ${C7_PREFIX}/bin/ \
&& make clean

WORKDIR /samtools-${SAMTOOLS_VERSION}
# Generic
RUN ./configure --prefix=${GENERIC_PREFIX} \
&& make -j"$(nproc)" \
&& make install \
&& make clean
# C5
RUN ./configure --prefix=${C5_PREFIX} CFLAGS='-O3 -march=skylake-avx512' \
&& make -j"$(nproc)" \
&& make install \
&& make clean
# C6
RUN ./configure --prefix=${C6_PREFIX} CFLAGS='-O3 -march=icelake-server' \
&& make -j"$(nproc)" \
&& make install \
&& make clean
# C7
RUN ./configure --prefix=${C7_PREFIX} CFLAGS='-O3 -march=sapphirerapids' \
&& make -j"$(nproc)" \
&& make install \
&& make clean
WORKDIR /
RUN rm -rf samtools*
COPY Dockerfile samtools /usr/local/bin