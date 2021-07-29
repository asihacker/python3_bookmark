# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/13 20:11
# @Author  : AsiHacker
# @File    : demo
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import time
def foo(x, y):
    tt = time.time()
    s = 0
    for i in range(x, y):
        s += i
    print('Time used: {} sec'.format(time.time() - tt))
    return s


print(foo(1, 100000000))


from numba import jit


@jit
def foo(x, y):
    tt = time.time()
    s = 0
    for i in range(x, y):
        s += i
    print('Time used: {} sec'.format(time.time() - tt))
    return s


print(foo(1, 100000000))
