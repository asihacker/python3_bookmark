#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/9 18:28
# @Author  : AsiHacker
# @Site    : 
# @File    : 自定义异常.py
# @Software: PyCharm

import multiprocessing
import os

import gevent.monkey

gevent.monkey.patch_all()  # 猴子补丁

debug = True
loglevel = 'debug'

name = 'asi-flask'
bind = os.getenv('HOST')
pidfile = "gunicorn.pid"
accesslog = "access.log"
errorlog = "debug.log"
daemon = False
threads = 20

# 启动的进程数
workers = multiprocessing.cpu_count()
worker_class = 'gevent'
x_forwarded_for_header = 'X-FORWARDED-FOR'
