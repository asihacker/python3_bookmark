#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/22 21:26
# @Author  : AsiHacker
# @Site    : 
# @File    : partial-偏函数.py
# @Software: PyCharm
from functools import partial


# 其实这个函数的作用就是：预先设置参数(也可以设置部分，比如下面)，使得之后调用的时候，减少函数的参数（也就是偏函数）

def add(a):
    print(a + 1)


add(2)  # 输出3

newAdd = partial(add, 100)

newAdd()  # 输出3


def add2(a, b):
    print(a + 1 + b)


add(2)  # 输出3

newAdd = partial(add2, a=100)

newAdd(b=3)
