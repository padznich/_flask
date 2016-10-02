from celery import Celery

import time

app = Celery('tasks', broker='amqp://localhost//', backend='db+mysql://root:root@localhost/fl_cl')
# app = Celery('tasks', broker='amqp://localhost//', backend='mongodb://localhost/test')


@app.task
def reverse(string):
    time.sleep(20)
    return string[::-1]


if __name__ == "__main__":

    res1 = reverse.delay('abcd')
    time.sleep(3)
    res2 = reverse.delay('qwer')
    time.sleep(3)
    res3 = reverse.delay('poiu')

    a = True
    while a:
        print res1.status, res2.status, res3.status
        time.sleep(1)
        if all(x == 'SUCCESS' for x in [res1.status, res2.status, res3.status]):
            a = False
