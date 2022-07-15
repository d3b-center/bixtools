FROM pypy:3
LABEL maintainer="Saksham Phul <phuls@chop.edu>"
LABEL description="PyPy docker image with numpy, pandas, and scipy with their dependencies"

WORKDIR /home

ENV NUMPY_VERSION 1.23.0
ENV SCIPY_VERSION 1.8.1
ENV PANDAS_VERSION 1.4.3
ENV PYREADR_VERSION 0.4.6
ENV LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:/opt/OpenBLAS/lib" 

RUN     apt update \ 
    && apt install gfortran gfortran-10 libgfortran-10-dev libgfortran5 \ 
    && apt install liblapack-dev libblas-dev libblas3 liblapack3 \ 
    && pypy -m pip install numpy cython  \
    && git clone https://github.com/xianyi/OpenBLAS \ 
    && cd OpenBLAS && make FC=gfortran \ 
    && make PREFIX=/opt/OpenBLAS install \  
    && cd .. \ 
    && pypy -m pip install scipy pandas pyreadr

ADD Dockerfile .    
