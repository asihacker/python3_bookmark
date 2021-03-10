#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 16:55
# @Author  : AsiHacker
# @File    : combinations实现组合.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from itertools import combinations

test_data = {'bet', 'b', 'c', 'd'}
for i in combinations(test_data, 2):
    print(i)
