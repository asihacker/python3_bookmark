#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/28 11:47
# @Author  : AsiHacker
# @File    : easydict-md5-Process启动子进程.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from easydict import EasyDict as edict

d = edict({'foo': 3, 'bar': {'x': 1, 'y': 2}})
print(d.bar.x)
