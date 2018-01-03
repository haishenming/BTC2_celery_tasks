


from celery_core import app
from tasks_func import task_20s, task_1d

@app.task
def add(x, y):
    return x + y

@app.task
def celery_20s():
    task_20s()

@app.task
def celery_1d():
    task_1d()