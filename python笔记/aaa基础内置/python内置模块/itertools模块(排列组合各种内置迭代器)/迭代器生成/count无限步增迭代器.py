#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/19 10:41
# @Author  : AsiHacker
# @File    : count无限步增迭代器.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import itertools
import time

natuals = itertools.count(0.1, 2)  # “无限”迭代器,每次加1 2为步长
print(next(natuals))
print(next(natuals))
print(next(natuals))
print(next(natuals))
print(next(natuals))
print(next(natuals))
print(next(natuals))
print(next(natuals))
print(next(natuals))
print(next(natuals))
print(next(natuals))
print(int(time.time() * 1000))
# for n in natuals:
#     print(n)
