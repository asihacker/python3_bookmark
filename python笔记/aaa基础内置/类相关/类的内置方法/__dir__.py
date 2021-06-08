#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 18:26
# @Author  : AsiHacker
# @File    : __dir__.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# dir()作用在一个实例对象上时，__dir__会被调用。返回值必须是序列。dir()将返回的序列转换成列表并排序。
# 通过此函数可以某个对象拥有的所有的属性名和方法名，该函数会返回一个包含有所有属性名和方法名的有序列表。
class CLanguage:
    def __init__(self, ):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"

    def say(self, ):
        pass


clangs = CLanguage()
print(dir(clangs))
