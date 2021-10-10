:: Django setup
SET DJANGO_SETTINGS_MODULE "apps.settings"

:: Celery setup 
SET CELERY_BROKER="redis://redis:6379/0"
SET CELERY_BACKEND="redis://redis:6379/0"

:: Database setup
SET DATABASE_NAME=cms
SET DATABASE_USER=admin
SET DATABASE_PASSWORD="admin
SET DATABASE_HOST=localhost
SET DATABASE_PORT=5433

:: CORS setup 
SET FRONTEND_URL="http://localhost:4200"

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py loaddata apps/init_data.json
python manage.py collectstatic --noinput

start "" celery -A celery worker -l DEBUG -B
start "" daphne -b 0.0.0.0 -p 8000 apps.asgi:application
