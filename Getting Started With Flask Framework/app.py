from flask import Flask
'''
It creates an instances of the Flask class,
Which will be your WSGI (web server gateway interface) application.
'''
## WSGI application
app = Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome to this flask course.This should be an amazing course.this is the best class course "

@app.route('/index')
def index():
    return "Welcome to this index page."

if __name__ == '__main__': ##Entry Code
    app.run(debug=True)