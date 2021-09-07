import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'carreg.settings')

app = Celery('carreg')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
