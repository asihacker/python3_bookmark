#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 23:47
# @Author  : AsiHacker
# @File    : __new__.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# 类实例化的时候触发
class Apple:
    def __new__(cls, *args, **kwargs):
        print('__new__')


a = Apple()
