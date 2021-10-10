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

python manage.py test