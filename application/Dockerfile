FROM python:3.8.4 as dev

RUN mkdir -p /usr/src/app
RUN mkdir -p /usr/config
WORKDIR /usr/src/app

ENV PYTHONPATH=/usr/src/app/

COPY requirements.txt /usr/src/app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y iproute2 iputils-ping