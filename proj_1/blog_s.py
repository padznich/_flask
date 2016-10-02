from flask import Flask, redirect, url_for, request, render_template, make_response

import time

app = Flask(__name__)


@app.route('/')
def student():
    return render_template('student.html')


@app.route('/result',methods=['POST', 'GET'])
def result():
    if request.method=='POST':
        result=request.form
        return render_template("result.html",result=result)


@app.route('/hello/<name>')
def hello_name(name):
    time.sleep(40)
    return 'Hello %s!' % name


@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d' % (postID + 2)

#
# url_for()
#____________________________________________________________
@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))
#____________________________________________________________


#
# HTTP methods
#____________________________________________________________
@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))

    # elif request.method == 'GET' and request.args.get('nm'):  # in login.html chage method t GET
    #     user = request.args.get('nm')
    #     return redirect(url_for('success', name=user))
    return render_template('login.html')
#____________________________________________________________


#
# Templates
#____________________________________________________________

#____________________________________________________________


#
# Request Object
#
#   form    args    cookies     files   method
#
#____________________________________________________________

#____________________________________________________________


if __name__ == '__main__':
    # app.run(host, port, debug, options)
    app.run()
