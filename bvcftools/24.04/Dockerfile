FROM ubuntu:24.04
LABEL maintainer="Miguel Brown (brownm28@chop.edu)"

RUN apt update && apt install -y bcftools vcftools tabix bedtools && \
apt autoclean -y && apt autoremove -y