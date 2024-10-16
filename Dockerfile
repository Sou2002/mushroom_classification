FROM python:3.12.1-bullseye

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

RUN chmod +x ./start.sh
RUN ./start.sh