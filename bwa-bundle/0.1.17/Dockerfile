FROM ubuntu:16.04
RUN apt-get update && apt-get install -y \
	autoconf \
	automake \
	make \
	g++ \
	gcc \
	build-essential \ 
	zlib1g-dev \
        libgsl0-dev \
	libbz2-dev \
	liblzma-dev \
	python \
	curl \
	git \
	cmake \
	wget \
	libncurses5-dev \
	pkg-config \
	libtool \
	libncursesw5-dev

# Install BWA
WORKDIR /opt
RUN wget http://downloads.sourceforge.net/project/bio-bwa/bwa-0.7.17.tar.bz2
RUN tar -jxvf bwa-0.7.17.tar.bz2 
WORKDIR /opt/bwa-0.7.17
RUN make 
RUN cp -s /opt/bwa-0.7.17/bwa /bin

# Install samblaster
WORKDIR /opt
RUN git clone https://github.com/GregoryFaust/samblaster.git samblaster
WORKDIR /opt/samblaster
RUN make 
RUN cp -s /opt/samblaster/samblaster /bin

# Install sambamba
WORKDIR /opt
RUN mkdir sambamba_0.6.7
WORKDIR sambamba_0.6.7
RUN curl -L "https://github.com/lomereiter/sambamba/releases/download/v0.6.7/sambamba_v0.6.7_linux.tar.bz2" > sambamba_v0.6.7_linux.tar.bz2 
RUN tar xvf sambamba_v0.6.7_linux.tar.bz2 

# Install java
RUN apt-get -y install software-properties-common
RUN add-apt-repository ppa:webupd8team/java
RUN apt-get update
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN apt-get -y install oracle-java8-installer && apt-get clean
RUN echo "JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> /etc/environment

# Download picard-tools 
RUN wget https://github.com/broadinstitute/picard/releases/download/2.1.1/picard-tools-2.1.1.zip
RUN apt-get install unzip
RUN unzip picard-tools-2.1.1.zip

# Install R
RUN apt-get -y install r-base-core

# Install Perl
RUN apt-get -y install perl

# Install Samtools
WORKDIR /opt
RUN wget https://github.com/samtools/samtools/releases/download/1.7/samtools-1.7.tar.bz2 && \
tar jxvf samtools-1.7.tar.bz2
WORKDIR /opt/samtools-1.7
RUN make

# Install biobambam2
WORKDIR /opt
RUN wget https://github.com/gt1/biobambam2/releases/download/2.0.87-release-20180301132713/biobambam2-2.0.87-release-20180301132713-x86_64-etch-linux-gnu.tar.gz && tar xzf biobambam2-2.0.87-release-20180301132713-x86_64-etch-linux-gnu.tar.gz && rm -rf biobambam2-2.0.87-release-20180301132713-x86_64-etch-linux-gnu.tar.gz

COPY Dockerfile /opt/
