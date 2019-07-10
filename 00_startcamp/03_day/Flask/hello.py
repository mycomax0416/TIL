from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello1():
    return 'Hello flask!!!!! hello!!!!!!!!!!!'

@app.route('/ssafy')
def hello2():
    return 'This is ssafy'