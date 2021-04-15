FROM python: 3.8

MAINTAINER Backend Developer YOUNG

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /usr/src/door_access_control_system/

WORKDIR /usr/src/door_access_control_system

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/door_access_control_system
EXPOSE 8000