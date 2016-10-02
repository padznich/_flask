from flask import Flask
from celery import Celery
import time


app = Flask('example')
# app.config['CELERY_BROKER_URL'] = 'amqp://localhost//'
# app.config['CELERY_RESULT_BACKEND'] = 'db+mysql://root:root@localhost/fl_cl'
celery = Celery('example', broker='amqp://localhost//', backend='db+mysql://root:root@localhost/fl_cl')


@celery.task()
def add_together(a, b):
    time.sleep(40)
    return a + b


@app.route('/')
def index():
    return "{}".format(add_together.delay(23, 42).get())


if __name__ == '__main__':
    app.run()
    # result = add_together.delay(23, 42)
    # print(result.get())
