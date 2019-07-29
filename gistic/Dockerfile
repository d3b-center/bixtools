FROM ubuntu:latest

RUN apt-get update && apt-get upgrade --yes && \ 
	apt-get install -y wget && \
	apt-get install --yes bc vim libxpm4 libXext6 libXt6 libXmu6 libXp6 zip unzip  build-essential

RUN mkdir /home/gistic
WORKDIR /home/gistic

RUN mkdir /home/gistic/MCRInstaller

RUN cd /home/gistic/MCRInstaller && \
   wget https://www.mathworks.com/supportfiles/downloads/R2014a/deployment_files/R2014a/installers/glnxa64/MCR_R2014a_glnxa64_installer.zip && \
   unzip MCR_R2014a_glnxa64_installer.zip && \
   rm MCR_R2014a_glnxa64_installer.zip

RUN cd /home/gistic && \
    wget ftp://ftp.broadinstitute.org/pub/GISTIC2.0/GISTIC_2_0_23.tar.gz && \
    tar -zxvf GISTIC_2_0_23.tar.gz && \
    rm GISTIC_2_0_23.tar.gz && \
    rm -r MCR_Installer

RUN  cd /home/gistic/MCRInstaller && \
     	/home/gistic/MCRInstaller/install -mode silent -agreeToLicense yes -destinationFolder /usr/local/MATLAB/MATLAB_Compiler_Runtime/ 

ENV LD_LIBRARY_PATH /usr/local/MATLAB/MATLAB_Compiler_Runtime/v83/runtime/glnxa64:/usr/local/MATLAB/MATLAB_Compiler_Runtime/v83/bin/glnxa64:/usr/local/MATLAB/MATLAB_Compiler_Runtime/v83/sys/os/glnxa64:${LD_LIBRARY_PATH}
ENV XAPPLRESDIR /usr/local/MATLAB/MATLAB_Compiler_Runtime/v83/X11/app-defaults

CMD ["/bin/bash"]

