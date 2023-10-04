FROM staphb/bcftools:1.18

LABEL maintainer="Daniel Miller (millerd15@email.chop.edu)"
LABEL description="BCFtools image with echtvar binary"

RUN apt update \
    && apt install -y wget

ENV ECHTVAR_VERSION 0.1.9

RUN wget -O /bin/echtvar https://github.com/brentp/echtvar/releases/download/v${ECHTVAR_VERSION}/echtvar \
    && chmod +x /bin/echtvar

RUN apt remove -y wget \
    && apt clean -y \
    && apt autoremove -y

COPY Dockerfile .
