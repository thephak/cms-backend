from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

from django.conf import settings

# setting the Django settings module.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apps.settings')

BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')

app = Celery('celery', broker=settings.CELERY_BROKER_URL, backend=settings.CELERY_BACKEND_URL)
app.config_from_object('django.conf:settings', namespace='CELERY')

# Looks up for task modules in Django applications and loads them
app.autodiscover_tasks()
