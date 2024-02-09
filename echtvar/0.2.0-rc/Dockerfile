FROM staphb/bcftools:1.18

LABEL maintainer="Miguel Brown (brownm28@email.chop.edu)"
LABEL description="Build RC version of echtvar"

RUN apt update && apt install -y git curl build-essential pkg-config libssl-dev cmake vim less
# install rust compiler
RUN cd / && curl -fsSL https://sh.rustup.rs | sh -s -- -y --default-toolchain=stable --profile=minimal
# I guess running a dumb command resets the env? It could not find the binaries until then
RUN echo "Reset env with this"
RUN /root/.cargo/bin/rustup component add rustfmt clippy && /root/.cargo/bin/cargo install bindgen-cli cbindgen cargo-audit cargo-outdated
# install rc from source code
RUN git clone https://github.com/brentp/echtvar && cd echtvar && git checkout 45b468eaed2119a4872bfb3ea04aea7ec7d9e11b \
&& /root/.cargo/bin/cargo build --target x86_64-unknown-linux-gnu --verbose --release && cp target/x86_64-unknown-linux-gnu/release/echtvar /bin
# cleanup pakcage and binaries
RUN apt remove -y build-essential && apt -y autoclean

COPY Dockerfile .
