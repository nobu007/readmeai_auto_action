# Dockerfile
FROM python:3.12

WORKDIR /usr/src/app

RUN git clone --recurse-submodules https://github.com/nobu007/readmeai_auto.git

RUN pip install -r readmeai_auto/requirements.txt

ENTRYPOINT ["python", "main.py"]
