#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/19 10:44
# @Author  : AsiHacker
# @File    : repeat有限迭代可以限制迭代次数.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import itertools

ns = itertools.repeat('A', 1000)  # 也是无限迭代，但是第2个参数可以限制迭代次数
for n in ns:
    print(n)
