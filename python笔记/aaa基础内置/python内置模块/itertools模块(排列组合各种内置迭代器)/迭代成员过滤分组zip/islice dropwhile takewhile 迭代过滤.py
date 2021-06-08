#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 17:16
# @Author  : AsiHacker
# @File    : islice dropwhile takewhile 迭代过滤.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from itertools import islice, dropwhile, takewhile, filterfalse

# 和切片类似
items = ['bet', 'b', 'c', 1, 4, 10, 15]
# 在这个例子中， islice() 函数最后那个 None 参数指定了你要获取从第3个到最后的所有元素，
# 如果 None 和3的位置对调，意思就是仅仅获取前三个元素恰恰相反， (这个跟切片的相反操作 [3:] 和 [:3] 原理是一样的)。
for x in islice(items, 1, 3, None):  # start、stop和step
    print(x)
# 段位筛选
print('-----------------')
print(list(dropwhile(lambda x: x < 3, [1, 0, 2, 4, 1, 1, 3, 5, -5])))  # 扫描列表，不满足条件处开始往后保留
print('-----------------')
print(list(takewhile(lambda x: x < 5, [1, 4, 6, 4, 1])))  # 扫描列表，不满足条件处开始往前保留
print('-----------------')
# 次品筛选
print(list(filterfalse(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])))
