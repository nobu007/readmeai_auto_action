# Dockerfile
FROM python:3.12

# GitHub Actionsのデフォルト作業ディレクトリに合わせる
WORKDIR /github/workspace

RUN git clone --recurse-submodules https://github.com/nobu007/readmeai_auto.git

RUN pip install -r readmeai_auto/requirements.txt
RUN apt update && apt install -y curl && \
    curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg && \
    chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | tee /etc/apt/sources.list.d/github-cli.list >/dev/null && \
    apt update && apt install -y gh

COPY . /github/workspace

ENTRYPOINT ["python", "/github/workspace/main.py"]
