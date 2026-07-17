FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /workspace

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        default-mysql-client \
        git \
        curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements-dev.txt /workspace/

RUN python -m pip install --upgrade pip \
    && python -m pip install --no-cache-dir \
        -r /workspace/requirements.txt \
        -r /workspace/requirements-dev.txt

COPY . /workspace

CMD ["tail", "-f", "/dev/null"]