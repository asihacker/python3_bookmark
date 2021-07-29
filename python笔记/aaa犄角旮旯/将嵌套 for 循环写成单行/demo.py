# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/13 19:33
# @Author  : AsiHacker
# @File    : demo
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from itertools import product

list1 = range(1, 3)
list2 = range(4, 6)
list3 = range(7, 9)
for item1, item2, item3 in product(list1, list2, list3):
    print(item1 + item2 + item3)
