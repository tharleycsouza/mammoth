# Dockerfile

# FROM directive instructing base image to build upon
FROM python:3.7-buster

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/amicool
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /usr/src/amicool/Pipfile
RUN pipenv install --skip-lock --system --dev

# copy project
COPY ./app/local_settings_dev.py /etc/amicool/local_settings.py
