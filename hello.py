from flask import Flask
import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/date/')
def getdate():
    while True:
        return str(datetime.date(2017, 6, 22))

app.debug = True
if __name__ == '__main__':
    app.run()

