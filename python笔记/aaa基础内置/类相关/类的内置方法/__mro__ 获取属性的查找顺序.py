# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/28 14:55
# @Author  : AsiHacker
# @File    : __mro__ 获取属性的查找顺序
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
class E():
    pass


class D():
    pass


class C(E):
    pass


class B(D):
    pass


class A(B, C):
    pass


print(A.__mro__)
