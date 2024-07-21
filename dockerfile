FROM python:3.10.4

RUN mkdir /telegram_app

WORKDIR /telegram_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR /telegram_app/src