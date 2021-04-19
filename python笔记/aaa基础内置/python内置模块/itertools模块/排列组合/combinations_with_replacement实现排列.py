#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 17:05
# @Author  : AsiHacker
# @File    : combinations_with_replacement实现排列.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import itertools

test_data = {1, 2, 3, 4}
for i in itertools.combinations_with_replacement(test_data, 2):
    print(i)
