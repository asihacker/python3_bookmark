#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 18:19
# @Author  : AsiHacker
# @File    : __slots__一个类变量 内存优化 限制属性.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# __slots__是什么:是一个类变量,变量值可以是列表,元祖,或者可迭代对象,也可以是一个字符串(意味着所有实例只有一个数据属性)
# 引子:使用点来访问属性本质就是在访问类或者对象的__dict__属性字典(类的字典是共享的,而每个实例的是独立的)
# 为何使用__slots__:字典会占用大量内存,如果你有一个属性很少的类,但是有很多实例,为了节省内存可以使用__slots__取代实例的__dict__
# 当你定义__slots__后,__slots__就会为实例使用一种更加紧凑的内部表示。实例通过一个很小的固定大小的数组来构建,而不是为每个实例定义一个
# 字典,这跟元组或列表很类似。在__slots__中列出的属性名在内部被映射到这个数组的指定小标上。使用__slots__一个不好的地方就是我们不能再给
# 实例添加新的属性了,只能使用在__slots__中定义的那些属性名。
# 注意事项:__slots__的很多特性都依赖于普通的基于字典的实现。另外,定义了__slots__后的类不再 支持一些普通类特性了,比如多继承。大多数情况下,你应该
# 只在那些经常被使用到 的用作数据结构的类上定义__slots__比如在程序中需要创建某个类的几百万个实例对象 。
# 关于__slots__的一个常见误区是它可以作为一个封装工具来防止用户给实例增加新的属性。尽管使用__slots__可以达到这样的目的,但是这个并不是它的初衷。
# 更多的是用来作为一个内存优化工具。
class Test:
    __slots__ = ['name', 'age']  # 类似于定制属性字典{'name':None, 'age':None}


t = Test()
t.name = 'zjs'
# setattr(t, 'aaa', '123')
print(t.name)


# print(t.aaa)


# t.xxxxxxxxxxxxx = 'debug'   # 会调用setattr然后通过t.__dict__['xxxxxxxxx'] = 'debug' 由于__dict__不存在所以不能设置
# t.__dict__    # 没有这个属性。

class Test2:
    pass


t = Test2()
t.name = 'zjs'
print(t.name)
