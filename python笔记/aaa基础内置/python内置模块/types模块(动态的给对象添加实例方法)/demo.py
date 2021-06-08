#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/29 15:23
# @Author  : AsiHacker
# @File    : findall.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import types

# class Foo:
#     def run(self):
#         return None
#
#
# def bark(self):
#     print('barking')
#
#
# a = Foo()
#
# print(type(1))
# print(type(Foo))
# print(type(Foo.run))
# print(type(Foo().run))
# print(type(bark))
###########
import types

class Foo:
    def run(self):
        return None


def bark(self):
    print('i am barking')


a = Foo()
a.bark = types.MethodType(bark, a)  # MethodType动态的给对象添加实例方法
a.bark()
# 下面是我想到的2个方法，还要吧自己传进去,真垃圾
b = Foo()
b.bark = bark
b.bark(b)
# 方法3
c = Foo()
setattr(c, 'bark', bark)
c.bark(c)
