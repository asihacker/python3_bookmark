#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 17:16
# @Author  : AsiHacker
# @File    : islice dropwhile跳过部分迭代.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from itertools import islice, dropwhile

items = ['bet', 'b', 'c', 1, 4, 10, 15]
# 在这个例子中， islice() 函数最后那个 None 参数指定了你要获取从第3个到最后的所有元素，
# 如果 None 和3的位置对调，意思就是仅仅获取前三个元素恰恰相反， (这个跟切片的相反操作 [3:] 和 [:3] 原理是一样的)。
for x in islice(items, 3, None):
    print(x)

for x in dropwhile(lambda x: isinstance(x, int), items):
    print(x)
