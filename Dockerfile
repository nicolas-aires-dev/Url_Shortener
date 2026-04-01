FROM python:3.12-slim

WORKDIR /code

# create a "celeryuser" user
RUN adduser --disabled-password celeryuser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# root changes user to a non-root
USER celeryuser
