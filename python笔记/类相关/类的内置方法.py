#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 00:06
# @Author  : AsiHacker
# @File    : 类的内置方法.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
class Apple1:

    def __init__(self, *args, **kwargs):
        self.name = 'asi'
        pass

    def __call__(self, *args, **kwargs):  # 可以让类支持 a1() 方式调用
        print(args, kwargs)
        return

    def __delattr__(self, item):
        print('__delattr__', item)

    def __getattr__(self, item):
        print('__getattr__', item)

    def __setattr__(self, key, value):
        print('__setattr__', key, value)


a1 = Apple1()
print(a1(1, 2, 3, a=1))
print(a1.__class__)  # 实例所在的类
a1.name = '778899'
