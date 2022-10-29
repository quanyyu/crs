from celery import Celery


app = Celery('ctest', broker='redis://localhost:6379/0',
backend='redis://localhost:6379/0')
app.conf.update(
    result_serializer='json',
    task_serializer='json'
)

@app.task
def hello():
    return 'hello world'