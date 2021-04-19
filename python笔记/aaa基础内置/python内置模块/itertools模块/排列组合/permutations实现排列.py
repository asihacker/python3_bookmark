#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 17:02
# @Author  : AsiHacker
# @File    : permutations实现排列.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import itertools

test_data = {1, 2, 3, 4}
for i in itertools.permutations(test_data, 2):
    print(i)
