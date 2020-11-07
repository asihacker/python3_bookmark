#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/5 12:32
# @Author  : AsiHacker
# @Site    : 
# @File    : 语种识别接口.py
# @Software: PyCharm
from flask import Flask, request
import langid

app = Flask(__name__)


@app.route('/<name>', methods=['GET', 'POST'])
def index(name):
    a = langid.classify(name)
    return str(langid.classify(name))


if __name__ == '__main__':
    import base64
    print(base64.b64encode('hello'.encode('utf-8')))
    # app.run(port=5001, debug=True)
