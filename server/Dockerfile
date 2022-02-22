FROM nvidia/cuda:11.4.0-base-ubuntu20.04
LABEL maintainer chiachun2491
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN apt-get install -y python3-pip --no-install-recommends
RUN mkdir /code
WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt
# RUN pip install  -i  https://pypi.python.org/simple/  -r requirements.txt