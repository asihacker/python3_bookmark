#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 16:06
# @Author  : AsiHacker
# @File    : accumulate计算数组前缀和.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import itertools

a = [1, 2, 3, 4, 5]
b = itertools.accumulate(a)  # 默认是累加 计算前缀和
print(list(b))