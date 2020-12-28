#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/19 10:43
# @Author  : AsiHacker
# @File    : cycle.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import itertools

cs = itertools.cycle('ABC')  # 无限迭代A B C
for c in cs:
    print(c)
