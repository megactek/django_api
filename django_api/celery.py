from argparse import Namespace
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_api.settings')

app = Celery('django_api')
app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()