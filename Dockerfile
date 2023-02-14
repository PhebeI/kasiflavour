FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

COPY ./requrements.txt /app/requirements.txt

RUN pip install -r requrements.txt
