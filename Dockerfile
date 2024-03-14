FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ADD . /app/

WORKDIR /app


RUN pip install -r requirements.txt
