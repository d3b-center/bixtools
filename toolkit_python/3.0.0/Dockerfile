FROM python:3.13.1-slim
LABEL maintainer="Alex Sickler (sicklera@chop.edu)"
LABEL description="Python3 base with all packages needed for toolkit analysis modules."

RUN apt update && python -m pip install --upgrade pip && python -m pip install pandas click

COPY Dockerfile .
