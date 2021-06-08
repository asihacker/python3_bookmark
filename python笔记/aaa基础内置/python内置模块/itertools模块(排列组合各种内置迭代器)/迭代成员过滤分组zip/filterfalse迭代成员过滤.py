#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 17:12
# @Author  : AsiHacker
# @File    : filterfalse迭代成员过滤.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import itertools

a = [1, 2, 3, 4, "", None, 0]
print(list(itertools.filterfalse(lambda x: not isinstance(x, int), a)))
print(list(itertools.filterfalse(lambda x: isinstance(x, int), a)))
print(list(filter(lambda x: isinstance(x, int), a)))
