#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/7 22:16
# @Author  : AsiHacker
# @Site    : 
# @File    : callable.py
# @Software: PyCharm
print(callable(0))
print(callable("runoob"))
print(callable('add'))

# callable() 函数用于检查一个对象是否是可调用的

def add():
    return


print(callable(add))


class A(object):
    def aaa(self):
        return


# 类返回True
print(callable(A))

a = A()

# 实列 bet 没有__call__ 为 false
print(callable(a))


class B(object):
    def aaa(self):
        return

    def __call__(self, *args, **kwargs):
        return 0


b = B()

# 实列 b 有__call__ 为 true
print(callable(b))
