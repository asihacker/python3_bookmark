#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/22 23:15
# @Author  : AsiHacker
# @File    : |=符号.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
a = {1, 3}
b = {2}
a |= b
print(a)
c = a | b
print(c)

e = -100
print(~e)  # 等价于-e-1
