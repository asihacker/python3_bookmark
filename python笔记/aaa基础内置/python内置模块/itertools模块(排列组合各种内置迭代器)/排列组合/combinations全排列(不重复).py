#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 17:05
# @Author  : AsiHacker
# @File    : combinations全排列(不重复).py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import itertools

test_data = {1, 2, 3, 4}
for i in itertools.combinations_with_replacement(test_data, 2):
    print(i)
print('---------')
for nums in itertools.permutations(test_data, 2):
    print(nums)
