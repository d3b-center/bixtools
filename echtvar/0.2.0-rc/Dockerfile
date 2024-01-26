FROM pgc-images.sbgenomics.com/brownm28/rust_compiler:latest

LABEL maintainer="Miguel Brown (brownm28@email.chop.edu)"
LABEL description="Build RC version of echtvar"

RUN apt update \
    && apt install -y git bcftools
RUN git clone https://github.com/migbro/echtvar && git checkout v0.2.0-rc
RUN cd echtvar && cargo build --target x86_64-unknown-linux-gnu --verbose --release && cp target/x86_64-unknown-linux-gnu/release/echtvar /bin
RUN apt remove build-essential && apt autoclean