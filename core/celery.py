import os

from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.local")


app = Celery("core")

# Si la variable de entorno para SQS está definida, la cargamos
if os.getenv("CELERY_BROKER_URL") == "sqs://" and os.getenv("CELERY_BROKER_TRANSPORT_OPTIONS"):
    broker_transport_options = json.loads(os.getenv("CELERY_BROKER_TRANSPORT_OPTIONS"))
    app.conf.broker_transport_options = broker_transport_options
else:
    # Si no estamos usando SQS, entonces no configuramos las opciones de SQS
    app.conf.broker_transport_options = {}

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object(settings, namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

