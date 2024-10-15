FROM python:3.12.1-slim-bullseye

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip3 install -r requirements.txt

RUN ./start.sh