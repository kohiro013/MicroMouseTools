
FROM python:3.8-slim-buster

# install development tools
RUN apt-get update \
 && apt-get upgrade -y \
 && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    python3-distutils \
    usbutils \
    gtkterm \
    libgl1-mesa-dev \
    libglib2.0-0 \
    libxkbcommon-x11-0 \
    libxcb-xinerama0 \
    libdbus-1-3 \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-keysyms1 \
    libxcb-render-util0 \
    x11-apps \
 && apt-get clean -y \
 && rm -rf /var/lib/apt/lists

# libxcb-uitl1がインストールできないため
RUN ln -s /usr/lib/x86_64-linux-gnu/libxcb-util.so.0.0.0 /usr/lib/x86_64-linux-gnu/libxcb-util.so.1

# install pip requirements
WORKDIR /opt/app
COPY requirements.txt /opt/app
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt

 # set X11 server address
ENV DISPLAY=host.docker.internal:0

# measures against warning(XDG_RUNTIME_DIR not set)
ENV XDG_RUNTIME_DIR=/tmp/runtime-root 
ENV RUNLEVEL=3