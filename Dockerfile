# Dockerfile
FROM python:3.12

WORKDIR /usr/src/app

RUN git clone --recurse-submodules https://github.com/nobu007/readmeai_auto.git

RUN pip install -r readmeai_auto/requirements.txt
RUN apt-get update && \
    curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg && \
    chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | tee /etc/apt/sources.list.d/github-cli.list > /dev/null && \
    apt-get update && apt-get install -y gh

COPY . /usr/src/app

WORKDIR /usr/src/app

ENTRYPOINT ["python", "main.py"]
# ENTRYPOINT ["ls"]
