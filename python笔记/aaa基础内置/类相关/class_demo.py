#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 17:40
# @Author  : AsiHacker
# @Site    : 
# @File    : class_demo.py
# @Software: PyCharm

# https://www.cnblogs.com/jayliu/p/9030725.html 一文详解python的类方法，普通方法和静态方法
class Apple(object):
    """
    123
    """
    ddd = set()

    def __init__(self):
        self.ccc = 123

    def __str__(self):
        return self.ccc

    @classmethod
    def test(cls, id: int):
        cls.ddd.add(id)  # 类方法调用
        return cls.ddd

    def test1(self):
        # 这里我想调用 debug 类方法
        Apple.test(id=3)
        print(111)


class Two(Apple):

    def test1(self):
        super().test1()  # 使用父类方法


def ddd():
    print(456)


a = Two()
yy = 'test1'
print(hasattr(a, 'test1'))
func = getattr(a, 'test1')
print(func())
# print(bet.test1())
# bet.yyy = '123'
# print(bet.yyy)
# b = Two()
# print(Apple.debug(1))
# print(Apple.debug(2))
# print(Apple.debug(3))
# print(Apple.debug(4))
