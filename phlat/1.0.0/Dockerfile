FROM python:2.7.18
LABEL maintainer="Miguel Brown (brownm28@chop.edu)"
LABEL description="Python2.7 base with software needed for PHLAT."

ENV PYSAM=0.8.3
ENV BOWTIE=2.0.0-beta7
ENV PATH=$PATH:/usr/local/bin/bowtie2-${BOWTIE}

RUN python -m pip install pysam==${PYSAM}
RUN curl -L  https://sourceforge.net/projects/bowtie-bio/files/bowtie2/${BOWTIE}/bowtie2-${BOWTIE}-linux-x86_64.zip/download --output ${BOWTIE}-linux-x86_64.zip \
&& unzip -d /usr/local/bin/ ${BOWTIE}-linux-x86_64.zip && rm ${BOWTIE}-linux-x86_64.zip