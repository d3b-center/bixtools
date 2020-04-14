FROM ubuntu:18.04
MAINTAINER Alex Sickler (sicklera@email.chop.edu)

ENV CELLRANGER_VERSION 3.1

RUN apt update && apt install -y curl; \
curl -o cellranger-3.1.0.tar.gz "http://cf.10xgenomics.com/releases/cell-exp/cellranger-3.1.0.tar.gz?Expires=1586907170&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cDovL2NmLjEweGdlbm9taWNzLmNvbS9yZWxlYXNlcy9jZWxsLWV4cC9jZWxscmFuZ2VyLTMuMS4wLnRhci5neiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTU4NjkwNzE3MH19fV19&Signature=T~TtPJd~qhtfWyH~B1c7c1XlTChxYy1eOPea2gv-M-lLgphEwMy~WxJ9k8rsthL7s~9oTiTzrPpweuQ~nvLVoQimxacw29uJYrzj3eUogvfVrCVlRWOM4zpzDrpqlDPrExQAtho2YqOxmSvrbwjBSGaEv5hashd2nxToh38baLOWTiJuNyVI4jI-rVJhEoBCCm-ECl~ZUEzxZs8h1f7p5XHKSULswpofQp9F-SGE0PNg2Im9kVtEHB5DpLfA9C9H3sgJ0a0ITTUSFGFnOwTLmz5Ji~mga1sjvGbi5Fmf~4vatpyvcQ~g1kh8xP8l8twL7e4iv6lWKi5i6Drfx22U-g__&Key-Pair-Id=APKAI7S6A5RYOXBWRPDA"; \
tar -zxvf cellranger-3.1.0.tar.gz; \
apt remove -y curl

ENV PATH /cellranger-3.1.0:$PATH
