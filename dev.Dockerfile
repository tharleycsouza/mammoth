# Dockerfile

# FROM directive instructing base image to build upon
FROM python:3.7-buster

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/mammoth
RUN pip install --upgrade pip
RUN pip install pipenv
RUN apt-get update
RUN apt-get install ipython -y
COPY ./Pipfile /usr/src/mammoth/Pipfile
RUN pipenv install --skip-lock --system --dev
RUN pip install https://github.com/darklow/django-suit/tarball/v2

# copy project
RUN mkdir -p /etc/barman.d
COPY ./app/local_settings_dev.py /etc/mammoth/local_settings.py
CoPY  ./barman/barman.conf /etc/
CoPY  ./barman/mammoth.conf /etc/barman.d

