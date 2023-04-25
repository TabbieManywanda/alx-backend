#!/usr/bin/env python3

'''Creating 'get_locale' function'''

from flask_babel import Babel
from flask import Flask, render_template, request


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    '''Application configuration'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    '''determine best match with supported languages'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=['GET', 'POST'])
def welcome() -> str:
    '''Returns hello world'''
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()
