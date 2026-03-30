import os
from settings.celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')

app = Celery('settings')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
