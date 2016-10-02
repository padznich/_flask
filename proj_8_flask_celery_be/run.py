'''
It works!
change permission https://www.google.com/settings/security/lesssecureapps
and password in the row 29
celery -A run.celery worker -l info
'''
import os

from flask import Flask, request, render_template, session, flash, redirect, url_for
from celery import Celery
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'random string'
app.config['CELERY_BROKER_URL'] = 'amqp://localhost//'
app.config['CELERY_RESULT_BACKEND'] = 'db+mysql://root:root@localhost/fl_cl'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
# app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USERNAME'] = 'slabkopg@gmail.com'
app.config['MAIL_PASSWORD'] = '***'
app.config['MAIL_DEFAULT_SENDER'] = 'slabkopgk@gmail.com'

mail = Mail(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', email=session.get('email', ''))
    email = request.form['email']
    session['email'] = email

    # send the email
    msg = Message('Hello from Flask',
                  recipients=[request.form['email']])
    msg.body = 'This is a test email sent from a background Celery task.'
    if request.form['submit'] == 'Send':
        # send right away
        send_async_email.delay(msg)
        flash('Sending email to {0}'.format(email))
    else:
        # send in one minute
        send_async_email.apply_async(args=[msg], countdown=60)
        flash('An email will be sent to {0} in one minute'.format(email))

    return redirect(url_for('index'))


@celery.task
def send_async_email(msg):
    """Background task to send an email with Flask-Mail."""
    with app.app_context():
        mail.send(msg)


if __name__ == '__main__':

    app.run()
