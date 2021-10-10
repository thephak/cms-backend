# pull the official base image
FROM python:3.9.7

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
  apt-get -y install gcc

RUN pip install --upgrade pip

# set work directory
WORKDIR /apps

# copy project
COPY . .

EXPOSE 8000

ENTRYPOINT [ "./entrypoint.sh" ]