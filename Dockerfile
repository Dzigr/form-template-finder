FROM python:3.11

RUN mkdir /form_app

WORKDIR /form_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
