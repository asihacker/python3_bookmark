#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 19:31
# @Author  : AsiHacker
# @File    : singledispatchmethod-泛型方法.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.

# singledispatch主要针对的是函数，但对于方法不友好，举个例子：
from functools import singledispatch, singledispatchmethod


class Dispatch:
    @singledispatch
    def foo(self, a):
        return a

    @foo.register(int)
    def _(self, a):
        return 'int'

    @foo.register(str)
    def _(self, a):
        return 'str'


# 在类的方法里面 singledispatch 失效了，因为 singledispatch 主要用于函数
cls = Dispatch()
print(cls.foo(1))
print(cls.foo('1'))


# 下面使用 singledispatchmethod 来处理----------
class Dispatch2:
    @singledispatchmethod
    def foo(self, a):
        return a

    @foo.register(int)
    def _(self, a):
        return 'int'

    @foo.register(str)
    def _(self, a):
        return 'str'


# 他有可以了
cls = Dispatch2()
print(cls.foo(1))
print(cls.foo('1'))
