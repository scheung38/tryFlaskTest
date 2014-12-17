import os
from flask import Flask, render_template
# from flask_heroku import Heroku

app = Flask(__name__)
# heroku = Heroku(app)


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)