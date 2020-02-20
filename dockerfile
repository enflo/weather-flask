FROM python:3.7-alpine3.11

ADD requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt

WORKDIR /opt