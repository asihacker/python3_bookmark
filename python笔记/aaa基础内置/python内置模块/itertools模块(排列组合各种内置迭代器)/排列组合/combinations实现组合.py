#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 16:55
# @Author  : AsiHacker
# @File    : combinations实现组合.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from itertools import combinations, product

test_data = {1, 2, 3, 4}
test_data2 = {66, 67, 68, 69}
test_data3 = {76, 77, 78, 79}
# for i in combinations(test_data, 2):
#     print(i)
# for i in combinations(test_data, 2):
#     for i2 in combinations(test_data2, 2):
#         for i3 in combinations(test_data3, 2):
#             print(i, i2, i3)
# a = []
for k in product(combinations(test_data, 2), combinations(test_data2, 2), combinations(test_data3, 2), repeat=1):
    print(k)
#     a.append(k)
# print(len(a))
