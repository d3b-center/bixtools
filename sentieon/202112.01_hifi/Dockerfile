FROM centos:8 as builder
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-Linux-* &&\
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-Linux-*

RUN yum upgrade -y \
  && yum -y install git wget bzip2 python3 \
  && yum install -y epel-release \
  && yum install -y boost169-devel zlib-devel
RUN yum -y groupinstall 'Development Tools'

RUN mkdir -p /opt/bcftools/ && \
    curl -L https://github.com/samtools/bcftools/releases/download/1.15.1/bcftools-1.15.1.tar.bz2 | \
      tar -jxf - -C /opt/bcftools/ --no-same-owner && \
      cd /opt/bcftools/bcftools-1.15.1/ && \
      ./configure --disable-bz2 --disable-lzma && make && make install
RUN mkdir -p /opt/samtools/ && \
    curl -L https://github.com/samtools/samtools/releases/download/1.15.1/samtools-1.15.1.tar.bz2 | \
      tar -jxf - -C /opt/samtools/ --no-same-owner && \
      cd /opt/samtools/samtools-1.15.1/ && \
      ./configure --without-curses --disable-bz2 --disable-lzma && make && make install
RUN wget -O /usr/local/bin/bedtools https://github.com/arq5x/bedtools2/releases/download/v2.30.0/bedtools.static.binary \
    && chmod a+x /usr/local/bin/bedtools
RUN mkdir -p /opt/sentieon/ && \
    wget -nv -O - "https://s3.amazonaws.com/sentieon-release/software/sentieon-genomics-202112.01.tar.gz" | \
      tar -zxf - -C /opt/sentieon/
RUN mkdir -p /opt/dnascope_hifi/ && \
    wget -nv -O - "https://s3.amazonaws.com/sentieon-release/other/DNAscopeHiFiBeta0.4.pipeline.tar.gz" | \
      tar -zxf - -C /opt/dnascope_hifi/

FROM centos:8
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-Linux-* &&\
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-Linux-*

RUN yum upgrade -y \
  && yum install -y which python3 \
  && yum install -y epel-release \
  && yum install -y jemalloc
COPY --from=builder /opt/sentieon/sentieon-genomics-202112.01 /opt/sentieon/sentieon-genomics-202112.01
COPY --from=builder /usr/local/bin/* /usr/local/bin/
COPY --from=builder /usr/local/libexec/bcftools/* /usr/local/libexec/bcftools/
COPY --from=builder /opt/dnascope_hifi/DNAscopeHiFiBeta0.4.pipeline /opt/dnascope_hifi/DNAscopeHiFiBeta0.4.pipeline

ENV PATH /opt/sentieon/sentieon-genomics-202112.01/bin/:$PATH
ENV LD_PRELOAD /usr/lib64/libjemalloc.so.2

ADD Dockerfile .
