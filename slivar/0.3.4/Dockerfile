FROM staphb/bcftools:1.23.1

RUN apt update \
    && apt install -y \
       less vim \
       curl

RUN curl -sL https://github.com/brentp/slivar/releases/download/v0.3.4/pslivar > /usr/local/bin/pslivar \
    && chmod +x /usr/local/bin/pslivar

RUN curl -sL https://github.com/brentp/slivar/releases/download/v0.3.4/slivar > /usr/local/bin/slivar \
    && chmod +x /usr/local/bin/slivar

RUN mkdir -p /opt/slivar \
    && curl -sL https://raw.githubusercontent.com/brentp/slivar/refs/tags/v0.3.4/js/slivar-functions.js > /opt/slivar/slivar-functions.js

COPY Dockerfile .
