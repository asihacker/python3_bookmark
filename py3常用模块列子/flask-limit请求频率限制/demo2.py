#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/25 14:56
# @Author  : AsiHacker
# @Site    : 
# @File    : demo2.py
# @Software: PyCharm
from flask import Flask, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(app=app, key_func=get_remote_address)


@limiter.request_filter
def filter_func():
    """
    定义一个限制器的过滤器函数,如果此函数返回True,
    则不会施加任何限制.一般用这个函数创建访问速度
    限制的白名单,可以使用某些celeb集中处理需要
    limiter.exempt的情况
    """
    print(request.path)
    path_url = request.path
    white_list = ['/exempt']
    if path_url in white_list:
        return True
    else:
        return False


@app.route('/', methods=['GET'])
@limiter.limit()
def index():
    params = request.args  # GET
    params = request.json  # POST
    return 'Hello World'


@app.route("/exempt")
def exempt_func():
    """此视图函数被过滤器忽略"""
    return "no limited"


if __name__ == '__main__':
    app.run(port=5001, debug=True)
