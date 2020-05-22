#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 22:22
# @Author  : AsiHacker
# @Site    : 
# @File    : app_test.py.py
# @Software: PyCharm
from celery import Celery

app = Celery('proj', include=['proj.tasks'])
app.config_from_object('proj.celeryconfig')

if __name__ == '__main__':
    app.start()
