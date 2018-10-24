FROM python:3.7-alpine

RUN apk update && pip install ptvsd
EXPOSE 5678