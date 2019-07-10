from flask import Flask
app = Flask(__name__)

@app.route('/')
def command1():
    return 'Hello flask!!!!! hello!!!!!!!!!!!'

@app.route('/ssafy')
def command2():
    return 'This is ssafy'