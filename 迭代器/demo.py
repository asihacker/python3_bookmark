#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/11 00:35
# @Author  : AsiHacker
# @Site    : 
# @File    : demo.py
# @Software: PyCharm
a = ['我', 'ai', 'ni', 'zg']
b = iter(a)
for k in b:
    print(k, sep='\t', end='   ')
