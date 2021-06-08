#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/19 10:49
# @Author  : AsiHacker
# @File    : compress迭代成员过滤.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import itertools

print(list(itertools.compress('abcdefg', [1, 2, 3, 1])))  # 第2个参数放匿名函数也是可以的
