#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/5 00:28
# @Author  : AsiHacker
# @File    : ChainMap映射串联.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from collections import ChainMap
# https://www.cnblogs.com/zydev/p/11760037.html
# ChainMap 类是为了将多个映射快速的链接到一起，这样它们就可以作为一个单元处理。它通常比创建一个新字典和多次调用 update() 要快很多。
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)
print(c['z'])
# 下面的合并串联方法就会占用比较大资源，同时也会慢很多
c1 = a | b
print(c1)
c2 = b | a
print(c2)

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)
print(c)
# ChainMap 通过引用合并底层映射。 所以，如果一个底层映射更新了，这些更改会反映到 ChainMap 。
a['x'] = 10
print(c)
print(ChainMap({}, {'x': 100, 'z': 10}, {'y': 2, 'z': 4}))
