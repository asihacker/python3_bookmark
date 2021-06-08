#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 23:57
# @Author  : AsiHacker
# @File    : OrderedDict有序字典.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# 普通字典
from collections import OrderedDict

# python3中 OrderedDict就是比dict多了一个 move_to_end 方法
# OrderedDict也支持反向迭代，例如reversed()。
d = dict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 1
d['e'] = 2
for k, v in d.items():
    print(k, v)
print(d.popitem())  # 移除并且返回字典元祖
# 使用OrderedDict会根据放入元素的先后顺序进行排序。
# 由于进行了排序，所以OrderedDict对象的字典对象，如果其顺序不同那么Python也会把他们当做是两个不同的对象
d1 = OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'
for k, v in d1.items():
    print(k, v)
d1.move_to_end('a')
for k, v in d1.items():
    print(k, v)
print(d1.popitem())

