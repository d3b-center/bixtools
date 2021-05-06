FROM ubuntu:18.04
LABEL maintainer="Alex Sickler (sicklera@email.chop.edu)"

ENV CELLRANGER_MAJ_VER 3.1

RUN apt update && apt install -y curl \
&& DL_INFO=$(/bin/bash -c "set -o pipefail && curl \"https://support.10xgenomics.com/single-cell-gene-expression/software/downloads/${CELLRANGER_MAJ_VER}/?\" -H 'Connection: keep-alive' \
--data-raw 'first_name=D3b&last_name=Center&email=bfx%40d3b.center&company=Children%27s+Hospital+of+Philadelphia&country=United+States&postalCode=19146&agreed=on&collectionConsent=Yes' | \
grep -Eo \"cellranger-${CELLRANGER_MAJ_VER}.[0-9]+.tar.gz \\\"https:\S+\\\"\" | head -n 1 | sed 's/\&amp\;/\&/g' | sed 's/\"//g'") \
&& CELLRANGER_VERSION=$(echo $DL_INFO | cut -f 1 -d ' ') \
&& CELLRANGER_VERSION=${CELLRANGER_VERSION%.tar.gz} \
&& echo ${CELLRANGER_VERSION} \
&& DL_LINK=$(echo $DL_INFO | cut -f 2 -d ' ') \
&& curl -o ${CELLRANGER_VERSION}.tar.gz $DL_LINK \
&& tar -zxvf ${CELLRANGER_VERSION}.tar.gz \
&& rm ${CELLRANGER_VERSION}.tar.gz \
&& ln -s ${CELLRANGER_VERSION} cellranger \
&& apt remove -y curl

ENV PATH /cellranger:$PATH

ADD Dockerfile .
