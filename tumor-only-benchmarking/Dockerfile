FROM ubuntu:22.04
LABEL maintainer="Saksham Phul (phuls@chop.edu)"
LABEL description="RTG tool for benchmarking vcf files"

#RUN export ant="home/apache-ant-1.9.16/bin/ant"

RUN apt update -y && apt install default-jre wget -y && apt install apache2 git -y && cd home/
RUN wget -c https://dlcdn.apache.org//ant/binaries/apache-ant-1.9.16-bin.tar.gz -O - | tar -xz 

RUN cp apache-ant-1.9.16/bin/ant /bin/ && cp -R apache-ant-1.9.16/lib/* /lib/
RUN git clone https://github.com/RealTimeGenomics/rtg-tools.git && cd rtg-tools && ant zip-nojre
