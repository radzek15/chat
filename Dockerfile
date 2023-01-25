FROM python:3.10

ENV PYTHONUNBUFFERED=1

RUN mkdir /CV_site

WORKDIR /CV_site

COPY . /CV_site

RUN pip install -r requirements.txt
