from flask import Flask, g, render_template
import flask_cache

print help(flask_cache)
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index'


@app.route('/hello')
def hello():
    def say_hi(obj_response):
        obj_response.alert('Hi there!')
    if g.sijax.is_sijax_request:# Sijax request detected - let Sijax handle it
        g.sijax.register_callback('say_hi', say_hi)
        return g.sijax.process_request()
    return render_template('sijaxexample.html')


if __name__ == '__main__':
    app.run(debug=True)