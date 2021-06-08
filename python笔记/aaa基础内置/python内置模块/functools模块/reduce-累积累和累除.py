#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 12:26
# @Author  : AsiHacker
# @File    : reduce-累积累和累除.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from functools import reduce

list1 = [1, 3, 5, 6, 7]
sum = reduce(lambda x, y: x * y, list1)
print(sum)
sum = reduce(lambda x, y: x + y, list1)
print(sum)
sum = reduce(lambda x, y: x / y, list1)
print(sum)
