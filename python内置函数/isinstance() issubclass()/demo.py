#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/22 21:16
# @Author  : AsiHacker
# @Site    : 
# @File    : demo.py
# @Software: PyCharm
class A(object):
    pass


a = A()

isinstance(a, A)
# true


class A(object):
    pass


class B(A):
    pass


issubclass(B, A)
# true