# syntax=docker/dockerfile:1

FROM python:3.10.0a7-alpine3.13

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "-m" , "jupyterlab"]