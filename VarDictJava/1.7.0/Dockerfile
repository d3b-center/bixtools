FROM staphb/bcftools:1.10.2
LABEL maintainer="Daniel Miller (millerd15@chop.edu)"

ENV VARDICT_VERSION=1.7.0
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y wget openjdk-8-jdk r-base perl
RUN wget -q https://github.com/AstraZeneca-NGS/VarDictJava/releases/download/${VARDICT_VERSION}/VarDict-${VARDICT_VERSION}.zip && \
unzip VarDict-${VARDICT_VERSION}.zip && \
rm VarDict-${VARDICT_VERSION}.zip && \
apt remove -y wget && apt clean -y && apt autoremove -y

ENV PATH /data/VarDict-${VARDICT_VERSION}/bin:$PATH

COPY Dockerfile .
