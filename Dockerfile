# This Dockerfile supports amd64 and arm64

FROM noelmni/antspy:v0.3.5 as builder

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