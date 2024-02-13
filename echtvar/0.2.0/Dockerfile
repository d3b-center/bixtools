FROM staphb/bcftools:1.18

LABEL maintainer="Miguel Brown(brownm28@chop.edu)"
LABEL description="BCFtools image with echtvar binary. Supercedes 0.2.0-rc iamge that compiles from source"

RUN apt update \
    && apt install -y wget

ENV ECHTVAR_VERSION 0.2.0

RUN wget -O /bin/echtvar https://github.com/brentp/echtvar/releases/download/v${ECHTVAR_VERSION}/echtvar \
    && chmod +x /bin/echtvar

RUN apt remove -y wget \
    && apt clean -y \
    && apt autoremove -y

COPY Dockerfile .
