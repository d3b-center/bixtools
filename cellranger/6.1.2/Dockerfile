FROM ubuntu:18.04
LABEL maintainer="Miguel Brown (brownm28@chop.edu)"

ENV CELLRANGER_MAJ_VER 6.1.2
ENV PATH="${PATH}:/cellranger-6.1.2"

RUN apt update && apt install -y curl \
&& curl -o cellranger-6.1.2.tar.gz "https://cf.10xgenomics.com/releases/cell-exp/cellranger-6.1.2.tar.gz?Expires=1678366778&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9jZi4xMHhnZW5vbWljcy5jb20vcmVsZWFzZXMvY2VsbC1leHAvY2VsbHJhbmdlci02LjEuMi50YXIuZ3oiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE2NzgzNjY3Nzh9fX1dfQ__&Signature=RFIHd-u17haNmjBug9bFkHDyh~oa7i7xMprSffMUzGW602zFTe07Yg4akJ-8pmEGuJKNXzuUEimK~~-gD0yYx5Isoq~PBJxF9MsAZXlZEy9NX9W7CUJPpPB9sTI656G17H49F8FAjN81kR3xxEczBCBM12jaGsNMVEp9wGCcKUy6wEkXjBJIikK4l1ztk4DkGJBr4c5iC2G95As2fCLp5KVv7V-I6CVpxr6k0rj4dqwqrJeGUJEFaLvyPxd1XmZsZTZlNCHj3zVNm5FivfCEoZq4-upjuUx6Tljd5MJoT9jaUQ0GG8gC9I1fJBnECKSd8og0MJ9Sq~fcEfbheH~JJg__&Key-Pair-Id=APKAI7S6A5RYOXBWRPDA" \
&& tar -xzf cellranger-6.1.2.tar.gz && rm cellranger-6.1.2.tar.gz \
&& apt remove -y curl

COPY Dockerfile .