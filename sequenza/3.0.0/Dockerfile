FROM sequenza/sequenza:3.0.0
LABEL maintainer="Daniel Miller (millerd15@chop.edu)"

USER root
RUN install2.r --error falcon getopt

# Sequenza3.0.0 uses R3.5.1; optparse 1.7.1 is the last version that works with that version
RUN wget https://cran.r-project.org/src/contrib/Archive/optparse/optparse_1.7.1.tar.gz \
    && R CMD INSTALL optparse_1.7.1.tar.gz \
    && rm optparse_1.7.1.tar.gz

COPY Dockerfile .
