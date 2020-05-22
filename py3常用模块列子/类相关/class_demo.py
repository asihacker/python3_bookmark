#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 17:40
# @Author  : AsiHacker
# @Site    : 
# @File    : class_demo.py
# @Software: PyCharm


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
    def clsss(cls, id: int):
        cls.ddd.add(id)
        return cls.ddd


print(Apple.clsss(1))
print(Apple.clsss(2))
print(Apple.clsss(3))
print(Apple.clsss(4))
