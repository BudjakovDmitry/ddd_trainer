FROM python:3.11

WORKDIR /adapty

COPY requirements.txt /adapty/
RUN pip install -r requirements.txt

COPY . /code/
