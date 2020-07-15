#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 14:28
# @Author  : AsiHacker
# @Site    : 
# @File    : demo.py
# @Software: PyCharm
from functools import lru_cache


@lru_cache(None)
def add(x, y):
    print("calculating: %s + %s" % (x, y))
    return x + y


print(add(1, 2))
print(add(1, 2))
print(add(2, 3))
