# Pull base image
FROM resin/rpi-raspbian:jessie
MAINTAINER Dieter Reuter <dieter@hypriot.com>

# Install dependencies
RUN apt-get update && apt-get install -y \
    python \
    python-dev \
    python-pip \
    python-virtualenv \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Dependencies for the ecotrust
RUN apt-get update
RUN apt-get install -y  pkg-config libpng12-0 \ 
	libpng12-dev libpng++-dev libpng3 \
	libpnglite-dev python-opencv build-essential cmake \
	python-matplotlib python-setuptools

RUN mkdir /code
WORKDIR /code
ADD reqs.txt /code/
RUN easy_install -U distribute
RUN pip install -r reqs.txt
ADD . /code/
