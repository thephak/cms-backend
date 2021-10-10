#!/bin/bash

# Install packages for Python script 
pip install -r requirements.txt

# Check for database migration, if there's structure change then migrate the current database.
python manage.py makemigrations
python manage.py migrate

# Load mock data from json file.
python manage.py loaddata apps/init_data.json

# Add default static files from Django 
python manage.py collectstatic --noinput

# Run celery worker and start web server
celery -A celery worker -l DEBUG -B &
daphne -b 0.0.0.0 -p 8000 apps.asgi:application