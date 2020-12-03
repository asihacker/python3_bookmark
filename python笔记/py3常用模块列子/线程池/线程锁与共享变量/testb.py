#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/27 12:45
# @Author  : AsiHacker
# @File    : testb.py
# @Software: PyCharm
from .testa import data
import threading


def dddd():
    print(threading.currentThread().getName(), '打印data', data)