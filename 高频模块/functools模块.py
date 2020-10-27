#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/22 21:26
# @Author  : AsiHacker
# @Site    : 
# @File    : functools模块.py
# @Software: PyCharm
import functools


# 其实这个函数的作用就是：预先设置参数，使得之后调用的时候，减少函数的参数

def add(a):
    print(a + 1)


add(2)  # 输出3

newAdd = functools.partial(add, 100)

newAdd()  # 输出3
