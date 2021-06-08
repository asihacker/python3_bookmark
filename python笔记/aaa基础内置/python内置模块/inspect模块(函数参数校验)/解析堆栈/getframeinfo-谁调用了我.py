#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 20:44
# @Author  : AsiHacker
# @File    : getframeinfo-谁调用了我.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from inspect import getframeinfo, currentframe


def foo():
    who = getframeinfo(currentframe().f_back)[2]
    print('{} call me'.format(who))


def a():
    foo()


def b():
    foo()


a()
b()
