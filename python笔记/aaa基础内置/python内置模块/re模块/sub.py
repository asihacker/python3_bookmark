#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/19 11:19
# @Author  : AsiHacker
# @File    : sub.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import re
import string

a = 'a1b2c3d4e5f6g7'
# '1234567'
b = ''.join(list(filter(lambda _: _ in string.digits, a)))
print(b)
b = ''.join([key for key in a if key in string.digits])
print(b)
b = ''.join(re.findall(r'\d',a))
print(b)
print(re.sub('\D', '', a))
print(a[1::2])
