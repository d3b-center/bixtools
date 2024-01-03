FROM staphb/samtools:1.16.1

RUN apt update && apt install -y curl python-is-python3 python3-pip git

WORKDIR /opt
ENV RSEQC_VERSION 5.0.1
RUN curl -sL https://sourceforge.net/projects/rseqc/files/RSeQC-${RSEQC_VERSION}.tar.gz/download | tar -xz && python -m pip install /opt/RSeQC-${RSEQC_VERSION}
ENV PATH $PATH:/opt/RSeQC-${RSEQC_VERSION}/scripts

RUN python -m pip install --upgrade pip \
    && python -m pip install pandas \
    && python -m pip install --no-deps git+https://github.com/zoomzoom1011/how_are_we_stranded_here.git

ENV KALLISTO_VERSION 0.44.0
RUN curl -sL https://github.com/pachterlab/kallisto/releases/download/v${KALLISTO_VERSION}/kallisto_linux-v${KALLISTO_VERSION}.tar.gz | tar -xz && cp kallisto_linux-v${KALLISTO_VERSION}/kallisto /usr/local/bin

WORKDIR /
COPY Dockerfile .
