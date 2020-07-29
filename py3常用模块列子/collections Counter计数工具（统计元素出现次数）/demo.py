#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 16:55
# @Author  : AsiHacker
# @Site    : 
# @File    : mingyanSpider.py
# @Software: PyCharm
from collections import Counter

a = Counter()  # a new, empty counter
b = Counter('gallahad')  # a new counter from an iterable
c = Counter({'a': 4, 'b': 2})  # a new counter from a mapping
print(c)
d = Counter(a=4, b=2)
print(d)
e = Counter([1, 2, 3, 4, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 0])
f = Counter('你好 我叫 陈俊 学 哈哈 你好'.split())
print(f)
g = Counter('你好我叫陈俊学哈哈你好'.split('你'))
print(g)
g=Counter('askdjakjhdsjkad')
print(g)
h = Counter([1, 2, 3, 3])
j = Counter([1, 2, 3, 4, 4, 4])
print(h)
print(j)
print(h + j)
print(h - j)
print(j - h)
k = Counter([1, 2, 3, 3])
print(k)
k.clear()
print(k)
