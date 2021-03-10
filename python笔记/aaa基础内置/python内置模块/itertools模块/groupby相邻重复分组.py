#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/19 10:47
# @Author  : AsiHacker
# @File    : groupby相邻重复分组.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import itertools

for key, group in itertools.groupby('AAFAFBBBCCAAA'):  # 把迭代器中相邻的重复元素挑出来放在一起
    print(key, list(group))  # 为什么这里要用list()函数呢？
