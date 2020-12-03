#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 17:01
# @Author  : AsiHacker
# @Site    : 
# @File    : reversed反转函数.py
# @Software: PyCharm
a = reversed([1, 2, 3, 4, 5, 6])
print(a)
for key in a:
    print(key)
a = reversed('123456')
print(a)
for key in a:
    print(key)
