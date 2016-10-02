'''
It works!
change permission https://www.google.com/settings/security/lesssecureapps
and password in the row 15
'''

from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'slabkopg@gmail.com'
app.config['MAIL_PASSWORD'] = '***'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route("/")
def index():
    msg = Message(
        'Hello in a third time',
        sender='slabkopg@gmail.com',
        recipients=['pgslabko@mail.ru'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return "Sent"

if __name__ == '__main__':
    app.run(debug=True)
