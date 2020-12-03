#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 20:09
# @Author  : AsiHacker
# @Site    : 
# @File    : property.py
# @Software: PyCharm
# 1. 作用
# 将类方法转换为类属性，可以用 . 直接获取属性值或者对属性进行赋值
#
# 2.实现方式
# 使用property类来实现，也可以使用property装饰器实现，二者本质是一样的。多数情况下用装饰器实现
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('分数必须是整数')
        if value < 0 or value > 100:
            raise ValueError('分数必须0-100之间')
        self._score = value

    def fuck(self, name: str):
        return name


student = Student()
student.fuck('123')
student.score = 111
print(student.score)
