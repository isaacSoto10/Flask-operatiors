from flask import Flask 

app = Flask(__name__)


@app.route('/welcome')
def welcome_page():
    return "welcome"
