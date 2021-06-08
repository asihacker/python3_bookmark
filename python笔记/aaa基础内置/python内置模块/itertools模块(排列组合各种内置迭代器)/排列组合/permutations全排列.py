#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 21:44
# @Author  : AsiHacker
# @File    : permutations全排列.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import itertools

test_data = {1, 2, 3, 4}
for nums in itertools.permutations(test_data, 2):
    print(nums)
