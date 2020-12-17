#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 18:31
# @Author  : AsiHacker
# @File    : __next__(self)与__iter__(self)实现迭代器.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
class Foo:
    def __init__(self, start, stop):
        self.num = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.num >= self.stop:
            raise StopIteration
        n = self.num
        self.num += 1
        return n


f = Foo(1, 5)
from collections import Iterable, Iterator

print(isinstance(f, Iterator))

for i in Foo(1, 5):
    print(i)
