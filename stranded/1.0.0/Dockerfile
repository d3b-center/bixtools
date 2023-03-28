FROM staphb/samtools:1.16.1

RUN apt update && apt install -y curl python-is-python3 python3-pip git

RUN python -m pip install --upgrade pip && python -m pip install git+https://github.com/zoomzoom1011/how_are_we_stranded_here.git

WORKDIR /opt
ENV KALLISTO_VERSION 0.44.0
RUN curl -sL https://github.com/pachterlab/kallisto/releases/download/v${KALLISTO_VERSION}/kallisto_linux-v${KALLISTO_VERSION}.tar.gz | tar -xz && cp kallisto_linux-v${KALLISTO_VERSION}/kallisto /usr/local/bin

WORKDIR /
COPY Dockerfile .
