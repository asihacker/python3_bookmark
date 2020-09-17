#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/2 12:28
# @Author  : AsiHacker
# @Site    : 
# @File    : run.py
# @Software: PyCharm
import time

from flask import Flask, render_template, request

from flask_babel import Babel, gettext as _
import flask_babel

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'zh'

babel = Babel(app)


@babel.localeselector
def get_locale():
    a = request.accept_languages.best_match(['zh', 'en'])
    print(a)
    return a


@app.route('/')
def hello():
    print(request.accept_languages.best)
    day = _(f"Saturday")
    return day


if __name__ == '__main__':
    app.debug = True
    app.run()
