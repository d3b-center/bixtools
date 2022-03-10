FROM ubuntu:focal
LABEL maintainer="Sebastian Uhrig @ DKFZ"
LABEL modified_by="Miguel Brown brownm28@email.chop.edu"

ENV ARRIBA_VERSION 2.2.1

# install dependencies
RUN export DEBIAN_FRONTEND=noninteractive && \
apt update -y && \
apt install -y --no-install-recommends wget ca-certificates samtools r-base r-cran-circlize r-bioc-genomicalignments r-bioc-genomicranges libxml2 && \
apt clean && rm -rf /var/lib/apt/lists/*

# install arriba
RUN wget -q https://github.com/suhrig/arriba/releases/download/v${ARRIBA_VERSION}/arriba_v${ARRIBA_VERSION}.tar.gz && tar -xzf arriba_v${ARRIBA_VERSION}.tar.gz && rm arriba_v${ARRIBA_VERSION}.tar.gz

# make wrapper script for download_references.sh
RUN echo '#!/bin/bash\n\
cd /references\n\
/arriba*/download_references.sh $1 && \\\n\
ASSEMBLY=$(sed -e "s/viral+.*//" -e "s/+.*//" <<<"$1") && \\\n\
cp /arriba*/database/*$ASSEMBLY* /references' > /usr/local/bin/download_references.sh && \
chmod a+x /usr/local/bin/download_references.sh


# make wrapper script for draw_fusions.R
RUN echo '#!/bin/bash\n\
Rscript /arriba*/draw_fusions.R --annotation=$(ls /references/*.gtf) --fusions=/fusions.tsv --output=/output/fusions.pdf --proteinDomains=$(ls /references/protein_domains_*.gff3) --alignments=/Aligned.sortedByCoord.out.bam --cytobands=$(ls /references/cytobands_*.tsv)' > /usr/local/bin/draw_fusions.sh && \
chmod a+x /usr/local/bin/draw_fusions.sh

ADD Dockerfile .