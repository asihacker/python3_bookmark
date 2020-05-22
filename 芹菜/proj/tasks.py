#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 22:22
# @Author  : AsiHacker
# @Site    : 
# @File    : tasks.py.py
# @Software: PyCharm
import time
from proj.app_test import app

@app.task
def add(x, y):
    time.sleep(1)
    return x + y