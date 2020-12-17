#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 18:30
# @Author  : AsiHacker
# @File    : __call__.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# 注：构造方法的执行是由创建对象触发的，即：对象 = 类名() ；而对于 __call__ 方法的执行是由对象后加括号触发的，即：对象() 或者 类()()
#
# Python中有一个有趣的语法，只要定义类型的时候，实现__call__函数，这个类型就成为可调用的。换句话说，我们可以把这个类的对象当作函数来使用，相当于重载了括号运算符。
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, a):
        print('My name is %s.' % self.name, a)


s = Student('Michael')
s(123)
# My name is Michael.
