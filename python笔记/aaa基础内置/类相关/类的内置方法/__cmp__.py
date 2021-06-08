#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 20:18
# @Author  : AsiHacker
# @File    : __cmp__.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# 了解即可
# __cmp__是python2的类中所使用的特殊函数，一般用于对类对象列表的排序。python3 已经取消了
"""
cmp(x, y)#python2
if  x > y:
    return 1
elif x < y:
    return -1
else:
    return 0
"""


class Student(object):
    def __init__(self, grade: int):
        self.grade = grade

    def __cmp__(self, other):
        if self.grade < other.grade:
            return -1
        elif self.grade > other.grade:
            return 1
        else:
            return 0


a = [Student(grade=k) for k in range(10)]
