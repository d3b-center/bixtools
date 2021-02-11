FROM ubuntu:18.04
MAINTAINER Alex Sickler (sicklera@email.chop.edu)

ENV CELLRANGER_MAJ_VER 3.1
ENV CELLRANGER_VERSION 3.1.0

RUN apt update && apt install -y curl \
&& DL_LINK=`curl "https://support.10xgenomics.com/single-cell-gene-expression/software/downloads/${CELLRANGER_MAJ_VER}/?" -H 'Connection: keep-alive' \
--data-raw 'first_name=D3b&last_name=Center&email=bfx%40d3b.center&company=Children%27s+Hospital+of+Philadelphia&country=United+States&postalCode=19146&agreed=on&collectionConsent=Yes' | \
grep -Eo "cellranger-${CELLRANGER_VERSION}.tar.gz \"https:\S+\"" | head -n 1 | sed 's/\&amp\;/\&/g' | cut -f 2 -d ' ' | sed 's/\"//g'` \
&& echo $DL_LINK \
&& curl -o cellranger-${CELLRANGER_VERSION}.tar.gz $DL_LINK \
&& tar -zxvf cellranger-${CELLRANGER_VERSION}.tar.gz \
&& rm cellranger-${CELLRANGER_VERSION}.tar.gz \
&& apt remove -y curl

ENV PATH /cellranger-${CELLRANGER_VERSION}:$PATH
