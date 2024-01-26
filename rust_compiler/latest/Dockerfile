FROM ubuntu:22.04
LABEL maintainer="brownm28@chop.edu"
LABEL description="Formalizing Dan's efforts creating a dockerfile to compile rust code"

RUN apt update && apt install -y curl build-essential pkg-config libssl-dev cmake vim less

ENV RUSTUP_HOME=/etc/skel/.rustup
ENV CARGO_HOME=/etc/skel/.cargo
RUN curl -fsSL https://sh.rustup.rs | sh -s -- -y --default-toolchain=stable --profile=minimal
# Initialize environment variables
ENV PATH="${CARGO_HOME}/env:${PATH}" 
RUN /etc/skel/.cargo/bin/rustup component add rustfmt clippy
RUN /etc/skel/.cargo/bin/cargo install bindgen-cli cbindgen cargo-audit cargo-outdated

COPY Dockerfile ./