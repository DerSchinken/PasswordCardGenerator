# syntax=docker/dockerfile:1

FROM python:3.9.5-slim-buster

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000:5000

CMD [ "python3", "main.py"]
