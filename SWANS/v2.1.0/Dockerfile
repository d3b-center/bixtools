ARG PLATFORM=linux/amd64

FROM --platform=${PLATFORM} francothyroidlab/pond:1.2
LABEL maintainer="Miguel Brown <brownm28@chop.edu>"
LABEL description="Single-entity Workflow ANalysiS Pipeline (SWANS)"

ENV SWANS_VERSION=2.1.0

RUN curl -L https://github.com/FrancoResearchLab/SWANS/archive/refs/tags/v${SWANS_VERSION}.tar.gz | tar -xz  --wildcards '*/scripts/' --strip-components=3
