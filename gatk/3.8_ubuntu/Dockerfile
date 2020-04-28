FROM ubuntu:18.04
LABEL maintainer="Miguel Brown (brownm28@email.chop.edu)"

ENV GATK3_VERSION 3.8

RUN apt update && apt install -y openjdk-8-jdk tabix curl gnupg
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
&& curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg add - \
&& apt update && apt install -y google-cloud-sdk
RUN gsutil cp gs://gatk-software/package-archive/gatk/GenomeAnalysisTK-${GATK3_VERSION}-0-ge9d806836.tar.bz2 . \
&& tar -xjf GenomeAnalysisTK-${GATK3_VERSION}-0-ge9d806836.tar.bz2 && mv GenomeAnalysisTK-${GATK3_VERSION}-0-ge9d806836/GenomeAnalysisTK.jar . \
&& rm -rf GenomeAnalysisTK-${GATK3_VERSION}-*/ GenomeAnalysisTK-${GATK3_VERSION}-0-ge9d806836.tar.bz2 \
&& apt remove -y curl google-cloud-sdk