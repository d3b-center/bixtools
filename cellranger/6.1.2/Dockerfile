FROM ubuntu:20.04
LABEL maintainer="Miguel Brown (brownm28@chop.edu)"

ENV CELLRANGER_MAJ_VER 6.1.2
ENV PATH="${PATH}:/cellranger-6.1.2"

RUN apt update && apt install -y curl \
&& curl -o cellranger-6.1.2.tar.gz "https://cf.10xgenomics.com/releases/cell-exp/cellranger-6.1.2.tar.gz?Expires=1686814325&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9jZi4xMHhnZW5vbWljcy5jb20vcmVsZWFzZXMvY2VsbC1leHAvY2VsbHJhbmdlci02LjEuMi50YXIuZ3oiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE2ODY4MTQzMjV9fX1dfQ__&Signature=UGfU3S6u-zviFeOWH2WvVIlwWA-A0PIElJ9fg9Uw~2vWiYnV~yO~jt-1omIU1W0Q5kDgUr9tdrpU7bSiiEscXdHpxFyGj3BNNU2-8LKiJDVRRRv4tG5K2Gnrb3LDqQjaDGGb4rMMHTa310UwHKgZ-BjQRicEWMgQcDMkenHF5TrUg80yHf6LrHOC2ANssd7n5z2cshHLRpSvdDp7zI6ToFfVca56nV2kN0~ySF2mmJfPIAQCyCDl-W6FojLzb8C9QJtvqfw-8SHOIRMGQ3NC2-y2RTmqWJ4TGeiTCyMTNSydfSpN9hu5eeVGtq7a8~Vd5Lt7Iui~-Vso0uIT47XhpQ__&Key-Pair-Id=APKAI7S6A5RYOXBWRPDA" \
&& tar -xzf cellranger-6.1.2.tar.gz && rm cellranger-6.1.2.tar.gz \
&& apt remove -y curl

COPY Dockerfile .