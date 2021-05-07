#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/21 22:06
# @Author  : AsiHacker
# @File    : func_demo.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from decorator import decorator


@decorator
def deco(func, *args, **kw):
    print("Ready to run task")
    func(*args, **kw)
    print("Successful to run task")


@deco
def myfunc():
    print("Running the task")


myfunc()
