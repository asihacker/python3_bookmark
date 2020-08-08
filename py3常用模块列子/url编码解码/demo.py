#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 10:38
# @Author  : AsiHacker
# @Site    : 
# @File    : demo.py
# @Software: PyCharm
from urllib.parse import quote, unquote

a = '/test+/test'
c = quote(a, safe='')  # safe表示哪些不编码
print(c)
print(unquote(c, encoding='UTF-8'))
