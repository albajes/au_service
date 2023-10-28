# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY /service_1/service_1/requirements.txt /app/
RUN pip install -r requirements.txt

ADD /service_1/service_1 /app/service_1
ADD /service_1/docker /app/docker
ADD /service_1/venv /app/venv

RUN chmod +x /app/docker/entrypoint.sh