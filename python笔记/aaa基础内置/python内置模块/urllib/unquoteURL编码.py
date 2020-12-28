#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/18 09:20
# @Author  : AsiHacker
# @File    : unquoteURL编码.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from urllib.parse import quote, unquote

a = '/test+/test'
c = quote(a, safe='')  # safe表示哪些不编码
print(c)
print(unquote(c, encoding='UTF-8'))