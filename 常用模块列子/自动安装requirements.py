#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-02-07 13:45
# @Author  : Lemon
# @File    : 自动安装requirements.py.py
# @Software: PyCharm

import os

with os.popen('pip3 freeze') as p:
    all = p.read().lower()

current = [x.split('==')[0] for x in all.split('\n')]

with open('requirements.txt', 'r') as f:
    need = f.read().lower()

li = [(x.split('==')[0], x.split('==')[1],) for x in need.split('\n')]
for name, ver in li:
    if not name in current:
        print('正在安装缺少的库: %s==%s' % (name, ver))
        res = os.popen('pip3 install %s==%s' % (name, ver)).read()
        print(res)
