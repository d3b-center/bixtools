FROM python:2.7.18
LABEL maintainer="Miguel Brown (brownm28@chop.edu)"
LABEL description="Python2.7 base with software needed for PHLAT."

ENV PYSAM=0.8.3
ENV BOWTIE=2.0.0-beta7
ENV PATH=$PATH:/usr/local/bin/bowtie2-${BOWTIE}
ENV COMMIT=5d977ee7b81f075968589c5e5bac76d83ff4287d

RUN python -m pip install pysam==${PYSAM}
RUN curl -L  https://sourceforge.net/projects/bowtie-bio/files/bowtie2/${BOWTIE}/bowtie2-${BOWTIE}-linux-x86_64.zip/download --output ${BOWTIE}-linux-x86_64.zip \
&& unzip -d /usr/local/bin/ ${BOWTIE}-linux-x86_64.zip && rm ${BOWTIE}-linux-x86_64.zip
RUN apt update && apt install -y git
RUN git clone https://github.com/d3b-center/HLA-Typing-Dev && cd HLA-Typing-Dev && git checkout ${COMMIT}

COPY Dockerfile .