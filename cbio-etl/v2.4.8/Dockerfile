ARG PLATFORM=linux/amd64
FROM --platform=${PLATFORM} pgc-images.sbgenomics.com/d3b-bixu/cbio-etl-base:v1.0.0

LABEL maintainer="Miguel Brown <brownm28@chop.edu>"
LABEL description="cbio-etl"

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /

ENV CBIO_ETL_VERSION=2.4.8
ENV CBIO_REFS_VERSION=1.1.1

RUN git clone https://github.com/kids-first/kf-cbioportal-etl.git \
    && cd kf-cbioportal-etl \
    && git checkout v${CBIO_ETL_VERSION} \
    && curl -L https://github.com/kids-first/kf-cbioportal-etl-refs/archive/refs/tags/v${CBIO_REFS_VERSION}.tar.gz | tar -xz -C cbioportal_etl/ --wildcards '*REFS/*' --strip-components=1 \
    && curl -L https://github.com/kids-first/kf-cbioportal-etl-refs/archive/refs/tags/v${CBIO_REFS_VERSION}.tar.gz | tar -xz -C cbioportal_etl/ --wildcards '*STUDY_CONFIGS/*' --strip-components=1 \
    && pip install --break-system-packages .
    
COPY Dockerfile .
