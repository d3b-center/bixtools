FROM ubuntu:18.04
LABEL maintainer="Miguel Brown (brownm28@email.chop.edu)"
LABEL developer="Jessica Wong wongj4@email.chop.edu"

ENV DEBIAN_FRONTEND=noninteractive
ENV CANVAS_VERSION=1.11.0

RUN apt update && apt install -y wget build-essential curl sudo zip tabix && \
wget https://github.com/Illumina/canvas/releases/download/v${CANVAS_VERSION}/Canvas-${CANVAS_VERSION}_x64.zip && \
unzip Canvas-${CANVAS_VERSION}_x64.zip && \
rm Canvas-${CANVAS_VERSION}_x64.zip && \
apt install -y  gnupg ca-certificates && \
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \
echo "deb https://download.mono-project.com/repo/ubuntu stable-bionic main" | sudo tee /etc/apt/sources.list.d/mono-official-stable.list && \
apt -y install mono-devel
RUN apt -y install mono-complete mono-dbg ca-certificates-mono mono-xsp4