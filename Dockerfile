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

# copy entrypoint.sh
#COPY /service_1/docker/entrypoint.sh /service1/

# copy project
#COPY . .

# run entrypoint.sh
#RUN #chmod +x /app/service_1/service_1/docker/entrypoint.sh
#ENTRYPOINT ["/service_1/service_1/entrypoint.sh"]



## pull official base image
#FROM python:3.8.3-alpine
#
## set work directory
#WORKDIR /service2/service2
#
## set environment variables
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#
## install psycopg2 dependencies
#RUN apk update \
#    && apk add postgresql-dev gcc python3-dev musl-dev
#
## install dependencies
#RUN pip install --upgrade pip
#COPY ../service2/requirements.txt .
#RUN pip install -r requirements.txt
#
## copy entrypoint.sh
#COPY entrypoint.sh .
#
## copy project
#COPY docker .
#
## run entrypoint.sh
#ENTRYPOINT ["/service2/service2/entrypoint.sh"]