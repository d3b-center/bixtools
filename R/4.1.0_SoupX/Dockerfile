FROM r-base:4.1.0
LABEL maintainer="Nathan Johnson (johnsonn13@chop.edu)"

RUN R -e "install.packages(c('optparse', 'codetools', 'survival', 'plyr', 'zoo', 'data.table', 'htmlwidgets', 'lazyeval', 'reshape2', 'SoupX'), dependencies=TRUE, repos='http://cran.us.r-project.org')"

ADD Dockerfile .
