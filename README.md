# CMS Backend API

This is an example project to show how to use Python Django framework as a backend service to connect to database and provide REST API for any other service to get data 

This project is using tools listed down below.<br /> 
- Language: Python 
- Framework: Django 
- Background Task Managememt: Celery
- Web server: Daphne ASGI 
- Database: PostgreSQL 

<hr />

## Usage
### Get published content 
```
curl GET http://localhost:8000/api/contents
```
### Example response 
```
[
    {
        "title": "First content!",
        "published_date": "2021-10-01T10:00:00Z",
        "author": "Phak",
        "summary": "First content of this website.",
        "content": "Hello everyone, this is a first content of this website I just developed as a webboard. Hope you guys enjoy reading this!"
    },
    {
        "title": "Joke #1",
        "published_date": "2021-10-03T10:00:00Z",
        "author": "Phak",
        "summary": "What’s the best thing about Switzerland?",
        "content": "What’s the best thing about Switzerland?\nI don’t know, but the flag is a big plus."
    },
    ... 
```
<hr />

## Local development
### Requirements
- Python 3.9.7
- pip
- PostgreSQL server

### Steps
1. Open terminal and create a PostgreSQL database in PostgreSQL server and a user 
```
$ psql -U postgres
$ create database <database_name>;
$ CREATE USER <user_name> WITH PASSWORD <user_password>;
```
2. Setup the environment variables in .env file. 
3. Open terminal and run command in run.bat
```
$ run.bat
```
4. Navigate to `http://localhost:8000/admin` and login with username "admin" password "12345678" to see the Django admin page.

<hr />

## Local deployment (Containerizing)
### Requirements
- Docker version 20
- Docker Compose version 2.0.0

### Steps
1. Setup the environment variables in .env file. 
2. Open terminal and build Docker images for all services
```
$ docker-compose build 
```
3. Deploy the images to Docker Container
```
$ docker-compose up
```
4. You will get the error from app container that it cannot connect to database, leave the docker container running. Open another terminal to create database inside db container 
```
$ docker exec -it cms_api-db-1 psql -U postgres 
$ create database <database_name>;
$ CREATE USER <user_name> WITH PASSWORD <user_password>;
$ ALTER USER <user_name> WITH SUPERUSER;
```
5. Kill the current docker process and deploy again. 
```
$ docker-compose up
```
4. Navigate to `http://localhost:8000/admin` and login with username "admin" password "12345678" to see the Django admin page.


<hr />

## Local testing
### Requirements
- Python 3.9.7
- pip
- PostgreSQL server

### Steps
1. Open terminal and create a PostgreSQL database in PostgreSQL server and a user 
```
$ psql -U postgres
$ create database <database_name>;
$ CREATE USER <user_name> WITH PASSWORD <user_password>;
$ ALTER USER <user_name> WITH SUPERUSER;
```
2. Setup the environment variables in .env file. 
3. Open terminal and run command in test.bat
```
$ test.bat
```
