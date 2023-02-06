FROM python:3.7

RUN apt-get update

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY . .
WORKDIR /app/djangostock

