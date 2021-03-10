#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 18:31
# @Author  : AsiHacker
# @Site    : 
# @File    : 深浅复制.py
# @Software: PyCharm
# 深复制1
a = [1, 2, 3]
b = a.copy()
for key in range(3):
    b.insert(0, key)
print('copy-bet', a, id(a))
print('copy-b', b, id(b))
# 深复制2
a = [1, 2, 3]
b = [*a]
for key in range(3):
    b.insert(0, key)
print('[*]-bet', a, id(a))
print('[*]-b', b, id(b))

# 浅复制
a = [1, 2, 3]
b = a
for key in range(3):
    b.insert(0, key)
print('=-bet', a, id(a))
print('=-b', b, id(b))
