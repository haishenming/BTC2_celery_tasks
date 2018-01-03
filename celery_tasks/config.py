from datetime import timedelta

CELERY_TIMEZONE = 'Asia/Shanghai'

from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    'add-every-20-seconds': {
         'task': 'tasks.celery_20s',
         'schedule': timedelta(seconds=20),
         'args': ()
    },
    'add-every-day': {
         'task': 'tasks.celery_1d',
         'schedule': crontab(hour=0, minute=1),
         'args': ()
    },

}