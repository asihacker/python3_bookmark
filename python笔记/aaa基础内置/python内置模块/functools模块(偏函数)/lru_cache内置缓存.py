#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/18 09:19
# @Author  : AsiHacker
# @File    : lru_cache内置缓存.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from functools import lru_cache


@lru_cache(maxsize=1)
def add(x, y):
    print("calculating: %s + %s" % (x, y))
    return x + y


print(add(1, 2))
print(add(1, 2))
print(add(1, 2))
print(add(1, 2))
print(add(1, 2))
print(add(1, 2))
print(add(1, 2))
print(add(1, 2))
print(add(1, 2))
print(add(1, 2))
print(add(1, 2))
print(add(1, 2))
print(add(2, 3))