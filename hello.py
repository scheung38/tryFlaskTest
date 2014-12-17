import os
from flask import Flask, render_template
from flask.ext.heroku import Heroku

app = Flask(__name__)
heroku = Heroku(app)


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=33507)
    heroku.init_app(app)