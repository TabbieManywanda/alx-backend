#!/usr/bin/env python3

'''Setting up a basic Flask app'''

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world() -> str:
    '''Returns html template with Hello World'''
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
