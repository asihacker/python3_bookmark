#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 22:22
# @Author  : AsiHacker
# @Site    : 
# @File    : app_test.py.py
# @Software: PyCharm
from celery import Celery
app = Celery('proj', include=['celery任务调度神器.proj.tasks'])
app.config_from_object('celery任务调度神器.proj.celeryconfig')

if __name__ == '__main__':
    app.worker_main(argv=['-l debug'])
