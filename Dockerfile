# This Dockerfile supports amd64 and arm64

# Use conda to resolve dependencies cross-platform
FROM noelmni/antspy:v0.3.5 as builder

# install libpng to system for cross-architecture support
# https://github.com/ANTsX/ANTs/issues/1069#issuecomment-681131938
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      apt-transport-https \
      bash \
      build-essential \
      git \
      libpng-dev

# install cmake binary using conda for multi-arch support
RUN conda install -c conda-forge cmake

WORKDIR /usr/local/src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# number of parallel make jobs
ARG j=2
RUN pip --no-cache-dir -v install .

# optimize layers
FROM debian:bullseye-20230109-slim
COPY --from=builder /opt/conda /opt/conda
ENV PATH=/opt/conda/bin:$PATH