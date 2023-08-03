# syntax=docker/dockerfile:1

FROM jupyter/base-notebook:latest

WORKDIR /app

COPY requirements.txt requirements.txt
RUN python -m pip install --no-cache -r requirements.txt

COPY . .

CMD ["python3", "-m" , "jupyterlab"]