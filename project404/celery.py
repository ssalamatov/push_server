import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project404.settings')

app = Celery()
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
