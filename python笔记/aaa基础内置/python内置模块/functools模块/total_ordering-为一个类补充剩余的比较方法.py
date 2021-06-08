#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 20:30
# @Author  : AsiHacker
# @File    : total_ordering-为一个类补充剩余的比较方法.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.


# 为一个类补充剩余的比较方法，不用自己把所有的比较方法都写全。
# 但是类本身必须已经实现__eq__方法，并且还实现了 __lt__(), __le__(), __gt__(), or __ge__()的其中一个方法。
# 比如下面
from functools import total_ordering


@total_ordering
class Student(object):
    def __init__(self, score):
        self.score = score

    def __eq__(self, other):
        return self.score == other.score

    def __gt__(self, other):
        return self.score > other.score


if __name__ == '__main__':
    s1 = Student(60)
    s2 = Student(70)
    print(s1 >= s2)  # 输出False
