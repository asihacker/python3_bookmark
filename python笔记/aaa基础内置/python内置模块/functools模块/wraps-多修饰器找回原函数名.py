#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 19:58
# @Author  : AsiHacker
# @File    : wraps-多修饰器找回原函数名.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from functools import wraps


def timer1(func):
    @wraps(func)
    def wrapper(*args, **kw):
        print(func.__name__)
        return func(*args, **kw)

    return wrapper


def timer2(func):
    @wraps(func)
    def wrapper(*args, **kw):
        print(func.__name__)
        return func(*args, **kw)

    return wrapper


@timer1
@timer2
def test():
    pass


if __name__ == '__main__':
    test()
