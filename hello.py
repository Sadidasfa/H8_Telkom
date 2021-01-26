from flask import flask
app = flask(_name_)

@app.route('/')
def hello_world():
    return 'Hello world!'
