# This Dockerfile supports amd64,arm64,ppc64le
# Note: QEMU emulated ppc64le build might take ~6 hours

# Use conda to resolve dependencies cross-platform
FROM noelmni/antspy:master-8edfac1 as builder

# install libpng to system for cross-architecture support
# https://github.com/ANTsX/ANTs/issues/1069#issuecomment-681131938
# Also install kitware key and get recent cmake
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/Montreal
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      apt-transport-https \
      build-essential \
      ca-certificates \
      curl \
      git \
      gnupg \
      libpng-dev \
      software-properties-common

# install cmake binary using conda for multi-arch support
# apt install fails because libssl1.0.0 is not available for newer Debian
RUN conda install -c anaconda cmake

WORKDIR /usr/local/src

COPY . .

# number of parallel make jobs
ARG j=2

RUN python -m pip install -r requirements.txt
RUN python setup.py install

# optimize layers
FROM debian:bullseye-slim
COPY --from=builder /opt/conda /opt/conda
ENV PATH=/opt/conda/bin:$PATH
