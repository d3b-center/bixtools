FROM quay.io/biocontainers/pysam:0.23.3--py313h7c062c9_1

RUN python -m pip install --upgrade pip && python -m pip install numpy

RUN wget -O /usr/bin/consensus_merge.py https://raw.githubusercontent.com/kids-first/kf-somatic-workflow/ee721ad1a0e438f11ab329d17bfd829aaf3cb27b/scripts/consensus_merge.py && \
    chmod +x /usr/bin/consensus_merge.py

ADD Dockerfile .
