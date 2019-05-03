FROM ubuntu:bionic
LABEL maintainer="Sebastian Uhrig @ DKFZ"
LABEL modified_by="Miguel Brown brownm28@email.chop.edu"

ENV ARRIBA_VERSION 1.1.0

# install dependencies
RUN export DEBIAN_FRONTEND=noninteractive && \
apt-get update -y && \
apt-get install -y samtools r-base rna-star wget libcurl4-openssl-dev libxml2-dev && \
Rscript -e 'install.packages("circlize", repos="http://cran.r-project.org"); source("https://bioconductor.org/biocLite.R"); biocLite(c("GenomicRanges", "GenomicAlignments"))'

# install arriba
RUN wget -q https://github.com/suhrig/arriba/releases/download/v${ARRIBA_VERSION}/arriba_v${ARRIBA_VERSION}.tar.gz && tar -xzf arriba_v${ARRIBA_VERSION}.tar.gz && rm arriba_v${ARRIBA_VERSION}.tar.gz

# make wrapper script for download_references.sh
RUN echo '#!/bin/bash\n\
cd /references\n\
/arriba*/download_references.sh $1 $2 && \\\n\
cp /arriba*/database/*${1%+*}* /references' > /usr/local/bin/download_references.sh && \
chmod a+x /usr/local/bin/download_references.sh

# make wrapper script for run_arriba.sh
RUN echo '#!/bin/bash\n\
cd /output\n\
/arriba*/run_arriba.sh /references/STAR_index_* /references/*.gtf /references/*.fa /references/blacklist_*.tsv.gz /read1.fastq.gz /read2.fastq.gz ${1-8}' > /usr/local/bin/arriba.sh && \
chmod a+x /usr/local/bin/arriba.sh

# make wrapper script for draw_fusions.R
RUN echo '#!/bin/bash\n\
Rscript /arriba*/draw_fusions.R --annotation=$(ls /references/*.gtf) --fusions=/fusions.tsv --output=/output/fusions.pdf --proteinDomains=$(ls /references/protein_domains_*.gff3) --alignments=/Aligned.sortedByCoord.out.bam --cytobands=$(ls /references/cytobands_*.tsv)' > /usr/local/bin/draw_fusions.sh && \
chmod a+x /usr/local/bin/draw_fusions.sh
