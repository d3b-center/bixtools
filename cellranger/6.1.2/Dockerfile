FROM ubuntu:20.04
LABEL maintainer="Miguel Brown (brownm28@chop.edu)"

ENV CELLRANGER_MAJ_VER 6.1.2
ENV PATH="${PATH}:/cellranger-6.1.2"

RUN apt update && apt install -y curl \
&& curl -sL  "https://cf.10xgenomics.com/releases/cell-exp/cellranger-${CELLRANGER_MAJ_VER}.tar.gz?Expires=1687836169&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9jZi4xMHhnZW5vbWljcy5jb20vcmVsZWFzZXMvY2VsbC1leHAvY2VsbHJhbmdlci02LjEuMi50YXIuZ3oiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE2ODc4MzYxNjl9fX1dfQ__&Signature=hP3Qa5KzkyzLID5E1xHUBUBRnhW5viNgzMiYDfLUHaXAL3rwgrD5x8Ix7lbwvcUe9NLLV92be9byFrvqlL5Mo4T7okxHNs41TsaPnWFzksmuBD4PlmBKexPmG~9x~9l3o1~JtOuZFj7ArbVOM1Mjr80wgoppa9qDeoMAgqhxrCQ9e2mRVaTEjVb03Op7uuCgUWHNgcfmPrfpQRyNUmLNHhsw0Nc2Vl6-c9UrYgVF~Q-bKUrJN7mKYsKQi8GN2NQCiqtjLxqd0KDZMGmdYSzthSX3Hmbg4xEwakCECg6qqDeQBfsHVqwDx7McPP755HNKJ9fRwWJsGsCHgcwADRY9Ng__&Key-Pair-Id=APKAI7S6A5RYOXBWRPDA" | tar -xz  \
&& apt remove -y curl

COPY Dockerfile .