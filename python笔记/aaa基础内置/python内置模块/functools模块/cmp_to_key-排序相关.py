#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 23:38
# @Author  : AsiHacker
# @File    : cmp_to_key-排序相关.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import functools
from collections import namedtuple

# 旧式的比较函数是接受两个参数，返回负值，0和正值比较大小的。现在直接key直接给一个参数就可以了 具体看一看内置函数的 sorted
# 该函数将旧式函数转化为可以被sorted(), min(), max(), heapq.nlargest(), heapq.nsmallest()
# 等函数接受的key。
Point = namedtuple('Point', ['x', 'y'])


def compare(p1, p2):
    """根据y坐标比较大小"""
    if p1.y > p2.y:
        return 1
    elif p1.y == p2.y:
        return 0
    else:
        return -1


if __name__ == '__main__':
    lst = [Point(-x, 2 * x - 1) for x in range(5)]
    res = sorted(lst, key=functools.cmp_to_key(compare))
    print(res)
