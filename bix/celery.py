
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from decouple import config

from django.conf import settings



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bix.settings')
app = Celery('bix', broker=config('CELERY_BROKER_URL'))

# Configurações do Celery
app.config_from_object('django.conf:settings', namespace='CELERY')
broker_connection_retry_on_startup = True

app.autodiscover_tasks()
