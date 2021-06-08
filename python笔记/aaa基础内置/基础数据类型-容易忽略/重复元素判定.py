#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 16:40
# @Author  : AsiHacker
# @Site    : 
# @File    : 重复元素判定.py
# @Software: PyCharm

def all_unique(lst):
    """
    重复元素判定
    :param lst:
    :return:
    """
    return len(lst) == len(set(lst))


x = [1, 1, 2, 2, 3, 2, 3, 4, 5, 6]
y = [1, 2, 3, 4, 5]
print(all_unique(x))  # False
print(all_unique(y))  # True
a = [1, 2, 3, 4]
b = [4, 5, 6]
print(a + b)
print(set(a) - set(b))  # 差集
print(set(a) | set(b))  # 交集
print(set(a) & set(b))  # 并集
print(set(a) ^ set(b))  # 对称差
