ARG PLATFORM=linux/amd64

FROM --platform=${PLATFORM} ubuntu:24.04
LABEL maintainer="Miguel Brown (brownm28@chop.edu)"
LABEL description="Cellranger - parses download URL for specific version."

ENV CR_VERSION=9.0.1

# Get SW to autoparse URL
RUN apt update && apt install -y \
    curl \
    jq \
    unzip
RUN curl -sOL https://github.com/ericchiang/pup/releases/download/v0.4.0/pup_v0.4.0_linux_amd64.zip \
&& unzip pup_v0.4.0_linux_amd64.zip
# Get desired CR version and cp to local bin
RUN DL_URL=`curl "https://www.10xgenomics.com/support/software/cell-ranger/downloads/previous-versions" \
    |  ./pup 'text{}' \
    | jq -r --arg VERSION $CR_VERSION '.props.pageProps.softwareDownloads[] | select(.versionNumber == $VERSION ).downloadLinks[] | select(.filename | endswith(".gz")).url'` \
    && curl -sL $DL_URL \
    | tar xz \
    && mv cellranger-9.0.1 /usr/local/bin/ \
    && ln -s /usr/local/bin/cellranger-9.0.1/cellranger /usr/local/bin/cellranger
# Cleanup
RUN rm -rf pup_v0.4.0_linux_amd64.zip pup \
    && apt remove -y curl jq unzip \
    && apt autoremove -y \
    && apt autoclean
