FROM python:3.8-slim-buster

# install development tools
RUN apt-get update \
 && apt-get upgrade -y \
 && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    python3-distutils \
    python3-tk \
    x11-apps \
 && apt-get clean -y \
 && rm -rf /var/lib/apt/lists

# install pip requirements
WORKDIR /opt/app
COPY requirements.txt /opt/app
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt

 # set X11 server address
ENV DISPLAY=host.docker.internal:0

