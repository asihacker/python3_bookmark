#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 23:50
# @Author  : AsiHacker
# @File    : __dict__.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.

# 为了方便用户查看类中包含哪些属性，Python 类提供了 __dict__ 属性。
# 需要注意的一点是，该属性可以用类名或者类的实例对象来调用，用类名直接调用 __dict__，会输出该由类中所有类属性组成的字典；
# 而使用类的实例对象调用 __dict__，会输出由类中所有实例属性组成的字典。
class CLanguage:
    a = 1
    b = 2

    def __init__(self):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"


# 通过类名调用__dict__
print(CLanguage.__dict__)

# 通过类实例对象调用 __dict__
clangs = CLanguage()
print(clangs.__dict__)
