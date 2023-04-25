#!/usr/bin/env python3

'''FlaskBabel setup'''

from flask_babel import Babel
from flask import Flask, render_template


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    '''list of supported languages'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/", methods=['GET', 'POST'])
def welcome() -> str:
    '''returns hello world'''
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
