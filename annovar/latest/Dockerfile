FROM centos
MAINTAINER Antony Le Bechec <antony.lebechec@gmail.com>

LABEL MODIFIED_BY brownm28@email.chop.edu

##############################################################
# Dockerfile Version:   1.0
# Software:             ANNOVAR
# Software Version:     current
# Software Website:     http://www.openbioinformatics.org/annovar/
# Description:          ANNOVAR
##############################################################


#######
# YUM #
#######

#RUN yum update -y
RUN yum install -y  wget \
                    perl \
                    bzip2 \
                    gcc \
                    ncurses-devel \
                    zlib-devel \
                    bzip2-devel \
                    xz-devel \
                    make;
#RUN yum clean all ;



###########
# ANNOVAR #
###########

ENV TOOLS=/home/TOOLS/tools
ENV TOOL_NAME=annovar
ENV TOOL_VERSION=current
ENV TARBALL_LOCATION=http://www.openbioinformatics.org/annovar/download/0wgxR2rIVP/
ENV TARBALL=annovar.latest.tar.gz
ENV TARBALL_FOLDER=$TOOL_NAME
ENV DEST=$TOOLS/$TOOL_NAME/$TOOL_VERSION
ENV PATH=$TOOLS/$TOOL_NAME/$TOOL_VERSION/bin:$PATH
# http://www.openbioinformatics.org/annovar/download/0wgxR2rIVP/annovar.latest.tar.gz


# INSTALL
RUN wget $TARBALL_LOCATION/$TARBALL ; \
    tar xf $TARBALL --wildcards *pl ; \
    rm -rf $TARBALL ; \
    cd $TARBALL_FOLDER ; \
    mkdir -p $TOOLS/$TOOL_NAME/$TOOL_VERSION/bin ; \
    cp *pl $TOOLS/$TOOL_NAME/$TOOL_VERSION/bin/ -R ; \
    mkdir /databases ; \
    ln -s /databases/ $TOOLS/$TOOL_NAME/$TOOL_VERSION/bin/humandb ; \
    cd ../ ; \
    rm -rf $TARBALL_FOLDER ;

####################
# samtools, htslib #
####################
ENV SAMTOOLS_VERSION 1.9
ENV HTSLIB_VERSION 1.9
RUN cd /; \
    wget -q https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2; \
    tar xjf samtools-${SAMTOOLS_VERSION}.tar.bz2; \
    cd /samtools-${SAMTOOLS_VERSION}/ && ./configure && make; \
    mv /samtools-${SAMTOOLS_VERSION}/samtools /bin/; \
    cd htslib-${HTSLIB_VERSION}/ && ./configure && make; \
    mv htsfile libhts.so* tabix bgzip /bin; \
    rm -rf /samtools*;

#######
# YUM #
#######

RUN yum erase -y  wget ;

RUN yum clean all ;

WORKDIR "$TOOLS/$TOOL_NAME/current/bin"

CMD ["/bin/bash"]