#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 20:59
# @Author  : AsiHacker
# @File    : getmro-获取mro解析顺序.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import inspect


# getmro()函数，它接受的参数为 类，然后返回值是一个 类的tuple，它会解析出传入类的所有基类，并按照mro的顺序排列。

class A(object):
    ...


class B(A):
    ...


class C(B):
    ...


class D(C, B, A):
    ...


print(inspect.getmro(C))
print(inspect.getmro(D))
